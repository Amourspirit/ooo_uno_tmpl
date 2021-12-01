#!/usr/bin/env python
import os
import argparse
from typing import Dict, List, NamedTuple, Set, Tuple, Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, SoupStrainer, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, TypeCheckKw
from kwhelp import KwArg, rules
from collections import namedtuple
from base import WriteBase, ParserBase, TYPE_MAP
from pathlib import Path
import textwrap
import xerox # requires xclip - sudo apt-get install xclip

dataitem = namedtuple(
    'dataitem', ['name', 'datatype', 'orig_type', 'lines'])


class Parser(ParserBase):
    # region init
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._data = None
        self._data_formated = None
        self._auto_imports = set()

    # endregion init
    # region Info
    def get_info(self) -> Dict[str, str]:
        """
        Gets info

        Returns:
            Dict[str, str]: {
                "name": "name of constant",
                "fullname": "full name such as com.sun.star.awt.Command"
                "desc": "description of constant",
                "url": "Url to LibreOffice of constant"
            }
        """
        if not self._url:
            raise ValueError('URL is not set')
        soup = BeautifulSoup(self.get_raw_html(), 'lxml')
        full_name = self._get_full_name(soup=soup)
        name = self._get_name(soup=soup)
        desc = self._get_desc(soup=soup)
        info = {
            "name": name,
            "fullname": full_name,
            "desc": desc,
            "url": self.url
        }
        return info
    # endregion Info

    # region Data
    def get_data(self) -> List[dataitem]:
        if self._data:
            return self._data
        if not self._url:
            raise ValueError('URL is not set')
        soup = BeautifulSoup(self.get_raw_html(), 'lxml')
        items = self._get_memitems(soup=soup)
        struct_info = self._get_struct_details(memitetms=items)
        self._data = struct_info
        return self._data

    def get_formated_data(self):
        if self._data_formated:
            return self._data_formated
        def get_lines(lines:List[str]) -> str:
            line_indent = self._indent * 2
            line_len = len(lines)
            if line_len == 1:
                return f'"{self._clean_str(lines[0])}"'
            s_ln = '['
            for j, line in enumerate(itm.lines):
                if j > 0:
                    s_ln += f',\n{line_indent}"",\n'
                    s_ln += f'{line_indent}"{self._clean_str(line)}"'
                else:
                    s_ln += f'"{self._clean_str(line)}"'
            s_ln += ']'
            return s_ln

        data = self.get_data()
        lines = []
        
        for itm in data:
            s = '{\n'
            s += self._indent + f'"name": "{itm.name}",\n'
            s += self._indent + f'"type": "{itm.datatype}",\n'
            s += self._indent + f'"orig_type": "{itm.orig_type}",\n'
            if len(itm.lines) > 0:
               ln_str = get_lines(itm.lines)
               s += self._indent + f'"lines": {ln_str}'
            else:
                s += self._indent + '"lines": ""'
            s += '\n}'
            lines.append(s)
        result = ',\n'.join(lines)
        self._data_formated = result
        return self._data_formated

    def _get_struct_details(self, memitetms: ResultSet) -> List[dataitem]:
        results = []
        def get_doc_lines(item_tag:Tag) -> list:
            docs = item_tag.find('div', class_='memdoc')
            lines = []
            if docs:
                doc_lines = docs.find_all('p')
                if doc_lines:
                    for ln in doc_lines:
                        lines.append(ln.text)
            return lines

        def get_py_type(in_type: str) -> str:
            _parts = in_type.split('.')
            p_type = _parts[len(_parts) - 1]
            n_type = TYPE_MAP.get(p_type, None)
            if n_type:
                return n_type
            # unknow type. wrap in quotes.
            # Todo: Consider auto import option for unknown types
            self._auto_imports.add(in_type)
            return f"'{p_type}'"

        for itm in memitetms:
            # text in format of com::sun::star::awt::AdjustmentType Type
            text: str = itm.find("td", class_='memname',
                                 recursive=True).text.strip().replace('::', '.')
            parts = text.split()
            _type = parts[0]
            py_type = get_py_type(_type)
            name = parts[1]
            lines = get_doc_lines(itm)
            di = dataitem(name=name,
                          datatype=py_type,
                          orig_type=_type,
                          lines=lines)
            results.append(di)
        if self._sort:
            results.sort()
        return results
    # endregion Data

    # region Properties
    @property
    def auto_imports(self) -> set:
        """Specifies auto_imports"""
        return self._auto_imports

    # endregion Properties
class StructWriter(WriteBase):
    @TypeCheckKw(arg_info={
        "sort": 0,
        "copy_clipboard": 0,
        "print": 0,
        "write_file": 0
        },
        types=[bool],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser:Parser, **kwargs):
        self._parser = parser
        self._sort = kwargs.get('sort', True)
        self._copy_clipboard = kwargs.get('copy_clipboard', False)
        self._print = kwargs.get('print', False)
        self._auto_import = kwargs.get('auto_import', True)
        self._indent_amt = 4
        self._write_file = kwargs.get('write_file', False)
        self._file_full_path = None
        self._p_name = None
        self._p_fullname = None
        self._p_url = None
        self._p_desc = None
        self._path_dir = Path(os.path.dirname(__file__))
        _path = Path(self._path_dir, 'template', 'struct.tmpl')
        if not _path.exists():
            raise FileNotFoundError(f"unable to find templae file '{_path}'")
        self._template_file = _path
        self._template: str = self._get_template()

    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def write(self):
        self._set_info()
        self._set_template_data()
        if self._copy_clipboard:
            xerox.copy(self._template)
        if self._print:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self._template)
        if self._write_file:
            self._write_to_file()

    def _set_template_data(self):
        self._template = self._template.replace('{sort}', str(self._sort))
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{link}', self._p_url)
        indent = ' ' * self._indent_amt
        indented = textwrap.indent(self._p_desc, indent).lstrip()
        self._template = self._template.replace('{desc}', indented)
        indented = textwrap.indent(self._p_data, indent)
        # indented = indented.lstrip()
        self._template = self._template.replace('{data}', indented)
        self._template = self._template.replace('{auto_import}', str(self._auto_imports()))

    def _write_to_file(self):
        with open(self._file_full_path, 'w') as f:
            f.write(self._template)


    def _set_info(self):
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_fullname = data['fullname']
        self._p_data = self._parser.get_formated_data()
        if self._write_file:
            self._file_full_path = self._get_uno_obj_path()
        

    def _get_uno_obj_path(self) -> Path:
        uno_obj_path = Path(self._path_dir.parent, 'uno_obj')
        name_parts = self._p_fullname.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        index = len(path_parts) -1
        path_parts[index] = path_parts[index] + '.tmpl'
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        return obj_path

    def _auto_imports(self) -> List[Tuple[str, str]]:
        results = []
        if not self._auto_import:
            return results
        auto: Set[str] = self._parser.auto_imports
        if len(auto) == 0:
            return results
        local_ns_str = self._p_fullname.rsplit('.', 1)[0]
        local_parts = local_ns_str.split('.')
        
        for name in auto:
            name_ns_str = name.rsplit('.', 1)[0]
            name_ns = name_ns_str.split('.')
            # struct_name = name_parts[len(name_parts)-1:][0]
            struct_name = name.rsplit('.', 1)[1]
            camel_name = self._parser.camel_to_snake(struct_name)
            if name_ns_str == local_ns_str:
                results.append((f'.{camel_name}', f'{struct_name}'))
                continue
            commmon_count = 0
            for i, ns in enumerate(name_ns):
                if ns != local_parts[i]:
                    break
                commmon_count += 1
            if commmon_count > 0:
                common_ns = name_ns[commmon_count:]
                dot_ext = len(local_parts) - commmon_count
                dot = "." * dot_ext
                rel = ".".join(common_ns)
                str_from = f'{dot}{rel}.{camel_name}'
                results.append((str_from, struct_name))
        return results
        
        
def _main():
    p = Parser(url='https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1EnhancedMouseEvent.html')
    w = StructWriter(parser=p, print=True)
    w.write()

def main():
    parser = argparse.ArgumentParser(description='const')
    parser.add_argument('-u', '--url',
                        help='Url to parse', type=str, required=True)
    parser.add_argument(
        '-s', '--sort', help='Sort results', type=bool, default=True)
    parser.add_argument(
        '-d', '--dual-colon', help='Replace :: with .', type=bool, default=True)
    
    parser.add_argument(
        '-c', '--clipboard', help='Copy to clipboard', type=bool, default=False)
    parser.add_argument(
        '-a', '--auto-import', help='Auto import types that are not python types', type=bool, default=True)
    parser.add_argument(
        '-p', '--print', help='print to terminal', type=bool, default=True)
    
    parser.add_argument(
        '-w', '--write-file', help='Write file into obj_uno subfolder', type=bool, default=False)
    
    args = parser.parse_args()
    p = Parser(url=args.url, sort=args.sort,
               replace_dual_colon=args.dual_colon)
    print('')
    w = StructWriter(parser=p, copy_clipboard=args.clipboard, print=args.print, write_file=args.write_file,
                     auto_import=args.auto_import)
    w.write()
    
if __name__ == '__main__':
    main()
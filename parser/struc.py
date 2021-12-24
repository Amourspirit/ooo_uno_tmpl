#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains a structure
"""
import os
import sys
import logging
import argparse
import base
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple, Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, TypeCheckKw
from kwhelp import rules
from collections import namedtuple
from pathlib import Path
import textwrap
import xerox # requires xclip - sudo apt-get install xclip
from logger.log_handle import get_logger
from type_mod import PythonType
from parser import __version__, JSON_ID

logger = None

def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l

_set_loggers(None)

# dataitem = namedtuple(
#     'dataitem', ['name', 'datatype', 'orig_type', 'lines'])
@dataclass
class DataItem:
    name: str
    is_py_type: bool
    datatype: str
    orig_type: str
    lines: List[str] = field(default_factory=list)

    def __lt__(self, other: 'DataItem'):
        return self.name < other.name
    

class Parser(base.ParserBase):
    # region Constructor
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._data = None
        self._data_formated = None
        self._data_info = None
        self._data_items = None
        self._auto_imports = set()
        self._requires_typing = False

    # endregion Constructor

    # region Data
    def get_dict_data(self) -> dict:
        info = self.get_info()
        items = self._get_data_items()
        # set to list for json
        info["imports"] = []
        info["auto_imports"] = self._get_auto_imports(ns=info['namespace'])
        info["from_imports"] = [] # placeholder. picked up in writer
        info["requires_typing"] = self.requires_typing
        info['items'] = items
        return info

    def _get_auto_imports(self, ns:str) -> List[Tuple[str, str]]:
        results = []
        if not self.auto_imports:
            return results
        auto: Set[str] = self.auto_imports
        if len(auto) == 0:
            return results
        for name in auto:
            results.append(base.Util.get_rel_import(i_str=name, ns=ns))
        return results
    # endregion Data
    # region Info
    def get_info(self) -> Dict[str, str]:
        """
        Gets info

        Returns:
            Dict[str, str]: {
                "name": "name of constant",
                "fullname": "full name such as com.sun.star.awt.Command"
                "desc": "(List[str]), description of constant",
                "url": "Url to LibreOffice of constant",
                "namespace": "namespace",
                "extends": "(List[str]), inherits"
            }
        """
        if not  self._data_info is None:
            return self._data_info
        try:
            soup_obj = base.SoupObj(self.url, allow_cache=True)
            soup =soup_obj.soup
            inherits = base.ApiInherited(soup=soup_obj, raise_error=False)
            ex = []
            for el in inherits.get_obj():
                ex.append(el.fullns)
            full_name = self._get_full_name(soup=soup)
            name = self._get_name(soup=soup)
            desc = self._get_desc(soup=soup)
            ns = base.UrlObj(self.url)
            info = {
                "name": name,
                "fullname": full_name,
                "desc": desc,
                "url": self.url,
                "namespace": ns.namespace_str,
                "extends": ex
            }
            self._data_info = info
            return self._data_info
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e

    def get_parser_args(self) -> dict:
        args = {
            "sort": self._sort
        }
        return args

    # endregion Info

    # region Data
    def get_data(self) -> List[DataItem]:
        if not self._data is None:
            return self._data
        try:
            if not self._url:
                raise ValueError('URL is not set')
            soup = BeautifulSoup(self.get_raw_html(), 'lxml')
            items = self._get_memitems(soup=soup)
            struct_info = self._get_struct_details(memitetms=items)
            self._data = struct_info
            return self._data
        except Exception as e:
            logger.error(e, exc_info=True)

    def get_formated_data(self) -> str:
        if not self._data_formated is None:
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
        try:
            lines = []
            
            for itm in data:
                s = '{\n'
                s += self._indent + f'"name": "{itm.name}",\n'
                s += self._indent + f'"is_py_type": "{itm.is_py_type}",\n'
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
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
    
    def _get_data_items(self) -> List[dict]:
        if not self._data_items is None:
            return self._data_items
        result = []
        data = self.get_data()
        try:
            for itm in data:
                d_itm = {
                    "name": itm.name,
                    "is_py_type": itm.is_py_type,
                    "type": itm.datatype,
                    "orig_type": itm.orig_type,
                    "lines": itm.lines
                }
                result.append(d_itm)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        self._data_items = result
        return self._data_items

    def _get_struct_details(self, memitetms: ResultSet) -> List[DataItem]:
        results = []
        def get_doc_lines(item_tag:Tag) -> list:
            docs = item_tag.find('div', class_='memdoc')
            lines = []
            if docs:
                doc_lines = docs.find_all('p')
                if doc_lines:
                    for ln in doc_lines:
                        _line = str(ln.text)
                        _lines = _line.splitlines()
                        for i, _nl in enumerate(_lines):
                            # if i > 0:
                            #     lines.append("")
                            _ln = _nl.replace('::', '.').strip()
                            lines.append(_ln)
                        # lines.append(ln.text)
            return lines

        def get_py_type(in_type: str) -> PythonType:
            
            p_type: PythonType = base.Util.get_python_type(in_type=in_type)
            for im in p_type.imports:
                self._auto_imports.add(im)
            if p_type.requires_typing:
                self._requires_typing = True
            return p_type

        for itm in memitetms:
            # text in format of com::sun::star::awt::AdjustmentType Type
            # or sequence< ::com::sun::star::uno::XInterface> TargetSet
            text: str = itm.find("td", class_='memname',
                                 recursive=True).text.strip().replace('::', '.')
            logger.debug("Processing line: %s", text)
            # parts = text.split()
            # if text.find('<') >= 0:
                # likely sequence< > such as sequence< ::com::sun::star::uno::XInterface> TargetSet
            parts = text.rsplit(maxsplit=1)
            # some unsigned short Data > ['some unsigned', 'short', 'Data3']
            # short Data > ['short', 'Data3']
            _type = parts[0] if len(parts) == 2 else parts[1]
            # _type = _type.strip('.').replace('>','').strip()
            py_type = get_py_type(_type)
            name = base.Util.get_clean_classname(parts.pop())
            lines = get_doc_lines(itm)
            logger.debug("Detils: Name: %s, Type: %s, Orig: %s", name, py_type, _type)
            di = DataItem(
                name=name,
                is_py_type=py_type.is_py_type,
                datatype=py_type.type,
                orig_type=_type,
                lines=lines
            )
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

    @property
    def requires_typing(self) -> set:
        """Gets if import if typing is required"""
        return self._requires_typing
    # endregion Properties


class StructWriter(base.WriteBase):

    # region Constructor
    @TypeCheckKw(arg_info={
        "sort": 0,
        "copy_clipboard": 0,
        "print_template": 0,
        "print_json": 0,
        "write_file": 0,
        "write_json": 0,
        "auto_import": 0,
        "write_template_long": 0,
        "_dynamic_struct": 0
        },
        types=[bool],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser:Parser, **kwargs):
        super().__init__(**kwargs)
        self._parser = parser
        self._sort = kwargs.get('sort', True)
        self._copy_clipboard = kwargs.get('copy_clipboard', False)
        self._print_template = kwargs.get('print_template', False)
        self._auto_import = kwargs.get('auto_import', True)
        self._write_file = kwargs.get('write_template', False)
        self._print_json = kwargs.get('print_json', True)
        self._write_json = kwargs.get('write_json', False)
        self._dynamic_struct = kwargs.get('dynamic_struct', False)
        self._write_template_long: bool = kwargs.get(
            'write_template_long', False)
        self._indent_amt = 4
        self._cache = {}
        self._json_str = None
        self._file_full_path = None
        self._p_name = None
        self._p_namespace = None
        self._p_fullname = None
        self._p_url = None
        self._p_desc = None
        self._p_extends: List[str] = None
        self._p_imports: Set[str] = set()
        
        self._path_dir = Path(os.path.dirname(__file__))
        t_file = 'struct'
        if not self._write_template_long:
            t_file += '_stub'
        t_file += '.tmpl'
        _path = Path(self._path_dir, 'template', t_file)
        try:
            if not _path.exists():
                raise FileNotFoundError(f"unable to find templae file '{_path}'")
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        self._template_file = _path
        self._template: str = self._get_template()
    # endregion Constructor


    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def write(self):
        self._set_info()
        self._set_template_data()
        logger.info("Processing %s", self._p_fullname)
        try:
            if self._copy_clipboard:
                xerox.copy(self._template)
                logger.debug('copied to clipbord')
            if self._print_template or self._print_json:
                logger.debug('Printing to terminal')
                os.system('cls' if os.name == 'nt' else 'clear')
            if self._print_template:
                print(self._template)
            if self._print_json:
                print(self._get_json())
            if self._write_file:
                self._write_to_file()
            if self._write_json:
                self._write_to_json()
        except Exception as e:
            logger.exception(e)

    def _get_json(self) -> str:
        if not self._json_str is None:
            return self._json_str
        p_dict = self._parser.get_dict_data()
        p_dict['from_imports'] = self._get_from_imports()
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "timestamp": str(base.Util.get_timestamp_utc()),
            "type": "struct",
            "name": p_dict['name'],
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {
                "sort": self._sort,
                "auto_import": self._auto_import,
                "dynamic_struct": self._dynamic_struct
            },
            "data": p_dict
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._json_str = str_jsn
        return self._json_str

    # region get Imports
    def _get_from_imports(self) -> List[List[str]]:
        key = '_get_from_imports'
        if key in self._cache:
            return self._cache[key]
        lst = []
        for ns in self._p_imports:
            f, n = base.Util.get_rel_import(
                i_str=ns, ns=self._p_namespace
            )
            lst.append([f, n])
        self._cache[key] = lst
        return self._cache[key]
    # endregion get Imports

    def _set_template_data(self):
        if self._write_template_long is False:
            return
        self._template = self._template.replace(
            '{dynamic_struct}', str(self._dynamic_struct))
        self._template = self._template.replace('{sort}', str(self._sort))
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{ns}', self._p_namespace)
        self._template = self._template.replace('{link}', self._p_url)
        self._template = self._template.replace(
            '{requires_typing}', str(self._parser.requires_typing))
        indent = ' ' * self._indent_amt
        str_json_desc = base.Util.get_formated_dict_list_str(self._p_desc)
        self._template = self._template.replace('{desc}', str_json_desc)
        indented = textwrap.indent(self._p_data, indent)
        self._template = self._template.replace('{data}', indented)
        self._template = self._template.replace('{auto_import}', str(self._auto_imports()))
        self._template = self._template.replace(
            '{from_imports}',
            base.Util.get_formated_dict_list_str(self._get_from_imports())
        )
        self._template = self._template.replace(
            '{inherits}', base.Util.get_string_list(lines=self._p_extends))

    def _write_to_file(self):
        with open(self._file_full_path, 'w') as f:
            f.write(self._template)
        logger.info("Created file: %s", self._file_full_path)
    
    def _write_to_json(self):
        p = self._file_full_path.parent
        jsn_p = p / (str(self._file_full_path.stem) + '.json')
        jsn_str = self._get_json()
        with open(jsn_p, 'w') as f:
            f.write(jsn_str)
        logger.info("Created file: %s", jsn_p)

    def _set_info(self):
        def get_extends(lst: List[str]) -> List[str]:
            return [base.Util.get_last_part(s) for s in lst]
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_fullname = data['fullname']
        self._p_data = self._parser.get_formated_data()
        self._p_namespace = data['namespace']
        self._p_imports.update(data['extends'])
        self._p_extends = get_extends(data['extends'])
        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()
        

    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        uno_obj_path = Path(self._path_dir.parent,
                            base.APP_CONFIG.uno_base_dir)
        name_parts = self._p_fullname.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        index = len(path_parts) -1
        if not path_parts[index]:
            try:
                raise Exception(
                    "StructWriter._get_uno_obj_path() parsing path yielded an empty string")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e
        path_parts[index] = base.Util.get_clean_filename(path_parts[index]) + '.tmpl'
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._cache[key] = obj_path
        return self._cache[key]

    def _auto_imports(self) -> List[Tuple[str, str]]:
        results = []
        if not self._auto_import:
            return results
        auto: Set[str] = self._parser.auto_imports
        if len(auto) == 0:
            return results
        local_ns_str = self._p_fullname.rsplit('.', 1)[0]
        for name in auto:
            
            im = base.Util.get_rel_import(i_str=name, ns=local_ns_str)
            results.append(im)
        return results
        
        
def _main():
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Ambiguous_3_01T_01_4.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1GetPropertyTolerantResult.html'
    url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1TextMarkupDescriptor.html'
    sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    main()

def main():
    global logger

    # http://pymotw.com/2/argparse/
    parser = argparse.ArgumentParser(description='const')
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=True)
    parser.add_argument(
        '-x', '--no-cache',
        help='No caching',
        action='store_false',
        dest='cache',
        default=True)
    parser.add_argument(
        '-p', '--no-print-clear',
        help='No clearing of terminal when output to terminal.',
        action='store_false',
        dest='no_print_clear',
        default=True)
    parser.add_argument(
        '-s', '--no-sort',
        help='No sorting of results',
        action='store_false',
        dest='sort',
        default=True)
    parser.add_argument(
        '-d', '--dynamic_struct',
        help='Template will generate dynamic struct content',
        action='store_true',
        dest='dynamic_struct',
        default=False)
    parser.add_argument(
        '-c', '--clipboard',
        help='Copy to clipboard',
        action='store_true',
        dest='clipboard',
        default=False)
    parser.add_argument(
        '-a', '--no-auto-import',
        action='store_false',
        dest='auto_import',
        help='Auto import types that are not python types',
        default=True)
    parser.add_argument(
        '-g', '--long-template',
        help='Writes a long format template. Requires --write-template is set. No Autoload',
        action='store_true',
        dest='long_format',
        default=False)
    parser.add_argument(
        '-t', '--write-template',
        help='Write template file into obj_uno subfolder',
        action='store_true',
        dest='write_template',
        default=False)
    parser.add_argument(
        '-m', '--print-template',
        help='Print template to terminal',
        action='store_true',
        dest='print_template',
        default=False)
    parser.add_argument(
        '-n', '--print-json',
        help='Print json to terminal',
        action='store_true',
        dest='print_json',
        default=False)
    parser.add_argument(
        '-j', '--write-json',
        help='Write json file into obj_uno subfolder',
        action='store_true',
        dest='write_json',
        default=False)
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use. Default to struct.log',
        type=str,
        required=False)

    args = parser.parse_args()

    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'struct.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')

    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)
    p = Parser(
        url=args.url,
        sort=args.sort,
        cache=args.cache
        )
    if args.print_template is False and args.print_json is False:
        print('')
    w = StructWriter(
        parser=p,
        copy_clipboard=args.clipboard,
        print_template=args.print_template,
        print_json=args.print_json,
        auto_import=args.auto_import,
        write_template=args.write_template,
        write_json=args.write_json,
        write_template_long=args.long_format,
        dynamic_struct=args.dynamic_struct
        )
    w.write()
    
if __name__ == '__main__':
    main()
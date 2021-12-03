#!/usr/bin/env python
import os
import sys
import argparse
from typing import Dict, List, Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, SoupStrainer, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, TypeCheckKw
from kwhelp import KwArg, rules
from collections import namedtuple
from base import WriteBase, ParserBase
from pathlib import Path
import textwrap
import xerox # requires xclip - sudo apt-get install xclip
from logger.log_handle import get_logger
logger = get_logger(Path(__file__).name)
dataitem = namedtuple(
    'dataitem', ['value', 'raw_value', 'name', 'datatype', 'lines'])

class Parser(ParserBase):
    
    # region init
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._data = None
        self._data_formated = None

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
        try:
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
        except Exception as e:
            logger.error(e)

    # endregion Info

    # region Data

    def get_data(self) -> List[dataitem]:
        """
        Gets constants data

        Returns:
            List: list of tuple (value:number|str, raw_value:str, name:str, type:str, lines:[])

        Raises:
            ValueError: If url is not set.
        """
        try:
            if self._data:
                return self._data
            if not self._url:
                raise ValueError('URL is not set')
            soup = BeautifulSoup(self.get_raw_html(), 'lxml')

            items = self._get_memitems(soup=soup)
            const_info = self._get_const_details(memitetms=items)
            self._data = const_info
            return self._data
        except Exception as e:
            logger.error(e)

    def get_formated_data(self):
        if self._data_formated:
            return self._data_formated
        try:
            data = self.get_data()
            lines = []
            for itm in data:
                s = f'"{itm.name}": ["{itm.raw_value}"'
                if len(itm.lines) > 0:
                    s_ln = ', [\n'
                    for j, line in enumerate(itm.lines):
                        if j > 0:
                            s_ln += ',\n    "",\n'
                        s_ln += f'    "{self._clean_str(line)}"'
                    s_ln += '\n]'
                    s += s_ln
                s += ']'
                lines.append(s)
            result = ',\n'.join(lines)
            self._data_formated = result
            return self._data_formated
        except Exception as e:
            logger.error(e)

    def _get_const_details(self, memitetms: ResultSet) -> List[dataitem]:
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

        for itm in memitetms:
            text: str = itm.find("td", class_='memname',
                                 recursive=True).text.replace(' ', ',')
            parts = text.split(',')
            _type = parts[1]
            name = parts[2]
            raw_value = parts[4]
            value = self._get_number(raw_value)
            lines = get_doc_lines(itm)
            di = dataitem(value=value, raw_value=raw_value, name=name,
                          datatype=_type, lines=lines)
            results.append(di)
        if self._sort:
            results.sort()
        return results

        

    def _get_tbl(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find('table', class_='memberdecls')

    def _get_rows_memitem(self, tbl: ResultSet) -> ResultSet:
        def check_row(tag: Tag) -> bool:
            if tag.has_attr('class'):
                _class = tag['class']
                if isinstance(_class, str):
                    return _class.startswith('memitem')
                else:
                    return _class[0].startswith('memitem')
            return False

        return tbl.find_all(check_row)
    # endregion Data



class ConstWriter(WriteBase):
    @TypeCheckKw(arg_info={
        "hex": 0,
        "sort": 0,
        "flags": 0,
        "copy_clipboard": 0,
        "print": 0,
        "write_file": 0
        },
        types=[bool],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser:Parser, **kwargs):
        self._parser = parser
        self._hex = kwargs.get('hex', False)
        self._sort = kwargs.get('sort', True)
        self._flags = kwargs.get('flags', False)
        self._copy_clipboard = kwargs.get('copy_clipboard', False)
        self._print = kwargs.get('print', True)
        self._indent_amt = 4
        self._write_file = kwargs.get('write_file', False)
        self._file_full_path = None
        self._p_name = None
        self._p_fullname = None
        self._p_url = None
        self._p_desc = None
        self._path_dir = Path(os.path.dirname(__file__))
        _path = Path(self._path_dir, 'template', 'const.tmpl')
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
        logger.info("Processing %s", self._p_fullname)
        try:
            if self._copy_clipboard:
                xerox.copy(self._template)
                logger.debug('copied to clipbord')
            if self._print:
                logger.debug('Printing to terminal')
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self._template)
            if self._write_file:
                self._write_to_file()
        except Exception as e:
            logger.exception(e)

    def _write_to_file(self):
        with open(self._file_full_path, 'w') as f:
            f.write(self._template)
        logger.info("Created file: %s", self._file_full_path)
        
    def _set_template_data(self):
        self._template = self._template.replace('{hex}', str(self._hex))
        self._template = self._template.replace('{sort}', str(self._sort))
        self._template = self._template.replace('{flags}', str(self._flags))
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{link}', self._p_url)
        indent = ' ' * self._indent_amt
        indented = textwrap.indent(self._p_desc, indent).lstrip()
        self._template = self._template.replace('{desc}', indented)
        indented = textwrap.indent(self._p_data, indent)
        # indented = indented.lstrip()
        self._template = self._template.replace('{data}', indented)

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
        self._create_sys_links(dest=obj_path.parent)
        return obj_path

def _main():
    # for debugging
    p = Parser(url='https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1Command.html')
    print('')
    w = ConstWriter(parser=p, write_file=True)
    w.write()
    
def main():
    logger.info('Executing command: %s', sys.argv[1:])
    parser = argparse.ArgumentParser(description='const')
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=True)
    parser.add_argument(
        '-s', '--no-sort',
        help='No sorting of results',
        action='store_false',
        dest='sort',
        default=True)
    parser.add_argument(
        '-d', '--no-dual',
        help='Do NOT replace :: with .',
        action='store_false',
        dest='dual_colon',
        default=True)
    parser.add_argument(
        '-f', '--flags',
        help='Treat as flags',
        action='store_true',
        dest='flags',
        default=False)
    parser.add_argument(
        '-x', '--hex',
        help='Treat as hex',
        action='store_true',
        dest='hex',
        default=False)
    parser.add_argument(
        '-c', '--clipboard',
        help='Copy to clipboard',
        action='store_true',
        dest='clipboard',
        default=False)
    parser.add_argument(
        '-p', '--no-print',
        help='Do NOT print to terminal',
        action='store_false',
        dest='print',
        default=True)
    parser.add_argument(
        '-w', '--write',
        help='Write file into obj_uno subfolder',
        action='store_true',
        dest='write_file',
        default=False)
    
    args = parser.parse_args()
    p = Parser(url=args.url, sort=args.sort,
               replace_dual_colon=args.dual_colon)
    if not args.print:
        print('')
    w = ConstWriter(parser=p, copy_clipboard=args.clipboard, print=args.print, flags=args.flags, hex=args.hex, write_file=args.write_file)
    w.write()
 


if __name__ == '__main__':
    main()

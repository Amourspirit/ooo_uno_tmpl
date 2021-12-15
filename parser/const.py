#!/usr/bin/env python
import os
import sys
import re
import logging
import argparse
import base
import xerox # requires xclip - sudo apt-get install xclip
import textwrap
from typing import Dict, List, Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, TypeCheckKw
from kwhelp import rules
from collections import namedtuple
from pathlib import Path
from logger.log_handle import get_logger
from parser import __version__, JSON_ID

logger = None

def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l

_set_loggers(None)

pattern_hex = re.compile(r"0x[0-9A-Fa-f]+")

dataitem = namedtuple(
    'dataitem', ['value', 'raw_value', 'name', 'datatype', 'lines'])


class Parser(base.ParserBase):
    
    # region init
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._soup = base.SoupObj(url=self.url, allow_cache=self.allow_cache)
        self._cache = {}

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
                "url": "Url to LibreOffice of constant",
                "namespace": "Namespace such as com.sun.star.awt.Command"
            }
        """
        key = 'get_info'
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = {}
        try:
            if not self._url:
                raise ValueError('URL is not set')
            soup = self._soup.soup
            full_name = self._get_full_name(soup=soup)
            name = self._get_name(soup=soup)
            desc = self._get_desc(soup=soup)
            ns = base.UrlObj(self.url)
            info = {
                "name": name,
                "fullname": full_name,
                "desc": desc,
                "url": self.url,
                "namespace": ns.namespace_str
            }
            self._cache[key].update(info)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._cache[key]

    def get_parser_args(self) -> dict:
        args = {
            "sort": self.sort
        }
        return args
    # endregion Info
    # region Data
    def get_dict_data(self) -> dict:
        info = self.get_info()
        items = self._get_data_items()
        # set to list for json
        info['items'] = items
        return info


    def get_data(self) -> List[dataitem]:
        """
        Gets constants data

        Returns:
            List: list of tuple (value:number|str, raw_value:str, name:str, type:str, lines:[])

        Raises:
            ValueError: If url is not set.
        """
        key = 'get_data'
        if key in self._cache:
            return self._cache[key]
        try:
            if not self._url:
                raise ValueError('URL is not set')
            soup = BeautifulSoup(self.get_raw_html(), 'lxml')

            items = self._get_memitems(soup=soup)
            const_info = self._get_const_details(memitetms=items)
            self._cache[key] = const_info
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._cache[key]

    def get_formated_data(self):
        key = 'get_formated_data'
        if key in self._cache:
            return self._cache[key]
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
            self._cache[key] = result
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._cache[key]
    
    def get_is_flags(self) -> bool:
        """
        Gets if const has values that can be Flags Enum.
        This is a calculated result.

        Returns:
            bool: ``True`` if can be flags; Otherwise, ``False``
        """
        key = 'get_is_flags'
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = False
        data = self.get_data()
        nums = []
        try:
            for itm in data:
                nums.append(int(itm.value))
        except:
            return self._cache[key]
        if len(nums) == 0:
            return self._cache[key]
        self._cache[key] = base.Util.is_enum_nums(*nums)
        return self._cache[key]

    def get_is_hex(self) -> bool:
        """
        Gets if the parsed data is in hex format of 0x12AB

        Returns:
            bool: ``True`` if hex is matched; Otherwise, ``False``
        """
        key = 'get_is_hex'
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = False
        data = self.get_data()
        if len(data) == 0:
            return self._cache[key]
        m = pattern_hex.match(data[0].raw_value)
        if m:
            self._cache[key] = True
        return self._cache[key]
        
        
    def _get_data_items(self) -> List[dict]:
        key = '_get_data_items'
        if key in self._cache:
            return self._cache[key]
        result = []
        data = self.get_data()
        try:
            for itm in data:
                d_itm = {
                    "name": itm.name,
                    "type": base.Util.get_py_type(itm.datatype),
                    "value": itm.value,
                    "lines": itm.lines
                }
                result.append(d_itm)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        self._cache[key] = result
        return self._cache[key]

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
                                 recursive=True).text.replace(' ', ',').replace('=,', '').replace('=', '')
            logger.debug("Parser._get_const_details() Processing: %s", text)
            try:
                parts = text.rsplit(',', maxsplit=3)
                raw_value = parts.pop()
                name = parts.pop() # parts[2]
                _type = parts.pop() # parts[1]
            except Exception as e:
                logger.warning('Failed to process Line: %s', text)
                continue
            value = self._get_number(raw_value)
            lines = get_doc_lines(itm)
            di = dataitem(value=value, raw_value=raw_value, name=name,
                          datatype=_type, lines=lines)
            results.append(di)
        if self.sort:
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


class ConstWriter(base.WriteBase):
    # region Constructor
    @TypeCheckKw(arg_info={
        "hex": 0,
        "sort": 0,
        "flags": 1,
        "copy_clipboard": 0,
        "write_template": 0,
        "print_template": 0,
        "print_json": 0,
        "write_json": 0,
        "write_template_long": 0
        },
        types=[bool, (bool, type(None))],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser:Parser, **kwargs):
        super().__init__(**kwargs)
        self._parser = parser
        self._hex = kwargs.get('hex', False)
        self._sort = kwargs.get('sort', True)
        self._flags = kwargs.get('flags', None)
        self._copy_clipboard = kwargs.get('copy_clipboard', False)
        self._print_template = kwargs.get('print_template', True)
        self._write_file = kwargs.get('write_template', False)
        self._print_json = kwargs.get('print_json', True)
        self._write_json = kwargs.get('write_json', False)
        self._write_template_long: bool = kwargs.get(
            'write_template_long', False)
        self._indent_amt = 4
        self._file_full_path = None
        self._p_name = None
        self._p_namespace = None
        self._p_fullname = None
        self._p_url = None
        self._p_desc = None
        self._path_dir = Path(os.path.dirname(__file__))
        t_file = 'const'
        if not self._write_template_long:
            t_file += '_stub'
        t_file += '.tmpl'
        _path = Path(self._path_dir, 'template', t_file)
        if not _path.exists():
            raise FileNotFoundError(f"unable to find templae file '{_path}'")
        self._template_file = _path
        self._template: str = self._get_template()
        self._cache = {}
        self._set_flags()
    # endregion Constructor
    def _set_flags(self):
        # if flags is not specifically set in constructor then get flags from parser
        if self._flags is None:
            self._flags = self._parser.get_is_flags()


    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def write(self):
        self._set_info()
        self._set_template_data()
        logger.info("Processing %s", self._p_fullname)
        try:
            if self._print_template or self._print_json:
                logger.debug('Printing to terminal')
                os.system('cls' if os.name == 'nt' else 'clear')
            if self._copy_clipboard:
                xerox.copy(self._template)
                logger.debug('copied to clipbord')
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
        key = '_get_json'
        if key in self._cache:
            return self._cache[key]
        p_dict = self._parser.get_dict_data()
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "name": p_dict['name'],
            "type": "const",
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {
                "hex": self._hex,
                "sort": self._sort,
                "flags": self._flags
            },
            "data": p_dict
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._cache[key] = str_jsn
        return self._cache[key]

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
        
    def _set_template_data(self):
        if self._write_template_long is False:
            return
        self._template = self._template.replace('{hex}', str(self._hex))
        self._template = self._template.replace('{sort}', str(self._sort))
        self._template = self._template.replace('{flags}', str(self._flags))
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{ns}', self._p_namespace)
        self._template = self._template.replace('{link}', self._p_url)
        indent = ' ' * self._indent_amt
        str_json_desc = base.Util.get_formated_dict_list_str(self._p_desc)
        self._template = self._template.replace('{desc}', str_json_desc)
        # indented = textwrap.indent(self._p_desc, indent).lstrip()
        # self._template = self._template.replace('{desc}', indented)
        indented = textwrap.indent(self._p_data, indent)
        # indented = indented.lstrip()
        self._template = self._template.replace('{data}', indented)

    def _set_info(self):
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_namespace = data['namespace']
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_fullname = data['fullname']
        self._p_data = self._parser.get_formated_data()
        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()
        

    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        uno_obj_path = Path(self._path_dir.parent, 'uno_obj')
        name_parts = self._p_fullname.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        index = len(path_parts) -1
        if not path_parts[index]:
            try:
                raise Exception(
                    "ConstWriter._get_uno_obj_path() parsing path yielded an empty string")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e
        path_parts[index] = path_parts[index] + '.tmpl'
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._cache[key] = obj_path
        return self._cache[key]

def _main():
    # for debugging
    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1accessibility_1_1AccessibleEventId.html'
    sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    main()

def main():
    global logger
    
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
        '-f', '--flags',
        help='Treat as flags',
        action='store_true',
        dest='flags',
        default=None)
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
        '-y', '--hex',
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
        '-n', '--print-json',
        help='Print json to terminal',
        action='store_true',
        dest='print_json',
        default=False)
    parser.add_argument(
        '-m', '--print-template',
        help='Print template to terminal',
        action='store_true',
        dest='print_template',
        default=False)
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
        help='Log file to use. Defaults to const.log',
        type=str,
        required=False)

    args = parser.parse_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'const.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    # endregion Parser
    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')

    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)

    p = Parser(
        url=args.url,
        sort=args.sort,
        cache=args.cache
    )
    if not args.print_json and not args.print_template:
        print('')
    w = ConstWriter(
        parser=p,
        copy_clipboard=args.clipboard,
        print_template=args.print_template,
        print_json=args.print_json,
        flags=args.flags,
        hex=args.hex,
        write_template=args.write_template,
        write_json=args.write_json,
        write_template_long=args.long_format
        )
    w.write()
 
if __name__ == '__main__':
    main()

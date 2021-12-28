#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains a constant
"""
from dataclasses import dataclass
import os
import sys
import re
import logging
import argparse
import xerox # requires xclip - sudo apt-get install xclip
import textwrap
from typing import Dict, List, Set, Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, TypeCheckKw
from kwhelp import rules
from collections import namedtuple
from pathlib import Path

from parser.base import SummaryInfo
try:
    import base
except ModuleNotFoundError:
    import parser.base as base
from logger.log_handle import get_logger
from parser import __version__, JSON_ID
from parser.type_mod import PythonType

logger = None

def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l

_set_loggers(None)

pattern_hex = re.compile(r"0x[0-9A-Fa-f]+")

dataitem = namedtuple(
    'dataitem', ['value', 'raw_value', 'name', 'datatype', 'lines'])

# region Dataclasses

# endregion Dataclasses

# region API classes
class ApiConstBlock(base.ApiSummaryBlock):
    def _get_match_name(self) -> str:
        return 'var-members'

class ApiNs(base.ApiNamespace):
    """Get the Name object for the interface"""

    def __init__(self, soup: base.SoupObj):
        super().__init__(soup)
        self._namespace_str = None
        self._namespace = None

    @property
    def namespace(self) -> List[str]:
        """Gets namespace value"""
        if self._namespace is None:
            self._namespace = self.get_obj()[:-1]
        return self._namespace

    @property
    def namespace_str(self) -> str:
        if self._namespace_str is None:
            self._namespace_str = '.'.join(self.namespace)
        return self._namespace_str

class ApiSummaries(base.BlockObj):
    def __init__(self, block: base.ApiSummaryRows) -> None:
        self._block: base.ApiSummaryRows = block
        super().__init__(self._block.soup)
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._data = None
    
    def get_obj(self) -> List[base.SummaryInfo]:
        if not self._data is None:
            return self._data
        self._data: List[base.SummaryInfo] = []
        # get all rows
        tags: List[Tag] = self._block.get_obj()
        if len(tags) == 0:
            msg = f"{self.__class__.__name__}.get_obj() no table rows that can be used to parse const info."
            msg += f" Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        
        for tag in tags:
            # parse out type, name, id
            sid = self._get_id(tag)
            name = self._get_name(tag)
            p_type = self._get_type(tag, name)
            si = SummaryInfo(
                id = sid,
                name = name,
                type = p_type.type,
                p_type=p_type
            )
            if p_type.requires_typing:
                self._requires_typing = True
            self._imports.update(p_type.get_all_imports())
            self._data.append(si)
        return self._data

    def _get_name(str, tr:Tag) -> str:
        # name should be in first a tag.
        tag: Tag = tr.findChild('td', class_='memItemRight')
        if not tag:
            msg = f"{self.__class__.__name__}._get_name() No data found to get name from. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        a_tag = tag.findChild('a')
        if a_tag:
            return a_tag.text.strip()
        # for some reason a_tag not found. Let try straight text
        text = tag.text.strip()
        # text: ASC_UPALPHA = 0x00000001
        parts = text.split(sep="=", maxsplit=1)
        if len(parts) == 1:
            msg = f"{self.__class__.__name__}._get_name() No valid name can be parsed. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        return parts[0]

    def _get_type(self, tr: Tag, name: str) -> PythonType:
        # select first cell
        tag: Tag = tr.findChild('td', class_='memItemLeft')
        # tag.text 'const long ' format
        if not tag:
            msg = f"{self.__class__.__name__}._get_type() {name}, No data found to get type for. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        text = tag.text.strip()
        parts = text.split()
        type_name = parts.pop()
        p_type = base.Util.get_python_type(type_name)
        logger.debug(
            "%s._get_type(), found type: %s for name: %s",
            self.__class__.__name__, p_type.type, name)
        return p_type
    
    def _get_id(self, tr:Tag) -> str:
        result = None
        classes: List[str] = tr.get('class', [])
        if len(classes) == 0:
            msg = f"{self.__class__.__name__}._get_id() No valid class that can be parsed. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        
        for c in classes:
            if c.startswith('memitem:'):
                result = base.Util.get_last_part(input=c, sep=":")
                break
        if result is None:
            msg = f"{self.__class__.__name__}._get_id() Failed to get id. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        return result

class ApiData(base.APIData):
    def __init__(self, url_soup: Union[str, base.SoupObj], allow_cache: bool):
        super().__init__(url_soup=url_soup, allow_cache=allow_cache)
        self._ns: ApiNs = None
        self._api_const_block: ApiConstBlock = None
        self._api_const_summary_rows: base.ApiSummaryRows = None
        self._api_summaries: ApiSummaries = None

    # region Properties

    @property
    def ns(self) -> ApiNs:
        """Gets the interface Description object"""
        if self._ns is None:
            self._ns = ApiNs(
                self.soup_obj)
        return self._ns

    @property
    def api_const_block(self):
        """Get Block containd all const types, names and values"""
        if self._api_const_block is None:
            self._api_const_block = ApiConstBlock(self.public_members)
        return self._api_const_block

    @property
    def api_summary_rows(self) -> base.ApiSummaryRows:
        """Gets the summary rows for api_const_block"""
        if self._api_const_summary_rows is None:
            self._api_const_summary_rows = base.ApiSummaryRows(self.api_const_block)
        return self._api_const_summary_rows
    @property
    def api_summaries(self) -> ApiSummaries:
        """
        Get the summaries. This classes get_object() returns a list of SummaryInfo
        """
        if self._api_summaries is None:
            self._api_summaries = ApiSummaries(self.api_summary_rows)
        return self._api_summaries
    # endregion Properties
# endregion API classes

class Parser(base.ParserBase):
    
    # region init
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._soup = base.SoupObj(url=self.url, allow_cache=self.allow_cache)
        self._cache = {
            "python_types": []
        }

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
        p_names: Set[str] = set()
        try:
            for itm in data:
                p_type = base.Util.get_python_type(itm.datatype)
                if not p_type.type in p_names:
                    self._cache['python_types'].append(p_type)
                    p_names.add(p_type.type)
                d_itm = {
                    "name": itm.name,
                    "type": p_type.type,
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

    # region Properties
    @property
    def python_types(self) -> List[PythonType]:
        """Gets a list of PythonTypes for this instance"""
        if not '_get_data_items' in self._cache:
            # raise Exception("Parser._get_data_items() must be called before python_types can be accessed.")
            self._get_data_items()
        return self._cache['python_types']
    # endregion Properties


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
        self._p_requires_typing = False
        self._p_from_imports = set()
        self._p_typing_imports = set()
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
        p_dict = {
            "name": 'place holder',
            "namespace": 'place holder',
            "url": 'place holder',
            'flags': self._flags,
            "base_class": self._get_const_base_class(),
            "quote": [],
            "typings": []
        }
        p_dict['quote'] = self._get_quote_flat()
        p_dict['typings'] = self._get_typings()
        p_dict['requires_typing'] = self._p_requires_typing
        p_dict['from_imports'] = self._get_from_imports()
        p_dict['from_imports_typing'] = self._get_from_imports_typing()
        # ConstIntFlagsBase
        p_dict.update(self._parser.get_dict_data())
        
        
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "timestamp": str(base.Util.get_timestamp_utc()),
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

    def _get_const_base_class(self) -> str:
        if self._flags:
            const_base_cls = base.APP_CONFIG.base_const_int_flags
        else:
            const_base_cls = base.APP_CONFIG.base_const_int
        return const_base_cls

    def _get_from_imports(self) -> List[List[str]]:
        key = '_get_from_imports'
        if key in self._cache:
            return self._cache[key]
        lst = [
            [base.APP_CONFIG.base_const, self._get_const_base_class()]
        ]
        self._cache[key] = lst
        return self._cache[key]

    def _get_from_imports_typing(self) -> List[List[str]]:
        key = '_get_from_imports_typing'
        if key in self._cache:
            return self._cache[key]
        t_set: Set[str] = set()
        p_lst = self._parser.python_types
        for t in p_lst:
            t_set.update(t.get_all_imports())
        self._cache[key] = list(t_set)
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
        self._template = self._template.replace('{base_class}', self._get_const_base_class())
        self._template = self._template.replace(
            '{requires_typing}', str(self._p_requires_typing))
        self._template = self._template.replace(
            '{from_imports}',
            base.Util.get_formated_dict_list_str(self._get_from_imports())
            )
        self._template = self._template.replace(
            '{from_typing_imports}',
            base.Util.get_formated_dict_list_str(self._get_from_imports_typing())
        )
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
        # prime cache and set other params such as self._p_requires_typing
        self._get_quote_flat()
        self._get_typings()

    # region quote/typings
    def _get_quote_flat(self) -> List[str]:
        key = '_get_quote_flat'
        if key in self._cache:
            return self._cache[key]
        t_set: Set[str] = set()
        p_lst = self._parser.python_types
        for t in p_lst:
            if t.requires_typing or t.is_py_type is False:
                t_set.add(t.type)
                self._p_requires_typing = True
        self._cache[key] = list(t_set)
        return self._cache[key]

    def _get_typings(self) -> List[str]:
        key = '_get_typings'
        if key in self._cache:
            return self._cache[key]
        t_set: Set[str] = set()
        p_lst = self._parser.python_types
        for t in p_lst:
            if t.requires_typing:
                t_set.add(t.type)
        self._cache[key] = list(t_set)
        return self._cache[key]

    # endregion quote/typing

    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        uno_obj_path = Path(self._path_dir.parent, base.APP_CONFIG.uno_base_dir)
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

# region Parse method


def _get_parsed_kwargs(**kwargs) -> Dict[str, str]:
    required = ("url",)
    lookups = {
        "u": "url",
        "url": "url",
        "L": "log_file",
        "log_file": "log_file"
    }
    result = {}
    for k, v in kwargs.items():
        if not isinstance(k, str):
            continue
        if k in lookups:
            key = lookups[k]
            result[key] = v
    for k in required:
        if not k in result:
            # k is missing from kwargs
            raise base.RequiredError(f"Missing required arg {k}.")
    return result


def _get_parsed_args(*args) -> Dict[str, bool]:
    # key, value and value is a key into defaults
    defaults = {
        'no_sort': True,
        "no_cache": True,
        "long_template": False,
        "clipboard": False,
        "print_json": False,
        "print_template": False,
        "write_template": False,
        "write_json": False,
        "verbose": False,
        "flags": False,
        "hex": False
    }
    found = {
        'no_sort': False,
        "no_cache": False,
        "long_template": True,
        "clipboard": True,
        "print_json": True,
        "print_template": True,
        "write_template": True,
        "write_json": True,
        "verbose": True,
        "flags": True,
        "hex": False
    }
    lookups = {
        "s": "no_sort",
        "no_sort": "no_sort",
        "x": "no_cache",
        "no_cache": "no_cache",
        "g": "long_template",
        "long_template": "long_template",
        "c": "clipboard",
        "clipboard": "clipboard",
        "n": "print_json",
        "print_json": "print_json",
        "m": "print_template",
        "print_template": "print_template",
        "t": "write_template",
        "write_template": "write_template",
        "j": "write_json",
        "write_json": "write_json",
        "v": "verbose",
        "verbose": "verbose",
        "f": "flags",
        "flags": "flags",
        "y": "hex",
        "hex": "hex"
    }
    result = {k: v for k, v in defaults.items()}
    for arg in args:
        if not isinstance(arg, str):
            continue
        if arg in lookups:
            key = lookups[arg]
            result[key] = found[key]
    return result


def parse(*args, **kwargs):
    """
    Parses data, alternative to running on command line.

    Other Arguments:
        'no_sort' (str, optional): Short form ``'s'``. No sorting of results. Default ``False``
        'no_cache' (str, optional): Short form ``'x'``. No caching. Default ``False``
        'no_print_clear (str, optional): Short form ``'p'``. No clearing of terminal
            when otuput to terminal. Default ``False``
        'long_template' (str, optional): Short form ``'g'``. Writes a long format template.
            Requires write_template is set. Default ``False``
        'clipboard' (str, optional): Short form ``'c'``. Copy to clipboard. Default ``False``
        'flags' (str, optional): Short form ``'f'``. Treat as flags. Default ``False``
        'hex' (str, optional): Short form ``'y```. Treat as hex. Default ``False``
        'print_json' (str, optional): Short form ``'n'``. Print json to termainl. Default ``False``
        'print_template' (str, optional): Short form ``'m'``. Print template to terminal. Default ``False``
        'write_template' (str, optional): Short form ``'t'``. Write template file into obj_uno subfolder. Default ``False``
        'write_json' (str, optional): Short form ``'j'``. Write json file into obj_uno subfolder. Default ``False``
        'verbose' (str, optional): Short form ``'v'``. Verobose output.

    Keyword Arguments:
        url (str): Short form ``u``. url to parse
        log_file (str, optional): Short form ``L``. Log File
    """
    global logger
    pkwargs = _get_parsed_kwargs(**kwargs)
    pargs = _get_parsed_args(*args)
    if logger is None:
        log_args = {}
        if 'log_file' in pkwargs:
            log_args['log_file'] = pkwargs['log_file']
        else:
            log_args['log_file'] = 'const.log'
        if pargs['verbose']:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    p = Parser(
        url=pkwargs['url'],
        sort=pargs['no_sort'],
        cache=pargs['no_cache']
    )
    w = ConstWriter(
        parser=p,
        copy_clipboard=pargs['clipboard'],
        print_template=pargs['print_template'],
        print_json=pargs['print_json'],
        flags=pargs['flags'],
        hex=pargs['hex'],
        write_template=pargs['write_template'],
        write_json=pargs['write_json'],
        write_template_long=pargs['long_template']
    )
    w.write()
# endregion Parse method

def _main():
    # for debugging
    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1KParseTokens.html'
    # sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    # main()
    args = ('v', 'n')
    kwargs = {
        "u": url,
        "log_file": "debug.log"
    }
    parse(*args, **kwargs)

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
    _main()

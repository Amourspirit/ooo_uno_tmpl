#!/usr/bin/env python
import os
import argparse
from typing import Dict, List, NamedTuple, Union
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
            return TYPE_MAP.get(p_type, p_type)

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
        self._print = kwargs.get('print', False)
        self._indent_amt = 4
        self._write_file = kwargs.get('write_file', False)
        self._file_full_path = None

def main():
    p = Parser(url='https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1KeyEvent.html')
    formated = p.get_formated_data()
    print(formated)

if __name__ == '__main__':
    main()
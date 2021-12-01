#!/usr/bin/env python
import os
import argparse
from typing import Dict, List, NamedTuple, Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, SoupStrainer, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, TypeCheckKw
from kwhelp import KwArg, rules
from collections import namedtuple
from base import WriteBase, ParserBase
from pathlib import Path
import textwrap
import xerox # requires xclip - sudo apt-get install xclip

dataitem = namedtuple(
    'dataitem', ['name', 'datatype', 'lines'])


class Parser(ParserBase):
    # region init
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        if not self._url:
            raise ValueError('URL is not set')
        soup = BeautifulSoup(self.get_raw_html(), 'lxml')
        items = self._get_memitems(soup=soup)

    def _get_struct_details(self, memitetms: ResultSet) -> List[dataitem]:
        result = []
        for itm in memitetms:
            # text in format of com::sun::star::awt::AdjustmentType Type
            text: str = itm.find("td", class_='memname',
                                 recursive=True).text.strip().replace('::', '.')
            parts = text.split()
            _type = parts[0]
            name = parts[1]
            
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
    p = Parser(url='https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1AdjustmentEvent.html')
    info = p.get_info()
    print(info)

if __name__ == '__main__':
    main()
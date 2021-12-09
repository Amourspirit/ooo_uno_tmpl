#!/usr/bin/env python
# exception parser
import os
import sys
import argparse
import xsrc
import logging
import re
import base
from typing import Dict, List
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, RequireArgs, TypeCheckKw
from kwhelp import rules
from collections import namedtuple
from pathlib import Path
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
from logger.log_handle import get_logger, LOG_FILE_HANDLER, get_file_handler
from parser import __version__, JSON_ID
import pprint
# some exceptions are Depreciated such as IntrospectionException https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1beans_1_1IntrospectionException.html

logger = get_logger(Path(__file__).stem)
xsrc.logger = logger
base.logger = logger
xsrc.re_component_start = re.compile(r"(exception.*){", re.DOTALL)
xsrc.re_name_info_start = re.compile(r"(exception)\s*[a-zA-Z0-9]+[ :]+")
xsrc.re_name_info_name = re.compile(r"exception\s*(?P<NAME>[a-zA-Z0-9_]+)")

class ParserEx(base.ParserBase):
    # region Constructor
    @RequireArgs('url', ftype=DecFuncEnum.METHOD)
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._api_info = xsrc.ApiInfo(url=self.url)
        self._sdk_method_info = xsrc.SdkMethods(url=self._api_info.sdk_link)
        self._sdk_property_info = xsrc.SdkProperties(
            self._sdk_method_info.component_lines)
        self._sort = True
        self._info = None
        self._cache ={}
    # endregion Constructor

    def get_info(self) -> Dict[str, object]:
        key = 'get_info'
        if key in self._cache:
            return self._cache[key]
        ns = base.UrlObj(self._url)
        start_ln = xsrc.SdkComponentStart(self._sdk_method_info.component)
        ni = xsrc.SdkNameInfo(start_ln)
        ex = xsrc.SdkExtends(start_ln, self._sdk_method_info.component_lines)
        desc = xsrc.ApiDesc(soup=self._api_info.soup)
        result = {
            'name': ni.name,
            'namespace': ns.namespace_str,
            'extends': ex.ex_lst,
            "url": self._api_info.soup.url
        }
        logger.debug('ParserEx.get_info() name: %s', ni.name)
        logger.debug('ParserEx.get_info() namespace: %s',
                     ns.namespace_str)
        self._cache[key] = result
        return self._cache[key]

class WriterEx(base.WriteBase):
    # region Constructor
    @TypeCheckKw(arg_info={
        "write_file": 0, "write_json": 0,
        "copy_clipboard": 0, "print_template": 0,
        "print_json": 0, "clear_on_print": 0,
        "write_template_long": 0
    },
        types=[bool],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser: ParserEx, **kwargs):
        super().__init__(**kwargs)
        self._parser: ParserEx = parser
        self._copy_clipboard: bool = kwargs.get('copy_clipboard', False)
        self._print_template: bool = kwargs.get('print_template', False)
        self._write_file: bool = kwargs.get('write_template', False)
        self._print_json: bool = kwargs.get('print_json', True)
        self._write_json: bool = kwargs.get('write_json', False)
        self._clear_on_print: bool = kwargs.get('clear_on_print', True)
        self._write_template_long: bool = kwargs.get(
            'write_template_long', False)
        self._indent_amt = 4
        self._json_str = None
        self._p_name: str = None
        self._p_namespace: str = None
        self._p_extends: List[str] = None
        self._p_desc: List[str] = None
        self._p_data: str = None
        self._p_url: str = None
        self._p_requires_typing = False
        self._path_dir = Path(os.path.dirname(__file__))
        self._cache: Dict[str, object] = {}

        t_file = 'exception'
        if not self._write_template_long:
            t_file += '_stub'
        t_file += '.tmpl'
        _path = Path(self._path_dir, 'template', t_file)
        try:
            if not _path.exists():
                raise FileNotFoundError(
                    f"unable to find templae file '{_path}'")
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        self._template_file = _path
        self._template: str = self._get_template()
    # endregion Constructor

    def write(self):
        self._set_info()
        self._set_template_data()
        logger.info("Processing %s.%s", self._p_namespace, self._p_name)
        try:
            if self._clear_on_print and (self._print_template or self._print_json):
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

def main():
    logger.removeHandler(LOG_FILE_HANDLER)
    hndl = get_file_handler('debug.log')
    logger.addHandler(hndl)
    logger.level = logging.DEBUG
    url = 'https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1uno_1_1Exception.html'
    p = ParserEx(url=url)
    pprint.pprint(p.get_info())
    
if __name__ == '__main__':
    main()

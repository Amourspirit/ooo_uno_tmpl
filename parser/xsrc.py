#!/usr/bin/env python
import os
import sys
import argparse
from typing import Dict, List
from bs4 import BeautifulSoup
from bs4.element import NavigableString, PageElement, ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, RequireArgs
from kwhelp import rules
from collections import namedtuple
from base import TYPE_MAP, TagsStrObj, WriteBase, ParserBase, SoupObj, UrlObj, BlockObj, str_clean
from pathlib import Path
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
from logger.log_handle import get_logger
from parser.enm import main
from dataclasses import dataclass
from enum import IntEnum
import re
logger = get_logger(Path(__file__).stem)

# region SDK API Reference
re_ln_pattern = re.compile(r"\A\s*(:?[0-9]*)\s*")
# https://regex101.com/r/xAqRAU/1/
re_args_pattern = re.compile(r"\s*(?:\[(\S{2,3})\])?\s*(\S*)\s(\S*)")
# https://regex101.com/r/HU09ZZ/1
re_method_pattern = re.compile(
    r"(\S*)\s*(?:(\S*)\()(?:\s(.*)\))|(\S*)\s*([0-9A-Z-a-z]*)")
# endregion SDK API Reference

@dataclass
class ParamInfo:
    direction: str
    name: str
    type: str

# region SDK API Reference
class CodeText(BlockObj):
    """Responsible for getting code from url"""

    def __init__(self, soup: SoupObj):
        super().__init__(soup=soup)
        self._data = None

    def get_obj(self) -> str:
        if self._data:
            return self._data

        def repl(m):
            multi_line: str = m.group(1)
            lines = multi_line.splitlines(keepends=False)
            return " ".join(lines)
        rows = self._soup.soup.find_all('div', class_='line')
        lines = []
        for row in rows:
            r_text = self._get_row_text(row)
            if r_text:
                lines.append(r_text)
        result = '\n'.join(lines)
        # some methods are are written on several lines. Replace to remove line breaks
        result = re.sub('((?:[a-zA-Z0-9]*)\( .*?\);)',
                        repl, result, flags=re.DOTALL)
        self._data = result
        return self._data

    def _get_row_text(self, row: Tag) -> str:
        # removes line numbers and leading whitespace
        row_text: str = row.text
        ls: str = re.sub(re_ln_pattern, '', row_text)
        return ls


class ComponentText:
    """
    gets the text of the Component area

    Example:
        published interface XWindow: com::sun::star::lang::XComponent
        {
        void setPosSize( [in] long X,
                [in] long Y,
                [in] long Width,
                [in] long Height,
                [in] short Flags );
        com::sun::star::awt::Rectangle getPosSize();
        void setVisible( [in] boolean Visible );
        void setEnable( [in] boolean Enable );
        }
    """

    def __init__(self, c_text: CodeText):
        self._code_text = c_text
        self._data = None

    def get_text(self) -> str:
        if self._data:
            return self._data
        text = self._code_text.get_obj()
        # https://regex101.com/r/xAqRAU/1/
        regex = r"published.*\s\{(\s*?.*?)*?\}"
        matches = re.search(regex, text)
        m = matches[0]
        self._data = m
        return self._data

    @property
    def code_text(self) -> CodeText:
        """Gets code_text value"""
        return self._code_text

class MethodData:
    """Gets the info for a single method"""

    def __init__(self, parm: str):
        self._param = parm
        self._p_name = ''
        self._p_return = ''
        self._p_args: List[ParamInfo] = []
        self._set_data()

    def _set_data(self):
        matches = re.search(re_method_pattern, self._param)
        # when there are parameters
        #   group 0 return type eg: com.sun.star.awt.Rectangle
        #   group 1 method name eg: getPosSize
        #   group 2 string of all params eg: '[in] long X, [in] long Y, [in] long Width, [in] long Height, [in] short Flags '
        #   group 3 None
        #   group 4 None
        # when there are no parameters
        #   group 0 None
        #   group 1 None
        #   group 2 None
        #   group 3 return type eg: void
        #   group 4 method name eg: setFoucs
        # if matches:
        #     groups = matches.groups()
        #     if len(groups)
        if matches:
            g = matches.groups()
            if g[0] is None:
                # no params
                self._p_name = g[4]
                self._p_return = TYPE_MAP.get(g[3], g[3])
            else:
                self._p_name = g[1]
                self._p_return = TYPE_MAP.get(g[0], g[0])
                self._process_args(g[2])
        return matches

    def _process_args(self, args: str):
        a = args.replace(', ', ',').strip()
        arg_lst = a.split(',')
        for arg in arg_lst:
            matches = re.search(re_args_pattern, arg)
            if not matches:
                continue
            g = matches.groups()
            _dir = 'in' if g[0] is None else g[0].lower()
            info = ParamInfo(
                direction=_dir, name=g[2], type=TYPE_MAP.get(g[1], g[1]))
            self._p_args.append(info)

    # region Properties
    @property
    def args(self) -> List[ParamInfo]:
        """Gets Method Args"""
        return self._p_args

    @property
    def name(self) -> str:
        """Gets Method Name"""
        return self._p_name

    @property
    def return_type(self) -> str:
        """Gets method Return Type"""
        return self._p_return

    # endregion Properties


class MethodsText:
    """
    Responsible for getting all lines of Component
    lines have a simple cleaning that replace :: with .
    """

    def __init__(self, f_text: ComponentText):
        self._component = f_text
        self._data = None

    def get_obj(self) -> List[str]:
        if self._data:
            return self._data
        text = self._component.get_text()
        regex = r"\{\s((\s*?.*?)*?)\}"
        matches = re.search(regex, text)
        m = matches[1]
        lines = self._remove_empty(m)
        self._data = self._clean_lines(lines=lines)
        return self._data

    def _remove_empty(self, input: str) -> List[str]:
        lines = input.splitlines(keepends=False)
        return [line for line in lines if line.strip() != '']

    def _clean_lines(self, lines: List[str]) -> List[str]:
        result = []
        for line in lines:
            result.append(line.replace('::', '.'))
        return result

    @property
    def component(self) -> ComponentText:
        """Gets component value"""
        return self._component


class Methods:
    """Iterable class that iterates through Methods and returns info"""

    def __init__(self, url: str):
        self._soup = SoupObj(url=url)
        self._c_text = CodeText(soup=self._soup)
        self._component = ComponentText(c_text=self._c_text)
        self._mt = MethodsText(f_text=self._component)
        self._index = 0
        self._len = 0
        self._init = False
        self._data: List[str] = None

    def __iter__(self):
        return self

    def __next__(self) -> MethodData:
        if not self._init:
            self._data: List[str] = self._mt.get_obj()
            self._len = len(self._data)
            self._init = True
        if self._index >= self._len:
            self._index = 0
            raise StopIteration
        ln = self._data[self._index]
        md = MethodData(ln)
        self._index += 1
        return md

    @property
    def component(self) -> ComponentText:
        """Gets component value"""
        return self._component

    @property
    def code_text(self) -> CodeText:
        """Gets component value"""
        return self._c_text

class Extends:
    def __init__(self, text: ComponentText):
        self._text = text
        self._name = ''
        self._init()
    
    def _init(self):
        regex = r"published\s*interface.*:\s*(com::.*)"
        s = self._text.get_text()
        matches = re.search(regex, s)
        if matches:
            g = matches.groups()
            self._name = g[0].strip().replace('::', '.')

    # region Properties
    @property
    def name(self) -> str:
        """Gets name value"""
        return self._name

    @property
    def component(self) -> ComponentText:
        """Gets component object"""
        return self._text
    # endregion Properties
class Imports:
    """
    Gets imports for interface/class etc
    Fromat: ``com.sun.star.awt.Rectangle``
    """
    def __init__(self, text: CodeText):
        self._text = text
        self._imports: List[str] = None

    def get_obj(self) -> List[str]:
        """
        Gets the imports as a list of strings
        Fromat: ``com.sun.star.awt.Rectangle``

        Returns:
            List[str]: list
        """
        if self._imports:
            return self._imports
        self._imports = []
        
        regex = r"#include\s*<(.*)\.idl"
        test_str = self._text.get_obj()
        matches = re.finditer(regex, test_str)
        for _, match in enumerate(matches, start=1):
            g = match.groups()
            self._process_match(g[0])
        return self._imports

    def _process_match(self, match: str):
        # com/sun/star/lang/XComponent
        s = match.strip()
        parts = s.split('/')
        ns = '.'.join(parts)
        self._imports.append(ns)
    # region Properties
    @property
    def code_text(self) -> CodeText:
        """Gets CodeText value"""
        return self._text
    # endregion Properties
class NamesSpaceInfo:
    def __init__(self, text: CodeText):
        self._text = text
        self._ns = ""
        self._ns_lst = None
        self._init()

    def _init(self) -> str:
        text = self._text.get_obj()
        regex = r"module (com \{.*)\{"
        # regex = r"module com \{  module sun \{  module star \{  module awt \{"
        matches = re.search(regex, text, flags=re.MULTILINE)
        result = []
        if matches:
            result = self._process(matches[0])
        self._ns_lst = result
        self._ns = '.'.join(self._ns_lst)

    def _process(self, input: str) -> List[str]:
        # module com {  module sun {  module star {  module awt
        results = []
        parts = input.split('{')
        for part in parts:
            p = part.split()
            if len(p) >= 2:
                results.append(p[1])
        return results

    # region Properties
    @property
    def namespace(self) -> str:
        """Gets namespace"""
        return self._ns

    @property
    def parts(self) -> List[str]:
        """Gets parts value"""
        return self._ns_lst

    @property
    def code_text(self) -> CodeText:
        """Gets CodeText value"""
        return self._text
    # endregion Properties


class NameInfo:
    """Gets Name of interface/class etc"""
    def __init__(self, text: ComponentText):
        self._text = text
        self._name = ''
        self._init()
    
    def _init(self):
        regex = r"published\s*interface\s*(\S*):"
        s = self._text.get_text()
        matches = re.search(regex, s)
        if matches:
            g = matches.groups()
            self._name = g[0].strip()
    # region Properties
    @property
    def name(self) -> str:
        """Gets name value"""
        return self._name

    @property
    def component(self) -> ComponentText:
        """Gets component object"""
        return self._text
    # endregion Properties

# endregion SDK API Reference

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    # url = 'https://api.libreoffice.org/docs/idl/ref/XWindow_8idl_source.html'
    url = 'https://api.libreoffice.org/docs/idl/ref/XFont_8idl_source.html'
    m = Methods(url=url)
    ns = NamesSpaceInfo(text=m.code_text)
    ni = NameInfo(text=m.component)
    im = Imports(text=m.code_text)
    ex = Extends(text=m.component)
    print(im.get_obj())
    print(ni.name)
    print("Extends:", ex.name)
    
    # for meth in m:
    #     print(meth.name)
    #     print(meth.return_type)
    #     print(meth.args)
    print(ns.namespace)


if __name__ == '__main__':
    main()

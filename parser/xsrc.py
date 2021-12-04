#!/usr/bin/env python
from logging import DEBUG
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

DEBUGGING = True

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
class SdkCodeText(BlockObj):
    """Responsible for getting code from url"""

    def __init__(self, soup: SoupObj):
        super().__init__(soup=soup)
        self._data = None
        if DEBUGGING:
            self._data = get_code_text_data()

    def get_obj(self) -> str:
        if self._data:
            return self._data
        
        print("")
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
        # print("")
        # print("CodeText Data:")
        # print("")
        # print(result)
        return self._data

    def _get_row_text(self, row: Tag) -> str:
        # removes line numbers and leading whitespace
        row_text: str = row.text
        ls: str = re.sub(re_ln_pattern, '', row_text)
        return ls


class SdkComponentText:
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

    def __init__(self, c_text: SdkCodeText):
        self._code_text = c_text
        self._data = None

    def get_text(self) -> str:
        if self._data:
            return self._data
        text = self._code_text.get_obj()
        # https://regex101.com/r/xAqRAU/1/
        # regex = r"published.*\s\{(\s*?.*?)*?\}"
        
        # https://regex101.com/r/xAqRAU/2/
        # much more generic
        regex = r"[a-zA-Z0-9]*\s[a-zA-Z0-9]*:.*\s\{(\s*?.*?)*?\}"
        matches = re.search(regex, text)
        m = matches[0]
        self._data = m
        return self._data

    @property
    def code_text(self) -> SdkCodeText:
        """Gets code_text value"""
        return self._code_text

class SdkMethodData:
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


class SdkMethodsText:
    """
    Responsible for getting all lines of Component
    lines have a simple cleaning that replace :: with .
    """

    def __init__(self, f_text: SdkComponentText):
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
    def component(self) -> SdkComponentText:
        """Gets component value"""
        return self._component


class SdkMethods:
    """Iterable class that iterates through Methods and returns info"""

    def __init__(self, url: str):
        self._soup = SoupObj(url=url)
        self._c_text = SdkCodeText(soup=self._soup)
        self._component = SdkComponentText(c_text=self._c_text)
        self._mt = SdkMethodsText(f_text=self._component)
        self._index = 0
        self._len = 0
        self._init = False
        self._data: List[str] = None

    def __iter__(self):
        return self

    def __next__(self) -> SdkMethodData:
        if not self._init:
            self._data: List[str] = self._mt.get_obj()
            self._len = len(self._data)
            self._init = True
        if self._index >= self._len:
            self._index = 0
            raise StopIteration
        ln = self._data[self._index]
        md = SdkMethodData(ln)
        self._index += 1
        return md

    @property
    def component(self) -> SdkComponentText:
        """Gets component value"""
        return self._component

    @property
    def code_text(self) -> SdkCodeText:
        """Gets component value"""
        return self._c_text

class SdkExtends:
    def __init__(self, text: SdkComponentText):
        self._text = text
        self._name = ''
        self._init()
    
    def _init(self):
        # regex = r"interface.*:\s*(com::.*)"
        
        # more generic so can work with struct, interface etc
        regex = r"[a-zA-Z]*:\s*(com::.*)"
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
    def component(self) -> SdkComponentText:
        """Gets component object"""
        return self._text
    # endregion Properties
class SdkImports:
    """
    Gets imports for interface/class etc
    Fromat: ``com.sun.star.awt.Rectangle``
    """

    def __init__(self, text: SdkCodeText):
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
    def code_text(self) -> SdkCodeText:
        """Gets CodeText value"""
        return self._text
    # endregion Properties
class SdkNamesSpaceInfo:
    def __init__(self, text: SdkCodeText):
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
    def code_text(self) -> SdkCodeText:
        """Gets CodeText value"""
        return self._text
    # endregion Properties


class SdkNameInfo:
    """Gets Name of interface/class etc"""

    def __init__(self, text: SdkComponentText):
        self._text = text
        self._name = ''
        self._init()
    
    def _init(self):      
        # https://regex101.com/r/aNblTo/1/
        # more generic so can work with struct, interface etc
        regex = r"([a-zA-Z0-9]*)\s*:\s*(:?::)?com::"
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
    def component(self) -> SdkComponentText:
        """Gets component object"""
        return self._text
    # endregion Properties

# endregion SDK API Reference

# region Main Page Parsing


@dataclass
class MethodBlockInfo:
    tag_id: Tag
    tag_title: Tag
    tag_main: Tag

class MethodBlock:
    def __init__(self, block: Tag, blocks: 'MethodBlocks'):
        self._block: Tag = block
        self._blocks: MethodBlocks = blocks
        self._data = None

    def _get_next_sibling(self, el: PageElement) -> PageElement:
        # get the next sibling recursivly because
        # BeautifulSoup will also find whitesapce on next_sibling
        if not isinstance(el, PageElement):
            raise TypeError(
                f"MethodBlock._get_next_sibling() el is not a PageElement")
        next = el.next_sibling
        # https://stackoverflow.com/questions/10711116/strip-spaces-tabs-newlines-python
        # use split join to remove whitespace and new line
        s = ''.join(str(next).split())
        if s == '':
            next = self._get_next_sibling(next)
        return next

    def get_obj(self) -> MethodBlockInfo:
        # BeautifulSoup will also find whitesapce on next_sibling
        # https://stackoverflow.com/questions/5690686/using-nextsibling-from-beautifulsoup-outputs-nothing
        if self._data:
            return self._data
        tag = self._block  # a tag with id
        try:
            title: PageElement = self._get_next_sibling(tag)
            main = self._get_next_sibling(title)
            mi = MethodBlockInfo(
                tag_id=tag,
                tag_title=title,
                tag_main=main
            )
        except Exception as e:
            logger.error(e)
            raise e
        self._data = mi
        return self._data

    def is_valid(self) -> bool:
        if not self._block:
            return False
        tag = self._block
        _id = tag.attrs.get('id', None)
        if not _id:
            return False
        if str(_id).lower() == 'details':
            return False
        return True

    @property
    def blocks(self) -> 'MethodBlocks':
        """
        Gets MethodBlocks instance that generated this instance.
        """
        return self._blocks

class MethodBlocks(BlockObj):
    """Get all methods"""

    def __init__(self, url:str):
        soup = SoupObj(url=url)
        super().__init__(soup=soup)
        self._obj_data = None
        self._index = 0
        self._len = 0

    def get_obj(self) -> ResultSet:
        """
        Gets all items, methods etc

        Returns:
            ResultSet: List of items
        """
        if self._obj_data:
            return self._obj_data
        # _cls = 'memitem'
        self._obj_data = self._soup.soup.select("a[id]")

        return self._obj_data

    def _get_next(self) -> MethodBlock:
        if self._index >= self._len:
            self._index = 0
            self._cur_obj = None
            raise StopIteration
        itm = self._obj_data[self._index]
        self._index += 1
        mb = MethodBlock(block=itm, blocks=self)
        if not mb.is_valid():
            mb = self._get_next()
        return mb

    def __iter__(self):
        return self

    def __next__(self) -> MethodBlock:
        if not self._obj_data:
            self.get_obj()
            self._len = len(self._obj_data)
        return self._get_next()


class PageMethodName:
    def __init__(self, block: MethodBlock):
        self._block: MethodBlock = block

    def get_obj(self) -> str:
        info = self._block.get_obj()
        name: str = info.tag_title.contents[1]
        name = name.replace('(', '').replace(')', '').strip()
        return name
class PageMethodDesc:
    """Gets Enum Description"""

    def __init__(self, block: MethodBlock):
        self._block = block
        self._cls = 'memdoc'
        self._el = 'div'

    def get_data(self) -> str:
        info = self._block.get_obj()
        tag = info.tag_main.find(self._el, class_=self._cls)
        lines_found: ResultSet = tag.select(f'{self._el}.{self._cls} > p')
        p_obj = TagsStrObj(tags=lines_found)
        desc = p_obj.get_data()
        return desc


class PageSDKLink:
    def __init__(self, soup: SoupObj):
        self._soup = soup
    
    def get_obj(self):
        a = self._soup.soup.select_one("body > div.contents > ul > li > a")
        url = self._soup.url
        parts = url.rsplit('/', 1)
        return parts[0] + '/' + a['href']

    @property
    def soup(self) -> SoupObj:
        """Gets SoupObj instance for this instance"""
        return self._soup

class PageInfo:
    def __init__(self, url: str):
        self._url = url
        self._sdk_link = ''
        self._dict = {}
        self._mb = MethodBlocks(url=self._url)
        self._init()
    
    def _init(self):
        lnk = PageSDKLink(soup=self.soup)
        self._sdk_link = lnk.get_obj()
        for block in self._mb:
            name = PageMethodName(block=block)
            desc = PageMethodDesc(block=block)
            self._dict[name.get_obj()] = desc.get_data()
    
    @property
    def desc_dict(self) -> Dict[str, str]:
        """Dictionary that contains descriptions. Key is method name"""
        return self._dict
    
    @property
    def sdk_link(self) -> str:
        """Gets sdk_link value"""
        return self._sdk_link
    
    @property
    def soup(self) -> SoupObj:
        """Gets SoupObj instance for this instance"""
        return self._mb.soup
    
    @property
    def method_blocks(self) -> MethodBlocks:
        """Gets method_blocks value"""
        return self._mb
# endregion Main Page Parsing

def main2():
    os.system('cls' if os.name == 'nt' else 'clear')
    url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XFont.html'
    m_blocks = MethodBlocks(url=url)
    lnk = PageSDKLink(soup=m_blocks.soup)
    print(lnk.get_obj())
    return
    # body > div.contents > ul > li > a
    for block in m_blocks:
        info = block.get_obj()
        name = PageMethodName(block=block)
        desc = PageMethodDesc(block=block)
        print(name.get_obj())
        print(desc.get_data())
        # print("tag",info.tag_id)
        # print("main", info.tag_main)
        # print("title",info.tag_title)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    # url = 'https://api.libreoffice.org/docs/idl/ref/XWindow_8idl_source.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/XFont_8idl_source.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XFont.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1media_1_1XPlayerWindow.html'
    url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.html'
    p_info = PageInfo(url=url)
    m = SdkMethods(url=p_info.sdk_link)
    ns = SdkNamesSpaceInfo(text=m.code_text)
    ni = SdkNameInfo(text=m.component)
    im = SdkImports(text=m.code_text)
    ex = SdkExtends(text=m.component)
    # print(im.get_obj())
    print(ni.name)
    print("Extends:", ex.name)
    print("Namespace:",ns.namespace)
    
    for meth in m:
        print("name:" ,meth.name)
        print("return type:",meth.return_type)
        print("args:", meth.args)
        print("Desc:", p_info.desc_dict.get(meth.name, ''))


def get_code_text_data():
    result = """
CodeText Data:

/* -*- Mode: C++; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- */
/*
* This file is part of the LibreOffice project.
*
* This Source Code Form is subject to the terms of the Mozilla Public
* License, v. 2.0. If a copy of the MPL was not distributed with this
* file, You can obtain one at http://mozilla.org/MPL/2.0/.
*
* This file incorporates work covered by the following license notice:
*
*   Licensed to the Apache Software Foundation (ASF) under one or more
*   contributor license agreements. See the NOTICE file distributed
*   with this work for additional information regarding copyright
*   ownership. The ASF licenses this file to you under the Apache
*   License, Version 2.0 (the "License"); you may not use this file
*   except in compliance with the License. You may obtain a copy of
*   the License at http://www.apache.org/licenses/LICENSE-2.0 .
*/
#ifndef __com_sun_star_beans_XHierarchicalPropertySet_idl__
#define __com_sun_star_beans_XHierarchicalPropertySet_idl__
#include <com/sun/star/uno/XInterface.idl>
#include <com/sun/star/beans/XHierarchicalPropertySetInfo.idl>
#include <com/sun/star/beans/UnknownPropertyException.idl>
#include <com/sun/star/beans/PropertyVetoException.idl>
#include <com/sun/star/lang/IllegalArgumentException.idl>
#include <com/sun/star/lang/WrappedTargetException.idl>
module com {  module sun {  module star {  module beans {
published interface XHierarchicalPropertySet: com::sun::star::uno::XInterface
{
com::sun::star::beans::XHierarchicalPropertySetInfo
getHierarchicalPropertySetInfo();
void setHierarchicalPropertyValue( [in] string aHierarchicalPropertyName, [in] any aValue ) raises( com::sun::star::beans::UnknownPropertyException, com::sun::star::beans::PropertyVetoException, com::sun::star::lang::IllegalArgumentException, com::sun::star::lang::WrappedTargetException );
any getHierarchicalPropertyValue( [in] string aHierarchicalPropertyName ) raises( com::sun::star::beans::UnknownPropertyException, com::sun::star::lang::IllegalArgumentException, com::sun::star::lang::WrappedTargetException );
};
}; }; }; };
#endif    
"""
    return result

if __name__ == '__main__':
    main()

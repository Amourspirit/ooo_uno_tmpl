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

re_ln_pattern = re.compile(r"\A\s*(:?[0-9]*)\s*")
# https://regex101.com/r/xAqRAU/1/
re_args_pattern = re.compile(r"\s*(?:\[(\S{2,3})\])?\s*(\S*)\s(\S*)")
# https://regex101.com/r/HU09ZZ/1
re_method_pattern = re.compile(
    r"(\S*)\s*(?:(\S*)\()(?:\s(.*)\))|(\S*)\s*([0-9A-Z-a-z]*)")


@dataclass
class ParamInfo:
    direction: str
    name: str
    type: str


class CodeText(BlockObj):
    def __init__(self, soup: SoupObj):
        super().__init__(soup=soup)
        self._data = """
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
#ifndef __com_sun_star_awt_XWindow_idl__
#define __com_sun_star_awt_XWindow_idl__
#include <com/sun/star/lang/XComponent.idl>
#include <com/sun/star/awt/Rectangle.idl>
#include <com/sun/star/awt/XWindowListener.idl>
#include <com/sun/star/awt/XFocusListener.idl>
#include <com/sun/star/awt/XKeyListener.idl>
#include <com/sun/star/awt/XMouseListener.idl>
#include <com/sun/star/awt/XMouseMotionListener.idl>
#include <com/sun/star/awt/XPaintListener.idl>
module com {  module sun {  module star {  module awt {
published interface XWindow: com::sun::star::lang::XComponent
{
void setPosSize( [in] long X, [in] long Y, [in] long Width, [in] long Height, [in] short Flags );
com::sun::star::awt::Rectangle getPosSize();
void setVisible( [in] boolean Visible );
void setEnable( [in] boolean Enable );
void setFocus();

void addWindowListener( [in] com::sun::star::awt::XWindowListener xListener );

void removeWindowListener( [in] com::sun::star::awt::XWindowListener xListener );
void addFocusListener( [in] com::sun::star::awt::XFocusListener xListener );
void removeFocusListener( [in] com::sun::star::awt::XFocusListener xListener );
void addKeyListener( [in] com::sun::star::awt::XKeyListener xListener );
void removeKeyListener( [in] com::sun::star::awt::XKeyListener xListener );
void addMouseListener( [in] com::sun::star::awt::XMouseListener xListener );
void removeMouseListener( [in] com::sun::star::awt::XMouseListener xListener );
void addMouseMotionListener( [in] com::sun::star::awt::XMouseMotionListener xListener );
void removeMouseMotionListener( [in] com::sun::star::awt::XMouseMotionListener xListener );
void addPaintListener( [in] com::sun::star::awt::XPaintListener xListener );
void removePaintListener( [in] com::sun::star::awt::XPaintListener xListener );
};
}; }; }; };
#endif
/* vim:set shiftwidth=4 softtabstop=4 expandtab: */
        """

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
        self._obj_text = c_text
        self._data = None

    def get_text(self) -> str:
        if self._data:
            return self._data
        text = self._obj_text.get_obj()
        # https://regex101.com/r/xAqRAU/1/
        regex = r"published.*\s\{(\s*?.*?)*?\}"
        matches = re.search(regex, text)
        m = matches[0]
        self._data = m
        return self._data


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
        self._obj_text = f_text
        self._data = None

    def get_obj(self) -> List[str]:
        if self._data:
            return self._data
        text = self._obj_text.get_text()
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

class Methods:
    def __init__(self, url:str):
        self._soup = SoupObj(url=url)
        c_text = CodeText(soup=self._soup)
        t_component = ComponentText(c_text=c_text)
        self._mt = MethodsText(f_text=t_component)
        self._index = 0
        self._len = 0
        self._init = False
        self._data:List[str] = None

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
    
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    url = 'https://api.libreoffice.org/docs/idl/ref/XWindow_8idl_source.html'
    m = Methods(url=url)
    for meth in m:
        print(meth.name)
        print(meth.return_type)
        print(meth.args)
 


if __name__ == '__main__':
    main()

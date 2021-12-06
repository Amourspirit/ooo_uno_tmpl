#!/usr/bin/env python
import logging
import pprint
from logging import DEBUG
import os
import sys
import argparse
import textwrap
from typing import Dict, List, Set, Tuple
from bs4 import BeautifulSoup
from bs4.element import PageElement, ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, RequireArgs
from kwhelp import rules
from base import TYPE_MAP, TagsStrObj, ParserBase, SoupObj, BlockObj, Util, WriteBase
from pathlib import Path
import xerox  # requires xclip - sudo apt-get install xclip
from logger.log_handle import get_logger
from parser.enm import main
from dataclasses import dataclass
import re

DEBUGGING = False

logger = get_logger(Path(__file__).stem)

# region SDK API Reference
re_ln_pattern = re.compile(r"\A\s*(:?[0-9]*)\s*")
# https://regex101.com/r/xAqRAU/1/
re_args_pattern = re.compile(r"\s*(?:\[(\S{2,3})\])?\s*(\S*)\s(\S*)")
# https://regex101.com/r/HU09ZZ/1
re_method_pattern = re.compile(
    r"(\S*)\s*(?:(\S*)\()(?:\s(.*)\))|(\S*)\s*([0-9A-Z-a-z]*)")
# https://regex101.com/r/BdDT4u/1
re_raises_pattern = re.compile(r"\s*(raises\s*\(.*\))")

re_interface_pattern = re.compile(r"interface\s*([a-zA-Z0-9.]*)\s*;")
re_property_pattern = re.compile(r"(?:\[attribute\])(?:[ ]+)([a-zA-Z0-9. {}()]*);")
# endregion SDK API Reference


@dataclass
class ParamInfo:
    direction: str
    name: str
    type: str

# region Exceptions


class MethodInvalidError(Exception):
    pass
# endregion Exceptions

# region SDK API Reference


class SdkCodeText(BlockObj):
    """Responsible for getting code from url"""

    def __init__(self, soup: SoupObj):
        super().__init__(soup=soup)
        self._data = None
        # if DEBUGGING:
        #     self._data = get_code_text_data()

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
        # xerox.copy(result)
        # some methods are are written on several lines. Replace to remove line breaks
        # result = re.sub(r'((?:[a-zA-Z0-9]*)\( .*?\);)',
        #                 repl, result, flags=re.DOTALL)
        self._data = result
        # logger.debug('SdkCodeText.get_ojb() data:\n%s', self._data)
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
        # https://regex101.com/r/xAqRAU/4/
        # much more generic
        # regex = r"[a-zA-Z0-9 :]*\n\{(\s*?.*?)*?\}"
        # matches = re.search(regex, text)
        
        regex_start = r"module (com \{.*)\{"
        regex_end = r"}; (?:[ ;}])*\n#endif"
        matches_start = re.search(regex_start, text)
        matches_end = re.search(regex_end, text)
        if matches_start and matches_end:
            # print(matches)
            print(matches_start.span())
            start = matches_start.span()[1]
            end = matches_end.span()[0]
            self._data = text[start:end].strip()
        # if matches:
        #     m = matches[0]
        #     self._data = m
        # else:
        #     # https://regex101.com/r/cYL6hj/1
        #     # matches when component is not extendes ( no trailing : ...)
        #     regex = r"[a-zA-Z0-9]*\s[a-zA-Z0-9]*.*\s\{(\s*?.*?)*?\}"
        #     matches = re.search(regex, text)
        #     if matches:
        #         m = matches[0]
        #         self._data = m
        if not self._data:
            self._data = ''
        # cleans out [atribute]
        # regex = r"\[(:?[a-zA-Z]*)\](?:[ ]*)"
        # self._data = re.sub(regex,'', self._data)
        logger.debug('Componnent text:\n%s', self._data)
        return self._data

    @property
    def code_text(self) -> SdkCodeText:
        """Gets code_text value"""
        return self._code_text


class SdkComponentLines:
    """
    Responsible for getting all lines of Component.
    Lines have a simple cleaning that replace :: with .
    """

    def __init__(self, f_text: SdkComponentText):
        self._component = f_text
        self._data = None

    def get_obj(self) -> List[str]:
        if self._data:
            return self._data
        text = self._component.get_text()
        # text includes name and {} such as interface XHierarchicalPropertySet: com::sun::star::uno::XInterface\n{...\n}
        # remove the outter text
        # inner_re = r"\{(.*)\}"
        # matches = re.search(inner_re, text, flags=re.DOTALL)
        inner_re = r"[{]((?:[^{}]*|[{][^{}]*[}])*)[}]"
        matches = re.search(inner_re, text)
        if matches:
            g = matches.groups()
            text = g[0]
        text = self._get_proper_lines(input=text)
        lines = self._remove_empty(text)
        self._data = self._clean_lines(lines=lines)
        if logger.level <= logging.DEBUG:
            logger.debug('SdkComponentLines.get_obj data:\n%s',
                         '\n'.join(self._data))
        return self._data

    def _get_proper_lines(self, input: str) -> str:
        if not input:
            return ''
        # methods may be split across multiple lines.
        # start by collapsing all lines into a single line
        single_line = " ".join(input.splitlines()).strip()
        # logger.debug('single Line\n%s', single_line)
        # bit of a hack here but best fix I can find so far
        # fixes parsing issue when interface such as:
        # https://api.libreoffice.org/docs/idl/ref/XAnimatedImages_8idl_source.html
        single_line = Util.encode_char(single_line, '); }')

        # now split all lines by ; and put on new lines again
        new_lines = ";\n".join(single_line.split(';'))
        return Util.decode_char(new_lines, '); }')
        # return new_lines

    def _remove_empty(self, input: str) -> List[str]:
        lines = input.splitlines(keepends=False)
        return [line.strip() for line in lines if line.strip() != '']

    def _clean_lines(self, lines: List[str]) -> List[str]:
        result = []
        for line in lines:
            result.append(line.replace('::', '.'))
        return result

    @property
    def component(self) -> SdkComponentText:
        """Gets component value"""
        return self._component

class SdkMethodLines:
    def __init__(self, c_lines: SdkComponentLines) -> None:
        self._c_lines = c_lines
        self._data = None
    
    def get_obj(self) -> List[str]:
        if self._data:
            return self._data
        results: List[str] = []
        lines = self._c_lines.get_obj()
        for line in lines:
            match = re.match(re_interface_pattern, line)
            if match:
                continue
            match = re.match(re_property_pattern, line)
            if match:
                continue
            match = re.match(re_method_pattern, line)
            if match:
                results.append(line)
        self._data = results
        if logger.level <= logging.DEBUG:
            logger.debug("SdkMethodLines.get_obj() data:\n%s", "\n".join(self._data))
        return self._data
    
    @property
    def component_lines(self) -> SdkComponentLines:
        """Gets component_lines value"""
        return self._c_lines


class SdkPropertyLines:
    def __init__(self, c_lines: SdkComponentLines) -> None:
        self._c_lines = c_lines
        self._data = None

    def get_obj(self) -> List[str]:
        if self._data:
            return self._data
        results: List[str] = []
        lines = self._c_lines.get_obj()
        for line in lines:
            match = re.match(re_property_pattern, line)
            if match:
                results.append(line)
        self._data = results
        if logger.level <= logging.DEBUG:
            logger.debug("SdkMethodLines.get_obj() data:\n%s",
                         "\n".join(self._data))
        return self._data

    @property
    def component_lines(self) -> SdkComponentLines:
        """Gets component_lines value"""
        return self._c_lines

class SdkMethodData:
    """Gets the info for a single method"""

    def __init__(self, parm: str):
        self._param = parm
        self._p_name = ''
        self._p_return = ''
        self._p_args: List[ParamInfo] = []
        self._p_raises: List[str] = []
        self._imports: Set[str] = set()
        self._requires_typing = False
        self._set_data()

    def _set_data(self):
        is_py_type = True

        def cb(data: dict):
            nonlocal is_py_type
            is_py_type = data['is_py_type']
            if not is_py_type:
                self._imports.add(data['type'])
            if data['is_typing']:
                self._requires_typing = True
        text = self._param
        matches = re.search(re_interface_pattern, text)
        if matches:
            logger.debug("SdkMethodData data matched interface. Raising error")
            raise MethodInvalidError(f"'{text}' matches interface")
        matches = re.search(re_property_pattern, text)
        if matches:
            logger.debug("SdkMethodData data matched property. Raising error")
            raise MethodInvalidError(f"'{text}' matches property")

        seq_regex = r"([a-zA-Z]*)< *([a-zA-A0-9]*) *>"
        m = re.match(seq_regex, text)
        if m:
            # replace sequence< string > with sequence<string>
            # this is necessary to prevent following steps from parsing incorectly
            text = re.sub(seq_regex, f'{m.group(1)}<{m.group(2)}>', text, 1)
        # check if method include raises...
        matches = re.search(re_raises_pattern, text)
        if matches:
            g = matches.groups()
            self._process_raises(g[0])
            # remove raises text section
            text = re.sub(re_raises_pattern, '', text)
        matches = re.search(re_method_pattern, text)
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
                result = Util.get_py_type(g[3], cb=cb)
                if is_py_type:
                    self._p_return = result
                else:
                    self._p_return = f"'{result}'"
            else:
                self._p_name = g[1]
                self._p_name = g[4]
                result = Util.get_py_type(g[0], cb=cb)
                if is_py_type:
                    self._p_return = result
                else:
                    self._p_return = f"'{result}'"
                
                self._process_args(g[2])
        return matches

    def _process_raises(self, text: str):
        # raises( com::sun::star::beans::UnknownPropertyException, com::sun::star::lang::IllegalArgumentException, com::sun::star::lang::WrappedTargetException )
        s = text.replace('(', '|').replace(')', '|').split('|')
        if len(s) <= 1:
            return
        ex = s[1].strip().replace('::', ".").replace(' ', '').replace('.com.', 'com.').split(',')
        self._p_raises.extend(ex)

    def _process_interface(self, text: str):
        # interface com::sun::star::beans::XPropertySet
        parts = text.strip().replace("::", '.').rsplit(
            '.', 1)  # 'com.sun.star.beans', 'XPropertySet'
        return

    def _process_args(self, args: str):
        is_py_type = True

        def cb(data: dict):
            nonlocal is_py_type
            is_py_type = data['is_py_type']
            if not is_py_type:
                self._imports.add(data['type'])
            if data['is_typing']:
                self._requires_typing = True
        logger.debug("SdkMethodData._process_args() Processing args: %s", args)
        a = args.replace(', ', ',').strip()
        arg_lst = a.split(',')
        for arg in arg_lst:
            is_py_type = True
            matches = re.search(re_args_pattern, arg)
            if not matches:
                continue
            g = matches.groups()
            _dir = 'in' if g[0] is None else g[0].lower()
            stype = Util.get_py_type(g[1], cb=cb)
            if not is_py_type:
                stype = f"'{stype}'"
            info = ParamInfo(
                direction=_dir, name=g[2], type=stype)
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

    @property
    def raises(self) -> List[str]:
        """Gets raises value"""
        return self._p_raises
    
    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        return self._imports

    @property
    def requires_typing(self) -> bool:
        """Gets requires_typing value"""
        return self._requires_typing
    # endregion Properties
class SdkProperyData:
    """Gets the info for a single method"""

    def __init__(self, parm: str):
        self._param = parm
        self._p_name = ''
        self._p_return = ''
        self._p_set_raises: List[str] = []
        self._p_get_raises: List[str] = []
        self._imports: Set[str] = set()
        self._requires_typing = False
        self._set_data()

    def _set_data(self):
        is_py_type = True
        def cb(data: dict):
            nonlocal is_py_type
            is_py_type = data['is_py_type']
            if not is_py_type:
                self._imports.add(data['type'])
            if data['is_typing']:
                self._requires_typing = True
        text = self._param
        # remove [attribute] from start of string
        regex = r"\[(:?[a-zA-Z<]*)\] *"
        text = re.sub(regex, '', text, 1)
   
        # check if method include raises...
        matches = re.search(re_raises_pattern, text)
        if matches:
            g = matches.groups()
            self._process_raises(g[0])
            # remove raises text section
            text = re.sub(re_raises_pattern, '', text)
        parts = text.split(maxsplit=2)
        result = Util.get_py_type(parts[0], cb=cb)
        if is_py_type:
            self._p_return = result
        else:
            self._p_return = f"'{result}'"
        self._p_name = Util.get_clean_name(parts[1])


    def _process_raises(self, text: str):
        # { set raises (::com::sun::star::lang::IllegalArgumentException, com::sun::star::beans::UnknownPropertyException); };
        s = text.replace('::', '.').replace('{', '').replace('}', '').strip()
        s = s.replace('.com.', 'com.')
        # set raises (com.sun.star.lang.IllegalArgumentException, com.sun.star.beans.UnknownPropertyException);
        parts = s.replace('(', '|').replace(')', '|').rsplit('|', 2)
        if len(parts) <= 1:
            return
        
        ex = parts[1].strip().replace(' ', '').split(',')
        if parts[0].split()[0] == 'get':
            self._p_get_raises.extend(ex)
        else:
            self._p_set_raises.extend(ex)

    # region Properties

    @property
    def name(self) -> str:
        """Gets Method Name"""
        return self._p_name

    @property
    def return_type(self) -> str:
        """Gets method Return Type"""
        return self._p_return

    @property
    def raises_get(self) -> List[str]:
        """Gets raises values for property get"""
        return self._p_get_raises

    @property
    def raises_set(self) -> List[str]:
        """Gets raises values for property set"""
        return self._p_set_raises

    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        return self._imports
    @property
    def requires_typing(self) -> bool:
        """Gets requires_typing value"""
        return self._requires_typing
    # endregion Properties

class SdkInterfaceData:
    def __init__(self, text: SdkComponentLines):
        self._text = text
        self._data = None

    def get_obj(self) -> List[str]:
        if self._data:
            return self._data
        self._data = []
        lines = self._text.get_obj()
        for line in lines:
            matches = re.search(re_interface_pattern, line)
            if matches:
                g = matches.groups()
                self._data.append(g[0].strip())
        return self._data


class SdkMethods:
    """Iterable class that iterates through Methods and returns info"""

    def __init__(self, url: str):
        self._soup = SoupObj(url=url)
        self._c_text = SdkCodeText(soup=self._soup)
        self._component = SdkComponentText(c_text=self._c_text)
        self._mt = SdkComponentLines(f_text=self._component)
        self._method_lines = SdkMethodLines(c_lines=self._mt)
        self._index = 0
        self._len = 0
        self._init = False
        self._data: List[str] = None

    def _get_next(self) -> SdkMethodData:
        if self._index >= self._len:
            self._index = 0
            raise StopIteration
        ln = self._data[self._index]
        self._index += 1
        try:
            md = SdkMethodData(ln)
        except MethodInvalidError:
            md = self._get_next()
        return md

    def __iter__(self):
        return self

    def __next__(self) -> SdkMethodData:
        if not self._init:
            self._data: List[str] = self._method_lines.get_obj()
            self._len = len(self._data)
            self._init = True
        return self._get_next()

    @property
    def component(self) -> SdkComponentText:
        """Gets component value"""
        return self._component

    @property
    def code_text(self) -> SdkCodeText:
        """Gets component value"""
        return self._c_text

    @property
    def component_lines(self) -> SdkComponentLines:
        return self._mt
class SdkProperties:
    """Iterable class that iterates through Properties and returns info"""

    def __init__(self, c_lines: SdkComponentLines):
        self._c_lines = c_lines
        self._property_lines: SdkPropertyLines = SdkPropertyLines(c_lines=self._c_lines)
        self._index = 0
        self._len = 0
        self._init = False
        self._data: List[str] = None

    def _get_next(self) -> SdkProperyData:
        if self._index >= self._len:
            self._index = 0
            raise StopIteration
        ln = self._data[self._index]
        self._index += 1
        return SdkProperyData(ln)

    def __iter__(self):
        return self

    def __next__(self) -> SdkProperyData:
        if not self._init:
            self._data: List[str] = self._property_lines.get_obj()
            self._len = len(self._data)
            self._init = True
        return self._get_next()

    @property
    def component_lines(self) -> SdkComponentLines:
        return self._c_lines


class SdkExtends:
    def __init__(self, c_text: SdkComponentText, m_text: SdkComponentLines):
        self._c_text: SdkComponentText = c_text
        self._m_text: SdkComponentLines = m_text
        self._ex_lst: List[str] = []
        self._i_data: SdkInterfaceData = SdkInterfaceData(text=m_text)
        self._init()

    def _init(self):
        lines = self._c_text.get_text().splitlines()
        if len(lines) == 0:
            return
        s = lines[0]
        logger.debug("SdkExtends._init() First Line: %s", s)
        # published interface XFont: com::sun::star::uno::XInterface
        s = s.replace('::', ".")
        logger.debug("SdkExtends._init() Replaced :: %s", s)
        parts = s.rsplit(sep=':', maxsplit=1)
        if len(parts) > 1:
            logger.debug("SdkExtends._init() No ':' seperator Did not find extends on first line.")
            s = parts[1]
            logger.debug("SdkExtends._init() Processing: '%s'", s)
            s = Util.get_clean_ns(s)
            self._ex_lst.append(s)
            logger.debug("SdkExtends._init() Added Extends: '%s'", s)

        logger.debug("SdkExtends._init() Processing lines for interfaces.")
        lines = self._m_text.get_obj()
        for line in lines:
            logger.debug("SdkExtends._init() Processing line: %s", line)
            if re_interface_pattern.match(line):
                logger.debug("SdkExtends._init() Found interface Match")
                # interface .com.sun.star.container.XContainer;
                s = line.rsplit(maxsplit=1)[1].lstrip('.')
                s = Util.get_clean_ns(s)
                self._ex_lst.append(s)
                logger.debug("SdkExtends._init() Added Extends: '%s'", s)

    # region Properties
    @property
    def name(self) -> str:
        """Gets name value"""
        return self._name

    @property
    def ex_lst(self) -> List[str]:
        """Gets ex_lst value"""
        return self._ex_lst

    @property
    def component(self) -> SdkComponentText:
        """Gets component object"""
        return self._c_text

    @property
    def method_text(self) -> SdkComponentLines:
        """Gets CodeText value"""
        return self._m_text
    # endregion Properties


class SdkImports:
    """
    Gets imports for interface/class etc
    Fromat: ``com.sun.star.awt.Rectangle``
    """

    def __init__(self, c_lines: SdkComponentLines):
        self._c_lines = c_lines
        self._imports: Set[str] = None

    def get_obj(self) -> Set[str]:
        """
        Gets the imports as a list of strings
        Fromat: ``com.sun.star.awt.Rectangle``

        Returns:
            List[str]: list
        """
        if self._imports:
            return self._imports
        self._imports = set()
        # interface ::com::sun::star::container::XContainer;
        regex = r"interface +([a-zA-Z0-9\.]*)"
        # group ::com::sun::star::container::XContainer
        lines = self._c_lines.get_obj()
        for line in lines:
            logger.debug("SdkImports.get_obj() Processing Line: %s", line)
            matches = re.search(regex, line)
            if matches:
                g = matches.groups()
                logger.debug(
                    'SdkImports.get_obj() Found Interface Line. Groups info: %s', str(g))
                logger.debug('SdkImports.get_obj() Found Interface Line: %s', g[0])
                s = g[0].lstrip('.')
                s = Util.get_clean_ns(s)
                logger.debug(
                    "SdkImports.get_obj() adding Import: '%s'", s)
                self._imports.add(s)

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
        return self._c_text

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
        # https://regex101.com/r/aNblTo/2/
        # https://regex101.com/r/aNblTo/3/
        # more generic so can work with struct, interface etc
        regex = r"([a-zA-Z0-9 :]*)\n\{"
        s = self._text.get_text()
        matches = re.search(regex, s)
        if matches:
            g = matches.groups()
            s: str = g[0]
            # published interface XFont: ::com::sun::star::uno::XInterface
            # or
            # published interface XPropertyBag
            s = s.replace(' ::com', ' com').replace('::', '.')
            # published interface XFont: com.sun.star.unoXInterface

            s = s.split(':', 1)[0]
            # published interface XFont
            self._name = s.rsplit(maxsplit=1)[1].strip()
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


class ApiMethodBlock:
    def __init__(self, block: Tag, blocks: 'ApiMethodBlocks'):
        self._block: Tag = block
        self._blocks: ApiMethodBlocks = blocks
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
    def blocks(self) -> 'ApiMethodBlocks':
        """
        Gets MethodBlocks instance that generated this instance.
        """
        return self._blocks


class ApiMethodBlocks(BlockObj):
    """Get all methods"""

    def __init__(self, url: str):
        soup = SoupObj(url=url)
        if DEBUGGING:
            soup._soup = BeautifulSoup(get_soup_data(), 'lxml')
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

    def _get_next(self) -> ApiMethodBlock:
        if self._index >= self._len:
            self._index = 0
            self._cur_obj = None
            raise StopIteration
        itm = self._obj_data[self._index]
        self._index += 1
        mb = ApiMethodBlock(block=itm, blocks=self)
        if not mb.is_valid():
            mb = self._get_next()
        return mb

    def __iter__(self):
        return self

    def __next__(self) -> ApiMethodBlock:
        if not self._obj_data:
            self.get_obj()
            self._len = len(self._obj_data)
        return self._get_next()


class ApiMethodName:
    def __init__(self, block: ApiMethodBlock):
        self._block: ApiMethodBlock = block

    def get_obj(self) -> str:
        info = self._block.get_obj()
        name: str = info.tag_title.contents[1]
        name = name.replace('(', '').replace(')', '').strip()
        return name


class ApiMethodDesc:
    """Gets Method Description"""

    def __init__(self, block: ApiMethodBlock):
        self._block = block
        self._cls = 'memdoc'
        self._el = 'div'

    def get_data(self) -> List[str]:
        info = self._block.get_obj()
        tag = info.tag_main.find(self._el, class_=self._cls)
        lines_found: ResultSet = tag.select(f'{self._el}.{self._cls} > p')
        p_obj = TagsStrObj(tags=lines_found)
        return p_obj.get_lines()


class ApiSdkLink:
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


class ApiDesc:
    """Gets the description"""
    def __init__(self, soup:SoupObj):
        self._soup = soup
        self._data = None

    def get_obj(self) -> List[str]:
        """
        Gets description as list of str

        Returns:
            List[str]: description lines
        """
        if self._data:
            return self._data
        lines_found: ResultSet = self._soup.soup.select(
            'body > div.contents > div.textblock > p')
        p_obj = TagsStrObj(tags=lines_found)
        self._data = p_obj.get_lines()
        return self._data
        
        
class ApiInfo:
    def __init__(self, url: str):
        self._url = url
        self._sdk_link = ''
        self._dict = {}
        self._mb = ApiMethodBlocks(url=self._url)
        self._init()

    def _init(self):
        lnk = ApiSdkLink(soup=self.soup)
        self._sdk_link = lnk.get_obj()
        for block in self._mb:
            name = ApiMethodName(block=block)
            desc = ApiMethodDesc(block=block)
            self._dict[name.get_obj()] = desc.get_data()

    @property
    def desc_dict(self) -> Dict[str, List[str]]:
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
    def method_blocks(self) -> ApiMethodBlocks:
        """Gets method_blocks value"""
        return self._mb
# endregion Main Page Parsing


# region Parse
class ParserInterface(ParserBase):


    @RequireArgs('url', ftype=DecFuncEnum.METHOD)
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._api_info = ApiInfo(url=self.url)
        self._sdk_method_info = SdkMethods(url=self._api_info.sdk_link)
        self._sdk_property_info = SdkProperties(c_lines=self._sdk_method_info.component_lines)
        self._sort = True
        self._info = None
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._formated_data = None

    def get_info(self) -> Dict[str, object]:
        """
        Gets info

        Returns:
            Dict[str, object]: {
                "name": "str, class name",
                "imports": "List[str], imports",
                "namespace": "str, Namespace",
                "extends": "List[str], class extends",
                "desc": "List[str], class description",
                "url": "str, api url"
            }
        """
        if self._info:
            return self._info
        ns = SdkNamesSpaceInfo(self._sdk_method_info.code_text)
        ni = SdkNameInfo(self._sdk_method_info.component)
        ex = SdkExtends(c_text=self._sdk_method_info.component,
                        m_text=self._sdk_method_info.component_lines)
        im = SdkImports(self._sdk_method_info.component_lines)
        desc = ApiDesc(soup=self._api_info.soup)
        result = {
            'name': ni.name,
            'imports': im.get_obj(),
            'namespace': ns.namespace,
            'extends': ex.ex_lst,
            'desc': desc.get_obj(),
            "url": self._api_info.soup.url
        }
        self._info = result
        return self._info
    
    def get_formated_data(self) -> str:
        if self._formated_data:
            return self._formated_data
        attribs = {}
        methods = self._get_methods_data()
        prop = self._get_properties_data()
        if 'methods' in methods:
            attribs.update(methods)
        if 'properties' in prop:
            attribs.update(prop)
        
        str_lst = Util.get_formated_dict_list_str(obj=attribs, indent=4)
        self._formated_data = str_lst
        return self._formated_data

    def _get_methods_data(self):
        attribs = {}
        for i, m in enumerate(self._sdk_method_info):
            if i == 0:
                attribs['methods'] = []
            if not m.name:
                continue
            if m.requires_typing:
                self._requires_typing = True
            self._imports.update(m.imports)
            attrib = {
                "name": m.name,
                "returns": m.return_type,
                "desc": self._api_info.desc_dict.get(m.name, []),
                "raises": m.raises
            }
            args = []
            for pi in m.args:
                args.append([pi.name, pi.type, pi.direction])
            attrib['args'] = args
            attribs['methods'].append(attrib)
        if self._sort:
            if 'methods' in attribs:
                newlist = sorted(attribs['methods'], key=lambda d: d['name'])
                attribs['methods'] = newlist
        return attribs
    
    def _get_properties_data(self):
        attribs = {}
        for i, m in enumerate(self._sdk_property_info):
            if i == 0:
                attribs['properties'] = []
            if not m.name:
                continue
            if m.requires_typing:
                self._requires_typing = True
            self._imports.update(m.imports)
            attrib = {
                "name": m.name,
                "returns": m.return_type,
                "desc": self._api_info.desc_dict.get(m.name, []),
                "raises_get": m.raises_get,
                "raises_set": m.raises_set
            }
            attribs['properties'].append(attrib)
        if self._sort:
            if 'properties' in attribs:
                newlist = sorted(attribs['properties'], key=lambda d: d['name'])
                attribs['properties'] = newlist
        return attribs

    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        try:
            if not self._formated_data:
                msg = "ParserInterface.get_formated_data() method must be called before accessing imports"
                raise Exception(msg)
        except Exception as e:
            logger.error(e)
            raise e
        return self._imports
    @property
    def requires_typing(self) -> Set[str]:
        """Gets requires typing value"""
        try:
            if not self._formated_data:
                msg = "ParserInterface.get_formated_data() method must be called before accessing imports"
                raise Exception(msg)
        except Exception as e:
            logger.error(e)
            raise e
        return self._requires_typing
# endregion Parse

# region Writer
class InterfaceWriter(WriteBase):
    def __init__(self, parser: ParserInterface, **kwargs):
        self._parser: ParserInterface = parser
        self._copy_clipboard = kwargs.get('copy_clipboard', False)
        self._print = kwargs.get('print', True)
        self._write_file = kwargs.get('write_file', False)
        self._indent_amt = 4
        self._p_name: str = None
        self._p_imports: Set[str] = set()
        self._p_imports_typing: Set[str] = set()
        self._p_namespace: str = None
        self._p_extends: List[str] = None
        self._p_desc: List[str] = None
        self._p_data: str = None
        self._p_url: str = None
        self._p_requires_typing = False
        self._path_dir = Path(os.path.dirname(__file__))
        _path = Path(self._path_dir, 'template', 'interface.tmpl')
        if not _path.exists():
            raise FileNotFoundError(f"unable to find templae file '{_path}'")
        self._template_file = _path
        self._template: str = self._get_template()
    
    def write(self):
        self._set_info()
        self._set_template_data()
        logger.info("Processing %s.%s", self._p_namespace, self._p_name)
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
    
    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def _set_template_data(self):
        def get_from_imports() -> List[List[str]]:
            lst = []
            for ns in self._p_imports:
                f, n = Util.get_rel_import(
                    i_str=ns, ns=self._p_namespace
                )
                lst.append([f, n])
            return lst

        def get_from_imports_typing() -> List[List[str]]:
            lst = []
            for ns in self._p_imports_typing:
                f, n = Util.get_rel_import(
                    i_str=ns, ns=self._p_namespace
                )
                lst.append([f, n])
            return lst

        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{ns}', str(self._p_namespace))
        self._template = self._template.replace('{link}', self._p_url)
        self._template = self._template.replace(
            '{requires_typing}', str(self._p_requires_typing))
        self._template = self._template.replace(
            '{inherits}', Util.get_string_list(lines=self._p_extends))
        self._template = self._template.replace(
            '{imports}', "[]")
        self._template = self._template.replace(
            '{from_imports}',
            Util.get_formated_dict_list_str(get_from_imports())
        )
        self._template = self._template.replace(
            '{from_imports_typing}',
            Util.get_formated_dict_list_str(get_from_imports_typing())
        )
        if len(self._p_desc) > 0:
            desc = Util.get_formated_dict_list_str(self._p_desc, indent=4)
        else:
            desc = "[]"
        self._template = self._template.replace('{desc}', desc)
        if self._indent_amt > 0:
            indent = ' ' * self._indent_amt
            indented = textwrap.indent(self._p_data, indent).lstrip()
        else:
            indented = self._p_data.lstrip()
        self._template = self._template.replace('{data}', indented)

    def _set_info(self):
        def get_extends(lst:List[str]) -> List[str]:
            return [Util.get_last_part(s) for s in lst]
            # return [s.rsplit('.', 1)[1] for s in lst]
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_namespace = data['namespace']
        self._p_extends = get_extends(data['extends'])
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_data = self._parser.get_formated_data()
        
        _imports = data['imports']
        self._p_imports.update(_imports)
        self._p_imports.update(data['extends'])
        self._p_imports_typing.update(self._parser.imports)
        if len(self._p_imports_typing) > 0:
            self._p_requires_typing = True
        if not self._p_requires_typing:
            self._p_requires_typing = self._parser.requires_typing
        if self._write_file:
            self._file_full_path = self._get_uno_obj_path()
    
    def _get_uno_obj_path(self) -> Path:
        uno_obj_path = Path(self._path_dir.parent, 'uno_obj')
        name_parts: List[str] = self._p_namespace.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append(self._p_name + '.tmpl')
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._create_sys_links(dest=obj_path.parent)
        return obj_path

    def _write_to_file(self):
        with open(self._file_full_path, 'w') as f:
            f.write(self._template)
        logger.info("Created file: %s", self._file_full_path)
# endregion Writer


def _main():
    os.system('cls' if os.name == 'nt' else 'clear')
    url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XFont.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1media_1_1XPlayerWindow.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XAnimatedImages.html'

    # interfaces
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertyBag.html'
    p = ParserInterface(url=url)
    pprint.pprint(p.get_info())
    print(p.get_formated_data())

def main():
    logger.info('Executing command: %s', sys.argv[1:])
    parser = argparse.ArgumentParser(description='enum')
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
        dest='write',
        default=False)

    args = parser.parse_args()
    logger.info('Parsing Url %s' % args.url)
    
    p = ParserInterface(url=args.url, sort=args.sort)
    w = InterfaceWriter(
        parser=p,
        print=args.print,
        copy_clipboard=args.clipboard,
        write_file=args.write)
    if not args.print:
        print('')
    w.write()

# region Debugging Data


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


def get_soup_data():
    result = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=9"/>
<meta name="generator" content="Doxygen 1.9.1"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>LibreOffice: XHierarchicalPropertySet Interface Reference</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<link href="search/search.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="search/searchdata.js"></script>
<script type="text/javascript" src="search/search.js"></script>
<link href="doxygen.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="top"><!-- do not remove this div, it is closed by doxygen! -->
<div id="titlearea">
<table cellspacing="0" cellpadding="0">
 <tbody>
 <tr style="height: 56px;">
  <td id="projectalign" style="padding-left: 0.5em;">
   <div id="projectname">LibreOffice
   </div>
   <div id="projectbrief">LibreOffice 7.2 SDK API Reference</div>
  </td>
 </tr>
 </tbody>
</table>
</div>
<!-- end header part -->
<!-- Generated by Doxygen 1.9.1 -->
<script type="text/javascript">
/* @license magnet:?xt=urn:btih:cf05388f2679ee054f2beb29a391d25f4e673ac3&amp;dn=gpl-2.0.txt GPL-v2 */
var searchBox = new SearchBox("searchBox", "search",false,'Search','.html');
/* @license-end */
</script>
<script type="text/javascript" src="menudata.js"></script>
<script type="text/javascript" src="menu.js"></script>
<script type="text/javascript">
/* @license magnet:?xt=urn:btih:cf05388f2679ee054f2beb29a391d25f4e673ac3&amp;dn=gpl-2.0.txt GPL-v2 */
$(function() {
  initMenu('',true,false,'search.php','Search');
  $(document).ready(function() { init_search(); });
});
/* @license-end */</script>
<div id="main-nav"></div>
<!-- window showing the filter options -->
<div id="MSearchSelectWindow"
     onmouseover="return searchBox.OnSearchSelectShow()"
     onmouseout="return searchBox.OnSearchSelectHide()"
     onkeydown="return searchBox.OnSearchSelectKey(event)">
</div>

<!-- iframe showing the search results (closed by default) -->
<div id="MSearchResultsWindow">
<iframe src="javascript:void(0)" frameborder="0" 
        name="MSearchResults" id="MSearchResults">
</iframe>
</div>

<div id="nav-path" class="navpath">
  <ul>
<li class="navelem"><a class="el" href="namespacecom.html">com</a></li><li class="navelem"><a class="el" href="namespacecom_1_1sun.html">sun</a></li><li class="navelem"><a class="el" href="namespacecom_1_1sun_1_1star.html">star</a></li><li class="navelem"><a class="el" href="namespacecom_1_1sun_1_1star_1_1beans.html">beans</a></li><li class="navelem"><a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.html">XHierarchicalPropertySet</a></li>  </ul>
</div>
</div><!-- top -->
<div class="header">
  <div class="summary">
<a href="#pub-methods">Public Member Functions</a> &#124;
<a href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet-members.html">List of all members</a>  </div>
  <div class="headertitle">
<div class="title">XHierarchicalPropertySet Interface Reference<span class="mlabels"><span class="mlabel">published</span></span></div>  </div>
</div><!--header-->
<div class="contents">

<p>provides information about and access to the a hierarchy of properties from an implementation.  
 <a href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.html#details">More...</a></p>

<p><code>import&quot;<a class="el" href="XHierarchicalPropertySet_8idl_source.html">XHierarchicalPropertySet.idl</a>&quot;;</code></p>
<div class="dynheader">
Inheritance diagram for XHierarchicalPropertySet:</div>
<div class="dyncontent">
 <div class="center">
  <img src="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.png" usemap="#XHierarchicalPropertySet_map" alt=""/>
  <map id="XHierarchicalPropertySet_map" name="XHierarchicalPropertySet_map">
<area href="interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html" title="base interface of all UNO interfaces" alt="XInterface" shape="rect" coords="89,0,258,24"/>
<area href="servicecom_1_1sun_1_1star_1_1configuration_1_1PropertyHierarchy.html" title="provides access to and information about properties and subproperties of an implementation." alt="PropertyHierarchy" shape="rect" coords="89,112,258,136"/>
<area href="servicecom_1_1sun_1_1star_1_1configuration_1_1GroupAccess.html" title="provides access to a predefined heterogeneous group of values and nested trees as part of a hierarchy..." alt="GroupAccess" shape="rect" coords="89,168,258,192"/>
<area href="servicecom_1_1sun_1_1star_1_1configuration_1_1ConfigurationAccess.html" title="provides read access to a fragment of the configuration hierarchy." alt="ConfigurationAccess" shape="rect" coords="0,224,169,248"/>
<area href="servicecom_1_1sun_1_1star_1_1configuration_1_1GroupUpdate.html" title="provides write access to a predefined heterogeneous group of values and nested trees as part of a hie..." alt="GroupUpdate" shape="rect" coords="179,224,348,248"/>
<area href="servicecom_1_1sun_1_1star_1_1configuration_1_1ConfigurationUpdateAccess.html" title="provides modifying access to a fragment of the configuration hierarchy." alt="ConfigurationUpdateAccess" shape="rect" coords="0,280,169,304"/>
<area href="servicecom_1_1sun_1_1star_1_1configuration_1_1ConfigurationUpdateAccess.html" title="provides modifying access to a fragment of the configuration hierarchy." alt="ConfigurationUpdateAccess" shape="rect" coords="179,280,348,304"/>
  </map>
</div></div>
<table class="memberdecls">
<tr class="heading"><td colspan="2"><h2 class="groupheader"><a name="pub-methods"></a>
Public Member Functions</h2></td></tr>
<tr class="memitem:a4d570f251588935879de379bfe7e90a3"><td class="memItemLeft" align="right" valign="top"><a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySetInfo.html">com::sun::star::beans::XHierarchicalPropertySetInfo</a>&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.html#a4d570f251588935879de379bfe7e90a3">getHierarchicalPropertySetInfo</a> ()</td></tr>
<tr class="memdesc:a4d570f251588935879de379bfe7e90a3"><td class="mdescLeft">&#160;</td><td class="mdescRight">retrieve information about the hierarchy of properties  <a href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.html#a4d570f251588935879de379bfe7e90a3">More...</a><br /></td></tr>
<tr class="separator:a4d570f251588935879de379bfe7e90a3"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:a3199a2c3aac68e54fb0c3e5678dd27d4"><td class="memItemLeft" align="right" valign="top">void&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.html#a3199a2c3aac68e54fb0c3e5678dd27d4">setHierarchicalPropertyValue</a> ([in] string aHierarchicalPropertyName, [in] any aValue)  raises ( com::sun::star::beans::UnknownPropertyException,                    com::sun::star::beans::PropertyVetoException,                    com::sun::star::lang::IllegalArgumentException,                    com::sun::star::lang::WrappedTargetException )</td></tr>
<tr class="memdesc:a3199a2c3aac68e54fb0c3e5678dd27d4"><td class="mdescLeft">&#160;</td><td class="mdescRight">sets the value of the property with the specified nested name.  <a href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.html#a3199a2c3aac68e54fb0c3e5678dd27d4">More...</a><br /></td></tr>
<tr class="separator:a3199a2c3aac68e54fb0c3e5678dd27d4"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:a57310c407a4938c0e3d7e1d9f9117750"><td class="memItemLeft" align="right" valign="top">any&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.html#a57310c407a4938c0e3d7e1d9f9117750">getHierarchicalPropertyValue</a> ([in] string aHierarchicalPropertyName)  raises ( com::sun::star::beans::UnknownPropertyException,                    com::sun::star::lang::IllegalArgumentException,                    com::sun::star::lang::WrappedTargetException )</td></tr>
<tr class="separator:a57310c407a4938c0e3d7e1d9f9117750"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="inherit_header pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface"><td colspan="2" onclick="javascript:toggleInherit('pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface')"><img src="closed.png" alt="-"/>&#160;Public Member Functions inherited from <a class="el" href="interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html">XInterface</a></td></tr>
<tr class="memitem:ac368fa472a7f656e0b7c77859c971fc4 inherit pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface"><td class="memItemLeft" align="right" valign="top">any&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html#ac368fa472a7f656e0b7c77859c971fc4">queryInterface</a> ([in] type aType)</td></tr>
<tr class="memdesc:ac368fa472a7f656e0b7c77859c971fc4 inherit pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface"><td class="mdescLeft">&#160;</td><td class="mdescRight">queries for a new interface to an existing UNO object.  <a href="interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html#ac368fa472a7f656e0b7c77859c971fc4">More...</a><br /></td></tr>
<tr class="separator:ac368fa472a7f656e0b7c77859c971fc4 inherit pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:af9f5b35a212d21af601a8213ed325871 inherit pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface"><td class="memItemLeft" align="right" valign="top">void&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html#af9f5b35a212d21af601a8213ed325871">acquire</a> ()</td></tr>
<tr class="memdesc:af9f5b35a212d21af601a8213ed325871 inherit pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface"><td class="mdescLeft">&#160;</td><td class="mdescRight">increases the reference counter by one.  <a href="interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html#af9f5b35a212d21af601a8213ed325871">More...</a><br /></td></tr>
<tr class="separator:af9f5b35a212d21af601a8213ed325871 inherit pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:a23b477d0e2d399f75d585d154c346591 inherit pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface"><td class="memItemLeft" align="right" valign="top">void&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html#a23b477d0e2d399f75d585d154c346591">release</a> ()</td></tr>
<tr class="memdesc:a23b477d0e2d399f75d585d154c346591 inherit pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface"><td class="mdescLeft">&#160;</td><td class="mdescRight">decreases the reference counter by one.  <a href="interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html#a23b477d0e2d399f75d585d154c346591">More...</a><br /></td></tr>
<tr class="separator:a23b477d0e2d399f75d585d154c346591 inherit pub_methods_interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface"><td class="memSeparator" colspan="2">&#160;</td></tr>
</table>
<a name="details" id="details"></a><h2 class="groupheader">Detailed Description</h2>
<div class="textblock"><p>provides information about and access to the a hierarchy of properties from an implementation. </p>
<p>Usually an object that implements this interface also implements <a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertySet.html" title="provides information about and access to the properties from an implementation.">XPropertySet</a> and at least some of the properties have subproperties. </p>
<p>This interface allows direct access to subsubproperties, ... up to an arbitrary nesting depth. Often the intermediate elements of the hierarchy implement <a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XProperty.html" title="Is implemented by objects that also are a property of some other object.">XProperty</a>. </p>
<p>Each implementation specifies how the hierarchical property names, that are used to access the elements of the hierarchy, are formed. </p>
<p>Commonly a notation similar to filesystem paths (separated by '/' slashes) or nested module names (separated by dots '.' or '::') is used. </p>
</div><h2 class="groupheader">Member Function Documentation</h2>
<a id="a4d570f251588935879de379bfe7e90a3"></a>
<h2 class="memtitle"><span class="permalink"><a href="#a4d570f251588935879de379bfe7e90a3">&#9670;&nbsp;</a></span>getHierarchicalPropertySetInfo()</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname"><a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySetInfo.html">com::sun::star::beans::XHierarchicalPropertySetInfo</a> getHierarchicalPropertySetInfo </td>
          <td>(</td>
          <td class="paramname"></td><td>)</td>
          <td></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>retrieve information about the hierarchy of properties </p>
<dl class="section return"><dt>Returns</dt><dd>the <a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySetInfo.html" title="specifies a hierarchy of properties.">XHierarchicalPropertySetInfo</a> interface, which describes the property hierarchy of the object which supplies this interface.</dd>
<dd>
<code>NULL</code> if the implementation cannot or will not provide information about the properties; otherwise the interface <a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySetInfo.html" title="specifies a hierarchy of properties.">XHierarchicalPropertySetInfo</a> is returned. </dd></dl>

</div>
</div>
<a id="a57310c407a4938c0e3d7e1d9f9117750"></a>
<h2 class="memtitle"><span class="permalink"><a href="#a57310c407a4938c0e3d7e1d9f9117750">&#9670;&nbsp;</a></span>getHierarchicalPropertyValue()</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">any getHierarchicalPropertyValue </td>
          <td>(</td>
          <td class="paramtype">[in] string&#160;</td>
          <td class="paramname"><em>aHierarchicalPropertyName</em></td><td>)</td>
          <td></td>
        </tr>
        <tr>
          <td align="right">raises </td><td>(</td><td colspan="2"> <a class="el" href="exceptioncom_1_1sun_1_1star_1_1beans_1_1UnknownPropertyException.html">com::sun::star::beans::UnknownPropertyException</a>,</td>
        </tr>
        <tr>
          <td align="right"></td><td></td><td colspan="2">                    <a class="el" href="exceptioncom_1_1sun_1_1star_1_1lang_1_1IllegalArgumentException.html">com::sun::star::lang::IllegalArgumentException</a>,</td>
        </tr>
        <tr>
          <td align="right"></td><td></td><td colspan="2"><a class="el" href="exceptioncom_1_1sun_1_1star_1_1lang_1_1WrappedTargetException.html">com::sun::star::lang::WrappedTargetException</a></td>
        </tr>
        <tr>
          <td align="right"></td><td>)</td><td></td><td></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="section return"><dt>Returns</dt><dd>the value of the property with the specified nested name.</dd></dl>
<dl class="params"><dt>Parameters</dt><dd>
  <table class="params">
    <tr><td class="paramname">aHierarchicalPropertyName</td><td>This parameter specifies the name of the property.</td></tr>
  </table>
  </dd>
</dl>
<dl class="exception"><dt>Exceptions</dt><dd>
  <table class="exception">
    <tr><td class="paramname"><a class="el" href="exceptioncom_1_1sun_1_1star_1_1beans_1_1UnknownPropertyException.html" title="This exception is thrown to indicate that the property name is unknown to the implementation.">UnknownPropertyException</a></td><td>if the property does not exist.</td></tr>
    <tr><td class="paramname">com::sun::star::uno::lang::IllegalArgumentException</td><td>if <em>aHierarchicalPropertyName</em> is not a well-formed nested name for this hierarchy. An implementation is not required to detect this condition.</td></tr>
    <tr><td class="paramname"><a class="el" href="exceptioncom_1_1sun_1_1star_1_1lang_1_1WrappedTargetException.html" title="This is a checked exception that wraps an exception thrown by the original target.">com::sun::star::lang::WrappedTargetException</a></td><td>if the implementation has an internal reason for the exception. In this case the original exception is wrapped into that <a class="el" href="exceptioncom_1_1sun_1_1star_1_1lang_1_1WrappedTargetException.html" title="This is a checked exception that wraps an exception thrown by the original target.">com::sun::star::lang::WrappedTargetException</a>.</td></tr>
  </table>
  </dd>
</dl>
<dl class="section see"><dt>See also</dt><dd><a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertySet.html#a233801155a885acba5038e2dfb414ab4">XPropertySet::getPropertyValue</a> </dd></dl>

</div>
</div>
<a id="a3199a2c3aac68e54fb0c3e5678dd27d4"></a>
<h2 class="memtitle"><span class="permalink"><a href="#a3199a2c3aac68e54fb0c3e5678dd27d4">&#9670;&nbsp;</a></span>setHierarchicalPropertyValue()</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">void setHierarchicalPropertyValue </td>
          <td>(</td>
          <td class="paramtype">[in] string&#160;</td>
          <td class="paramname"><em>aHierarchicalPropertyName</em>, </td>
        </tr>
        <tr>
          <td class="paramkey"></td>
          <td></td>
          <td class="paramtype">[in] any&#160;</td>
          <td class="paramname"><em>aValue</em>&#160;</td>
        </tr>
        <tr>
          <td></td>
          <td>)</td>
          <td></td><td></td>
        </tr>
        <tr>
          <td align="right">raises </td><td>(</td><td colspan="2"> <a class="el" href="exceptioncom_1_1sun_1_1star_1_1beans_1_1UnknownPropertyException.html">com::sun::star::beans::UnknownPropertyException</a>,</td>
        </tr>
        <tr>
          <td align="right"></td><td></td><td colspan="2">                    <a class="el" href="exceptioncom_1_1sun_1_1star_1_1beans_1_1PropertyVetoException.html">com::sun::star::beans::PropertyVetoException</a>,</td>
        </tr>
        <tr>
          <td align="right"></td><td></td><td colspan="2">                    <a class="el" href="exceptioncom_1_1sun_1_1star_1_1lang_1_1IllegalArgumentException.html">com::sun::star::lang::IllegalArgumentException</a>,</td>
        </tr>
        <tr>
          <td align="right"></td><td></td><td colspan="2"><a class="el" href="exceptioncom_1_1sun_1_1star_1_1lang_1_1WrappedTargetException.html">com::sun::star::lang::WrappedTargetException</a></td>
        </tr>
        <tr>
          <td align="right"></td><td>)</td><td></td><td></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>sets the value of the property with the specified nested name. </p>
<dl class="params"><dt>Parameters</dt><dd>
  <table class="params">
    <tr><td class="paramname">aHierarchicalPropertyName</td><td>This parameter specifies the name of the property.</td></tr>
    <tr><td class="paramname">aValue</td><td>This parameter specifies the new value for the property.</td></tr>
  </table>
  </dd>
</dl>
<dl class="exception"><dt>Exceptions</dt><dd>
  <table class="exception">
    <tr><td class="paramname"><a class="el" href="exceptioncom_1_1sun_1_1star_1_1beans_1_1UnknownPropertyException.html" title="This exception is thrown to indicate that the property name is unknown to the implementation.">UnknownPropertyException</a></td><td>if the property does not exist.</td></tr>
    <tr><td class="paramname"><a class="el" href="exceptioncom_1_1sun_1_1star_1_1beans_1_1PropertyVetoException.html" title="This exception is thrown when a proposed change to a property represents an unacceptable value.">PropertyVetoException</a></td><td>if the property is constrained and the change is vetoed by a <a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XVetoableChangeListener.html" title="is used to receive PropertyChangeEvents whenever a &quot;constrained&quot; property is changed.">XVetoableChangeListener</a>.</td></tr>
    <tr><td class="paramname">com::sun::star::uno::lang::IllegalArgumentException</td><td>if <em>aValue</em> is not a legal value for this property or if <em>aHierarchicalPropertyName</em> is not a well-formed nested name for this hierarchy. An implementation is not required to detect the latter condition.</td></tr>
    <tr><td class="paramname"><a class="el" href="exceptioncom_1_1sun_1_1star_1_1lang_1_1WrappedTargetException.html" title="This is a checked exception that wraps an exception thrown by the original target.">com::sun::star::lang::WrappedTargetException</a></td><td>if the implementation has an internal reason for the exception. In this case the original exception is wrapped into that <a class="el" href="exceptioncom_1_1sun_1_1star_1_1lang_1_1WrappedTargetException.html" title="This is a checked exception that wraps an exception thrown by the original target.">com::sun::star::lang::WrappedTargetException</a>.</td></tr>
  </table>
  </dd>
</dl>
<dl class="section see"><dt>See also</dt><dd><a class="el" href="interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertySet.html#ac83d5c7678aa889b81dd1d59ebcd2a96" title="sets the value of the property with the specified name.">XPropertySet::setPropertyValue</a> </dd></dl>

</div>
</div>
<hr/>The documentation for this interface was generated from the following file:<ul>
<li>com/sun/star/beans/<a class="el" href="XHierarchicalPropertySet_8idl_source.html">XHierarchicalPropertySet.idl</a></li>
</ul>
</div><!-- contents -->
<!-- start footer part -->
<hr class="footer"/><address class="footer"><small>
Generated by&#160;<a href="https://www.doxygen.org/index.html"><img class="footer" src="doxygen.svg" width="104" height="31" alt="doxygen"/></a> 1.9.1
</small></address>
</body>
</html>
"""
    return result

# endregion Debugging Data


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains an interface
"""
import os
import sys
import argparse
import logging
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
import re
import base
from typing import Dict, List, Set, Union
from bs4.element import PageElement, ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, TypeCheckKw
from pathlib import Path
from logger.log_handle import get_logger
from parser.enm import main
from dataclasses import dataclass
from parser import __version__, JSON_ID

logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l


_set_loggers(None)

re_component_start = re.compile(r"(interface.*){", re.DOTALL)
re_name_info_start = re.compile(r"(interface)\s*[a-zA-Z0-9]+[ :]+")
re_name_info_name = re.compile(r"interface\s*(?P<NAME>[a-zA-Z0-9_]+)")
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
re_property_pattern = re.compile(r"(?:\[attribute[ ,a-z]*\])(?:[ ]+)([a-zA-Z0-9. {}()]*);")
re_comment_start_pattern = re.compile(r"(?:(\/\*)|(?:\*)\s)")
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


class SdkCodeText(base.BlockObj):
    """Responsible for getting code from url"""

    def __init__(self, soup: base.SoupObj):
        super().__init__(soup=soup)
        self._data = None

    def get_obj(self) -> str:
        if self._data:
            return self._data

        def clean_lines(text: str) -> str:
            lns = text.splitlines()
            new_lines = []
            for l in lns:
                ln = l.strip()
                if ln == '':
                    continue
                if ln.startswith('#'):
                    continue
                new_lines.append(ln)
            return "\n".join(new_lines)

        def comment_remover(text):

            def replacer(match):
                s = match.group(0)
                if s.startswith('/'):
                    return " "  # note: a space and not an empty string
                else:
                    return s
            pattern = re.compile(
                r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
                re.DOTALL | re.MULTILINE
            )
            return re.sub(pattern, replacer, text)
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
        self._data = comment_remover(result)
        self._data = clean_lines(self._data)
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
        self._init = False

    def get_text(self) -> str:
        if self._init:
            return self._data
        self._init = True
        text = self._code_text.get_obj()
        # it is possible that SDK file has more than one interface
        # See: https://api.libreoffice.org/docs/idl/ref/XComponentContext_8idl_source.html
        # for this reason will narrow text untill the last match is found.
        self._data = self._get_text_aggresive(text)
        # logger.debug('Component text:\n%s', self._data)
        
        return self._data

    def _get_text_aggresive(self, text:str) -> str:
        def single_line_ns(input: str) -> str:
            _regex = r"(module[{ \na-z-A-Z0-9]+)interface"
            def cb(match) -> str:
                return str(match.group(1)).replace('\n', ' ') + '\ninterface'
            return re.sub(pattern=_regex, repl=cb, string=input, flags=re.DOTALL)
        def clean_curly(input: str) -> str:
            _regex = r"^(}[ ;}]+)"
            def cb(match) -> str:
                return base.Util.clean_curly_brace_close(match.group(1))
            return re.sub(pattern=_regex, repl=cb, string=input, flags=re.MULTILINE)
        def remove_single_line_comments(input: str) -> str:
            return re.sub(r"(//[ a-z-A-Z0-9]+\n)",'', input, re.DOTALL)
        # remove all spaces between } and ;
        _text = single_line_ns(text)
        _text = remove_single_line_comments(_text)
        _text = clean_curly(_text)

        regex_start = r"module (com \{.*)\{"
        regex_end = r"^(};){3,5}"
        matches_start = re.search(regex_start, _text)
        matches_end = re.search(pattern=regex_end, string=_text, flags=re.MULTILINE)
        if not matches_end:
            regex_end = r"(\};){2,4}(\}[;])+\n"
            matches_end = re.search(pattern=regex_end, string=_text, flags=re.DOTALL)
        result = ''
        if matches_start and matches_end:
            start = matches_start.span()[1]
            end = matches_end.span()[0]
            result = _text[start:end]
            matches_start = re.search(regex_start, result)
        while matches_start:
            start = matches_start.span()[1]
            result = result[start:]
            matches_start = re.search(regex_start, result)
        return result.strip()

        
    @property
    def code_text(self) -> SdkCodeText:
        """Gets code_text value"""
        return self._code_text

class SdkComponentStart:
    """
    Responsible for getting first line of component such as:
    interface XAccessibleHyperlink : ::com::sun::star::accessibility::XAccessibleAction
    """
    def __init__(self, c_text: SdkComponentText):
        self._component: SdkComponentText = c_text
        self._data = None
    
    def get_obj(self) -> str:
        if not self._data is None:
            return self._data
        self._data = ''
        try:
            text = self._component.get_text()
            # regex = r"(interface.*){"
            matches = re.search(
                r"(interface[ ]+[a-zA-Z0-9]+[^;][a-z-A-Z0-9_: ]+)\n{", text)
            if not matches:
                matches = re_component_start.search(text)
            if not matches:
                matches = re.search(r"interface[a-zA-Z0-9_ :]+\n{", text)
            if matches:
                g = matches.groups()
                self._data = " ".join(g[0].replace("{","").rstrip().split())
            else:
                if logger.level <= logging.DEBUG:
                    logger.debug("SdkComponentStart.get_obj() unable to match first line. Returning text. URL: %s",
                                 self._component.code_text.url_obj.url)
                    self._data = text
                # raise Exception("SdkComponentStart: Unable to match regex for first line")
        except Exception as e:
            url = self._component.code_text.url_obj.url
            logger.error("SdkComponentStart: Processing first line. Url: %s", url)
            raise e
        return self._data

    @property
    def component_text(self) -> str:
        """Gets component_text value"""
        return self._component

class SdkComponentLines:
    """
    Responsible for getting all lines of Component.
    Lines have a simple cleaning that replace :: with .
    """

    def __init__(self, f_text: SdkComponentText):
        self._component = f_text
        self._data = None
        self._init = False

    def get_obj(self) -> List[str]:
        if self._init:
            return self._data
        self._init = True
        text = self._component.get_text()
        # text includes name and {} such as interface XHierarchicalPropertySet: com::sun::star::uno::XInterface\n{...\n}
        # remove the outter text
        inner_re = r"\{(.*)\}"
        matches = re.search(inner_re, text, flags=re.DOTALL)
        if matches:
            g = matches.groups()
            text = g[0]
        text = self._get_proper_lines(input=text)
        lines = self._remove_empty(text)
        self._data = self._clean_lines(lines=lines)
        if logger.level <= logging.DEBUG:
            for line in self._data:
                logger.debug("SdkComponentLines.get_obj() found: %s", line)
        return self._data

    def _get_proper_lines(self, input: str) -> str:
        if not input:
            return ''
        # methods may be split across multiple lines.
        # start by collapsing all lines into a single line
        lines  = input.splitlines()
        new_lines = list[str]()
        for line in lines:
            s = line.strip().lstrip(':')
            m = re_comment_start_pattern.match(s)
            if m:
                logger.debug(
                    'SdkComponentLines: Skipping comment line: %s', line)
                continue
            new_lines.append(s)
        single_line = " ".join(new_lines)
        # logger.debug('single Line\n%s', single_line)
        # bit of a hack here but best fix I can find so far
        # fixes parsing issue when interface such as:
        # https://api.libreoffice.org/docs/idl/ref/XAnimatedImages_8idl_source.html
        single_line = base.Util.encode_char(single_line, '); }')

        # now split all lines by ; and put on new lines again
        new_lines = ";\n".join(single_line.split(';'))
        return base.Util.decode_char(new_lines, '); }')
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
            logger.debug("SdkMethodLines.get_obj() Processing Line: %s", line)
            match = re.match(re_interface_pattern, line)
            if match:
                logger.debug("SdkMethodLines.get_obj() Line Matched Interface. continuing...")
                continue
            match = re.match(re_property_pattern, line)
            if match:
                logger.debug(
                    "SdkMethodLines.get_obj() Line Matched Property. continuing...")
                continue
            match = re.match(re_method_pattern, line)
            if match:
                logger.debug("SdkMethodLines.get_obj() Line Matched")
                results.append(line)
            else: 
                logger.debug("SdkMethodLines.get_obj() No Match")
        self._data = results
        # if logger.level <= logging.DEBUG:
        #     logger.debug("SdkMethodLines.get_obj() data:\n%s", "\n".join(self._data))
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
            logger.debug(
                "SdkPropertyLines.get_obj() Processing Line: %s", line)
            match = re.match(re_property_pattern, line)
            if match:
                results.append(line)
                logger.debug("SdkPropertyLines.get_obj() Line Matched")
            else:
                logger.debug("SdkPropertyLines.get_obj() No Match")
        self._data = results
        # if logger.level <= logging.DEBUG:
        #     logger.debug("SdkMethodLines.get_obj() data:\n%s",
        #                  "\n".join(self._data))
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

        text = self._param
        logger.debug('SdkMethodData._set_data() Processing: %s', text)
        matches = re.search(re_interface_pattern, text)
        if matches:
            logger.debug("SdkMethodData._set_data() data matched interface. Raising error")
            raise MethodInvalidError(f"'{text}' matches interface")
        matches = re.search(re_property_pattern, text)
        if matches:
            logger.debug("SdkMethodData._set_data() data matched property. Raising error")
            raise MethodInvalidError(f"'{text}' matches property")

        seq_regex = r"([a-zA-Z]*)< *([a-zA-A0-9]*) *>"
        m = re.match(seq_regex, text)
        if m:
            # replace sequence< string > with sequence<string>
            # this is necessary to prevent following steps from parsing incorectly
            replacement = f'{m.group(1)}<{m.group(2)}>'
            text = re.sub(seq_regex, replacement, text, 1)
            logger.debug("SdkMethodData._set_data() replaced < spaces >. Now: %s", text)
        # check if method include raises...
        matches = re.search(re_raises_pattern, text)
        if matches:
            logger.debug('SdkMethodData._set_data() found raises for method.')
            g = matches.groups()
            self._process_raises(g[0])
            # remove raises text section
            text = re.sub(re_raises_pattern, '', text)
            logger.debug('SdkMethodData._set_data() remove raise match: %s', text)
        else:
            logger.debug('SdkMethodData._set_data() did not find raises for method.')
        
        # imports are handled in _get_py_type that is called in this method and in _process_args
        # self._process_imports(text)
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
            logger.debug("SdkMethodData._set_data() Matches for method Params: %s", str(g))
            if g[0] is None:
                # no params
                self._p_name = g[4]
                # result = Util.get_py_type(g[3], cb=cb)
                result = self._get_py_type(g[3])
                self._p_return = result
            else:
                self._p_name = g[1]
                # result = Util.get_py_type(g[0], cb=cb)
                result = self._get_py_type(g[0])
                self._p_return = result
                self._process_args(g[2])
        else:
            logger.debug(
                "SdkMethodData._set_data() No method found in: %s", text)
        return matches

    def _process_imports(self, text: str):
        regex = r"(com.sun[\w.]+)"
        matches = re.finditer(regex, text)
        for matchNum, match in enumerate(matches, start=1):
            logger.debug("SdkMethodData._process_imports() Match {matchNum} was found at {start}-{end}: {match}".format(
                matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                ns = match.group(groupNum)
                logger.debug("SdkMethodData._process_imports() Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                    start=match.start(groupNum), end=match.end(groupNum), group=ns))
                self._imports.add(match.group(groupNum))
                logger.debug("SdkMethodData._process_imports() added import: %s", ns)
                self._requires_typing = True
                
    def _process_raises(self, text: str):
        # raises( com::sun::star::beans::UnknownPropertyException, com::sun::star::lang::IllegalArgumentException, com::sun::star::lang::WrappedTargetException )
        s = text.replace('(', '|').replace(')', '|').split('|')
        if len(s) <= 1:
            logger.debug('SdkMethodData._process_raises() Invalid raises text: %s', text)
            return
        ex_parts = s[1].replace("::",".").split(',')
        new_parts = list[str]()
        for part in ex_parts:
            new_parts.append(base.Util.get_clean_ns(input=part, ltrim=True))
        # ex = s[1].strip().replace('::', ".").replace(' ', '').replace('.com.', 'com.').split(',')
        self._p_raises.extend(new_parts)
        if logger.level <= logging.DEBUG:
            logger.debug('SdkMethodData._process_raises() added raise: %s', str(new_parts))

    def _process_interface(self, text: str):
        # interface com::sun::star::beans::XPropertySet
        parts = text.strip().replace("::", '.').rsplit(
            '.', 1)  # 'com.sun.star.beans', 'XPropertySet'
        return

    def _get_py_type(self, in_type: str) -> str:
        cb_data = None

        def cb(data: dict):
            nonlocal cb_data
            cb_data = data

        n_type = base.TYPE_MAP.get(in_type, None)
        if n_type:
            logger.debug(
                "SdkMethodData._get_py_type() Found python type: %s", n_type)
            return n_type
        n_type = base.Util.get_py_type(uno_type=in_type, cb=cb)
        is_wrapper = cb_data['is_wrapper']
        is_py = cb_data['is_py_type']
        _result = n_type
        if is_wrapper:
            self._requires_typing = True
            logger.debug("SdkMethodData._get_py_type() wrapper arg %s", in_type)
            logger.debug("SdkMethodData._get_py_type() wrapper arg Typing is Required.")
            wdata: dict = cb_data['wdata']
            if not wdata['py_type_inner']:
                logger.debug(
                    "SdkMethodData._get_py_type() wrapper inner requires typing arg %s", in_type)
                self._imports.add(cb_data['long_type'])
                logger.debug(
                    "SdkMethodData._get_py_type() added import %s", cb_data['long_type'])
        else:
            if is_py is False:
                logger.debug(
                    "SdkMethodData._get_py_type() requires typing arg %s", in_type)
                self._requires_typing = True
                self._imports.add(cb_data['long_type'])
                logger.debug(
                    "SdkMethodData._get_py_type() added import %s", cb_data['long_type'])
        return _result

    def _process_args(self, args: str):      
        a = args.replace(' ', '').strip()
        logger.debug('SdkMethodData._process_args() parsing args: %s', a)
        arg_lst = a.split(',')
        for arg in arg_lst:
            matches = re.search(re_args_pattern, arg)
            if not matches:
                continue
            logger.debug('SdkMethodData_process_args() parsing arg: %s', arg)
            g = matches.groups()
            _dir = 'in' if g[0] is None else g[0].lower()
            stype = self._get_py_type(g[1])
            info = ParamInfo(
                direction=_dir, name=g[2], type=stype)
            logger.debug(
                'SdkMethodData_process_args() ParamInfo DIRECTION: %s, NAME: %s, TYPE: %s'
                , arg)
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
        text = self._param
        # remove [attribute] from start of string
        text = base.Util.clean_sq_braces(text).lstrip()
        
        # check if method include raises...
        matches = re.search(re_raises_pattern, text)
        if matches:
            g = matches.groups()
            self._process_raises(g[0])
            # remove raises text section
            text = re.sub(re_raises_pattern, '', text)
        parts = text.split(maxsplit=2)
        # result = base.Util.get_py_type(parts[0], cb=cb)
        ns_clean = base.Util.get_clean_ns(input=parts[0], ltrim=True)
        result = self._get_py_type(in_type=ns_clean)
        self._p_return = result
        self._p_name = base.Util.get_clean_name(parts[1])

    def _get_py_type(self, in_type: str) -> str:
        cb_data = None

        def cb(data: dict):
            nonlocal cb_data
            cb_data = data

        n_type = base.TYPE_MAP.get(in_type, None)
        if n_type:
            logger.debug(
                "SdkProperyData._get_py_type() Found python type: %s", n_type)
            return n_type
        n_type = base.Util.get_py_type(uno_type=in_type, cb=cb)
        is_wrapper = cb_data['is_wrapper']
        is_py = cb_data['is_py_type']
        _result = n_type
        if is_wrapper:
            self._requires_typing = True
            logger.debug(
                "SdkProperyData._get_py_type() wrapper arg %s", in_type)
            logger.debug(
                "SdkProperyData._get_py_type() wrapper arg Typing is Required.")
            wdata: dict = cb_data['wdata']
            if not wdata['py_type_inner']:
                logger.debug(
                    "SdkProperyData._get_py_type() wrapper inner requires typing arg %s", in_type)
                self._imports.add(cb_data['long_type'])
                logger.debug(
                    "SdkProperyData._get_py_type() added import %s", cb_data['long_type'])
        else:
            if is_py is False:
                logger.debug(
                    "SdkProperyData._get_py_type() requires typing arg %s", in_type)
                self._requires_typing = True
                self._imports.add(cb_data['long_type'])
                logger.debug(
                    "SdkProperyData._get_py_type() added import %s", cb_data['long_type'])
        return _result


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

    def __init__(self, url_soup: Union[str, base.SoupObj]):
        if isinstance(url_soup, str):
            self._soup = base.SoupObj(url_soup)
        else:
            self._soup = url_soup
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
    def soup(self) -> base.SoupObj:
        """Gets soup value"""
        return self._soup

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
    def __init__(self, c_text: SdkComponentStart, m_text: SdkComponentLines):
        self._c_start: SdkComponentStart = c_text
        self._m_text: SdkComponentLines = m_text
        self._ex_lst: List[str] = []
        self._i_data: SdkInterfaceData = SdkInterfaceData(text=m_text)
        self._init()

    def _init(self):
        s = self._c_start.get_obj()
        logger.debug("SdkExtends._init() First Line: %s", s)
        # published interface XFont: com::sun::star::uno::XInterface
        s = s.replace('::', ".")
        logger.debug("SdkExtends._init() Replaced :: %s", s)
        parts = s.rsplit(sep=':', maxsplit=1)
        if len(parts) > 1:
            logger.debug("SdkExtends._init() ':' seperator found extends on first line.")
            s = parts[1]
            logger.debug("SdkExtends._init() Processing: '%s'", s)
            s = base.Util.get_clean_ns(s).lstrip('.')
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
                s = base.Util.get_clean_ns(s)
                self._ex_lst.append(s)
                logger.debug("SdkExtends._init() Added Extends: '%s'", s)

    # region Properties
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
                s = base.Util.get_clean_ns(input=g[0], ltrim=True)
                logger.debug(
                    "SdkImports.get_obj() adding Import: '%s'", s)
                self._imports.add(s)
            else:
                logger.debug("SdkImports.get_obj() No Match")
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


class SdkNameInfo:
    """Gets Name of interface/class etc"""

    def __init__(self, c_start: SdkComponentStart):
        self._name = ''
        self._start_info = c_start
        self._init()

    def _init(self):
        # https://regex101.com/r/aNblTo/1/
        # https://regex101.com/r/aNblTo/2/
        # https://regex101.com/r/aNblTo/3/
        # more generic so can work with struct, interface etc
        s = self._start_info.get_obj()
        try:
            # regex_start = r"(interface)\s*[a-zA-Z0-9]+[ :]+"

            matches = re_name_info_start.search(s)
            if matches:
                # find the index of interface and drop anything before
                start = matches.span(1)[0]
                if start > 0:
                    s = s[start:]
            # regex = r"interface\s*(?P<NAME>[a-zA-Z0-9_]+)"
            m = re_name_info_name.match(s)
            if m:
                s = m.group('NAME')
            else:
                raise Exception(
                    "SdkNameInfo: Unable to find name in %s" % s)
            self._name = s
        except Exception as e:
            logger.error("SdkNameInfo: Error Processing: %s", s)
            raise e
        logger.debug('SdkNameInfo.name: %s', self._name)
        

    @property
    def name(self) -> str:
        """Gets name value"""
        return self._name

    @property
    def component_start(self) -> SdkComponentStart:
        """Gets component object"""
        return self._start_info
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
                f"MethodBlock._get_next_sibling() el is not a PageElement Url: {self._blocks.url_obj.url}")
        next = el.next_sibling
        # https://stackoverflow.com/questions/10711116/strip-spaces-tabs-newlines-python
        # use split join to remove whitespace and new line
        s = ''.join(str(next).split())
        if s == '':
            next = self._get_next_sibling(next)
            # if next is None:
            #     print(None)
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
            logger.error(e, exc_info=True)
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


class ApiMethodBlocks(base.BlockObj):
    """Get all methods"""

    def __init__(self, url_soup: Union[str, base.SoupObj]):
        if isinstance(url_soup, str):
            self._soup_obj = base.SoupObj(url_soup)
        else:
            self._soup_obj = url_soup
        soup = self._soup_obj
        super().__init__(soup=soup)
        self._obj_data: ResultSet = None
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
        # self._obj_data = self._soup.soup.select("a[id]")
        self._obj_data = self._soup.soup.find_all("a", id=base.pattern_id)

        return self._obj_data

    def _get_next(self) -> ApiMethodBlock:
        if self._index >= self._len:
            self._index = 0
            self._cur_obj = None
            raise StopIteration
        itm = self._obj_data[self._index]
        self._index += 1
        try:
            mb = ApiMethodBlock(block=itm, blocks=self)
            if not mb.is_valid():
                mb = self._get_next()
        except Exception as e:
            # probally nothing to worrie about. could simple be a bad match
            logger.warning("")
            mb = self._get_next("ApiMethodBlocks.Next() No method data block for '%s' Url: %s", str(itm), self.url_obj.url)
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
        p_obj = base.TagsStrObj(tags=lines_found)
        return p_obj.get_lines()


class ApiSdkLink:
    """Manages getting SDK Link from API page"""
    def __init__(self, soup: base.SoupObj):
        self._soup = soup

    def get_obj(self) -> str:
        """
        Gets url of SDK link from API page

        Raises:
            Excepton: If unable to parse page link

        Returns:
            str: Url of SDK
        """
        try:
            a = self._soup.soup.select_one("body > div.contents > ul > li > a")
            url = self._soup.url
            parts = url.rsplit('/', 1)
            href = parts[0] + '/' + a['href']
            logger.debug("ApiSdkLink.get_obj() Link: %s", href)
            return href
        except Exception as e:
            logger.error("ApiSdk Failed to get Link: Are you sure you inputing correct url?")
            raise e
    @property
    def soup(self) -> base.SoupObj:
        """Gets SoupObj instance for this instance"""
        return self._soup



class ApiDesc:
    """Gets the description"""

    def __init__(self, soup: base.SoupObj):
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
        p_obj = base.TagsStrObj(tags=lines_found)
        self._data = p_obj.get_lines()
        see_obj = ApiDescSeeAlso(self._soup)
        see = see_obj.get_obj()
        if see:
            self._data.append('')
            self._data.append('**See Also**')
            self._data.append('')
            self._data.append(f"    {see}")
        return self._data
    @property
    def soup(self) -> base.SoupObj:
        """Gets soup value"""
        return self._soup

class ApiDescSeeAlso:
    """Gets the description"""

    def __init__(self, soup: base.SoupObj):
        self._soup = soup
        self._data = None
        self._init = False

    def get_obj(self) -> str:
        """
        Gets See alos of Interface

        Returns:
            str: See also. if it exist; Otherwise empty string.
        """
        if self._init:
            return self._data
        self._init = True
        tag = self._soup.soup.select_one(
            'body > div.contents > div.textblock > dl > dd')
        if not tag:
            self._data = ''
            return self._data
        self._data = base.str_clean(" ".join(tag.text.split()))
        return self._data
    
    @property
    def soup(self) -> base.SoupObj:
        """Gets soup value"""
        return self._soup
class ApiInfo:
    def __init__(self,  url_soup: Union[str, base.SoupObj]):
        if isinstance(url_soup, str):
            self._url = url_soup
            self._soup_obj = base.SoupObj(url_soup)
        else:
            self._url = url_soup.url
            self._soup_obj = url_soup
        self._sdk_link = None
        self._dict = None
        self._mb = ApiMethodBlocks(self._soup_obj)
        self._api_sdk_link = None
        
    @property
    def desc_dict(self) -> Dict[str, List[str]]:
        """Dictionary that contains descriptions. Key is method name"""
        if not self._dict is None:
            return self._dict
        self._dict = {}
        for block in self._mb:
            name = ApiMethodName(block=block)
            desc = ApiMethodDesc(block=block)
            self._dict[name.get_obj()] = desc.get_data()
        return self._dict

    @property
    def sdk_link(self) -> str:
        """Gets sdk_link value"""
        if not self._sdk_link is None:
            return self._sdk_link
        self._sdk_link = self.api_sdk_link.get_obj()
        return self._sdk_link

    @property
    def soup(self) -> base.SoupObj:
        """Gets SoupObj instance for this instance"""
        return self._mb.soup

    @property
    def method_blocks(self) -> ApiMethodBlocks:
        """Gets method_blocks value"""
        return self._mb
    
    @property
    def api_sdk_link(self) -> ApiSdkLink:
        if not self._api_sdk_link is None:
            return self._api_sdk_link
        self._api_sdk_link = ApiSdkLink(soup=self.soup)
        return self._api_sdk_link
# endregion Main Page Parsing


class SdkData():
    """Sdk Data bring together most Sdk object in one easy to upse place"""
    def __init__(self, url: str, allow_cache: bool = True):
        """
        Constructor

        Args:
            url (str): Url to Api Main Page
            allow_cache (bool, optional): determins if file caching is used
                on response data. Default ``True``
        """
        self._url = url
        self._api_sdk_link = ApiSdkLink(base.SoupObj(url=self._url, allow_cache=allow_cache))
        self._soup_obj = None
        self._code_text = None
        self._componnet_text = None
        self._component_start = None
        self._component_lines = None
        self._method_lines = None
        self._property_lines = None
        self._properties = None
        self._extends = None
        self._imports = None
        self._name_info = None
        self._url_obj = None
    
    @property
    def url_obj(self) -> base.UrlObj:
        """Url Object for Api main page"""
        if self._url_obj is None:
            self._url_obj = base.UrlObj(self._url)
        return self._url_obj
    
    @property
    def code_text(self) -> SdkCodeText:
        """Gets sdk_code_text value"""
        if self._code_text is None:
            self._code_text = SdkCodeText(self.sdk_soup_obj)
        return self._code_text

    @property
    def componnet_text(self) -> SdkComponentText:
        """Gets componnet value"""
        if self._componnet_text is None:
            self._componnet_text = SdkComponentText(self.code_text)
        return self._componnet_text

    @property
    def component_start(self) -> SdkComponentStart:
        """Gets component_start value"""
        if self._component_start is None:
            self._component_start = SdkComponentStart(self.componnet_text)
        return self._component_start
    
    @property
    def component_lines(self) -> SdkComponentLines:
        """Gets component_lines value"""
        if self._component_lines is None:
            self._component_lines = SdkComponentLines(self.componnet_text)
        return self._component_lines
    
    @property
    def method_lines(self) -> SdkMethodLines:
        """Gets method_lines value"""
        if self._method_lines is None:
            self._method_lines = SdkMethodLines(self.component_lines)
        return self._method_lines
    
    @property
    def property_lines(self) -> SdkPropertyLines:
        """Gets property_lines value"""
        if self._property_lines is None:
            self._property_lines = SdkPropertyLines(self.component_lines)
        return self._property_lines
    
    @property
    def properties(self) -> SdkProperties:
        """Get properites value"""
        if self._properties is None:
            self._properties = SdkProperties(self.component_lines)
    @property
    def extends(self) -> SdkExtends:
        """Gets extends value"""
        if self._extends is None:
            self._extends = SdkExtends(self.component_start, self.component_lines)
        return self._extends
    
    @property
    def imports(self) -> SdkImports:
        """Gets imports value"""
        if self._imports is None:
            self._imports = SdkImports(self.component_lines)
        return self._imports
    
    @property
    def name_info(self) -> SdkNameInfo:
        """Gets name_info value"""
        if self._name_info is None:
            self._name_info = SdkNameInfo(self.component_start)
        return self._name_info
    @property
    def api_sdk_link(self) -> ApiSdkLink:
        """Gets api_sdk_link value"""
        return self._api_sdk_link
    
    @property
    def sdk_soup_obj(self) -> base.SoupObj:
        """Gets the Soup object reated to SDK page"""
        if self._soup_obj is None:
            self._soup_obj = base.SoupObj(self.api_sdk_link.get_obj())
        return self._soup_obj

    @property
    def api_soup_obj(self) -> base.SoupObj:
        """Gets the Soup object reated to Api page"""
        return self.api_sdk_link.soup
# region Parse
class ParserInterface(base.ParserBase):

    # region Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._sdk_data = SdkData(self.url, allow_cache=self.allow_cache)
        soup = self._sdk_data.api_sdk_link.soup
        self._api_info = ApiInfo(soup)
        self._sdk_method_info = SdkMethods(soup)
        self._sdk_property_info = SdkProperties(self._sdk_data.component_lines)
        self._info = None
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._formated_data = None
        self._data_items = None
    # endregion Constructor

    def get_dict_data(self) -> dict:
        info = self.get_info()
        items = self._get_data_items()
        info['items'] = items
        return info
    
    def get_parser_args(self) -> dict:
        args = {
            "sort": self.sort
        }
        return args
        
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
        if self._info is not None:
            return self._info
        # ns = SdkNamesSpaceInfo(self._sdk_method_info.component)
        ns = base.UrlObj(self._url)
        
        # ni = self._sdk_data.name_info
        ex = self._sdk_data.extends
        # im = self._sdk_data.imports
        desc = ApiDesc(soup=self._api_info.soup)
        result = {
            # 'name': ni.name,
            'name': ns.name,
            # convert set to list for json
            # 'imports': list(im.get_obj()),
            'imports': [],
            'namespace': ns.namespace_str,
            'extends': ex.ex_lst,
            'desc': desc.get_obj(),
            "url": self._api_info.soup.url
        }
        logger.debug('ParserInterface.get_info() name: %s', ns.name)
        logger.debug('ParserInterface.get_info() namespace: %s', ns.namespace_str)
        self._info = result
        return self._info
    
    def get_formated_data(self) -> str:
        if self._formated_data:
            return self._formated_data
        attribs = self._get_data_items()
        str_lst = base.Util.get_formated_dict_list_str(obj=attribs, indent=4)
        self._formated_data = str_lst
        return self._formated_data

    def _get_data_items(self) -> dict:
        if not self._data_items is None:
            return self._data_items
        attribs = {}
        methods = self._get_methods_data()
        prop = self._get_properties_data()
        if 'methods' in methods:
            attribs.update(methods)
        if 'properties' in prop:
            attribs.update(prop)
        self._data_items = attribs
        return self._data_items
        
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
        if self.sort:
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
        if self.sort:
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
            logger.error(e, exc_info=True)
            raise e
        return self._imports
    @property
    def requires_typing(self) -> bool:
        """Gets requires typing value"""
        try:
            if not self._formated_data:
                msg = "ParserInterface.get_formated_data() method must be called before accessing requires_typing"
                raise Exception(msg)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._requires_typing
# endregion Parse

# region Writer


class InterfaceWriter(base.WriteBase):
    # region Constructor
    @TypeCheckKw(arg_info={
        "write_file": 0, "write_json": 0,
        "copy_clipboard": 0, "print_template": 0,
        "print_json": 0, "clear_on_print": 0,
        "write_template_long": 0
        },
        types=[bool],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser: ParserInterface, **kwargs):
        super().__init__(**kwargs)
        self._parser: ParserInterface = parser
        self._copy_clipboard: bool = kwargs.get('copy_clipboard', False)
        self._print_template: bool = kwargs.get('print_template', False)
        self._write_file: bool = kwargs.get('write_template', False)
        self._print_json: bool = kwargs.get('print_json', True)
        self._write_json: bool = kwargs.get('write_json', False)
        self._clear_on_print: bool = kwargs.get('clear_on_print', True)
        self._write_template_long: bool = kwargs.get('write_template_long', False)
        self._indent_amt = 4
        self._json_str = None
        self._p_name: str = None
        self._p_imports: Set[str] = set()
        self._p_imports_typing: Set[str] = set()
        self._p_namespace: str = None
        self._p_extends: List[str] = None
        self._p_desc: List[str] = None
        self._p_data: str = None
        self._p_url: str = None
        self._p_requires_typing = False
        self._path_dir = Path(__file__).parent
        self._cache: Dict[str, object] = {}
        
        t_file = 'interface'
        if not self._write_template_long:
            t_file += '_stub'
        t_file += '.tmpl'
        _path = Path(self._path_dir, 'template', t_file)
        try:
            if not _path.exists():
                raise FileNotFoundError(f"unable to find templae file '{_path}'")
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
    
    def _get_json(self) -> str:
        if not self._json_str is None:
            return self._json_str
        p_dict = {}
        p_dict['from_imports'] = self._get_from_imports()
        p_dict['from_imports_typing'] = self._get_from_imports_typing()
        p_dict.update(self._parser.get_dict_data())
        
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "timestamp": str(base.Util.get_timestamp_utc()),
            "name": p_dict['name'],
            "type": "interface",
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {},
            "data": p_dict
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._json_str = str_jsn
        return self._json_str
    
    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    # region get Imports
    def _get_from_imports(self) -> List[List[str]]:
        key = '_get_from_imports'
        if key in self._cache:
            return self._cache[key]
        lst = []
        for ns in self._p_imports:
            f, n = base.Util.get_rel_import(
                i_str=ns, ns=self._p_namespace
            )
            lst.append([f, n])
        self._cache[key] = lst
        return self._cache[key]

    def _get_from_imports_typing(self) -> List[List[str]]:
        key = '_get_from_imports_typing'
        if key in self._cache:
            return self._cache[key]
        lst = []
        for ns in self._p_imports_typing:
            f, n = base.Util.get_rel_import(
                i_str=ns, ns=self._p_namespace
            )
            # lst.append(f)
            # lst.append(n)
            lst.append([f, n])
        self._cache[key] = lst
        return self._cache[key]
    # endregion get Imports
    
    def _set_template_data(self):
        if self._write_template_long is False:
            return
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{ns}', str(self._p_namespace))
        self._template = self._template.replace('{link}', self._p_url)
        self._template = self._template.replace(
            '{requires_typing}', str(self._p_requires_typing))
        self._template = self._template.replace(
            '{inherits}', base.Util.get_string_list(lines=self._p_extends))
        self._template = self._template.replace(
            '{imports}', "[]")
        self._template = self._template.replace(
            '{from_imports}',
            base.Util.get_formated_dict_list_str(self._get_from_imports())
        )
        self._template = self._template.replace(
            '{from_imports_typing}',
            base.Util.get_formated_dict_list_str(
                self._get_from_imports_typing())
        )
        if len(self._p_desc) > 0:
            desc = base.Util.get_formated_dict_list_str(self._p_desc, indent=4)
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
            return [base.Util.get_last_part(s) for s in lst]
            # return [s.rsplit('.', 1)[1] for s in lst]
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_namespace = data['namespace']
        self._p_extends = get_extends(data['extends'])
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_data = self._parser.get_formated_data()
        self._validate_p_info()
        _imports = data['imports']
        self._p_imports.update(_imports)
        self._p_imports.update(data['extends'])
        self._p_imports_typing.update(self._parser.imports)
        if len(self._p_imports_typing) > 0:
            self._p_requires_typing = True
        if not self._p_requires_typing:
            self._p_requires_typing = self._parser.requires_typing
        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()
    
    def _validate_p_info(self):
        try:
            if not self._p_name:
                raise Exception(
                    "InterfaceWriter: validation fail: name is an empty string.")
            if not self._p_url:
                raise Exception(
                    "InterfaceWriter: validation fail: url is an empty string.")
            if not self._p_namespace:
                raise Exception(
                    "InterfaceWriter: validation fail: namespace is an empty string.")
        except Exception as e:
            logger.error(e)
            raise e
    
    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        if not self._p_name:
            try:
                raise Exception("InterfaceWriter._get_uno_obj_path() Parser provided a name that is an empty string.")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e
            
        uno_obj_path = Path(self._path_dir.parent, 'uno_obj')
        name_parts: List[str] = self._p_namespace.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append(self._p_name + '.tmpl')
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._cache[key] = obj_path
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
# endregion Writer


def _main():
   
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XSvgParser.html'
    url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1office_1_1XAnnotation.html'
    sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    main()

def main():
    global logger
    # region Parser
    parser = argparse.ArgumentParser(description='interface')
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
        '-g', '--long-template',
        help='Writes a long format template. Requires --write-template is set. No Autoload',
        action='store_true',
        dest='long_format',
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
        help='Log file to use. Defaults to interface.log',
        type=str,
        required=False)

    args = parser.parse_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'interface.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    # endregion Parser
    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)
    
    p = ParserInterface(
        url=args.url,
        sort=args.sort,
        cache=args.cache
    )
    w = InterfaceWriter(
        parser=p,
        print_template=args.print_template,
        print_json=args.print_json,
        copy_clipboard=args.clipboard,
        write_template=args.write_template,
        write_json=args.write_json,
        clear_on_print=(not args.no_print_clear),
        write_template_long=args.long_format
        )
    if args.print_template is False and args.print_json is False:
        print('')
    w.write()

if __name__ == '__main__':
    main()

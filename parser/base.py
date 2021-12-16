# coding: utf-8
"""
Base classes and helper functions of various types that are used with different parsers
"""
from dataclasses import dataclass
import os
import sys
import re
import requests
import textwrap
import json
import logging
import tempfile
import time
import calendar
import hashlib
import inspect
import importlib
from types import ModuleType
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from glob import glob
from kwhelp.decorator import AcceptedTypes, DecArgEnum, DecFuncEnum, RequireArgs, RuleCheckAll, RuleCheckAllKw, TypeCheck, TypeCheckKw
from kwhelp import rules
from pathlib import Path
from typing import Iterable, List, Set, Tuple, Union
from datetime import datetime, timezone

# this is for VS code debuging
_app_root = os.environ.get('project_root', str(Path(__file__).parent.parent))
if not _app_root in sys.path:
    sys.path.insert(0, _app_root)
# print(sys.path)
# this is for command line
# sys.path.insert(0, os.path.abspath('..'))

logger: logging.Logger  = None

#  \W = [^a-zA-Z0-9_]
py_name_pattern = re.compile('[\W_]+')
py_ns_pattern = re.compile(r'[^a-zA-Z0-9\._]+')
curly_brace_close_pattern = re.compile(r'[^};]')
RESPONSE_CACHE: 'FileCache' = None
pattern_http = re.compile(r"^https?:\/\/")
"""FileCache object for caching response data"""

TYPE_MAP = {
    "any": "object",
    "short": "int",
    "long": "int",
    "float": "float",
    "double": "float",
    "string": "str",
    "char": "str",
    "boolean": "bool",
    "sequence": "list",
    "aDXArray": "list",
    "void": "None",
    'type': 'object'
}


def str_clean(input: str, **kwargs) -> str:
    """
    Cleans and encodes string for template replacemnt

    Keyword Arguments:
        replace_dual (bool, optional): Replace ``::`` with ``.`` Default ``True``
    """
    _replace_dual = bool(kwargs.get('replace_dual', True))
    result = input
    if _replace_dual:
        result = result.replace("::", ".")
    result = result.replace('\\n', '\\\\\\\\n').replace('\\r', '\\\\\\\\r')
    result = result.replace('"', '\\"')
    return result.strip()

class FileCache:
    """
    Caches files and retreives cached files.
    Cached file are in a subfolder of system tmp dir.
    """
    
    def __init__(self, tmp_dir='ooo_uno_tmpl', lifetime: float = 60.0) -> None:
        """
        Constructor

        Args:
            tmp_dir (str, optional): Dir name to create in tmp folder. Defaults to 'ooo_uno_tmpl'.
            lifetime (float, optional): Time in seconds that cache is good for. Defaults to 60 seconds.
        """
        t_path =Path(tempfile.gettempdir())
        self._cache_path = t_path / tmp_dir
        Util.mkdirp(self._cache_path)
        self._lifetime = lifetime   

    def fetch_from_cache(self, filename: Union[str, Path]) -> Union[str, None]:
        """
        Fetches file contents from cache if it exist and is not expired

        Args:
            filename (Union[str, Path]): File to retrieve

        Returns:
            Union[str, None]: File contents if retrieved; Otherwise, ``None``
        """
        f = Path(self._cache_path, filename)
        if not f.exists():
            return None

        if self._lifetime > 0:
            f_stat = f.stat()
            ti_m = f_stat.st_mtime
            age = time.time() - ti_m
            if age >= self._lifetime:
                return None
        try:
            # Check if we have this file locally
            
            with open(f) as fin:
                content = fin.read()
            # If we have it, let's send it
            return content
        except IOError:
            return None

    def save_in_cache(self, filename: Union[str, Path], content: str):
        """
        Saves file contents into cache

        Args:
            filename (Union[str, Path]): filename to write.
            content (str): Contents to write into file.
        """
        f = Path(self._cache_path, filename)
        # print('Saving a copy of {} in the cache'.format(filename))
        with open(f, 'w') as cached_file:
            cached_file.write(content)


class ResponseObj:
    """Gets response data"""
    @RuleCheckAllKw(
        arg_info={
            "url": rules.RuleStrNotNullEmptyWs,
            "cache_seconds": rules.RuleNumber
        },
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, url: str, cache_seconds:float = 604800.0, **kwargs):
        """
        Constructor

        Args:
            url (str): Url to retrieve html
            allow_cache (bool, optional): Determins if caching is used.
                If ``True`` html will be written to cache. Defaults to True.
            cache_seconds (float, optional): The number of seconds that html
                contents will be cached for. Default is ``604800.0`` ( one week )

        Keyword Arguments:
            has_name (bool, optional): If ``True`` name is extracted from
                url and namespace excludes name. Default ``True``.
                This applies to ``url_obj`` property
        """
        self._url = url
        self._url_obj = UrlObj(url=self._url, **kwargs)
        self._lifetime = cache_seconds
        if self._lifetime > 0:
            self._url_hash = hashlib.md5(self._url_obj.url_only.encode('utf-8')).hexdigest()
        else:
            self._url_hash = ''
        self._text = None

    # cache for one week - 604800.0 seconds
    def _get_request_text(self) -> str:
        global RESPONSE_CACHE
        allow_cache = self._lifetime > 0
        if allow_cache:
            if not RESPONSE_CACHE:
                RESPONSE_CACHE = FileCache(lifetime=self._lifetime)
            html_text = RESPONSE_CACHE.fetch_from_cache(self._url_hash)
            if html_text:
                logger.debug("ResponseObj._get_request_text() retreived data from Cache")
                return html_text
        response = requests.get(url=self._url)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        html_text = response.text
        if allow_cache:
            RESPONSE_CACHE.save_in_cache(self._url_hash, html_text)
            logger.debug("ResponseObj._get_request_text() Saving to cache as: %s", self._url_hash)
        return html_text

    @property
    def url(self) -> str:
        """Specifies url"""
        return self._url
    
    @property
    def url_obj(self) -> 'UrlObj':
        """Gets url_obj value"""
        return self._url_obj

    @property
    def raw_html(self) -> str:
        """
        Gets raw html of url
        """
        if self._text is None:
            self._text = self._get_request_text()
        return self._text
    @property
    def cache_seconds(self) -> float:
        """Specifies allow_cache
    
            :getter: Gets cache_seconds value.
            :setter: Sets cache_seconds value.
        """
        return self._lifetime
    
    @cache_seconds.setter
    def cache_seconds(self, value: float):
        self._lifetime = value
        logger.debug('ResponseObj: caching is set to: %d', value)


class SoupObj:
    """Wrapper for BeautifulSoup"""
    @RuleCheckAllKw(
        arg_info={
            'url': rules.RuleStrNotNullEmptyWs,
            'allow_cache': rules.RuleBool
        },
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, url: str, allow_cache: bool = True, **kwargs) -> None:
        """
        Constructor

        Args:
            url (str): Url of http page
            allow_cache (bool, optional): If ``True`` html contents are cached. Defaults to ``True``.

        Keyword Arguments:
            has_name (bool, optional): If ``True`` name is extracted from
                url and namespace excludes name. Default ``True``.
                This applies to ``url_obj`` property
        """
        if allow_cache:
            self._response = ResponseObj(url=url, **kwargs)
        else:
            self._response = ResponseObj(url=url, cache_seconds=0, **kwargs)
        self._soup = None

    @property
    def soup(self) -> BeautifulSoup:
        """Gets soup for this instance"""
        if not self._soup:
            self._soup = BeautifulSoup(self._response.raw_html, 'lxml')
        return self._soup

    @property
    def response(self) -> ResponseObj:
        """Gets this instance response"""
        return self._response

    @property
    def url(self) -> str:
        """Specifies url"""
        return self._response.url
    
    @property
    def url_obj(self) -> 'UrlObj':
        """Specifies url"""
        return self._response.url_obj

    @property
    def allow_cache(self) -> bool:
        """Specifies allow_cache
    
            :getter: Gets allow_cache value.
            :setter: Sets allow_cache value.
        """
        return self._response.allow_cache
    
    @allow_cache.setter
    def allow_cache(self, value: bool):
        self._response.allow_cache = value

class Util:
    """Utility class of static methods for operations"""
    @dataclass
    class RealitiveInfo:
        """
        Realitive info
        """
        in_branch: str
        """Original input branch"""
        comp_branch: str
        """Original branch to compare to in_branch"""
        sep: str
        """Seperator"""
        in_branch_rel: List[str]
        """Compare result relative part of in_branch"""
        comp_branch_rel: List[str]
        """Compare result relative part of comp_branch"""
        distance: int
        """Distance between branches"""
        common_parts: List[str]
        """part that in_branch and comp_branch have in common"""

    @staticmethod
    def get_rel_info(in_branch: str, comp_branch: str, sep: str = '.') -> RealitiveInfo:
        """
        Gets realitive info between branches such as ``com.sun.star.configuration``
        and ``com.sun.star.uno``

        Args:
            in_branch (str): branch to compare
            comp_branch (str): branch to get realitive information from compared to ``in_branch``
            sep (str, optional): Branch seperator. Defaults to ``.``

        Returns:
            RealitiveInfo: Class instance containing realitive info.
        """
        in_branch_parts = in_branch.split(sep)
        comp_branch_parts = comp_branch.split(sep)
        rel_len = len(comp_branch_parts)
        common_roots = 0
        for i, b in enumerate(in_branch_parts):
            if i > rel_len:
                break
            try:
                if b == comp_branch_parts[i]:
                    common_roots += 1
                    continue
            except IndexError:
                break
            break
        # comp_branch_rel = in_branch_parts[common_roots:]
        comp_branch_rel = comp_branch_parts[common_roots:]
        in_branch_rel = in_branch_parts[common_roots:]
        diff = len(in_branch_rel)
        distance = diff
        common_parts = in_branch_parts[:common_roots]
        # result = ((diff + 1), sep.join(comp_branch_rel))
        result = Util.RealitiveInfo(
            in_branch=in_branch,
            comp_branch=comp_branch,
            sep=sep,
            in_branch_rel=in_branch_rel,
            comp_branch_rel=comp_branch_rel,
            distance=distance,
            common_parts=common_parts
        )
        # sep_str = sep * (diff + 1)
        logger.debug("Util.get_rel_info(): %s", str(result))
        return result
    
    @staticmethod
    def get_timestamp_utc() -> datetime:
        """
        Gets utc timestamp in format of ``2021-12-16 11:37:50+00:00``

        Returns:
            datetime: utc timestamp
        """
        current_GMT = time.gmtime()
        ts = calendar.timegm(current_GMT)
        return datetime.fromtimestamp(ts, tz=timezone.utc)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_timestamp_from_str(input:str) -> datetime:
        """
        Converts input in the format of ``2021-12-16 11:37:50+00:00`` into datetime

        Args:
            input (str): input date string

        Returns:
            datetime: input converted to ``datetime``
        """
        try:
            dt_object = datetime.strptime(input, "%Y-%m-%d %H:%M:%S%z")
            return dt_object
        except ValueError as e:
            logger.error("Util.get_timestamp_from_str() Error: %s", str(e))
            raise e

    @AcceptedTypes(int, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def is_enum_nums(*args: int) -> bool:
        """
        Test to see if a sequence of numbers can be combinded a flags

        Returns:
            bool: ``True`` if can be combined as flags; Otherwise ``False``
        """
        nums = [*args]
        nums.sort()
        n = 0
        for num in nums:
            if num < 0:
                return False
            _n = n
            _n = _n ^ num
            if _n <= n:
                return False
            n = _n
        return True

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_clean_name(input: str, sub: str = '') -> str:
        """
        Removes all char from a string except for ``a-zA-Z0-9_``

        Args:
            input (str): string to clean
            sub (str, optional): replacement string for non matching characters.
                Default is empty string.

        Returns:
            str: input with any other chars replaced
        """
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        return py_name_pattern.sub(sub, input)
    
    @AcceptedTypes(str,str, bool, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_clean_ns(input: str, sub: str='', ltrim=False) -> str:
        """
        Removes all char from a string except for ``a-zA-Z0-9_.``

        Args:
            input (str): string to clean
            sub (str, optional): replacement string for non matching characters.
                Default is empty string.
            ltrim (bool, optonal): if ``True`` leading ``.`` are removed. Default ``False``

        Returns:
            str: input with any other chars replaced
        """
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        if ltrim is False:
            return py_ns_pattern.sub(sub, input)
        return py_ns_pattern.sub(sub, input).lstrip('.')
    
    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def clean_curly_brace_close(input: str) -> str:
        """
        Removes all char from a string except for ``};``

        Args:
            input (str): string to clean

        Returns:
            str: input with any other chars replaced
        """
        return curly_brace_close_pattern.sub('', input)

    @AcceptedTypes((dict, list), int, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_formated_dict_list_str(obj: Union[dict, list], indent=4) -> str:
        """
        Get a formated dictionary or list

        Args:
            obj (Union[dict, list]): Dict or list to get formates string for.
            indent (int, optional): The number of spaces to indent string.. Defaults to ``2``.

        Returns:
            str: string of formated dictionary properties and values
        """
        if not isinstance(obj, dict) and not isinstance(obj, list):
            return "{}"
        _indent = 4 if indent < 0 else indent
        formatted = json.dumps(obj, indent=_indent)
        return formatted

    @AcceptedTypes((list, tuple), int, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_string_list(lines: List[str], indent_amt: int = 0) -> str:
        """
        Converts a list into str.
        Similar to calling str(lines) but handles more edge cases.

        Args:
            lines (List[str]): list to convert
            indent_amt (int, optional): Amount to indent results. Defaults to 0.

        Returns:
            str: List as string.
        """
        _lines = Util._encode_list(lines)
        c_lines = Util._decode_list(str(_lines).split(','))
        s = ',\n'.join(c_lines)
        if indent_amt > 0:
            s = Util.indent(text=s, indent_amt=indent_amt)
        return s

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_last_part(input: str, sep='.') -> str:
        """
        Splits a string and returns the last part

        Args:
            input (str): string to get last part of.
            sep (str, optional): string used to split. Defaults to ``.``

        Returns:
            str: [description]
        """
        if not input:
            return ''
        _parts = input.rsplit(sep, 1)
        return _parts[0] if len(_parts) == 1 else _parts[1]

    @AcceptedTypes(str, int, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def indent(text: str, indent_amt: int = 4) -> str:
        """
        Indents a multi line string

        Args:
            text (str): text to apply indent
            indent_amt (int, optional): Amout of indent. Defaults to 4.

        Returns:
            str: indented text.
        """
        if indent_amt <= 0:
            return text
        indent = ' ' * indent_amt
        s = textwrap.indent(text, indent)
        return s

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def camel_to_snake(input: str) -> str:
        """
        Converts Camel case to snake clase

        Args:
            name (str): Camel name

        Returns:
            str: snake case
        """
        _input = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', _input).lower()

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_rel_import(i_str: str, ns: str, sep: str = '.') -> Tuple[str, str]:
        """
        Gets realitive import Tuple

        Args:
            i_str (str): Namespace and object such as ``com.sun.star.uno.Exception``
            ns (str): Namespace used to get realitive postion such as ``com.sun.star.awt``
            sep (str, optional): Namespace seperator. Defaults to ``.``

        Returns:
            Tuple[str, str]: realitive import info such as ``('..uno.exception', 'Exception')``
        """
        # i_str = com.sun.star.uno.Exception
        # ns = com.sun.star.configuration
        # ("..uno.exception", "Exception")
        # compare ns to ns so drop last name of i_str
        name_parts = i_str.split(sep)
        name = name_parts.pop()
        camel_name = Util.camel_to_snake(name)
        ns2 = sep.join(name_parts)
        if ns2 == ns:
            logger.debug("get_rel_import(): Names are equal: '%s'", ns)
            logger.debug(f"get_rel_import(): Returning (.{camel_name}', '{name})")
            return (f'.{camel_name}', f'{name}')
        if len(name_parts) == 1:
            # this is a single word
            # assume it is in the same namespace as this import
            logger.debug(
                "get_rel_import(): '%s', single word. Converting to from import and returning", i_str)
            return (f'.{Util.camel_to_snake(i_str)}', f'{i_str}')
        try:
            info = Util.get_rel_info(in_branch=ns, comp_branch=ns2, sep=sep)
            prefix = sep * (info.distance + 1)
            result_parts = info.comp_branch_rel + [camel_name]
            from_str = prefix
            from_str = from_str + sep.join(result_parts)
            return (from_str, name)
        except Exception as e:
            logger.error(e, exc_info=True)
        short = ns2.replace('com.sun.star.', '')
        logger.warn(
            f"get_rel_import(): Last ditch effort. Returning: (ooo_uno.uno_obj.{short}.{camel_name}', {name})")
        return (f'ooo_uno.uno_obj.{short}.{camel_name}', f'{name}')

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def encode_char(input:str, replace:str, en:str = '\xff') -> str:
        """
        Encodes all matching chars in a string with the value of ``en``.
        Chars ``\\xff`` and ``\\xfe`` are BOM

        Args:
            input (str): text to search and replace
            replace (str): char to replace all instances of
            en (str, optional): Value to replace. Defaults to ``\\xff``.

        Returns:
            str: input with chars replace with ``en`` value
        """
        return input.replace(replace, en)

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def decode_char(input: str, restore: str, de: str = '\xff') -> str:
        """
        Decodes allmathing chars in a string with the value of ``restore``.
        Chars ``\\xff`` and ``\\xfe`` are BOM

        Args:
            input (str): text to search and restore
            restore (str): char to restore
            de (str, optional): value to decode. Defaults to ``\\xff``.

        Returns:
            str: [description]
        """
        return input.replace(de, restore)

    @TypeCheckKw(arg_info={"typings": 0, "quote": 0}, types=[bool], ftype=DecFuncEnum.METHOD_STATIC)
    @AcceptedTypes(str, opt_args_filter=DecArgEnum.NAMED_ARGS, ftype = DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_py_type(uno_type: str, **kwargs) -> str:
        """
        Gets python type from uno type.
        
        Converts values such as ``sequence< ::com::sun::star::uno::XInterface>`` =>
        ``List[XInterface]``. Also simple conversion such as ``long`` => ``int``
        
        Args:
            uno_type (str): Uno type such as ``long``
        
        Keyword Args:
            typings (bool, optional): If ``True`` typings is added in front of wrapped
                so ``List[int]`` => ``typing.List[int]. Default ``True``
            cb (callable, optional): callback function. eg: ``cb(data)``
            quote (bool, optional): If ``True`` return value will be wrapped in quotes
                for non python types such as ``'XInterface'``. Default ``True``

        Returns:
            str: ``uno_type`` converted to python type.

        Notes:
            Conversion can be complex operation. For this reason a callback function
            can be passed in.
            
            Callback function signature is ``cb(data)``
            Callback ``data`` is a dictionary of information about the conversion.
            If ``uno_type`` is a sequence (list) then ``data['wdata']`` contains info
            on the sequence.
            
            ``data``: {
                "uno_type":     "(str): original uno_type value passed in",
                "is_py_type":   "(bool): Will be True if uno_type is converted to a python type
                                    such as long => int. Will also be True for sequences that match
                                    such as sequence<long> => list[int].",
                "is_wrapper":   "(bool): if conversoin results in sequence<long> => List[int]",
                "is_typing":    "(bool): True if is wrapped and typings arg is True; Otherwise, False",
                "long_type":    "(str): ns and type such as com.sun.star.awt.AdjustmentType
                                    When sequence is found this will still be the long name of the inner wrapped.
                "wdata": {
                    "is_py_type":    "(bool): True if wrapper type is a python type such as List; Otherwise, False",
                    "py_type_inner": "(bool): True if wrapped is a python type such as int; Otherwise, False",
                    "prefix":        "(str): prefixe will not be added if typings arg is False",
                    "wrapper":       "(str): Wrapper such as typing.List or List",
                    "long_type":     "(str); ns and type such as com.sun.star.awt.AdjustmentType
                },
                "returns": "(object, optional): Default value is None. If a value is assigned
                            during callback then the value of returns will be returned from method.
            }
        """
        if not uno_type:
            return ''
        def do_cb(_cb:callable, data):
            if not _cb:
                return
            _cb(data)
    
        add_typings = bool(kwargs.get('typings', True))
        arg_quote = bool(kwargs.get('quote', True))
        cb = kwargs.get('cb', None)
        cb_data = {
            "uno_type": uno_type,
            "is_py_type": False,
            "is_wrapper": False,
            "is_typing": False,
            "returns": None,
            "wdata": {}
        }
        _u_type = uno_type.strip().lstrip(':').lstrip().replace("::", ".")
        # check for # sequence< string >
        parts = _u_type.split(sep='<', maxsplit=1)
        if len(parts) > 1:
            is_pytype = True
            cb_data['is_wrapper'] = True
            clean_wrapper = Util.get_last_part(Util.get_clean_name(parts[0]))
            wrapper = TYPE_MAP.get(clean_wrapper, None)
            if wrapper:
                cb_data['wdata']['is_py_type'] = True
            else:
                is_pytype = False
                cb_data['wdata']['is_py_type'] = False
            type_pre = "typing." if add_typings else ''
            cb_data['is_typing'] = add_typings
            cb_data['wdata']['prefix'] = type_pre
            if wrapper:
                # got a match from TYPE_MAP
                # title case the word and add typings
                wrapper = type_pre + wrapper.title()
            else:
                wrapper = type_pre + 'List'
            cb_data['wdata']['wrapper'] = wrapper
            _type = Util.get_clean_ns(input=parts[1],ltrim=True)
            cb_data['long_type'] = _type
            _type = Util.get_last_part(_type)
            map_type = TYPE_MAP.get(_type, None)
            is_inner_py_type = True
            if not map_type:
                is_inner_py_type = False
                is_pytype = False
                map_type = _type
            cb_data['wdata']['py_type_inner'] = is_inner_py_type
                
            cb_data['is_py_type'] = is_pytype
            cb_data['type'] = map_type
                
            do_cb(cb, cb_data)
            if cb_data['returns']:
                return cb_data['returns']
            if is_inner_py_type is False and arg_quote is True:
                return f"'{wrapper}[{map_type}]'"
            return f"{wrapper}[{map_type}]"
        cb_data['long_type'] = Util.get_clean_ns(_u_type)
        _u_type_clean = Util.get_clean_name(Util.get_last_part(_u_type))
        result = TYPE_MAP.get(_u_type_clean, None)
        if result:
            if _u_type_clean == "type":
                # edge case of type of type
                # type is mapped to object in TYPE_MAP
                cb_data['is_typing'] = True
                result = f"typing.Type"
            cb_data['is_py_type'] = True
            cb_data['type'] = result
            do_cb(cb, cb_data)
            return result
        cb_data['type'] = _u_type_clean
        do_cb(cb, cb_data)
        if cb_data['returns']:
            return cb_data['returns']
        if arg_quote:
            return f"'{_u_type_clean}'"
        return _u_type_clean

    @AcceptedTypes((str, Path), ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def mkdirp(dest_dir: Union[str, Path]):
        """
        Creates directory and all child directories if needed

        Args:
            dest_dir (Union[str, Path]): path to create directories for.
                Must be dir path only. No checking is done for file names.
        """
        # Python ≥ 3.5
        if isinstance(dest_dir, Path):
            dest_dir.mkdir(parents=True, exist_ok=True)
        else:
            Path(dest_dir).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _encode_list(lst: List[str]) -> List[str]:
        results = []
        for el in lst:
            s = Util.encode_char(el, ',')
            results.append(s)
        return results

    @staticmethod
    def _decode_list(lst: List[str]) -> List[str]:
        results = []
        for el in lst:
            s = Util.decode_char(el, ',')
            results.append(s)
        return results

# region Import check


class ImportCheck:
    """
    Dynamically imports classes from scratch.
    Allows for testing of classes that are inherited so
    services do not inherit classes that are already inherited by a
    child class.
    """
    # https://stackoverflow.com/questions/31028237/getting-all-superclasses-in-python-3
    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def __init__(self, ns: str):
        """
        Constructor

        Args:
            ns (str): Namespace of the component being tested
                such as ``com.sun.star.uno``
        """
        self._imports = {}
        self._prefix = 'scratch.uno_obj'
        self._unique: Set[str] = set()
        self._ns = ns
        self._ns_mod = Util.get_last_part(self._ns)

    def _get_name_part(self, import_name: str) -> str:
        name = import_name
        if name.startswith('com.sun'):
            name = name[13:]
            # accessibility.XAccessibleContext
        else:
            name = self._ns_mod + '.' + name
        return name

    @AcceptedTypes((list, tuple, set), ftype=DecFuncEnum.METHOD)
    def load_imports(self, imports: List[str]):
        """
        Load a list of import names for later comparsion.
        Name can be in format of ``com.sun.star.accessibility.XAccessibleContext``
        or ``XAccessibleContext``

        Args:
            imports (List[str]): List of imports
    
        Note:
            If an import is unable to load then it is simpley ignored
            and not tested.
        """
        # imports will be in format of:
        # com.sun.star.accessibility.XAccessibleContext
        # or
        # XAccessibleContext
        for im in imports:
            name = self._get_name_part(im)
            parts = name.rsplit(sep='.', maxsplit=1)
            pkg_name = f"{self._prefix}.{parts[0]}"
            cls_name = parts[1]
            mod_name = Util.camel_to_snake(cls_name)
            try:
                mod, cl = self.dynamic_imp(pkg_name, mod_name, cls_name)
            except Exception as e:
                logger.warn(
                    'ImportCheck.load_imports() Unable to load module for : Package:%s, Module: %s Class: %s', pkg_name, mod_name, cls_name)
                continue
            names_lst = self.get_class_names(cl, False)

            for n in names_lst:
                self._unique.add(n)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def is_inherited(self, import_name: str) -> bool:
        """
        Test if the ``import_name`` is inherited by any of the current
        classes loaded through ``load_imports()``.

        Args:
            import_name (str): import to test

        Returns:
            bool: ``True`` if already inherited by another class; Otherwise, ``False``
        """
        name = self._get_name_part(import_name)
        return name in self._unique

    def get_class_name(self, obj):
        if (inspect.isclass(obj) == False):
            obj = obj.__class__
        class_name = obj.__name__
        return class_name

    # Works both for python 2 and 3
    @AcceptedTypes(object, bool, ftype=DecFuncEnum.METHOD)
    def get_class_names(self, obj: object, include_obj: bool = True):
        class_name = []
        if (inspect.isclass(obj) == False):
            obj = obj.__class__
        classes = inspect.getmro(obj)
        c_name = str(obj.__name__)
        for cl in classes:
            name = cl.__name__
            if include_obj is False:
                if name == c_name:
                    continue
            mod = cl.__module__
            if mod.startswith(self._prefix):
                # scratch.uno_obj.uno.x_interface
                _mod = mod.split(sep='.', maxsplit=2)[2]  # uno.x_interface
                _mod = _mod.rsplit(sep='.', maxsplit=1)[0]  # uno
                class_name.append(f"{_mod}.{name}")
        return class_name

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD)
    def dynamic_imp(self, package: str, mod_name: str, class_name: str) -> Tuple[ModuleType, object]:
        try:
            key = f"{package}.{mod_name}"
            if key in self._imports:
                module = self._imports[key]
            else:
                module = importlib.import_module(key)
                self._imports[key] = module
            my_class = getattr(module, class_name)
            return module, my_class
        except Exception as e:
            # print(e)
            raise e

# endregion Import check

class UrlObj:
    """Properties of url"""
    @RuleCheckAllKw(
        arg_info={
            "url": rules.RuleStrNotNullEmptyWs,
            "has_name": rules.RuleBool
        },
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, url: str, **kwargs):
        """
        Constructor

        Args:
            url (str): Url

        Keyword Arguments:
            has_name (bool, optional): If ``True`` name is extracted from
                url and namespace excludes name. Default ``True``
        """
        self._url = url
        self._has_name = kwargs.get('has_name', True)
        u_parts = self._url.rsplit('/', 1)
        # similar to: namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925
        self._page_link = u_parts[1]
        self._url_base = u_parts[0]
        f_parts = self._url.split(sep='#', maxsplit=1)
        if len(f_parts) > 1:
            self._url_only = f_parts[0]
            self._fragment = f_parts[1]
            self._is_frag = True
        else:
            self._url_only = self._url
            self._fragment = ''
            self._is_frag = False
        self._name = None if self._has_name else ''
        
        self._ns = None
        self._ns_str = None
        

    def get_split_ns(self) -> List[str]:
        result = []
        try:
            ns_part = self._page_link.split('.')[0]
            s = ns_part.replace('_1_1', '.').lstrip('.')
            # the frist part on the str usually is prefixed with namespace, interface or whatever.
            # namespace always start with com so just drop the first part to clean it up.
            s = 'com.' + s.split('.', maxsplit=1)[1]
            result = s.split('.')
        except Exception as e:
            logger.error(e)
            logger.info('UrlObj._get_ns() returning empty list.')
        return result
    
    def _get_ns(self) -> List[str]:
        try:
            result = self.get_split_ns()
        
            # get that last item
            self._name = result[-1:][0]
            # Drop the component from the result
            if self._has_name:
                self._ns = result[:-1]
            else:
                self._ns = result
        except Exception as e:
            logger.error(e)
            logger.info('UrlObj._get_ns() returning empty list.')
        return result



    @property
    def page_link(self) -> str:
        """
        Gets page link similar to ``namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925``
        """
        return self._page_link

    @property
    def fragment(self) -> str:
        """
        Gets fragment simalar to a3ae28cb49c180ec160a0984600b2b925
        """
        return self._fragment

    @property
    def name(self) -> str:
        """
        Get name portion of html link such as SpinningProgressControlModel
        """
        if self._name is None:
            self._get_ns()
        return self._name

    @property
    def is_fragment(self) -> bool:
        """
        Gets if there is a fragment
        """
        return self._is_frag

    @property
    def namespace(self) -> List[str]:
        """
        Gets Namespace in format of ['com', 'sun', 'star', 'style']
        """
        if self._ns is None:
            self._get_ns()
        return self._ns

    @property
    def namespace_str(self) -> str:
        """
        Gets namespace in format of 'com.sun.star.style'
        """
        if not self._ns_str:
            self._ns_str = '.'.join(self.namespace)
        return self._ns_str

    @property
    def url(self) -> str:
        """Gets url value"""
        return self._url

    @property
    def url_base(self) -> str:
        """
        Gets url base value such as:
        ``https://api.libreoffice.org/docs/idl/ref``
        """
        return self._url_base
    
    @property
    def url_only(self) -> str:
        """
        Gets full url without fragment
        """
        return self._url_only

class BlockObj(ABC):
    """
    Abstract Class.

    Represents a Html Block.
    """

    def __init__(self, soup: SoupObj):
        """
        Constructor

        Args:
            soup (SoupObj): soup for this instance
        """
        self._soup = soup
        self._url = soup.url
        self._urlobj = self._get_url_obj()

    def _get_url_obj(self):
        return UrlObj(self._url)

    @abstractmethod
    def get_obj(self) -> Tag:
        """Get object"""

    @property
    def url(self) -> str:
        """Gets Url"""
        return self._url

    @property
    def soup(self) -> SoupObj:
        """Gets SoupObj instance for this instance"""
        return self._soup

    @property
    def url_obj(self) -> UrlObj:
        """Gets UrlObj instance for this instance"""
        return self._urlobj


class TagsStrObj:
    """Class that converts list of tags to string"""

    def __init__(self, tags: Iterable[Tag], **kwargs):
        """
        Constructor

        Args:
            tags (Iterable[Tag]): List of tags

        Keyword Arguments:
            clean (bool, optional): If ``True`` then data will be cleaned
                using ``str_clean`` method. Default ``True``
            empty (bool, optional): If ``True`` empty lines will be added
                between other lines. Default ``True``
            indent (int, optional): The number of spaces to indent for 
                methods that return a string. Default ``0``
        """
        self._tags = tags
        self._clean = bool(kwargs.get('clean', True))
        self._empty_lines = bool(kwargs.get('empty', True))
        self._indent_amt = int(kwargs.get('indent', 0))

    def get_lines(self) -> List[str]:
        """Gets lines for this instance"""
        lines = []
        i = 0
        for ln in self._tags:
            s = ln.text.strip()
            if not s:
                continue
            if self._clean:
                s = str_clean(input=s)
            if i > 0 and self._empty_lines:
                lines.append("")
            lines.append(s)
            i += 1
        return lines

    def get_data(self) -> List[str]:
        """Gets Lines as string for this instance"""
        return self.get_lines()

    def get_string_list(self) -> str:
        # lines = self._encode_list(self.get_lines())
        # c_lines = self._decode_list(str(lines).split(','))
        # s = ',\n'.join(c_lines)
        s = Util.get_string_list(self.get_lines())
        if self._indent_amt > 0:
            s = Util.indent(text=s, indent_amt=self._indent_amt)
        return s


class WriteBase(object):
    def __init__(self, **kwargs):
        pass
    def _mkdirp(self, dest_dir):
        Util.mkdirp(dest_dir=dest_dir)

    def _get_project_path(self) -> Path:
        return Path(__file__).parent.parent

    def _get_template_path(self) -> Path:
        project_path = self._get_project_path()
        return project_path.joinpath('template')

    def _get_template_files(self) -> List[str]:
        p = self._get_template_path()
        pattern = str(p) + '/_*.py'
        files = glob(pattern, recursive=False)
        return files


class ParserBase(object):
    @RequireArgs('url', ftype=DecFuncEnum.METHOD)
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "cache": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        self._allow_cache: bool = kwargs.get('cache', True)
        self._indent = '    '
        self._url = kwargs.get('url', '')
        self._raw = ''
        self._sort = kwargs.get('sort', True)
        self._replace_dual_colon = kwargs.get('replace_dual_colon', True)
        self._title_full = None
        self._response_obj = None

    # region internal Non specific methods
    def _get_number(self, input: str) -> Union[str, int, float]:
        if not input:
            return ''
        try:
            return int(input)
        except ValueError:
            pass
        try:
            return int(input, 16)
        except ValueError:
            pass
        try:
            return float(input)
        except ValueError:
            pass
        return input
    # endregion internal Non specific methods

    # region request
    def get_request_text(self, url: str) -> str:
        if self._response_obj is None:
            if self.allow_cache:
                self._response_obj = ResponseObj(url=url)
            else:
                self._response_obj = ResponseObj(url=url, cache_seconds=0)
        return self._response_obj.raw_html

    # endregion request

    # region raw html

    def get_raw_html(self) -> str:
        if not self._url:
            return ''
        if not self._raw:
            self._raw = self.get_request_text(self.url)
        return self._raw

    # endregion raw html

    # region Info
    def _get_full_name(self, soup: BeautifulSoup) -> str:
        """
        Gets full name from nav bar

        Returns:
            str: such as com.sun.star.awt.AdjustmentEvent
        """
        if self._title_full is None:
            nav = soup.find('div', id='nav-path')
            els = nav.find_all('a', class_='el')
            text = ''
            for i, el in enumerate(els):
                if i > 0:
                    text += '.'
                text += el.text.strip()
            # text = nav.text.replace('\n', '.').strip()
            self._title_full = text
        return self._title_full

    def _get_name(self, soup: BeautifulSoup):
        full = self._get_full_name(soup=soup)
        parts = full.split('.')
        return parts[len(parts) - 1]

    def _get_desc(self, soup: BeautifulSoup) -> List[str]:
        contents = soup.find('div', class_='contents')
        block = contents.find('div', class_='textblock')
        soup_lines: ResultSet = block.find_all('p')
        lines = []
        for i, ln in enumerate(soup_lines):
            s = ln.text.strip()
            if i > 0:
                lines.append("")
            lines.append(s)
        since = self._get_since(block=block)
        if len(since) > 0:
            lines.append('')
            lines.extend(since)
        # result = "\n".join(lines)
        return lines

    def _get_since(self, block: Tag) -> List[str]:
        result = []
        since = block.find('dl', class_='section since')
        if since:
            s = since.find('dd').text.strip()
            result.append("**Since**")
            result.append("")
            result.append(self._indent + s)
        return result
    # endregion Info

    # region Tidy
    def _clean_str(self, input: str) -> str:
        """
        Cleans and encodes string for template replacemnt
        """
        return str_clean(input=input, replace_dual=self._replace_dual_colon)

    # endregion Tidy

    # region Data
    def _get_memitems(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all('div', class_='memitem')

    # endregion Data

    # region util
    def camel_to_snake(self, name: str) -> str:
        """
        Converts Camel case to snake clase

        Args:
            name (str): Camel name

        Returns:
            str: snake case
        """
        return Util.camel_to_snake(name)

    # endregion util

    # region Properties
    
    @property
    def sort(self) -> bool:
        """Specifies sort
    
            :getter: Gets sort value.
            :setter: Sets sort value.
        """
        return self._sort
    
    @sort.setter
    def sort(self, value: bool):
        self._sort = value    
     
    @property
    def url(self) -> str:
        """Specifies url

            :getter: Gets url value.
            :setter: Sets url value.
        """
        return self._url

    @url.setter
    def url(self, value: str):
        self._url = value

    @property
    def allow_cache(self) -> bool:
        """Specifies allow_cache
    
            :getter: Gets allow_cache value.
            :setter: Sets allow_cache value.
        """
        return self._allow_cache
    
    @allow_cache.setter
    def allow_cache(self, value: bool):
        self._allow_cache = value 
    # endregion Properties

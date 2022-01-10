# coding: utf-8
"""
Base classes and helper functions of various types that are used with different parsers.
Module logger must be set before calling any class or function.
eg: import base
    base.logger = mylogger
"""
# region imports
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
import shutil  # to save it locally
import numpy as np
import pickle
from dataclasses import dataclass, field
from deprecated import deprecated
from PIL import Image
from types import ModuleType
from abc import ABC, abstractmethod, abstractproperty
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from glob import glob
from kwhelp.decorator import AcceptedTypes, DecArgEnum, DecFuncEnum, RequireArgs, RuleCheckAllKw, TypeCheck, TypeCheckKw
from kwhelp import rules
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union
from datetime import datetime, timezone
from functools import cache
def _set_sys_paths():

    # due to the way some scritps run and cache it is required to ensure this modules path is in sys.path
    # this has to do with pickle caching.
    f_path = Path(__file__).parent
    if not str(f_path) in sys.path:
        sys.path.insert(0, str(f_path))
    # append path to project root
    _app_root = os.environ.get('project_root', str(f_path.parent))
    if not _app_root in sys.path:
        sys.path.insert(0, _app_root)
_set_sys_paths()

from parser import mod_type as ModType
from parser import mod_rel as RelInfo
from config import AppConfig, read_config_default
# endregion imports

# region Logger
logger: logging.Logger  = None

def _set_loggers(l: Union[logging.Logger, None]):
    global logger
    logger = l

# endregion Logger

# region CONST
URL_SPLIT = '_1_1'
"""Default stirng for splitting url string into it parts"""
TEXT_CACHE: 'TextCache' = None
PICKLE_CACHE: 'PickleCache' = None
_KNOWN_EXTENDS: List['Ns'] = None
# endregion CONST

# region config
APP_CONFIG: AppConfig = None
def _load_config():
    global APP_CONFIG
    APP_CONFIG = read_config_default()
    
_load_config()
# endregion config

# region regex
#  \W = [^a-zA-Z0-9_]
py_name_pattern = re.compile('[\W_]+')
py_ns_pattern = re.compile(r'[^a-zA-Z0-9\._]+')
curly_brace_close_pattern = re.compile(r'[^};]')
"""TextCache object for caching response data"""
pattern_sq_braket = re.compile(r"\[.*\]")
pattern_http = re.compile(r"^https?:\/\/")
pattern_id = re.compile(r'[a-z0-9]{28,38}')
pattern_generic_name = re.compile(r"([a-zA-Z0-9_]+)(<[A-Z, ]+>)")
re_dir_pattern = re.compile(r"\[((?:in)|(?:out))\]", re.IGNORECASE)
# endregion regex

def get_known_extends(ns:str, class_name: str) -> Union[List['Ns'], None]:
    global _KNOWN_EXTENDS
    key = ns + '.' + class_name
    if _KNOWN_EXTENDS is None:
        _KNOWN_EXTENDS = {
            "com.sun.star.awt.AccessibleMenu": [
                'com.sun.star.accessibility.XAccessibleContext',
                'com.sun.star.accessibility.XAccessibleEventBroadcaster',
                'com.sun.star.accessibility.XAccessibleExtendedComponent',
                'com.sun.star.accessibility.XAccessibleText',
                'com.sun.star.accessibility.XAccessibleAction',
                'com.sun.star.accessibility.XAccessibleValue',
                'com.sun.star.accessibility.XAccessibleSelection',
            ]
        }
    if not key in _KNOWN_EXTENDS:
        return None
    results = []
    known = _KNOWN_EXTENDS[key]
    for s in known:
        parts = s.rsplit(sep='.', maxsplit=1)
        results.append(Ns(name=parts[1], namespace=parts[0]))
    return results
        
    


# region Type Map
# TYPE_MAP and TYPE_MAP_EX are only used with deprecated method get_py_type

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
    'type': 'object',
    'T': 'object',
    'U': 'object'
}
TYPE_MAP_EX = {
    "com.sun.star.beans.Pair": {
        "replace": "typing.Tuple[{0}, {1}]",
        "regex": r".*<[ ]*([a-zA-Z]+),[ ]*([a-zA-Z]+)",
        "is_typing": True,
        "is_wrapper": False,
        "is_py_type": True
    }
}
# endregion Type Map

# region image process const
IMG_CACHE: 'ImageCache' = None
# RESPONSE_IMG: 'ResponseImg' = None
# endregion image process const

# region Exceptions
class RequiredError(Exception):
    """Error for required"""
# endregion Exceptions

# region Data Classes

@dataclass
class Shape:
    x1: int
    y1: int
    x2: int
    y2: int

@dataclass
class AreaInfo:
    is_inherited: bool
    shape: Optional[Shape] = None



@dataclass
class ImportInfo:
    requires_typing: bool = False
    imports: Set[str] = field(default_factory=set)



@dataclass(frozen=True)
class Ns:
    name: str
    namespace: str

    @property
    def fullns(self):
        return self.namespace + '.' + self.name
    
    def __lt__(self, other: object):
        if not isinstance(other, Ns):
            return NotImplemented
        return self.fullns < other.fullns


@dataclass(frozen=True)
class Area:
    name: str
    ns: Ns
    href: str
    x1: int
    y1: int
    x2: int
    y2: int
    title: str = ''
    
    def __lt__(self, other: object):
        if not isinstance(other, Area):
            return NotImplemented
        return self.name < other.name


@dataclass
class SummaryInfo:
    id: str
    """Summary Info ID obtained from web page"""
    name: str
    """Name from page summary"""
    type: str
    """Type from page summary"""
    p_type: ModType.PythonType
    """Python Type obtaind usually from Util.get_python_type()"""
    extra_data: object = None
    """Extra data that can be set in rules or otherwise"""

    def __lt__(self, other: object):
        if not isinstance(other, SummaryInfo):
            return NotImplemented
        return self.name < other.name

@dataclass(frozen=True, eq=True)
class NameInfo:
    name: str
    "Name to use in code gen"
    orig_name: str
    """Origin name found from html"""
    extra_data: Optional[object] = None
    """Extra data that can be set in rules or otherwise"""

    def __lt__(self, other: object):
        if not isinstance(other, NameInfo):
            return NotImplemented
        return self.name < other.name

@dataclass
class ParamInfo:
    direction: str = ''
    name: str = ''
    type: str = ''
    p_type: Optional[ModType.PythonType] = None
    
    def __lt__(self, other: object):
        if not isinstance(other, ParamInfo):
            return NotImplemented
        return self.name < other.name
# endregion Data Classes

# region Cache
class CacheBase(ABC):
    """
    Caches files and retreives cached files.
    Cached file are in a subfolder of system tmp dir.
    """

    def __init__(self, tmp_dir: str, lifetime: Optional[float] = None) -> None:
        """
        Constructor

        Args:
            tmp_dir (str, optional): Dir name to create in tmp folder. Defaults to 'ooo_uno_tmpl'.
            lifetime (float, optional): Time in seconds that cache is good for. Defaults to 60 seconds.
        """
        t_path = Path(tempfile.gettempdir())
        self._cache_path = t_path / tmp_dir
        Util.mkdirp(self._cache_path)
        self._lifetime = lifetime or APP_CONFIG.cache_duration

    @abstractmethod
    def fetch_from_cache(self, filename: Union[str, Path]):
        """
        Fetches file contents from cache if it exist and is not expired

        Args:
            filename (Union[str, Path]): File to retrieve

        Returns:
            Union[str, None]: File contents if retrieved; Otherwise, ``None``
        """

    @abstractmethod
    def save_in_cache(self, filename: Union[str, Path], content):
        """
        Saves file contents into cache

        Args:
            filename (Union[str, Path]): filename to write.
            content (any): Contents to write into file.
        """

    def del_from_cache(self,  filename: Union[str, Path]) -> None:
        """
        Deletes a file from cache if it exist

        Args:
            filename (Union[str, Path]): file to delete.
        """
        try:
            f = Path(self.path, filename)
            if os.path.exists(f):
                os.remove(f)
        except Exception as e:
            logger.warning(
                'Not able to delete file: %s, error: %s', filename, str(e))

    @property
    def seconds(self) -> float:
        """Gets/Sets cache time in seconds"""
        return self._lifetime
    
    @seconds.setter
    def seconds(self, value: float) -> None:
        self._lifetime = float(value)
    
    @property
    def path(self) -> Path:
        """Gets cache path"""
        return self._cache_path


class TextCache(CacheBase):
    """
    Caches files and retreives cached files.
    Cached file are in a subfolder of system tmp dir.
    """

    def fetch_from_cache(self, filename: Union[str, Path]) -> Union[str, None]:
        """
        Fetches file contents from cache if it exist and is not expired

        Args:
            filename (Union[str, Path]): File to retrieve

        Returns:
            Union[str, None]: File contents if retrieved; Otherwise, ``None``
        """
        if self.seconds <= 0:
            return None
        f = Path(self.path, filename)
        if not f.exists():
            return None

        f_stat = f.stat()
        if f_stat.st_size == 0:
            # shoud not be zero byte file.
            try:
                self.del_from_cache(f)
            except Exception as e:
                logger.warning(
                    'Not able to delete 0 byte file: %s, error: %s', filename, str(e))
            return None
        ti_m = f_stat.st_mtime
        age = time.time() - ti_m
        if age >= self.seconds:
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
        f = Path(self.path, filename)
        # print('Saving a copy of {} in the cache'.format(filename))
        with open(f, 'w') as cached_file:
            cached_file.write(content)


class PickleCache(CacheBase):
    """
    Caches files and retreives cached files.
    Cached file are in a subfolder of system tmp dir.
    """

    def fetch_from_cache(self, filename: Union[str, Path]) -> Union[object, None]:
        """
        Fetches file contents from cache if it exist and is not expired

        Args:
            filename (Union[str, Path]): File to retrieve

        Returns:
            Union[object, None]: File contents if retrieved; Otherwise, ``None``
        """
        if self.seconds <= 0:
            return None
        f = Path(self.path, filename)
        if not f.exists():
            return None

        f_stat = f.stat()
        if f_stat.st_size == 0:
            # shoud not be zero byte file.
            try:
                self.del_from_cache(f)
            except Exception as e:
                logger.warning(
                    'Not able to delete 0 byte file: %s, error: %s', filename, str(e))
            return None
        ti_m = f_stat.st_mtime
        age = time.time() - ti_m
        if age >= self.seconds:
            return None

        try:
            # Open the file in binary mode
            with open(f, 'rb') as file:
                # Call load method to deserialze
                content = pickle.load(file)
            return content
        except IOError:
            return None
        except Exception as e:
            logger.exception(e, exc_info=True)
            raise e

    def save_in_cache(self, filename: Union[str, Path], content: object):
        """
        Saves file contents into cache

        Args:
            filename (Union[str, Path]): filename to write.
            content (object): Contents to write into file.
        """
        f = Path(self.path, filename)
        with open(f, 'wb') as file:
            pickle.dump(content, file)

# endregion Cache

# region Response
class ResponseBase(ABC):
    """Gets response data"""
    @RuleCheckAllKw(
        arg_info={
            "url": rules.RuleStrNotNullEmptyWs,
            "cache_seconds": rules.RuleNumber,
            "file_ext": rules.RuleStr
        },
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, url: str, cache_seconds: float, **kwargs):
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
            file_ext (str, optional): Extension if file. Default is read from url.
                Format must prepend ``.`` such as ``.png``
        """
        self._url = url
        self._url_obj = UrlObj(url=self._url, **kwargs)
        self._lifetime = cache_seconds
        self._url_hash = hashlib.md5(
            self._url_obj.url_only.encode('utf-8')).hexdigest()

        self._file_ext = kwargs.get('file_ext', None)
        if self._file_ext is None:
            self._file_ext = self._url_obj.ext

    @property
    def url(self) -> str:
        """Specifies url"""
        return self._url

    @property
    def url_obj(self) -> 'UrlObj':
        """Gets url_obj value"""
        return self._url_obj

    @property
    def url_hash(self) -> str:
        """Gets url_hash value"""
        return self._url_hash

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
        logger.debug('ResponseBase: caching is set to: %d', value)


class ResponseObj(ResponseBase):
    """Gets response data"""

    def __init__(self, url: str, cache_seconds: Optional[float] = None, **kwargs):
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
            file_ext (str, optional): Extension if file. Default is empty ``.html``.
                Format must prepend ``.`` such as ``.png``
        """
        if cache_seconds is None:
            cache_seconds = APP_CONFIG.cache_duration
        super().__init__(url=url, cache_seconds=cache_seconds, **kwargs)
        self._text = None
        if not 'file_ext' in kwargs:
            self._file_ext = '.html'

    # cache for one week - 604800.0 seconds
    def _get_request_text(self) -> str:
        global TEXT_CACHE
        allow_cache = self.cache_seconds > 0
        filename = self._url_hash + self._file_ext
        if allow_cache:
            if not TEXT_CACHE:
                TEXT_CACHE = TextCache(
                    tmp_dir=APP_CONFIG.cache_dir, lifetime=self.cache_seconds)
            html_text = TEXT_CACHE.fetch_from_cache(filename=filename)
            if html_text:
                logger.debug(
                    "ResponseObj._get_request_text() retreived data from Cache")
                return html_text
        response = requests.get(url=self.url)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        html_text = response.text
        if allow_cache:
            TEXT_CACHE.save_in_cache(filename=filename, content=html_text)
            logger.debug(
                "ResponseObj._get_request_text() Saving to cache as: %s", Path(TEXT_CACHE.path, filename))
        return html_text

    @property
    def raw_html(self) -> str:
        """
        Gets raw html of url
        """
        if self._text is None:
            try:
                self._text = self._get_request_text()
            except Exception as e:
                logger.error(e)
                raise e
        return self._text


# endregion Response

# region Soup Related:
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

# endregion Soup Related:

# region Url
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
        self._ext = None

    def get_split_ns(self) -> List[str]:
        result = []
        try:
            ns_part = self._page_link.split('.')[0]
            s = ns_part.replace(URL_SPLIT, '.').lstrip('.')

            # in some cases such as generics the name can have _3_01 and or _01_4 in the last part of the name
            # best guess _3 is < and _4 is > and _01 is space.
            # just split _3 dropping the end
            s = s.rsplit(sep='_3', maxsplit=1)[0]

            # https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Pair_3_01T_00_01U_01_4.html
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

    @property
    def ext(self) -> str:
        """Gets ext value such as ``.html`` or ``.png``"""
        if self._ext is None:
            parts = self.url_only.rsplit(sep='.', maxsplit=1)
            self._ext = '' if len(parts) == 1 else ('.' + parts[1])
        return self._ext

# endregion Url

# region block and api classes

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
        lines: List[str] = []
        i = 0
        for ln in self._tags:
            s = ln.text.strip().replace("::", '.')
            if not s:
                continue
            if self._clean:
                s = str_clean(input=s)
            if i > 0 and self._empty_lines:
                lines.append("")
            lines.extend(s.splitlines())
            i += 1
        return [line.strip() for line in lines]

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


class ApiName(BlockObj):
    """Get the Name object for the interface"""

    def __init__(self, soup: SoupObj, rules_engine: 'IRulesName' = None):
        super().__init__(soup)
        self._data = None
        self._rules_engine = rules_engine

    def get_obj(self) -> NameInfo:
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        try:
            tag_div_nav: Tag = soup.select_one('div#nav-path')
            name = tag_div_nav.find_all(
                'li', class_='navelem')[-1].text.strip()
            ni = NameInfo(name=name, orig_name=name)
            if self._rules_engine:
                self._rules_engine.process_name(ni)

            self._data = ni
            return self._data
        except Exception as e:
            logger.error(
                "ApiName.get_obj() Error getting name.", exc_info=True)
            raise e


class ApiNamespace(BlockObj):
    """Get the Namespace object for component"""

    def __init__(self, soup: SoupObj):
        super().__init__(soup)
        self._data = None
        self.__namespace_str = None
        self.__namespace = None

    def get_obj(self) -> List[str]:
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        self._data = []
        try:
            tag_div_nav: Tag = soup.select_one('div#nav-path')
            names = tag_div_nav.find_all('li', class_='navelem')
            for name in names:
                self._data.append(name.text.strip())
            return self._data
        except Exception as e:
            logger.error(
                "ApiNamespace.get_obj() Error getting Namespace.", exc_info=True)
            raise e

    @property
    def namespace(self) -> List[str]:
        """Gets namespace value"""
        if self.__namespace is None:
            self.__namespace = self.get_obj()
        return self.__namespace

    @property
    def namespace_str(self) -> str:
        if self.__namespace_str is None:
            self.__namespace_str = '.'.join(self.namespace)
        return self.__namespace_str

class ApiPublicMembers(BlockObj):
    """Gets all blocks with condensed info such as Public Member Functions"""
    @TypeCheck(SoupObj, ftype=DecFuncEnum.METHOD)
    def __init__(self, soup: SoupObj):
        self._soup = soup
        super().__init__(soup)
        self._data = False

    def get_obj(self) -> Union[ResultSet, None]:
        if not self._data is False:
            return self._data
        self._data = None
        soup = self.soup.soup
        rs = soup.find_all('table', class_='memberdecls')
        self._data = rs
        return self._data


class ApiSummaryBlock(BlockObj):
    """
    Abstract class for getting sumary block form ApiPublicMembers
    """
    def __init__(self, block: ApiPublicMembers):
        self._block: ApiPublicMembers = block
        super().__init__(self._block.soup)
        self._data = False

    @abstractmethod
    def _get_match_name(self) -> str:
        """
        Name of a sction to match

        Returns:
            str: section heading name such as ``interfaces``
        """

    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        rs = self._block.get_obj()
        if not rs:
            return self._data
        match_name = self._get_match_name()
        for tag in rs:
            # tag is a table
            # body > div.contents > table > tbody > tr.heading > td > h2 > a
            t: Tag = tag
            a_lnk = t.select_one('tr.heading > td > h2 > a')
            if a_lnk:
                name = a_lnk.get('name', None)
                if name == match_name:
                    self._data = tag
                    break
        if self._data is None and logger.level <= logging.WARNING:
            logger.warning(
                "ApiSummaryBlock.get_obj() No summary block found for '%s'", match_name)
        return self._data


class ApiSummaryRows(BlockObj):
    """Gets the rows that contain short details and desc for a Function/properyty block"""

    def __init__(self, block: ApiSummaryBlock):
        self._block: ApiSummaryBlock = block
        super().__init__(self._block.soup)
        self._data = None

    def get_obj(self) -> List[Tag]:
        if not self._data is None:
            return self._data
        self._data = []
        tbl_tag: Tag = self._block.get_obj()
        if not tbl_tag:
            return self._data
        rs_rows: ResultSet = tbl_tag.find_all('tr')
        if not rs_rows:
            return self._data
        for row in rs_rows:
            r: Tag = row
            _class = r.get('class', [])
            if len(_class) == 0:
                continue
            class_str = _class[0]
            if class_str == 'inherit_header':
                # Public Member Functions inherited from ...
                break
            if class_str.startswith('memitem:'):
                self._data.append(row)
        return self._data

class ApiSummaries(BlockObj):
    """Gets summary information for a public member block"""

    def __init__(self
                 ,block: ApiSummaryRows
                 ,name_info: NameInfo
                 ,ns: str
                 ,rule_engine: Optional['IRulesSummaryInfo'] = None
                 , long_names:bool = False
                 ) -> None:
        """
        [summary]

        Args:
            block (ApiSummaryRows): Block of html that contains summary rows.
            rule_engine (IRulesSummaryInfo, optional): Rules engine to process each found Summary Info. Defaults to None.
        """
        self._block: ApiSummaryRows = block
        super().__init__(self._block.soup)
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._rule_engine = rule_engine
        self._ns = ns
        self._long_names = long_names
        self._name_info = name_info
        self._data = None
    
    def _get_type_from_inner_link(self, mem_item_left: Tag, name:str) -> Union[str, None]:
        logger.debug('ApiSummaries._get_type_from_inner_link() Searching for %s link.', name)
        if not mem_item_left:
            return None
        a_tag = mem_item_left.findChild('a')
        if not a_tag:
            return None
        a_name = a_tag.text.strip()
        if a_name != name:
            return None
        s = Util.get_ns_from_a_tag(a_tag=a_tag)
        logger.debug(
            'ApiSummaries._get_type_from_inner_link() found: %s', s)
        return s

    def get_obj(self) -> List[SummaryInfo]:
        """
        Get list of Summary Info from html page.

        Returns:
            List[SummaryInfo]: summary info.

        Note:
            If a rules engine is present then each summary info will have any relevant rules applied.
        """
        if not self._data is None:
            return self._data
        self._data = []
        rows = self._block.get_obj()
        for row in rows:
            cls_name = row.get('class')[0]
            id_str = cls_name.rsplit(sep=':', maxsplit=1)[1]
            itm_lft = row.find('td', class_='memItemLeft')
            r_type = ''
            name = ''
            if itm_lft:
                r_type = itm_lft.text.strip().replace('::', '.').lstrip('.')
            itm_rgt = row.find('td', class_='memItemRight')
            if itm_rgt:
                itm_name = itm_rgt.select_one('a')
                if itm_name:
                    name = itm_name.text.strip()
                    name = Util.get_clean_method_name(name)
            # logger.debug('ApiSummaries.get_obj() r_type in: %s', r_type)
            p_type = Util.get_python_type(
                in_type=r_type,
                name_info=self._name_info,
                ns=self._ns,
                long_names=self._long_names
                )
            # logger.debug('ApiSummaries.get_obj() p_type in: %s', p_type.type)
            if p_type.is_default():
                logger.debug(
                    'ApiSummaries.get_obj() %s: p_type is Default. Looking for %s', name, r_type)
                # defaulted to object.
                # this could be an object in the same namespace.
                # test for link and namespace and try again.
                r2_type = self._get_type_from_inner_link(itm_lft, r_type)
                if r2_type:
                    p2_type = Util.get_python_type(
                        in_type=r2_type,
                        name_info=self._name_info,
                        ns=self._ns,
                        long_names=self._long_names
                        )
                    if not p2_type.is_default():
                        p_type = p2_type
                        logger.debug(
                            'ApiSummaries.get_obj() %s: p_type is now %s', name, r_type)
            else:
                logger.debug(
                    'ApiSummaries.get_obj() %s: p_type is %s for %s', name, p_type.type, r_type)
            si = SummaryInfo(id=id_str, name=name, type=p_type.type, p_type=p_type)
            if p_type.requires_typing:
                self._requires_typing = True
            im = p_type.get_all_imports()
            self._imports.update(im)
            self._data.append(si)

        if self._rule_engine:
            for si in self._rule_engine:
                self._rule_engine.process_summary_info(si)
        return self._data

    @property
    def requires_typing(self) -> bool:
        """Gets requires_typing value"""
        return self._requires_typing

    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        return self._imports

class ApiDescDetailSince(BlockObj):
    """Gets the Since part if it exist of a detailed block section"""
    def __init__(self, block: BlockObj) -> None:
        self._block: BlockObj = block
        super().__init__(self._block.soup)
        self._data = False

    def get_obj(self) -> Union[str, None]:
        if not self._data is False:
            return self._data
        self._data = None
        tag: Tag = self._block.get_obj()
        if not tag:
            return self._data
        dl_tag = tag.select_one('dl.section.since')
        if not dl_tag:
            return self._data
        dd_tag = dl_tag.find('dd')
        if not dd_tag:
            return self._data
        self._data = dd_tag.text.strip()
        return self._data
class ApiDescDetail(BlockObj):
    """Gets description of a detail block section"""
    def __init__(self, block: BlockObj) -> None:
        self._block: BlockObj = block
        super().__init__(self._block.soup)
        self._data = None
        self._cls = 'memdoc'
        self._el = 'div'

    def get_obj(self) -> List[str]:
        if not self._data is None:
            return self._data
        self._data = []
        tag = self._block.get_obj()
        if not tag:
            return self._data
        lines_found: ResultSet = tag.select(f'{self._el}.{self._cls} > p')
        if not lines_found:
            return self._data
        p_obj = TagsStrObj(tags=lines_found)
        self._data = p_obj.get_lines()
        since_obj = ApiDescDetailSince(self._block)
        since = since_obj.get_obj()
        if since:
            self._data.append('')
            self._data.append('**since**')
            self._data.append('')
            self._data.append(f"    {since}")
        return self._data


class ApiDesc(BlockObj):
    """Gets the description"""

    def __init__(self, soup: SoupObj):
        super().__init__(soup)
        self._data = None

    def get_obj(self) -> List[str]:
        """
        Gets description as list of str

        Returns:
            List[str]: description lines
        """
        if self._data:
            return self._data
        lines_found: ResultSet = self.soup.soup.select(
            'body > div.contents > div.textblock > p')
        p_obj = TagsStrObj(tags=lines_found)
        self._data = p_obj.get_lines()
        since_obj = ApiDescSince(self.soup)
        since = since_obj.get_obj()
        if since:
            self._data.append('')
            self._data.append('**since**')
            self._data.append('')
            self._data.append(f"    {since}")
        #.. deprecated::
        dep_obj = ApiDepreciated(self.soup)
        dep = dep_obj.get_obj()
        if dep:
            self._data.append('')
            self._data.append('.. deprecated::')
            self._data.append('')
            self._data.append('    Class is deprecated.')
        return self._data


class ApiDescSince(BlockObj):
    """Gets the Since if it exist"""

    def __init__(self, soup: SoupObj):
        super().__init__(soup)
        self._data = False

    def get_obj(self) -> Union[str, None]:
        """
        Gets See alos of Interface

        Returns:
            str: See also. if it exist; Otherwise empty string.
        """
        if not self._data is False:
            return self._data
        self._data = None
        dl_tag = self._soup.soup.select_one('dl.section.since')
        if not dl_tag:
            return self._data
        dd_tag = dl_tag.find('dd')
        if not dd_tag:
            return self._data
        self._data = dd_tag.text.strip()
        return self._data


class ApiDepreciated(BlockObj):
    """Gets if block is deprecated"""
    # eg: https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XVclContainerPeer.html

    def __init__(self, soup: SoupObj):
        super().__init__(soup)
        self._data = None

    def get_obj(self) -> bool:
        """
        Gets See alos of Interface

        Returns:
            str: See also. if it exist; Otherwise empty string.
        """
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        tag = soup.select_one('div.textblock > dl.deprecated')
        if tag:
            self._data = True
        else:
            self._data = False
        return self._data


class ApiDetailBlock(BlockObj):
    """Get Details block from block id"""

    def __init__(self, soup: SoupObj, a_id: str) -> None:
        """
        ApiDetailBlock Constructor

        Args:
            soup (base.SoupObj): Soup Obj
            a_id (str): id of block such as ``aa1d747451151fbd244196e6305348dbc``
        """
        super().__init__(soup)
        self._a_d = a_id
        self._data = False

    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        soup = self.soup.soup
        a_tag: Tag = soup.find('a', id=self._a_d)
        if not a_tag:
            return self._data
        self._data = a_tag.find_next('div', class_='memitem')
        return self._data


class ApiProtoBlock(BlockObj):
    """Gets Detailed data block"""

    def __init__(self, block: ApiDetailBlock) -> None:
        self._block: ApiDetailBlock = block
        super().__init__(self._block.soup)
        self._data = False

    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        tag = self._block.get_obj()
        if not tag:
            return self._data
        proto = tag.findChild('div', class_='memproto')
        self._data = proto
        self._data


class ApiDescBlock(BlockObj):
    """Gets Detailed description block of method or component"""

    def __init__(self, block: ApiDetailBlock) -> None:
        self._block: ApiDetailBlock = block
        super().__init__(self._block.soup)
        self._data = False

    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        tag = self._block.get_obj()
        if not tag:
            return self._data
        desc = tag.findChild('div', class_='memdoc')
        self._data = desc
        return self._data

# region        API Summary Blocks


class ApiFunctionsBlock(ApiSummaryBlock):
    def _get_match_name(self) -> str:
        return 'pub-methods'


class ApiTypesBlock(ApiSummaryBlock):
    def _get_match_name(self) -> str:
        return 'pub-types'


class ApiPropertiesBlock(ApiSummaryBlock):
    def _get_match_name(self) -> str:
        return 'pub-attribs'


class ApiInterfacesBlock(ApiSummaryBlock):
    """Gets Block object for Exported Interfaces"""

    def _get_match_name(self) -> str:
        return 'interfaces'

# endregion     API Summary Blocks

# region        Method Api


class ApiMethodPramsInfo(BlockObj):
    """Gets List of Parameter information for a funciton"""

    def __init__(self, block: ApiProtoBlock, name_info: NameInfo, ns: str, long_names: bool = False) -> None:
        self._block: ApiProtoBlock = block
        super().__init__(self._block.soup)
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._ns = ns
        self._long_names = long_names
        self._name_info = name_info
        self._data = None

    def get_obj(self) -> List[ParamInfo]:
        if not self._data is None:
            return self._data
        self._data = []
        proto = self._block.get_obj()
        if not proto:
            return self._data
        p_type_tag = proto.find_all('td', class_='paramtype')
        p_name_tag = proto.find_all('td', class_='paramname')
        if not p_type_tag and not p_name_tag:
            if logger.level <= logging.DEBUG:
                logger.debug(
                    'ApiInterfacePramsInfoget_obj() No Parmas for %s', self._block.summary_info.name)
            return self._data

        try:
            if len(p_type_tag) != len(p_name_tag):
                if len(p_type_tag) == 0 and len(p_name_tag) == 1:
                    # no params. p_name_tag will usually be 1
                    # when there are not paramters.
                    return self._data
                raise Exception
        except Exception as e:
            msg = "ApiFnPramsInfo.get_obj(), Parameter Name and Parameter Types do not have the same length. Function Summary: %s Url: %s" % (str(
                self._block.summary_info), self.url_obj.url)
            logger.error(msg)
            raise Exception(msg)
        p_info = zip(p_name_tag, p_type_tag)
        self._data = self._process_params(params=p_info)
        return self._data

    def _process_name_tag(self, name_tag: Tag, pinfo: ParamInfo):
        name = name_tag.text
        pinfo.name = Util.get_clean_name(name)

    def _get_type_from_inner_link(self, paramtype: Tag, name: str) -> Union[str, None]:
        logger.debug(
            'ApiFnPramsInfo._get_type_from_inner_link() Searching for %s link.', name)
        if not paramtype:
            return None
        a_tag = paramtype.findChild('a')
        if not a_tag:
            return None
        a_name = a_tag.text.strip()
        if a_name != name:
            return None
        s = Util.get_ns_from_a_tag(a_tag=a_tag)
        logger.debug(
            'ApiFnPramsInfo._get_type_from_inner_link() found: %s', s)
        return s

    def _process_type_tag(self, type_tag: Tag, pinfo: ParamInfo):
        pinfo.direction = 'in'
        # dir_tag: NavigableString = type_tag.find(text=True, recursive=False)
        # dir_str could be in format of: [in] sequence< ::
        dir_str: str = type_tag.text.strip()
        m = re_dir_pattern.match(dir_str)
        if m:
            g_dir = m.group(1).lower()
            pinfo.direction = g_dir  # in or out
            dir_str = dir_str.split(maxsplit=1)[1]
        _type = dir_str.replace("::", '.').lstrip('.')
        t_info: ModType.PythonType = Util.get_python_type(
            in_type=_type,
            ns=self._ns,
            name_info=self._name_info,
            long_names=self._long_names
            )
        if t_info.is_default():
            logger.debug(
                'ApiFnPramsInfo._process_type_tag() %s type is Default. Looking for %s', pinfo.name, _type)
            t2_type = self._get_type_from_inner_link(type_tag, _type)
            if t2_type:
                t2_info = Util.get_python_type(
                    t2_type,
                    ns=self._ns,
                    name_info=self._name_info,
                    long_names=self._long_names
                    )
                if not t2_info.is_default():
                    t_info = t2_info
        logger.debug(
            "ApiFnPramsInfo._process_type_tag() param '%s' type '%s' converted to '%s'", pinfo.name, _type, t_info.type)
        pinfo.type = t_info.type
        pinfo.p_type = t_info
        if t_info.requires_typing:
            self._requires_typing = True
        self._imports.update(t_info.get_all_imports())
        return

    def _process_params(self, params: zip) -> List[ParamInfo]:
        results = []
        for p_name_tag, p_type_tag in params:
            p_info = ParamInfo()
            self._process_name_tag(name_tag=p_name_tag, pinfo=p_info)
            if not p_info.name:
                msg = f"ApiFnPramsInfo: unable to find parameter name for method {self.summary_info.name!r}. Url: {self.url_obj.url}"
                logger.error(msg)
                raise Exception(msg)
            self._process_type_tag(type_tag=p_type_tag, pinfo=p_info)
            if not p_info.type:
                msg = f"ApiFnPramsInfo: unable to find parameter type for method {self.summary_info.name!r} with param name of {p_info.name!r}. Url: {self.url_obj.url}"
                logger.error(msg)
                raise Exception(msg)
            results.append(p_info)
        return results

    @property
    def requires_typing(self) -> bool:
        """Gets require_typing value"""
        return self._requires_typing

    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        return self._imports

    @property
    def summary_info(self) -> SummaryInfo:
        """Gets summary_info value"""
        return self._block.summary_info


class ApiMethodException(BlockObj):
    """Gets errors for a funciton"""
    # have not found an example with more than one exception so assuming
    # singular excpetion
    # returning as a list of str for future consideration

    def __init__(self, block: ApiProtoBlock) -> None:
        self._block: ApiProtoBlock = block
        super().__init__(self._block.soup)
        self._data = False

    def _get_raises_lst(self) -> List[str]:
        # rows for raise a bit messy.
        # see: https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XTimeContainer.html
        # first row of raise will contain only the first exception.
        # if there is another exception then the row text should end with a comma
        row: Tag = None

        def ex_gen():
            nonlocal row
            while row:
                if row is None:
                    break
                text = self._get_raises_text(row)
                s = text
                if text.endswith(","):
                    row = row.find_next_sibling('tr')
                    s = s.rstrip(',')
                else:
                    row = None
                yield s

        results = []
        row = self._get_raises_row()
        if not row:
            return results
        # errs = ex()
        for err in ex_gen():
            results.append(err)
        return results

    def _get_raises_row(self) -> Union[Tag, None]:
        proto = self._block.get_obj()
        rows: ResultSet = proto.find_all('tr')
        result = None
        for row in rows:
            td: Tag = row.select_one('td')
            if td.text.strip().lower() == 'raises':
                result = row
                break
        return result

    def _get_raises_text(self, row: Tag):
        if not row:
            return None
        parts = row.text.rsplit(maxsplit=1)  # in case starts with raises
        s: str = parts.pop()
        s = s.replace('(', '').replace(')', '').replace(
            '::', '.').strip().lstrip('.')
        return s

    def get_obj(self) -> Union[List[str], None]:
        """
        Get name of error that is raises

        Returns:
            Union[str, None]: String containing type of error if it exist; Otherwise, ``None``
        """
        if not self._data is False:
            return self._data
        self._data = None
        # row = self._get_raises_row()
        # if not row:
        #     return self._data
        # self._data = [self._get_raises_text(row)]
        self._data = self._get_raises_lst()
        return self._data

    @property
    def summary_info(self) -> SummaryInfo:
        """Gets summary_info value"""
        return self._block.summary_info


# endregion     Method Api

# region        API Data
class APIData:
    """Class the brings together parts for scraping API Html pages"""
    # region Constructor

    def __init__(self, url_soup: Union[str, SoupObj], allow_cache: bool, long_names: bool = False, remove_parent_inherited: bool = True):
        """
        Constructor

        Args:
            url_soup (Union[str, SoupObj]): Soup Object
            allow_cache (bool): Determines if cache is used
            long_names (bool, optional): Determsin if name are short or long in various components.
                Short name may look like ``XInterface`` whereas a long name might look like
                ``uno.XInterface``. Defaults to ``False``.
        """
        if isinstance(url_soup, str):
            self.__url = url_soup
            self.__soup_obj = SoupObj(
                url=url_soup, allow_cache=allow_cache)
        else:
            self.__url = url_soup.url
            self.__soup_obj = url_soup
            self.__soup_obj.allow_cache = allow_cache
        self.__allow_cache = allow_cache
        self.__ns: ApiNamespace = None
        self.__long_names = long_names
        self.__api_data_public_members: ApiPublicMembers = None
        self.__api_data_name: ApiName = None
        self.__desc: ApiDesc = None
        self.__properties_block: ApiPropertiesBlock = None
        self.__func_block: ApiFunctionsBlock = None
        self.__interfaces_block: ApiInterfacesBlock = None
        self.__types_block: ApiTypesBlock = None
        self.__func_summary_rows: ApiSummaryRows = None
        self.__property_summary_rows: ApiSummaryRows = None
        self.__export_summary_rows: ApiSummaryRows = None
        self.__func_summaries: ApiSummaries = None
        self.__property_summaries: ApiSummaries = None
        self.__exported_summaries: ApiSummaries = None
        self.__type_summaries: ApiSummaries = None
        self.__type_summary_rows: ApiSummaryRows = None
        self.__inherited: ApiInherited = None
        self.__area_filter_rules_engine: IRulesArea = None
        self.__remove_parent_inherited = remove_parent_inherited

    # endregion Constructor

    # region Methods
    def _get_name_rules_engine(self) -> Union['IRulesName', None]:
        """
        Gets name rules engine instance or None.
        Can be overrides in subclasses.

        Returns:
            [type]: None
        """
        return None

    def _set_area_filter_rules_engine_rules(self, rules_engine: 'IRulesArea') -> None:
        """
        Registers rules for Area Filter Rules Engine.
        Can be overriden in subclasses.

        Args:
            rules_engine (IRulesArea): Area Rules Engine
        """
        # order of rules matter here.
        # RuleAreaSingle would also match if it were RuleAreaVertical
        rules_engine.register_rule(rule=RuleAreaMulti)
        rules_engine.register_rule(rule=RuleAreaVertical)
        rules_engine.register_rule(rule=RuleAreaSingle)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_import_info_method(self, a_id: str) -> ImportInfo:
        """
        Gets imports for method params and return type

        Args:
            si_id (str): Function summary Info

        Returns:
            base.ImportInfo: Import info
        """
        key = 'get_import_info_method_' + a_id
        info = ImportInfo()
        params_info = self.get_prams_info(a_id=a_id)
        fn_info = self.func_summaries
        # ensure data is primed
        fn_info.get_obj()
        params_info.get_obj()

        info.requires_typing = params_info.requires_typing or fn_info.requires_typing
        info.imports.update(params_info.imports)
        info.imports.update(fn_info.imports)
        return info

    def get_import_info_property(self) -> ImportInfo:
        """
        Gets imports for properties

        Args:
            si_id (str): Property summary Info

        Returns:
            base.ImportInfo: Import info
        """
        info = ImportInfo()
        p_info = self.property_summaries
        # ensure data is primed
        p_info.get_obj()
        info.requires_typing = p_info.requires_typing
        info.imports.update(p_info.imports)
        return info

    def get_import_info_type(self) -> ImportInfo:
        """
        Gets imports for typedefs

        Args:
            si_id (str): Types summary Info

        Returns:
            base.ImportInfo: Import info
        """
        info = ImportInfo()
        p_info = self.types_summaries
        # ensure data is primed
        p_info.get_obj()
        info.requires_typing = p_info.requires_typing
        info.imports.update(p_info.imports)
        return info

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_detail_block(self, a_id: str) -> ApiDetailBlock:
        """
        Gets detail block of a function.
        Gets the 

        Args:
            si (SummaryInfo): Function summary Info to get the details block for.

        Returns:
            ApiDetailBlock: object
        """
        return ApiDetailBlock(soup=self.soup_obj, a_id=a_id)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_desc_detail(self, a_id: str) -> ApiDescDetail:
        """Gets Description obj for method or property"""
        block = self.get_desc_block(a_id=a_id)
        return ApiDescDetail(block=block)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_prams_info(self, a_id: str) -> ApiMethodPramsInfo:
        """Gets parameter info for all parameters of a a method"""
        block = self.get_proto_block(a_id=a_id)
        result = ApiMethodPramsInfo(
            block=block,
            name_info=self.name.get_obj(),
            ns=self.ns.namespace_str,
            long_names=self.__long_names
        )
        return result

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_method_ex(self, a_id: str) -> ApiMethodException:
        """Gets raises info for method"""
        block = self.get_proto_block(a_id=a_id)
        result = ApiMethodException(block=block)
        return result

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_proto_block(self, a_id: str) -> ApiProtoBlock:
        """Gets the block for a method information"""

        detail_block = self.get_detail_block(a_id=a_id)
        return ApiProtoBlock(block=detail_block)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_desc_block(self, a_id: str) -> ApiDescBlock:
        """Gets the block for a method description"""
        detail_block = self.get_detail_block(a_id=a_id)
        return ApiDescBlock(block=detail_block)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_desc_detail(self, a_id: str) -> ApiDescDetail:
        """Gets Description obj for method or property"""
        block = self.get_desc_block(a_id=a_id)
        return ApiDescDetail(block=block)
    # endregion Methods

    # region Properties
    @property
    def name(self) -> ApiName:
        if self.__api_data_name is None:
            self.__api_data_name = ApiName(
                soup=self.__soup_obj,
                rules_engine=self._get_name_rules_engine()
            )
        return self.__api_data_name

    @property
    def public_members(self) -> ApiPublicMembers:
        if self.__api_data_public_members is None:
            self.__api_data_public_members = ApiPublicMembers(self.soup_obj)
        return self.__api_data_public_members

    @property
    def func_block(self) -> ApiFunctionsBlock:
        """Gets Summary Functions block"""
        if self.__func_block is None:
            self.__func_block = ApiFunctionsBlock(
                self.public_members)
        return self.__func_block

    @property
    def properties_block(self) -> ApiPropertiesBlock:
        """Gets Summary Properties block"""
        if self.__properties_block is None:
            self.__properties_block = ApiPropertiesBlock(
                self.public_members)
        return self.__properties_block

    @property
    def interfaces_block(self) -> ApiInterfacesBlock:
        """Gets Summary Exported Interfaces block"""
        if self.__interfaces_block is None:
            self.__interfaces_block = ApiInterfacesBlock(
                self.public_members)
        return self.__interfaces_block

    @property
    def types_block(self) -> ApiTypesBlock:
        """Gets Summary Properties block"""
        if self.__types_block is None:
            self.__types_block = ApiTypesBlock(
                self.public_members)
        return self.__types_block

    @property
    def func_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for functions"""
        if self.__func_summary_rows is None:
            self.__func_summary_rows = ApiSummaryRows(
                self.func_block)
        return self.__func_summary_rows

    @property
    def property_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for Properties"""
        if self.__property_summary_rows is None:
            self.__property_summary_rows = ApiSummaryRows(
                self.properties_block)
        return self.__property_summary_rows

    @property
    def export_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for Exported Interfaces"""
        if self.__export_summary_rows is None:
            self.__export_summary_rows = ApiSummaryRows(
                self.interfaces_block)
        return self.__export_summary_rows

    @property
    def func_summaries(self) -> ApiSummaries:
        """Get Summary info list for functions"""
        if self.__func_summaries is None:
            self.__func_summaries = ApiSummaries(
                block=self.func_summary_rows,
                name_info=self.name.get_obj(),
                ns=self.ns.namespace_str,
                long_names=self.__long_names)
        return self.__func_summaries

    @property
    def property_summaries(self) -> ApiSummaries:
        """Get Summary info list for Properties"""
        if self.__property_summaries is None:
            self.__property_summaries = ApiSummaries(
                block=self.property_summary_rows,
                name_info=self.name.get_obj(),
                ns=self.ns.namespace_str,
                long_names=self.__long_names)
        return self.__property_summaries

    @property
    def exported_summaries(self) -> ApiSummaries:
        """Get Summary info list for Exported Interfaces"""
        if self.__exported_summaries is None:
            self.__exported_summaries = ApiSummaries(
                block=self.export_summary_rows,
                name_info=self.name.get_obj(),
                ns=self.ns.namespace_str,
                long_names=self.__long_names)
        return self.__exported_summaries

    @property
    def inherited(self) -> 'ApiInherited':
        """Gets class that get all inherited value"""
        if self.__inherited is None:
            ni = self.name.get_obj()    
            self.__inherited = ApiInherited(
                soup=self.soup_obj,
                area_filter_rules_engine=self.area_filter_rules_engine,
                class_name=ni.name,
                ns=self.ns.namespace_str,
                raise_error=False,
                allow_cache=self.allow_cache
            )
        return self.__inherited

    @property
    def types_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for Properties"""
        if self.__type_summary_rows is None:
            self.__type_summary_rows = ApiSummaryRows(
                block=self.types_block)
        return self.__type_summary_rows

    @property
    def types_summaries(self) -> ApiSummaries:
        """Get Summary info list for Properties"""
        if self.__type_summaries is None:
            self.__type_summaries = ApiSummaries(
                block=self.types_summary_rows,
                name_info=self.name.get_obj(),
                ns=self.ns.namespace_str,
                long_names=self.__long_names)
        return self.__type_summaries

    @property
    def desc(self) -> ApiDesc:
        """Gets the interface Description object"""
        if self.__desc is None:
            self.__desc = ApiDesc(self.soup_obj)
        return self.__desc

    @property
    def ns(self) -> ApiNamespace:
        """Gets the interface Description object"""
        if self.__ns is None:
            self.__ns = ApiNamespace(
                self.soup_obj)
        return self.__ns

    @property
    def soup_obj(self) -> SoupObj:
        """Gets soup_obj value"""
        return self.__soup_obj

    @property
    def url_obj(self) -> UrlObj:
        return self.__soup_obj.url_obj

    @property
    def area_filter_rules_engine(self) -> 'IRulesArea':
        if self.__area_filter_rules_engine is None:
            self.__area_filter_rules_engine = RulesArea(
                remove_parent_inherited=self.remove_parent_inherited)
            self._set_area_filter_rules_engine_rules(
                rules_engine=self.__area_filter_rules_engine
            )
        return self.__area_filter_rules_engine

    @property
    def allow_cache(self) -> bool:
        """Specifies allow_cache
    
            :getter: Gets allow_cache value.
            :setter: Sets allow_cache value.
        """
        return self.__allow_cache

    @allow_cache.setter
    def allow_cache(self, value: bool):
        self.__allow_cache = value

    @property
    def remove_parent_inherited(self) -> bool:
        """Gets remove_parent_inherited value"""
        return self.__remove_parent_inherited
    # endregion Properties

# endregion     API Data

# endregion block and api classes

# region SummaryInfo Rules
class IRuleSummaryInfo(ABC):
    @abstractmethod
    def __init__(self, rules: 'IRulesSummaryInfo') -> None:
        """Constructor"""

    @abstractmethod
    def get_is_match(self, si: SummaryInfo) -> bool:
        """
        Gets if rule is a match
        
        Args:
            si (SummaryInfo): Summary Info
        """

    @abstractmethod
    def process_summary_info(self, si: SummaryInfo) -> None:
        """
        Makes changes to si based upon rule

        Args:
            si (SummaryInfo): Summary Info
        """


class IRulesSummaryInfo(ABC):
    @abstractmethod
    def process_summary_info(self, si: SummaryInfo) -> None:
        """Process Summary Info making changes to si by rules"""

    @abstractmethod
    def get_rule_instance(self, rule: IRuleSummaryInfo) -> IRuleSummaryInfo:
        """Gets a rule instance"""

class RuleSummaryInfoCleanName(IRuleSummaryInfo):
    """Cleans name to remove any non class name chars"""
    def __init__(self, rules: 'IRulesSummaryInfo') -> None:
        self._rules = rules
    
    def get_is_match(self, si: SummaryInfo) -> bool:
        name = si.name
        clean_name = Util.get_clean_classname(name)
        return name != clean_name
    
    def process_summary_info(self, si: SummaryInfo) -> None:
        """
        Cleans si.name to remove any non class name chars

        Args:
            si (SummaryInfo): Summary Info
        """
        si.name = Util.get_clean_classname(si.name)


class RulesSummaryInfo(IRulesSummaryInfo):
    def __init__(self) -> None:
        self._rules: List[type[IRuleSummaryInfo]] = []
        self._cache = {}
        self._register_known_rules()

    def register_rule(self, rule: type[IRuleSummaryInfo]) -> None:

        if not issubclass(rule, IRuleSummaryInfo):
            msg = f"{self.__class__.__name__}.register_rule(), rule arg must be child class of ITypeRule"
            raise TypeError(msg)
        if rule in self._rules:
            msg = f"{self.__class__.__name__}.register_rule() Rule is already registered"
            logger.warning(msg)
            return
        self._reg_rule(rule=rule)

    def unregister_rule(self,  rule: type[IRuleSummaryInfo]):
        """
        Unregister a rule

        Args:
            rule (ITypeRule): Rule to unregister
        """
        try:
            key = str(id(rule))
            if key in self._cache:
                del self._cache[key]
            self._rules.remove(rule)
        except ValueError as e:
            msg = f"{self.__class__.__name__}.unregister_rule() Unable to unregister rule."
            raise ValueError(msg) from e

    def _reg_rule(self, rule: type[IRuleSummaryInfo]):
        self._rules.append(rule)

    def _register_known_rules(self):
        pass

    def _get_rule(self, si: SummaryInfo) -> Union[IRuleSummaryInfo, None]:

        match_inst = None
        for rule in self._rules:
            key = str(id(rule))
            if key in self._cache:
                inst = self._cache[key]
            else:
                inst: IRuleSummaryInfo = rule(self)
                self._cache[key] = inst
            if inst.get_is_match(si):
                match_inst = inst
                break
        return match_inst


    def process_summary_info(self, si: SummaryInfo) -> None:
        """
        Process Summary info. Making changes base upon first match if a rule match is found.

        Args:
            si (SummaryInfo): [description]
        """
        match = self._get_rule(si)
        if match:
            match.process_summary_info(si)
        

    def get_rule_instance(self, rule: IRuleSummaryInfo) -> IRuleSummaryInfo:
        if not issubclass(rule, IRuleSummaryInfo):
            msg = f"{self.__class__.__name__}.get_rule_instance(), rule arg must be child class of IRuleSummaryInfo"
            logger.error(msg)
            raise TypeError(msg)
        key = str(id(rule))
        if key in self._cache:
            return self._cache[key]
        else:
            self._cache[key] = rule(self)
        return self._cache[key]

# endregion SummaryInfo Rules

# region Name Rules

# region     Name Rules Interfaces
class IRuleName(ABC):
    @abstractmethod
    def __init__(self, rules: 'IRulesName') -> None:
        """Constructor"""

    @abstractmethod
    def get_is_match(self, ni: NameInfo) -> bool:
        """
        Gets if rule is a match
        
        Args:
            ni (NameInfo): name info
        """

    @abstractmethod
    def process_name(self, ni: NameInfo) -> None:
        """
        Changes name info based upon rules match

        Args:
            ni (NameInfo): name info
        """


class IRulesName(ABC):
    @abstractmethod
    def process_name(self, ni: NameInfo) -> None:
        """
        Changes name info based upon rules match

        Args:
            ni (NameInfo): name info
        """

    @abstractmethod
    def get_rule_instance(self, rule: IRuleName) -> IRuleName:
        """Gets a rule instance"""

# endregion     Name Rules Interfaces

# region     IRuleName rules
class RuleNameCleanClass(IRulesName):
    """Cleans name to remove any non class name chars"""
    def __init__(self, rules: IRulesName) -> None:
        self._rules = rules

    def get_is_match(self, ni: NameInfo) -> bool:
        """Gets if name is a match"""
        clean_name = Util.get_clean_classname(ni.name)
        return ni.name != clean_name

    def process_name(self, ni: NameInfo) -> None:
        """
        Cleans ni.name to remove any non class name chars

        Args:
            ni (NameInfo): name info
        """
        ni.name = Util.get_clean_classname(ni.name)


class RuleNameNoGenerics(IRuleName):
    """Cleans name to remove any Generic < U, T > like strings"""

    def __init__(self, rules: IRulesName) -> None:
        self._rules = rules

    def get_is_match(self, ni: NameInfo) -> bool:
        """Gets if name is a match"""
        parts = ni.name.split(sep='<', maxsplit=1)
        if len(parts) == 1:
            return False
        return True

    def process_name(self, ni: NameInfo) -> None:
        """
        Cleans ni.name to remove any Generic < U, T > like strings

        Args:
            ni (NameInfo): name info
        """
        ni.name = Util.get_clean_classname(ni.name)
# endregion IRuleName rules

# region     IRulesName Engine

class RulesName(IRulesName):
    """Manages rules for NameInfo"""
    def __init__(self) -> None:
        self._rules: List[type[IRuleName]] = []
        self._cache = {}
        self._register_known_rules()

    def register_rule(self, rule: type[IRuleName]) -> None:
        """
        Register rule

        Args:
            rule (type[IRuleName]): Rule to register

        Raises:
            TypeError: If rules is not inherited form IRuleName
        """
        if not issubclass(rule, IRuleName):
            msg = f"{self.__class__.__name__}.register_rule(), rule arg must be child class of ITypeRule"
            raise TypeError(msg)
        if rule in self._rules:
            msg = f"{self.__class__.__name__}.register_rule() Rule is already registered"
            logger.warning(msg)
            return
        self._reg_rule(rule=rule)

    def unregister_rule(self,  rule: type[IRuleName]):
        """
        [summary]

        Args:
            rule (type[IRuleName]): Rule to unregister

        Raises:
            ValueError: If rule is not present
        """
        try:
            key = str(id(rule))
            if key in self._cache:
                del self._cache[key]
            self._rules.remove(rule)
        except ValueError as e:
            msg = f"{self.__class__.__name__}.unregister_rule() Unable to unregister rule."
            raise ValueError(msg) from e

    def _reg_rule(self, rule: type[IRuleName]):
        self._rules.append(rule)

    def _register_known_rules(self):
        pass

    def _get_rule(self, ni: NameInfo) -> Union[IRuleName, None]:

        match_inst = None
        for rule in self._rules:
            key = str(id(rule))
            if key in self._cache:
                inst = self._cache[key]
            else:
                inst: IRuleName = rule(self)
                self._cache[key] = inst
            if inst.get_is_match(ni):
                match_inst = inst
                break
        return match_inst

    def process_name(self, ni: NameInfo) -> None:
        match = self._get_rule(ni)
        if match:
            match.process_name(ni)


    def get_rule_instance(self, rule: IRuleName) -> IRuleName:
        if not issubclass(rule, IRuleName):
            msg = f"{self.__class__.__name__}.get_rule_instance(), rule arg must be child class of IRuleName"
            logger.error(msg)
            raise TypeError(msg)
        key = str(id(rule))
        if key in self._cache:
            return self._cache[key]
        else:
            self._cache[key] = rule(self)
        return self._cache[key]

# endregion IRulesName Engine

# endregion Name Rules

# region util


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
class Util:
    """Utility class of static methods for operations"""
    
    TYPE_RULES: ModType.TypeRules = None

    @staticmethod
    def is_fragment_url(in_str: str) -> bool:
        """
        Gets if an input string contains ``#`` character

        Args:
            in_str (str): input to test

        Returns:
            bool: ``True`` if ``#`` is found; Otherwise, ``False``
        """
        if not in_str:
            return False
        i = in_str.find('#')
        return i >= 0

    @staticmethod
    def get_ns_from_url(url: str, name: Optional[str] = None) -> str:
        """
        Gets full name form a realitive for full url string.

        ``com.sun.star.awt`` from ``namespacecom_1_1sun_1_1star_1_1awt.html#ad249d76933bdf54c35f4eaf51a5b7965``.

        ``com.sun.star.awt.XMessageBoxFactory`` from ``com_1_1sun_1_1star_1_1awt_1_1XMessageBoxFactory``.

        Args:
            url (str): full or realitve Url string
            name (str, optional): Optional name that is use to replace or appnd to namespace return.
                Some urls may have a unexpected ending such as ``structcom_1_1sun_1_1star_1_1beans_1_1Pair_3_01T_00_01U_01_4.html``.
                Defaults to ``None``.

        Returns:
            str: namespace format sucha as ``com.sun.star.awt`` or ``com.sun.star.awt.XMessageBoxFactory``

        Note:
            ``name`` param is appended with urls that contain a fragment ( # ).
            ``name`` param replaces name part of urls that do not have a fragment.
        """
        parts = url.split(URL_SPLIT)
        parts[0] = 'com'
        if Util.is_fragment_url(url):
            # fragment such as: namespacecom_1_1sun_1_1star_1_1awt.html#ad249d76933bdf54c35f4eaf51a5b7965
            last = parts.pop() # awt.html#ad249d76933bdf54c35f4eaf51a5b7965
            parts.append(last.split(sep='.', maxsplit=1)[0])
            if name:
                parts.append(name)
        else:
            # No fragment sucha as: interfacecom_1_1sun_1_1star_1_1awt_1_1XMessageBoxFactory.html
            last = parts.pop() # XMessageBoxFactory.html
            if name:
                parts.append(name)
            else:
                # caution to be used with not providing a name.
                # some url are not ending in a clean name such as
                # urls for generic types Pair < U, T > ect...
                parts.append(last.split(sep='.', maxsplit=1)[0])
        return ".".join(parts)

    @staticmethod
    def get_ns_from_a_tag(a_tag: Tag) -> Union[str, None]:
        """
        Gets a namespace from an anchor tag

        Args:
            a_tag (Tag): Anchor Tag

        Returns:
            Union[str, None]: Namesapce if Valid anchor tag. Otherwise ``None``

        See also:
            ``Util.get_ns_from_url()``
        """
        if not a_tag:
            return None
        href: str = a_tag.get('href', None)
        if not href:
            return None
        text = a_tag.text.strip().replace('::', '.').rstrip('.')
        name = None
        if text:
            parts = text.rsplit(sep='.', maxsplit=1)
            name = parts.pop()
        return Util.get_ns_from_url(url=href, name=name)

    @staticmethod
    def encode_file_name(name: Union[Path, str]) -> str:
        _name = str(name)
        _name = _name.replace(' ', '_').replace('<', '').replace('>', '')
        return _name
    
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
        # get the biggest number and then find all its possible flags.
        # if any smaller number is not a possible flag then return false
        num_in = [*args]
        num_len = len(num_in)
        num_in.sort()
        if num_len < 2:
            return False
        if num_len == 3:
            tmp_lst = [0, 1, 2]
            is_simple = True
            for i, y in enumerate(tmp_lst):
                is_simple = num_in[i] == y
                if not is_simple:
                    break
            if is_simple:
                return False
            tmp_lst = [1, 2, 3]
            is_simple = True
            for i, y in enumerate(tmp_lst):
                is_simple = num_in[i] == y
                if not is_simple:
                    break
            if is_simple:
                return False
        num = num_in.pop()
        mod = num % 2
        if mod != 0:
            return False
        nums = set()
        shift_num = num
        while shift_num > 0:
            shift_num = shift_num >> 1
            nums.add(shift_num)
        is_flags = True
        for i in num_in:
            if i < 0:
                is_flags = False
                break
            if not i in nums:
                is_flags = False
                break
        return is_flags

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
    
    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    def get_clean_method_name(input: str) -> str:
        """
        Clean a methpd/property name and changes name suah as ``Pair< T, U >`` to ``Pair``

        Args:
            input (str): name

        Returns:
            str: cleaned name
        """
        return Util.get_clean_classname(input=input)
    
    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    def get_clean_classname(input: str) -> str:
        """
        Clean a class name and changes name suah as ``Pair< T, U >`` to ``Pair``

        Args:
            input (str): name

        Returns:
            str: cleaned name
        """
        # convert 'Pair< T, U >' to 'Pair'
        s = pattern_generic_name.sub(r'\g<1>', input)
        s = s.replace(" ", "_")
        return s
    
    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_clean_filename(input: str) -> str:
        """
        Clean a file name and changes name suah as ``Pair< T, U >`` to ``Pair``

        Args:
            input (str): filename

        Returns:
            str: cleaned file name
        """
        # convert 'Pair< T, U >' to 'Pair'
        s = pattern_generic_name.sub(r'\g<1>', input)
        s = s.replace(" ", "_")
        return s
  
    
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
    
    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def clean_sq_braces(input: str) -> str:
        """
        Removes opening ``[.*]``

        Args:
            input (str): string to clean

        Returns:
            str: input to remove square brackets and all in between
        """
        return pattern_sq_braket.sub('', input)

    @AcceptedTypes((dict, list), int, ftype=DecFuncEnum.METHOD_STATIC)
    @staticmethod
    def get_formated_dict_list_str(obj: Union[dict, list], indent=4) -> str:
        """
        Get a formated dictionary or list

        Args:
            obj (Union[dict, list]): Dict or list to get formats string for.
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
        return RelInfo.camel_to_snake(input=input)

    @staticmethod
    def get_clean_imports(ns: str, imports: Iterable[str]) -> Set[str]:
        """
        Gets a set of unique imports.

        Args:
            ns (str): namespace to append if any item in imports is misssing ns part
            imports (Iterable[str]): Imports list, set, tuple, etc

        Returns:
            Set[str]: Set of imports. Each import is guaranteed to be full ns object.
        """
        sep = '.'
        results: Set[str] = set()
        for im in imports:
            if im.find(sep) < 0:
                s = ns + sep + im
            else:
                s = im
            results.add(s)
        return results


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
        return RelInfo.get_rel_import(in_str=i_str,ns=ns, sep=sep)
    
    @staticmethod
    def get_rel_import_long(i_str: str, ns: str, sep: str = '.') -> Tuple[str, str, str]:
        """
        Gets realitive import Tuple

        Args:
            i_str (str): Namespace and object such as ``com.sun.star.uno.Exception``
            ns (str): Namespace used to get realitive postion such as ``com.sun.star.awt``
            sep (str, optional): Namespace seperator. Defaults to ``.``

        Returns:
            Tuple[str, str]: realitive import info such as ``('..uno.exception', 'Exception')``
        """
        return RelInfo.get_rel_import_long(in_str=i_str,ns=ns, sep=sep)

    def get_rel_import_long_name(i_str: str, ns: str, sep: str = '.') -> str:
        """
        Geta a long Name. Same as getting last part of ```get_rel_import_long()```

        Args:
            in_str (str): Namespace and object such as ``com.sun.star.uno.Exception``
            ns (str): Namespace used to get realitive postion such as ``com.sun.star.awt``
            sep (str, optional): Namespace seperator. Defaults to ``.``

        Returns:
            str: Long name such as ``uno_exception``
        """
        return RelInfo.get_rel_import_long_name(
            in_str=i_str,
            ns=ns,
            sep=sep
        )

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

    @deprecated(version='0.1.4', reason='Deprecated, use get_python_type() instead')
    @AcceptedTypes(str, opt_args_filter=DecArgEnum.NAMED_ARGS, ftype = DecFuncEnum.METHOD_STATIC)
    @TypeCheckKw(arg_info={"typings": 0, "quote": 0}, types=[bool], ftype=DecFuncEnum.METHOD_STATIC)
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
        logger.warning(
            'Util.get_py_type is deprecated, use get_python_type() instead')

        if not uno_type:
            return ''
        def ex_type(in_parts: List[str]) -> Union[dict, None]:
            start = in_parts[0].rstrip()
            if not start in TYPE_MAP_EX:
                return None
            params: dict = TYPE_MAP_EX[start]
            _results = {
                "is_typing": params.get("is_typing", False),
                "is_py_type": params.get("is_py_type", True)
            }
            full = '<'.join(in_parts)
            _regx = params.get('regex', None)
            _replace: str = params['replace']
            if _regx:
                m = re.match(_regx, full)
                if m:
                    groups = m.groups()
                    replacements = []
                    for t in groups:
                        replacements.append(TYPE_MAP.get(t, 'object'))
                    _replace = _replace.format(*replacements)
            _results['type'] = _replace
            _results['long_type'] = params.get('long_type', _replace)
            return _results

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
            "wdata": {
                "is_wrapper": False,
                "is_py_type": False,
                "wdata": {
                    "prefix": "",
                    "wrapper": "",
                    "py_type_inner": False
                }
            }
        }
        _u_type = uno_type.strip().lstrip().replace("::", ".").lstrip('.')
        # check for # sequence< string >
        parts = _u_type.split(sep='<', maxsplit=1)
        if len(parts) > 1:
            ex_info = ex_type(parts)
            if ex_info:
                cb_data['is_wrapper'] = ex_info.get('is_wrapper', False)
                cb_data['is_typing'] = ex_info.get('is_typing', False)
                cb_data['long_type'] = ex_info['long_type']
                cb_data['is_py_type'] = ex_info['is_py_type']
                do_cb(cb, cb_data)
                return ex_info['type']
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

    @staticmethod
    @TypeCheckKw(arg_info={"in_type": 0, "ns": 1}, types=[str, (str, type(None))], ftype=DecFuncEnum.METHOD_STATIC)
    def get_python_type(in_type: str, name_info: NameInfo, ns: str, long_names: bool = False) -> ModType.PythonType:
        """
        Gets Python Type info including an required imports.

        Args:
            in_type (str): uno type

        Returns:
            PythonType: class that contains type, requires typing and imporst info.
        """
        if Util.TYPE_RULES is None:
            Util.TYPE_RULES = ModType.TypeRules()

        logger.debug("Util.get_python_type() in_type: '%s'", in_type)

        def is_self_import(s:str, class_name:str) -> bool:
            try:
                p_type = Util.TYPE_RULES.get_python_type(in_type=s)
                if not p_type.imports:
                    return False
                if p_type.imports == class_name:
                    return True
                full_name = ns + '.' + class_name
                return p_type.imports == full_name
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e

        Util.TYPE_RULES.namespace = ns
        Util.TYPE_RULES.long_names = long_names
        self_import = is_self_import(in_type, name_info.name)
        if self_import:
            Util.TYPE_RULES.long_names = False

        try:
            py_type = Util.TYPE_RULES.get_python_type(in_type)
            if self_import:
                py_type.imports = None
            return py_type
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e

    @staticmethod
    @AcceptedTypes((str, Path), ftype=DecFuncEnum.METHOD_STATIC)
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

# endregion util

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

# region Writer/parser base
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
            self._title_full = Util.get_clean_classname(text)
        return self._title_full

    def _get_name(self, soup: BeautifulSoup):
        full = self._get_full_name(soup=soup)
        parts = full.split('.')
        return parts[len(parts) - 1]

    def _get_desc(self, soup: BeautifulSoup) -> List[str]:
        lines = []
        contents = soup.find('div', class_='contents')
        if not contents:
            return lines
        block = contents.find('div', class_='textblock')
        if not block:
            return lines
        soup_lines: ResultSet = block.find_all('p')
        if not soup_lines:
            return lines
        for i, ln in enumerate(soup_lines):
            s = ln.text.strip().replace('::', '.')
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

# endregion Writer/parser base

# region Image Process

# region Cache


class ImageCache(CacheBase):
    """
    Caches files and retreives cached files.
    Cached file are in a subfolder of system tmp dir.
    """

    def fetch_from_cache(self, filename: Union[str, Path]) -> Union[Image.Image, None]:
        """
        Fetches file contents from cache if it exist and is not expired

        Args:
            filename (Union[str, Path]): File to retrieve

        Returns:
            Union[str, None]: File contents if retrieved; Otherwise, ``None``
        """
        if self.seconds <= 0:
            return None
        f = Path(self.path, filename)
        if not f.exists():
            return None

        f_stat = f.stat()
        if f_stat.st_size == 0:
            # shoud not be zero byte file.
            try:
                self.del_from_cache(f)
            except Exception as e:
                logger.warning(
                    'Not able to delete 0 byte file: %s, error: %s', filename, str(e))
            return None
        ti_m = f_stat.st_mtime
        age = time.time() - ti_m
        if age >= self.seconds:
            return None

        try:
            # Check if we have this file locally
            with Image.open(f) as img:
                img.load()
                return img
        except IOError:
            return None

    def save_in_cache(self, filename: Union[str, Path], content: Any):
        """
        Saves file contents into cache

        Args:
            filename (Union[str, Path]): filename to write.
            content (str): Contents to write into file.
        """
        f = Path(self.path, filename)
        # print('Saving a copy of {} in the cache'.format(filename))
        with open(f, 'wb') as file:
            shutil.copyfileobj(content, file)

# endregion Cache

# region Response


class ResponseImg(ResponseBase):
    """Gets response data for an image"""

    def __init__(self, url: str, cache_seconds: Optional[float] = None, **kwargs):
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
            file_ext (str, optional): Extension if file. Default ext of url.
                Format must prepend ``.`` such as ``.png``
        """
        if cache_seconds is None:
            cache_seconds = APP_CONFIG.cache_duration
        super().__init__(url=url, cache_seconds=cache_seconds, **kwargs)
        self._img: Image.Image = None

    # cache for one week - 604800.0 seconds
    def _get_request_data(self) -> Image.Image:
        global IMG_CACHE
        allow_cache = self.cache_seconds > 0
        filename = self._url_hash + self._file_ext
        if not IMG_CACHE:
            IMG_CACHE = ImageCache(
                tmp_dir=APP_CONFIG.cache_dir, lifetime=self.cache_seconds)
        if allow_cache:
            img = IMG_CACHE.fetch_from_cache(filename=filename)
            if img:
                logger.debug(
                    "ResponseImg._get_request_data() retreived data from Cache")
                return img
        response = requests.get(url=self.url, stream=True)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        response.raw.decode_content = True
        IMG_CACHE.save_in_cache(
            filename=filename, content=response.raw)
        img = IMG_CACHE.fetch_from_cache(filename=filename)
        if allow_cache:
            logger.debug(
                "ResponseImg._get_request_data() Saving to cache as: %s", Path(IMG_CACHE.path, filename))
        else:
            IMG_CACHE.del_from_cache(filename=filename)
        return img

    @property
    def img(self) -> Image.Image:
        """
        Gets image
        """
        if self._img is None:
            try:
                self._img = self._get_request_data()
            except Exception as e:
                logger.error(e)
                raise e
        return self._img
# endregion Response

class ImageInfo:
    """Gets various image data like is inherited and pixel data"""
    @staticmethod
    def get_image_pixels_by_mode(image: Image.Image, dtype='int8'):
        """Get a numpy array of an image so that one can access values[x][y]."""
        # https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
        width, height = image.size
        if image.mode == "RGB":
            channels = 3
        elif image.mode == "L":
            channels = 1
        elif image.mode == "P":
            channels = 1
        else:
            print("Unknown mode: %s" % image.mode)
            return None
        pixel_values = np.array(image.getdata(), dtype=dtype).reshape(
            (height, width, channels))
        # pixel_values = numpy.array(pixel_values).reshape((width, height))
        return pixel_values

    @staticmethod
    def get_image_pixels(image: Image.Image, dtype='int8', reshape=True):
        """Get a numpy array of an image so that one can access values[x][y]."""
        if reshape:
            width, height = image.size
            pixel_values = np.array(
                image.getdata(), dtype=dtype).reshape((height, width))
        else:
            pixel_values = np.array(
                image.getdata(), dtype=dtype)
        return pixel_values

    @staticmethod
    def get_area_info(url: str, **kwargs) -> AreaInfo:
        """
        Gets Area info and shape if shape is available

        Args:
            url (str): Url of image

        Keyword Arguments:
            allow_cache (bool, optional) If ``False`` caching is ignored. Default ``True``

        Raises:
            Exception: [description]
            e: [description]

        Returns:
            AreaInfo: Area Info with optionl shape.
        """
        global PICKLE_CACHE
        allow_cache = bool(kwargs.get('allow_cache', True))
        def get_cord(px: np.ndarray, color_index: int) -> Union[Shape, None]:
            # Tested this method against images in GNU. Result are perfect on images viewed.
            # Cordinates are exact. Borders are 1 px in size
            def zero_runs(a):
                # https://coderedirect.com/questions/302557/find-indexes-of-repeated-elements-in-an-array-python-numpy
                iszero = np.concatenate(
                    ([0], np.equal(a, 0).view(np.int8), [0]))
                absdiff = np.abs(np.diff(iszero))
                ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
                return ranges
            # to find a actual block must match several pixels in a row on the horizontal plane.
            # words have the same index color as non shape we are looking for.
            i_rows = px.shape[0]
            cords = None
            x1_y1 = None
            x2_y2 = None
            r1 = None
            r2 = None
            for y in range(0, i_rows):
                row = px[y,:]
                # start_seq = search_sequence_numpy(row, seq)
                runs = zero_runs(np.diff(row))
                # runs of 7 or more, to illustrate filter
                f_runs = runs[runs[:, 1]-runs[:, 0] > APP_CONFIG.pixel_map_min_shape_width]
                if not x1_y1 is None:
                    for r in f_runs:
                        index = int(r[-1]) # last element
                        v = row[index]
                        if v == color_index:
                            x2_y2 = index, int(y),
                            r2 = r
                            break
                if x1_y1 is None:
                    for r in f_runs:
                        index = int(r[0])
                        v = row[index]
                        if v == color_index:
                            x1_y1 = index,  int(y)
                            r1 = r
                            break
                if x1_y1 and x2_y2:
                    # compare top border pixel length with bottom border
                    # the number should match or something is wrong
                    if (r1==r2).all():
                        cords = x1_y1 + x2_y2
                    else:
                        msg = f"ImageInfo.get_area_info(). Image to and bottom borders did not mathc! Url: {url}"
                        logger.warning(msg)
                if not cords is None:
                    break
            if cords is None:
                return None
            return Shape(x1=cords[0], y1=cords[1], x2=cords[2], y2=cords[3])
    
        r_img = ResponseImg(url=url, cache_seconds=0)
        if PICKLE_CACHE is None:
            PICKLE_CACHE = PickleCache(tmp_dir=APP_CONFIG.cache_dir)
        seconds = PICKLE_CACHE.seconds
        if allow_cache is False:
            PICKLE_CACHE.seconds = 0.0
        try:
            filename = r_img.url_hash + '_ai.pkl'
            obj: AreaInfo = PICKLE_CACHE.fetch_from_cache(filename=filename)
            if obj:
                return obj
            
            im = r_img.img
            pix = ImageInfo.get_image_pixels(im)
            row = pix[0, :]  # row 0
            found_px = -1
            # images are expected to be indexed png files
            # find the first pixel that does not have index of 0
            # if first pixes is 1 then not inherited, if 3 inherited
            for px in row:
                if px != 0:
                    found_px = px
                    break
            if found_px == -1:
                msg = f"Failed to find colored pixel in first row of image pixels. Url: {url}"
                raise Exception(msg)
            

            cord = get_cord(pix, APP_CONFIG.pixel_map_no_link)
            ai = AreaInfo(
                is_inherited=found_px == APP_CONFIG.pixel_inherit,
                shape=cord
                )
            
            PICKLE_CACHE.save_in_cache(filename=filename, content=ai)
            return ai
        except Exception as e:
            logger.error(e)
            raise e
        finally:
            # resotore cache time
            PICKLE_CACHE.seconds = seconds

    @staticmethod
    def is_inherit_img(url: str) -> bool:
        global TEXT_CACHE
        r_img = ResponseImg(url=url, cache_seconds=0)
        if TEXT_CACHE is None:
            TEXT_CACHE = TextCache(tmp_dir=APP_CONFIG.cache_dir)
        try:
            filename = r_img.url_hash + '.txt'
            result = -1
            txt = TEXT_CACHE.fetch_from_cache(filename=filename)
            if txt:
                result = int(txt)
                return result == APP_CONFIG.pixel_inherit
            im = r_img.img
            pix = ImageInfo.get_image_pixels(im)
            row = pix[0, :]  # row 0
            # images are expected to be indexed png files
            # find the first pixel that does not have index of 0
            # if first pixes is 1 then not inherited, if 3 inherited
            for px in row:
                if px != 0:
                    result = px
                    break
            if result == -1:
                msg = f"Failed to find colored pixel in first row of image pixels. Url: {url}"
                raise Exception(msg)
            content = str(result)
            TEXT_CACHE.save_in_cache(filename=filename, content=content)
            return result == APP_CONFIG.pixel_inherit
        except Exception as e:
            logger.error(e)
            raise e

# endregion Image Process

# region Area Process


class ApiDyContent(BlockObj):
    """Gets dyncontent block that contains area data and image data"""

    def __init__(self, soup: SoupObj):
        """
        Constructor

        Args:
            block (BlockObj): Block obj containing full page html
        """
        super().__init__(soup)
        self._data = False

    def _log_missing(self):
        logger.warning(
            "ApiDyContent.get_obj() Failed to get find data. Url: %s", self.url_obj.url)

    def get_obj(self) -> Union[Tag, None]:
        """Gets dyncontent block that contains area data and image data"""
        if not self._data is False:
            return self._data
        soup = self.soup.soup
        tag_dyn = soup.find('div', class_='dyncontent')
        if not tag_dyn:
            self._log_missing()
            return self._data
        self._data = tag_dyn
        return self._data


class ApiAreaBlock(BlockObj):
    def __init__(self, block: ApiDyContent):
        self._block: ApiDyContent = block
        super().__init__(self._block.soup)
        self._data = False

    def _log_missing(self):
        logger.warning(
            "ApiAreaBlock.get_obj() Failed to get find data. Url: %s", self.url_obj.url)

    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        tag: Tag = self._block.get_obj()
        if not tag:
            self._log_missing()
            return self._data
        tag_map = tag.find('map')
        if not tag_map:
            self._log_missing()
            return self._data
        self._data = tag_map
        return self._data


class ApiImage(BlockObj):
    """Gets url of image that represents map"""

    def __init__(self, block: ApiDyContent):
        self._block: ApiDyContent = block
        super().__init__(self._block.soup)
        self._data = False

    def _log_missing(self, for_str: Optional[str] = None):
        if for_str:
            f_str = f" for {for_str}"
        else:
            f_str = ''
        logger.warning(
            "ApiImage.get_obj() Failed to get find data%s. Url: %s", f_str, self.url_obj.url)

    def get_obj(self) -> Union[str, None]:
        """Gets url of image that represents map"""
        if not self._data is False:
            return self._data
        self._data = None
        tag: Tag = self._block.get_obj()
        if not tag:
            self._log_missing()
            return self._data
        tag_img = tag.find('img')
        if not tag_img:
            self._log_missing()
            return self._data
        src = tag.img.get('src', None)
        if src is None:
            self._log_missing('image src')
            return self._data
        m = pattern_http.match(src)
        if m:
            self._data = src
        else:
            self._data = self.url_obj.url_base + '/' + src
        return self._data


class ApiArea(BlockObj):
    """List of area items"""

    def __init__(self, block: ApiAreaBlock):
        self._block: ApiAreaBlock = block
        super().__init__(self._block.soup)
        self._data = None

    def _log_missing(self, for_str: Optional[str] = None):
        if for_str:
            f_str = f" for {for_str}"
        else:
            f_str = ''
        logger.warning(
            "ApiArea.get_obj() Failed to get find data%s. Url: %s", f_str, self.url_obj.url)
    
    def _get_ns(self,name: str, href: str) -> Ns:
        parts = href.split(sep=URL_SPLIT)
        parts[0] = 'com' # rename interfacecom etc...
        parts.pop() # drop XShapeDescriptor.html etc...
        ns = ".".join(parts)
        return Ns(name=name, namespace=ns)

    def get_obj(self) -> List[Area]:
        """List of area items"""
        if not self._data is None:
            return self._data
        self._data = []
        tag = self._block.get_obj()
        if not tag:
            self._log_missing('ApiAreaBlock instance')
            return self._data
        rs = tag.select('area')
        if not rs:
            self._log_missing('area tags')
            return self._data
        for el in rs:
            href = el.get('href', None)
            if not href:
                self._log_missing('area href')
                continue
            name = el.get('alt', None)
            if not name:
                self._log_missing('area alt')
                continue
            coords = el.get('coords', None)
            if not coords:
                self._log_missing('area cords')
                continue
            title = el.get('title', '')
            a_coords = coords.split(',')
            if len(a_coords) != 4:
                logger.warning(
                    "ApiArea.get_obj() Bad Coords for %s. Url: %s", name, self.url_obj.url)
                continue
            ns = self._get_ns(name=name, href=href)
            x1 = int(a_coords[0].strip())
            y1 = int(a_coords[1].strip())
            x2 = int(a_coords[2].strip())
            y2 = int(a_coords[3].strip())
            m = pattern_http.match(href)
            if not m:
                href = self.url_obj.url_base + '/' + href
            area = Area(name=name, ns=ns, href=href, x1=x1,
                        y1=y1, x2=x2, y2=y2, title=title)
            self._data.append(area)
        return self._data

class AreaFilter:
    def __init__(self, alst: List[Area], area_info: AreaInfo, rules_engine: 'IRulesArea') -> None:
        self._lst = alst
        self._ai = area_info
        self._rules_engine: IRulesArea = rules_engine
        self._first: Area = None if len(self._lst) == 0 else self._lst[0]
        # self._inherited = self._get_inherited()
        self._inherited = self._get_from_rules()

    def _get_from_rules(self) -> List[Area]:
        if self._ai.is_inherited is False:
            return []
        if len(self._rules_engine) == 0:
            msg = f"{self.__class__.__name__}._get_from_rules() Rules must not contain rules to process."
            logger.error(msg)
            raise Exception(msg)

        # rules_engine determines sorting
        area_lst = self._rules_engine.get_area(ai=self._ai, alst=self._lst)
        return area_lst or []


    def get_as_ns(self) -> List[Ns]:
        """
        Gets the current inherited list of Area as a list of ``Ns``
        
        Sorting if any has been determined by IRulesArea

        Returns:
            List[Ns]: List if inherited Namespaces
        """
        # no sorting should be done here.
        return [el.ns for el in self._inherited]

    @property
    def inherited(self) -> List[Area]:
        """Gets inherited value"""
        return self._ai.is_inherited
    
    @property
    def area_info(self) -> AreaInfo:
        """Gets the area info containing inherited and cordinates info."""
        return self._ai

# region        Area Rules

# region            Rule Area Interfaces


class IRulesArea(ABC):

    @abstractmethod
    def get_area(self,  ai: AreaInfo, alst: List[Area]) -> List[Area]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """

    @abstractmethod
    def __len__(self) -> int:
        """Gets the length of rules"""

    @abstractproperty
    def remove_parent_inherited(self) -> bool:
        """Removes Parent Inherite Property"""

class IRuleArea(ABC):
    
    @abstractmethod
    def __init__(self, rules:IRulesArea) -> None:
        """constructor"""

    @abstractmethod
    def get_is_match(self, ai: AreaInfo, alst: List[Area]) -> bool:
        """
        Gets if rule is a match
        
        Args:
            alst (List[Area]): Areas to match
        """

    @abstractmethod
    def get_area(self, ai: AreaInfo,  alst: List[Area]) -> List[Area]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """


# endregion         Rule Area Interfaces

# region            Area Rules
class RuleAreaBase(IRuleArea):
    """Matches when there is a single parent"""
    def __init__(self, rules:IRulesArea) -> None:
        """constructor"""
        self._rules = rules
      # region Private Methods
    def _get_with_parent_removed(self, first: Area, d_lst: Dict[int, List[Area]],  match_lst: List[Area]) -> None:
        """
        Remove any parent inherits from match_lst. This method does not affect sort order of match_lst

        Args:
            first (Area): First Area
            d_lst (Dict[int, List[Area]]): dict of y1 grouped Area list
            match_lst (List[Area]): List of area that is considered inherits. Out Arg.
        """
        # flatten all others into a single set
        # Any keys in d_lst that are are lower y1 then first.y1 are parent objects. Higher are child object.
        # The lower the y1 value the closer it is to the top if image.
        flat = set()
        for k, v in d_lst.items():
            if k >= first.y1:
                continue
            for area in v:
                flat.add(area.ns.fullns)

        # find any
        remove: List[int] = []
        for i, area in enumerate(match_lst):
            if area.ns.fullns in flat:
                remove.append(i)
        # any entry that is found in flat then remove it.
        if len(remove) > 0:
            remove.sort(reverse=True)
            for i in remove:
                match_lst.pop(i)

    def _list_dict_y1(self, lst: List[Area]) -> Dict[int, List[Area]]:
        """groups lst into area y1"""
        d = {}
        for area in lst:
            if not area.y1 in d:
                d[area.y1] = []
            d[area.y1].append(area)
        return d
    
    def _list_dict_x1(self, lst: List[Area]) -> Dict[int, List[Area]]:
        """groups lst into area x1"""
        d = {}
        for area in lst:
            if not area.x1 in d:
                d[area.x1] = []
            d[area.x1].append(area)
        return d

    def _get_upper(self, first: Area, d_lst: Dict[int, List[Area]]) -> List[Area]:
        """
        Get a list of all areas that have a y1 value equal then first.y1

        In area map lower y1 values are higer in inheritance.
        """
        lst: List[Area] = []
        for k, v in d_lst.items():
            if k < first.y1:
                lst.extend(v)
        return lst

    def _remove_duplicates_lst(self, lst: List[Area]) -> bool:
        """
        Removes any duplicates base upon namespace.
        Method does not change the sort order of lst

        Args:
            clean_lst (List[Area]): List to remove duplicates from
            filter_lst (List[Area]): List used as filter

        Returns:
            bool: True if any duplicates were found; Otherwise False.
        """
        unique_names: Set[str] = set()
        remove_indexes: List[int] = []
        for i, area in enumerate(lst):
            if area.ns.fullns in unique_names:
                remove_indexes.append(i)
            else:
                unique_names.add(area.ns.fullns)
        if len(remove_indexes) == 0:
            return False
        remove_indexes.sort(reverse=True)
        for i in remove_indexes:
            lst.pop(i)
        return True

    def _get_first_y1(self, ai: AreaInfo, alst: List[Area]) -> Area:
        if not ai.shape:
            return alst[0] # go with first it should always work. However order is scraped form html
        first = None
        lst_y = [(a.y1, i) for i, a in enumerate(alst)]
        lst_y.sort(reverse=True)
        for y in lst_y:
            if y[0] < ai.shape.y1:
                first = alst[y[1]]
                break
        if first:
            return first
        return alst[0]

    # endregion Privae Methods

    # region Properties
    @property
    def rules(self) -> IRulesArea:
        """Gets rules value"""
        return self._rules
    # endregion Properties

class RuleAreaSingle(RuleAreaBase):
    """Matches when there is a single parent"""

    def __init__(self, rules: IRulesArea) -> None:
        """constructor"""
        super().__init__(rules=rules)
    
    # region IRuleArea Methods
    def get_is_match(self, ai: AreaInfo, alst: List[Area]) -> bool:
        """
        Gets if rule is a match
        
        Args:
            alst (List[Area]): Areas to match
        """
        if len(alst) == 0:
            return False
        d_lst = self._list_dict_y1(lst=alst)
        match_lst = d_lst[alst[0].y1]
        if len(match_lst) != 1:
            return False
        if ai.shape:
            m = match_lst[0]
            if m.x1 != ai.shape.x1:
                return False
        return True

    def get_area(self, ai: AreaInfo, alst: List[Area]) -> List[Area]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """
        d_lst = self._list_dict_y1(lst=alst)
        return d_lst[alst[0].y1]
    # endregion IRuleArea Methods


class RuleAreaMulti(RuleAreaBase):
    """Matches when there is a multiple adjacent parents"""
    def __init__(self, rules: IRulesArea) -> None:
        """constructor"""
        super().__init__(rules=rules)
    # region IRuleArea Methods
    def get_is_match(self, ai: AreaInfo, alst: List[Area]) -> bool:
        """
        Gets if rule is a match
        
        Args:
            alst (List[Area]): Areas to match
        """
        if len(alst) == 0:
            return False
        d_lst = self._list_dict_y1(lst=alst)
        first = self._get_first_y1(ai=ai, alst=alst)
        match_lst = d_lst[first.y1]
        if len(match_lst) <= 1:
            return False
        return True


    def get_area(self, ai: AreaInfo, alst: List[Area]) -> List[Area]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """
        first = self._get_first_y1(ai=ai, alst=alst)
        d_lst: Dict[int, List[Area]] = self._list_dict_y1(lst=alst) # grouped by y1
        # extract group I want
        match_lst: List[Area] = [area for area in d_lst[first.y1]] # list of y1 matches
        if len(match_lst) == 0:
            return match_lst
        del d_lst[first.y1]
        if self.rules.remove_parent_inherited:
            self._get_with_parent_removed(first=first,d_lst=d_lst, match_lst=match_lst)
        
        return match_lst
    # endregion IRuleArea Methods

class RuleAreaVertical(RuleAreaBase):
    """Matches when there is a vertical parent"""

    def __init__(self, rules: IRulesArea) -> None:
        """constructor"""
        super().__init__(rules=rules)
    # region IRuleArea Methods
    def get_is_match(self, ai: AreaInfo, alst: List[Area]) -> bool:
        """
        Gets if rule is a match
        
        Args:
            alst (List[Area]): Areas to match
        """
        # vertical matches are when all areas have the sam x1 value:
        # see: https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ucb_1_1ContentResultSet.html
        if len(alst) < 2:
            return False
        first = self._get_first_y1(ai=ai, alst=alst)
        if ai.shape:
            # vertical are ofset left or right on x1, Usually right
            # more likley this is a single
            if first.x1 == ai.shape.x1:
                return False
        is_vert = True
        d_lst: Dict[int, List[Area]] = self._list_dict_x1(
            lst=alst)  # grouped by y1
        for area in d_lst[first.x1]:
            if area.x1 != first.x1:
                is_vert = False
                break
        
        return is_vert

    def get_area(self, ai: AreaInfo, alst: List[Area]) -> List[Area]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """       
        # remove any duplicates and return list.
        # is it unlikely there would ever be duplicates, but just in case.
        first = self._get_first_y1(ai=ai, alst=alst)
        d_lst: Dict[int, List[Area]] = self._list_dict_x1(
            lst=alst)  # grouped by y1
        upper: List[Area] = d_lst[first.x1]
        sorted_u = sorted(upper, key=lambda a: a.y1)
        if self.rules.remove_parent_inherited:
            self._remove_duplicates_lst(sorted_u)
        return sorted_u
    # endregion IRuleArea Methods
# endregion         Area Rules

# region            Rules Area Engine


class RulesArea(IRulesArea):
    """Manages rules for NameInfo"""

    def __init__(self, remove_parent_inherited) -> None:
        self._remove_parent_inherited: bool = remove_parent_inherited
        self._rules: List[type[IRuleArea]] = []
        self._cache = {}
        self._register_known_rules()

    def __len__(self) -> int:
        return len(self._rules)

    # region Methods

    def register_rule(self, rule: type[IRuleArea]) -> None:
        """
        Register rule

        Args:
            rule (type[IRuleArea]): Rule to register

        Raises:
            TypeError: If rules is not inherited form IRuleArea
        """
        if not issubclass(rule, IRuleArea):
            msg = f"{self.__class__.__name__}.register_rule(), rule arg must be child class of ITypeRule"
            raise TypeError(msg)
        if rule in self._rules:
            msg = f"{self.__class__.__name__}.register_rule() Rule is already registered"
            logger.warning(msg)
            return
        self._reg_rule(rule=rule)

    def unregister_rule(self,  rule: type[IRuleArea]):
        """
        [summary]

        Args:
            rule (type[IRuleArea]): Rule to unregister

        Raises:
            ValueError: If rule is not present
        """
        try:
            key = str(id(rule))
            if key in self._cache:
                del self._cache[key]
            self._rules.remove(rule)
        except ValueError as e:
            msg = f"{self.__class__.__name__}.unregister_rule() Unable to unregister rule."
            raise ValueError(msg) from e

    def _reg_rule(self, rule: type[IRuleArea]):
        self._rules.append(rule)

    def _register_known_rules(self):
        pass

    def _get_rule(self, ai: AreaInfo, alst: List[Area]) -> Union[IRuleArea, None]:

        match_inst = None
        for rule in self._rules:
            key = str(id(rule))
            if key in self._cache:
                inst = self._cache[key]
            else:
                inst: IRuleArea = rule(rules=self)
                self._cache[key] = inst
            if inst.get_is_match(ai=ai, alst=alst):
                match_inst = inst
                break
        return match_inst

    def get_area(self, ai: AreaInfo, alst: List[Area]) -> Union[List[Area], None]:
        """
        Gets filtered Area list

        Args:
            alst (List[Area]): Areas to filter

         Returns:
            List[Area]: Filtered Area List
        """
        match = self._get_rule(ai=ai, alst=alst)
        if match:
            return match.get_area(ai=ai, alst=alst)
        return None
    # endregion Methods

    # region Properties
    @property
    def remove_parent_inherited(self) -> bool:
        """Specifies remove_parent_inherited

            :getter: Gets remove_parent_inherited value.
            :setter: Sets remove_parent_inherited value.
        """
        return self._remove_parent_inherited

    @remove_parent_inherited.setter
    def remove_parent_inherited(self, value: bool):
        self._remove_parent_inherited = value
    # endregion Properties
# endregion         Rules Area Engine
# endregion     Area Rules
class ApiInherited(BlockObj):

    def __init__(self, soup: SoupObj, area_filter_rules_engine: IRulesArea, ns: str, class_name: str, **kwargs) -> None:
        """
        Constructor

        Args:
            soup (SoupObj): Soup object
            area_filter_rules_engine (IRulesArea): Rules engine for procesing area data.
            ni (NameInfo): Contains name of current class being processed.

        Keyword Arguments:
            raise_error (bool, optional): Determines if errors will be raised when they occur: Default ``False``
        """
        super().__init__(soup)
        self._api_dy_content: ApiDyContent = ApiDyContent(self.soup)
        self._ns: str = ns
        self._class_name = class_name
        self._data = None
        self._raise_errors = bool(kwargs.get('raise_error', False))
        self._area_fileter_rules_engine = area_filter_rules_engine
        self._ai: AreaInfo = None
        self._allow_cache = bool(kwargs.get('allow_cache', True))

    def _log_missing(self, for_str: Optional[str] = None, raise_error: bool = False):
        if for_str:
            f_str = f" for {for_str}"
        else:
            f_str = ''
        msg = f"ApiInherited.get_obj() Failed to get find data{f_str}. Url: {self.url_obj.url}"
        if raise_error:
            logger.error(msg)
            raise Exception(msg)
        logger.warning(msg)

    def get_obj(self) -> List[Ns]:
        """
        Gets a list of Ns objects. Sorting is dertimined by IRulesArea

        Returns:
            List[Ns]: List of Ns objects for class inherites
        """
        if not self._data is None:
            return self._data
        known = get_known_extends(ns=self._ns, class_name=self._class_name)
        if known:
            logger.info('%s: Found Known inherites for %s.%s', self.__class__.__class__, self._ns, self._class_name)
            self._data = known
            return self._data
        self._data = []
        ai = ApiImage(self._api_dy_content)
        image_url = ai.get_obj()
        if not image_url:
            self._log_missing(for_str='image url',
                              raise_error=self._raise_errors)
            return self._data
        self._ai = ImageInfo.get_area_info(url=image_url, allow_cache=self._allow_cache)
        if not self._ai.is_inherited:
            return self._data
        ab: ApiAreaBlock = ApiAreaBlock(self._api_dy_content)
        api_area: ApiArea = ApiArea(ab)
        lst = api_area.get_obj()
        filter = AreaFilter(lst, area_info=self._ai, rules_engine=self._area_fileter_rules_engine)
        extends = filter.get_as_ns()
        if not extends:
            return self._data
        self._data = extends
        return self._data
    
    @property
    def area_info(self) -> AreaInfo:
        """Gets the area info containing inherited and cordinates info."""
        if self._ai is None:
            raise Exception('ApiInherited.area_info can not be called before get_obj()')
        return self._ai
    
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
# endregion Area Process

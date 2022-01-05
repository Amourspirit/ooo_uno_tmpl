#!/usr/bin/env python
# coding: utf-8
"""
Module reads a json file of links that contain links to enum pages
This module then parses each link and calls the correct module to process each link.
"""
# region imports
import os
import sys
import argparse
import subprocess
import json
import logging
import concurrent.futures
from collections import namedtuple
from typing import Callable, Dict, List, Tuple, Union
from pathlib import Path
from verr import Version
from abc import ABC, abstractmethod, abstractproperty
from kwhelp.decorator import RequireArgs, SubClasskKw, TypeCheckKw
import parser.base as base
from logger.log_handle import get_logger
from parser import __version__, JSON_ID

# endregion imports

# region Logger
logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger
    logger = l
    base._set_loggers(l)


_set_loggers(None)
# endregion Logger

urldata = namedtuple('urldata', ['name', 'href'])
# region IParser Class

class IParser(ABC):
    @abstractmethod
    def __init__(self, json_path: Union[str, Path]) -> None:
        """Constructor"""

    @abstractmethod
    def get_links(self) -> List[urldata]:
        """Gets Links"""

    @abstractmethod
    def get_min_version(self) -> Version:
        """Gets Min version"""
    
    @abstractmethod
    def get_is_classes_data(self) -> bool:
        """Gets if data is from classes section"""

    @abstractmethod
    def get_section_name(self) -> str:
        """Gets the section name such as enum or interface"""

    @abstractproperty
    def app_root(self) -> Path:
        """Gets the app root path"""


class Parser(IParser):
    def __init__(self, json_path: Union[str, Path]) -> None:
        self._json_path = json_path
        self._json_data: dict = None
        self._dir = Path(__file__).parent
        self._app_root = self._dir.parent.parent
        self._cache = {}
        self._load_json()

    def _load_json(self):
        j_p = Path(self._json_path)
        if not j_p.is_absolute():
            j_p = Path(self._app_root, j_p)
        if not j_p.exists():
            msg = f"Unable to find json file: '{self._json_path}'"
            logger.error(msg)
            raise FileNotFoundError(msg)
        with open(j_p) as j_file:
            json_data = json.load(j_file)
        self._validite_json(json_data)
        self._json_data = json_data

    def _validite_json(self, data: dict) -> bool:
        msg = f"{self.__class__.__name__}._validite_json() {self.get_section_name()}:"
        
        key = 'id'
        if not key in data:
            _msg = f"{msg} Json missing id field. File: {self._json_path}"
            logger.error(_msg)
            raise Exception(_msg)
        if data[key] != JSON_ID:
            _msg = f"{msg} Json data bad id field. Expected: {JSON_ID}, Got: {data[key]}. File: {self._json_path}"
            logger.error(_msg)
            raise Exception(_msg)
        key = 'type'
        if not key in data:
            _msg = f"{msg} Json missing type field. File: {self._json_path}"
            logger.error(_msg)
            raise Exception(_msg)
        if data[key] != 'module_links':
            _msg = f"{msg} Json data bad id field. Expected: module_links, Got: {data[key]}. File: {self._json_path}"
            logger.error(_msg)
            raise Exception(_msg)
        key = 'url_base'
        if not key in data:
            _msg = f"{msg} Json missing url_base field. File: {self._json_path}"
            logger.error(_msg)
            raise Exception(_msg)
        key = 'version'
        if not key in data:
            _msg = f"{msg} Json missing version field. File: {self._json_path}"
            logger.error(_msg)
            raise Exception(_msg)
        min_ver = self.get_min_version()
        json_ver = Version.parse(data[key])
        if json_ver < min_ver:
            _msg = f"{msg} Version fail Expect a min version of '{min_ver}', got '{json_ver}'. File: {self._json_path}"
            logger.error(_msg)
            raise Exception(_msg)
        key = 'data'
        if not key in data:
            _msg = f"{msg} Json missing data field. File: {self._json_path}"
            logger.error(_msg)
            raise Exception(_msg)
        if not isinstance(data[key], dict):
            _msg = f"{msg} Json data field is not a dictionary. File: {self._json_path}"
            logger.error(_msg)
            raise Exception(_msg)


    def get_is_classes_data(self) -> bool:
        return True

    def get_links(self) -> List[urldata]:
        key = 'get_links'
        if key in self._cache:
            return self._cache[key]
        result: List[urldata] = []
        data = self._json_data['data']
        c_data = self.get_is_classes_data()
        if c_data:
            if not 'classes' in data:
                return result
            link_data = data['classes']
        else:
            link_data = data

        url_base = self._json_data['url_base']
        links: List[dict] = link_data.get(self.get_section_name(), [])
        for itm in links:
            name = itm['name']
            href = itm['href']
            m = base.pattern_http.match(href)
            if not m:
                href = url_base + '/' + href
            result.append(urldata(name=name, href=href))
        self._cache[key] = result
        return self._cache[key]

    @property
    def app_root(self) -> Path:
        """Gets app_root value"""
        return self._app_root

# endregion IParser Class

# region IWriter class

class IWriter(ABC):
    @abstractmethod
    def __init__(self, parser: IParser, func: Callable) -> None:
        """Constructor"""

    @abstractmethod
    def get_parser_name(self) -> str:
        """Gets parser name sucha as xsrc or struc"""

    @abstractmethod
    def write(self, *args, **kwargs) -> None:
        """Writes data"""

    @abstractmethod
    def get_parse_fn(seff) -> Callable:
        """Gets parse function such as xsrc.parse"""

class Writer(IWriter):
    def __init__(self, parser: IParser) -> None:
        self._parser: IParser = parser
        self._proc = Path(self._parser.app_root, 'parser',
                          self.get_parser_name())

    def _process_link(self, url_data: urldata) -> str:
        cmd_str = f"{self._proc} -t -j -u {url_data.href}"
        logger.info('Running subprocess: %s', cmd_str)
        cmd = [sys.executable] + cmd_str.split()
        res = subprocess.run(cmd)
        result = f"Success, {url_data.name}"
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            result = result = f"Fail, {url_data.name}"
            logger.error(res.stderr)
        return result

    def _process_direct(self, url_data: urldata, fn: Callable, *args, **kwargs) -> Tuple[bool, str]:
        flags = [arg for arg in args if isinstance(arg, str)]
        if len(flags) == 0:
            flags.append('t')
            flags.append('j')
        kargs = kwargs.copy()
        kargs['url'] = url_data.href
        result = True
        try:
            fn(*flags, **kargs)
        except Exception:
            result = False
        return result, url_data.name

    def write(self, *args, **kwargs):
        links = self._parser.get_links()
        fn = self.get_parse_fn()
        # for link in links:
        #     self._process_direct(link, fn, *args, **kwargs)
        # return
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(self._process_direct, link, fn, *args, **kwargs)
                       for link in links]
            for f in concurrent.futures.as_completed(results):
                state, name = f.result()
                if state:
                    logger.info(f"Success processing: {name}")
                else:
                    logger.error(f"Failed processing: {name}")

# endregion IWriter class
# region Parse method

def _get_parsed_kwargs(**kwargs) -> Dict[str, str]:
    required = ("json_file",)
    ignore = ("iparser", "iwriter")
    lookups = {
        "f": "json_file",
        "json_file": "json_file",
        "L": "log_file",
        "log_file": "log_file"
    }
    result = {}
    for k, v in kwargs.items():
        if not isinstance(k, str):
            continue
        if k in lookups:
            key = lookups[k]
            result[key] = v
        else:
            if not k in ignore:
                result[k] = v
    for k in required:
        if not k in result:
            # k is missing from kwargs
            raise base.RequiredError(f"Missing required arg {k}.")
    return result


def _get_parsed_args(*args) -> Dict[str, bool]:
    # key, value and value is a key into defaults
    defaults = {
        "verbose": False
    }
    found = {
        "verbose": True
    }
    lookups = {
        "v": "verbose",
        "verbose": "verbose"
    }
    result = {k: v for k, v in defaults.items()}
    for arg in args:
        if not isinstance(arg, str):
            continue
        if arg in lookups:
            key = lookups[arg]
            result[key] = found[key]
    return result

@RequireArgs('iparser','iwriter')
def parse(*args, **kwargs):
    """
    Parses data, alternative to running on command line.
    Any extra ``kwargs`` values are passet to ``IWriter.write()`` method

    Other Arguments:
        iparser (type[IParser]): IParser subclass
        iwriter (type[IWriter]): IWriter subclass

    Keyword Arguments:
        json_file (str): Short form ``f``. url to parse
        log_file (str, optional): Short form ``L``. Log File
    """
    global logger
    parser: type[IParser] = kwargs.get('iparser')
    writer: type[IWriter] = kwargs.get('iwriter')
    pkwargs = _get_parsed_kwargs(**kwargs)
    pargs = _get_parsed_args(*args)

    if logger is None:
        log_args = {}
        if 'log_file' in pkwargs:
            log_args['log_file'] = pkwargs['log_file']
        else:
            log_args['log_file'] = 'base_parse.log'
        if pargs['verbose']:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    p: IParser = parser(json_path=pkwargs['json_file'])
    w: IWriter = writer(parser=p)
    w.write(*args, **pkwargs)

# endregion Parse method


def get_cmd_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='interface')
    parser.add_argument(
        '-f', '--json-file',
        help='Source json',
        type=str,
        dest='json_file',
        required=True
    )
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use. Defaults to interface_parse.log',
        type=str,
        required=False)

    args = parser.parse_args()
    return args


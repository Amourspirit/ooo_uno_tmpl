#!/usr/bin/env python
# coding: utf-8
"""
Module reads a json file of links that contain links to enum pages
This module then parses each link and calls the correct module to process each link.
"""
# region imports
import sys
import argparse
import subprocess
import json
import logging
import concurrent.futures
from collections import namedtuple
from typing import Callable, List, Tuple, Union
from pathlib import Path
from verr import Version
from abc import ABC, abstractmethod, abstractproperty
from kwhelp.decorator import RequireArgs
from ..common import log_load
from ..common.config import APP_CONFIG
from ..common.regx import pattern_http
from ...logger.log_handle import get_logger
from ...parser import __version__, JSON_ID
from ...utilities import util

# endregion imports

# region Logger
logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger
    log = log_load.Log()
    log.logger = l
    logger = log.logger


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
        self._app_root = Path(util.get_root())
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
            m = pattern_http.match(href)
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
    def get_parser_path(self) -> Path:
        """Gets parser full path"""

    @abstractmethod
    def write(self, **kwargs) -> None:
        """
        Writes data

        Keyword Arguments:
            url (str): url to parse
            no_sort (str, optional): No sorting of results. Default ``False``
            no_cache (str, optional): No caching. Default ``False``
            no_print_clear (str, optional):No clearing of terminal when otuput to terminal. Default ``False``
            no_desc (str, optional): No description will be outputed in template. Default ``False``
            json_out (bool, optional): returns json to caller if ``True``. Default ``False``
            long_names (str, optional): Long names. Default set in config ``use_long_import_names`` property.
                Toggles values set in config.
            long_template (str, optional): Writes a long format template.
                Requires write_template is set. Default ``False``
            clipboard (str, optional): Copy to clipboard. Default ``False``
            print_json (str, optional): Print json to termainl. Default ``False``
            print_template (str, optional): Print template to terminal. Default ``False``
            write_template (str, optional): Write template file into obj_uno subfolder. Default ``False``
            write_json (str, optional): Write json file into obj_uno subfolder. Default ``False``
            verbose (str, optional): Verobose output.
            log_file (str, optional): Log File
        """

    @abstractmethod
    def get_parse_fn(self) -> Callable:
        """Gets parse function such as xsrc.parse"""


class Writer(IWriter):
    def __init__(self, parser: IParser) -> None:
        self._parser: IParser = parser
        self._proc = self.get_parser_path()

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

    def _process_direct(self, url_data: urldata, fn: Callable, **kwargs) -> Tuple[bool, str]:
        kargs = kwargs.copy()
        kargs['url'] = url_data.href
        result = True
        try:
            fn(**kargs)
        except Exception:
            result = False
        return result, url_data.name

    def write(self, **kwargs):
        """
        Writes data

        Keyword Arguments:
            url (str): url to parse
            no_sort (str, optional): No sorting of results. Default ``False``
            no_cache (str, optional): No caching. Default ``False``
            no_print_clear (str, optional):No clearing of terminal when otuput to terminal. Default ``False``
            no_desc (str, optional): No description will be outputed in template. Default ``False``
            long_names (str, optional): Long names. Default set in config ``use_long_import_names`` property.
                Toggles values set in config.
            long_template (str, optional): Writes a long format template.
                Requires write_template is set. Default ``False``
            clipboard (str, optional): Copy to clipboard. Default ``False``
            print_json (str, optional): Print json to termainl. Default ``False``
            print_template (str, optional): Print template to terminal. Default ``False``
            write_template (str, optional): Write template file into obj_uno subfolder. Default ``False``
            write_json (str, optional): Write json file into obj_uno subfolder. Default ``False``
            verbose (str, optional): Verobose output.
            log_file (str, optional): Log File
        """
        links = self._parser.get_links()
        fn = self.get_parse_fn()
        # for link in links:
        #     self._process_direct(link, fn, *args, **kwargs)
        # return
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(self._process_direct, link, fn, **kwargs)
                       for link in links]
            for f in concurrent.futures.as_completed(results):
                state, name = f.result()
                if state:
                    logger.info(f"Success processing: {name}")
                else:
                    logger.error(f"Failed processing: {name}")

# endregion IWriter class
# region Parse method


@RequireArgs('iparser', 'iwriter', 'json_file')
def parse(**kwargs):
    """
    Parses data, alternative to running on command line.
    Any extra ``kwargs`` values are passet to ``IWriter.write()`` method

    Keyword Arguments:
        iparser (type[IParser]): IParser subclass
        iwriter (type[IWriter]): IWriter subclass
        json_file (str): file to parse
        url (str): url to parse
        no_sort (str, optional): No sorting of results. Default ``False``
        no_cache (str, optional): No caching. Default ``False``
        no_print_clear (str, optional):No clearing of terminal when otuput to terminal. Default ``False``
        no_desc (str, optional): No description will be outputed in template. Default ``False``
        long_names (str, optional): Long names. Default set in config ``use_long_import_names`` property.
            Toggles values set in config.
        long_template (str, optional): Writes a long format template.
            Requires write_template is set. Default ``False``
        clipboard (str, optional): Copy to clipboard. Default ``False``
        print_json (str, optional): Print json to termainl. Default ``False``
        print_template (str, optional): Print template to terminal. Default ``False``
        write_template (str, optional): Write template file into obj_uno subfolder. Default ``False``
        write_json (str, optional): Write json file into obj_uno subfolder. Default ``False``
        verbose (str, optional): Verobose output.
        log_file (str, optional): Log File
    """
    global logger
    parser: type[IParser] = kwargs.get('iparser')
    writer: type[IWriter] = kwargs.get('iwriter')
    json_file: str = str(kwargs['json_file'])
    log_file = kwargs.get('log_file', None)
    verbose = bool(kwargs.get('verbose', False))

    if logger is None:
        log_args = {}
        if log_file:
            log_args['log_file'] = log_file
        else:
            log_args['log_file'] = 'base_parse.log'
        if verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    logger.info("Processing Json File: %s", json_file)
    p: IParser = parser(json_path=json_file)
    w: IWriter = writer(parser=p)
    w.write(**kwargs)

# endregion Parse method

# region Parser

def set_cmd_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-f', '--json-file',
        help='Source json',
        type=str,
        dest='json_file',
        required=True
    )
    parser.add_argument(
        '-k', '--no-allow-known-json',
        help='Do not allow Known Json',
        action='store_false',
        dest='allow_know_json',
        default=True)
    parser.add_argument(
        '-o', '--out',
        help=f"Out path of templates and json data. Default: '{APP_CONFIG.uno_base_dir}'",
        type=str,
        dest='write_path',
        default=None,
        required=False)

def set_cmd_args_local(parser) -> None:
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

# endregion Parser


def get_cmd_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='interface')
    set_cmd_args(parser)
    set_cmd_args_local(parser)

    args = parser.parse_args()
    return args

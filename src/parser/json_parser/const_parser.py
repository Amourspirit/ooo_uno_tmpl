#!/usr/bin/env python
# coding: utf-8
"""
Module reads a json file of links that contain links to enum pages
This module then parses each link and calls the correct module to process each link.
"""
# region imports
import sys
import argparse
import logging
import subprocess
import json
import concurrent.futures
from collections import namedtuple
from typing import List, Tuple, Union
from pathlib import Path
from kwhelp.decorator import RequireArgs
from verr import Version
from ...logger.log_handle import get_logger
from ...parser import __version__, JSON_ID, base, const
from ...utilities import util

# endregion imports

# region Logger
logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l


_set_loggers(None)
# endregion Logger

urldata = namedtuple('urldata', ['name', 'href'])


class ParserConst:
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
        if not self._is_valid_json(json_data):
            msg = "ParserConst: Json data failed validation"
            logger.error(msg)
            raise Exception(msg)
        self._json_data = json_data

    def _is_valid_json(self, data: dict) -> bool:
        key = 'id'
        if not key in data:
            return False
        if data[key] != JSON_ID:
            return False
        key = 'type'
        if not key in data:
            return False
        if data[key] != 'module_links':
            return False
        key = 'url_base'
        if not key in data:
            return False
        key = 'version'
        if not key in data:
            return False
        min_ver = Version(0, 1, 8)
        json_ver = Version.parse(data[key])
        if json_ver < min_ver:
            return False
        key = 'data'
        if not key in data:
            return False
        if not isinstance(data[key], dict):
            return False
        return True

    def get_links(self) -> List[urldata]:
        key = 'get_links'
        if key in self._cache:
            return self._cache[key]
        url_base = self._json_data['url_base']
        enum_links: List[dict] = self._json_data['data'].get('constants', [])

        result: List[urldata] = []
        for itm in enum_links:
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


class WriterConst:
    def __init__(self, parser: ParserConst) -> None:
        self._parser: ParserConst = parser
        # self._proc = Path(self._parser.app_root, 'parser', 'const.py')
        self._proc = Path(const.__file__)

    def _process_link(self, url_data: urldata) -> str:
        cmd_str = f"{self._proc} -t -j -u {url_data.href}"
        logger.info('Running subprocess: %s', cmd_str)
        cmd = [sys.executable] + cmd_str.split()
        res = subprocess.run(cmd)
        result = f"Success, {url_data.name}"
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            result = f"Fail, {url_data.name}"
            logger.error(res.stderr)
        return result

    def _process_direct(self, url_data: urldata, **kwargs) -> Tuple[bool, str]:
        kargs = kwargs.copy()
        kargs['url'] = url_data.href
        result = True
        try:
            const.parse(**kargs)
        except Exception:
            result = False
        return result, url_data.name

    def Write(self, **kwargs):
        links = self._parser.get_links()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(self._process_direct, link, **kwargs)
                       for link in links]
            for f in concurrent.futures.as_completed(results):
                state, name = f.result()
                if state:
                    logger.info(f"Success processing: {name}")
                else:
                    logger.error(f"Failed processing: {name}")


# region Parse method

@RequireArgs('json_file')
def parse(**kwargs):
    """
    Parses data, alternative to running on command line.

    Keyword Arguments:
        json_file (str): file to parse
        url (str): url to parse
        cache (str, optional): Caching. Default ``True``
        include_desc (str, optional): Description will be outputed in template. Default ``True``
        flags (str, optional): Treat as flags. Default ``False``
        hex (str, optional): Treat as hex. Default ``False``
        long_names (str, optional): Long names. Default set in config ``use_long_import_names`` property.
            Toggles values set in config.
        long_template (str, optional): Writes a long format template.
            Requires write_template is set. Default ``False``
        clipboard (str, optional): Copy to clipboard. Default ``False``
        print_json (str, optional): Print json to termainl. Default ``False``
        print_template (str, optional): Print template to terminal. Default ``False``
        write_template (str, optional): Write template file into obj_uno subfolder. Default ``False``
        write_json (str, optional): Write json file into obj_uno subfolder. Default ``False``
        write_path (str, optional): The root path to write data files (json, tmpl) into. Defaut set in config ``uno_base_dir`` property.
        verbose (str, optional): Verobose output.
        log_file (str, optional): Log File
    """
    global logger
    _verbose = bool(kwargs.get('verbose', False))
    _log_file = kwargs.get('log_file', None)
    _json_file = str(kwargs['json_file'])
    if logger is None:
        log_args = {}
        if _log_file:
            log_args['log_file'] = _log_file
        else:
            log_args['log_file'] = 'const_parser.log'
        if _verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    p = ParserConst(json_path=_json_file)
    w = WriterConst(parser=p)
    w.Write(**kwargs)

# endregion Parse method

# region Parser
def set_cmd_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-f', '--json-file',
        help='Source Url',
        type=str,
        dest='json_file',
        required=True
    )


def set_cmd_args_local(parser) -> None:
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

# endregion Parser

def main():
    global logger
    # region Parser
    # json_file = "uno_obj/chart2/module_links.json"
    # json_file = "uno_obj/chart2/data/module_links.json"
    parser = argparse.ArgumentParser(description='interface')
    set_cmd_args(parser)
    set_cmd_args_local(parser)
    args = parser.parse_args()

    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'const_parser.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    # endregion Parser
    if len(sys.argv) > 1:
        logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing File %s' % args.json_file)

    p = ParserConst(json_path=args.json_file)
    w = WriterConst(parser=p)
    w.Write(write_json=True, write_template=True)

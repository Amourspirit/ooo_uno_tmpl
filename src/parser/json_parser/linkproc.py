#!/usr/bin/env python
# coding: utf-8
"""
Module reads a json file of links that contain links to modules.
This module then parses each link and calls the correct module to process each link.
This module reads star.json and calls mod.py to write module_links.json files.
"""
# region imports
import sys
import argparse
import logging
import json
import concurrent.futures
from collections import namedtuple
from typing import List, Tuple, Union
from pathlib import Path
from ...logger.log_handle import get_logger
from verr import Version
from ..common.regx import pattern_http
from ..common import log_load
from ...parser import __version__, JSON_ID
from ...parser.json_parser import mod
from ...utilities import util as mutil
# endregion imports

# region Logger
logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger
    logger = l
    log_load.set_logger(l)


_set_loggers(None)
# endregion Logger

# pattern_http = re.compile(r"^https?:\/\/")

urldata = namedtuple('urldata', ['name', 'href'])


class ParserLinks:
    def __init__(self, json_path: Union[str, Path]) -> None:
        self._json_path = json_path
        self._json_data: dict = None
        self._cache = {}
        self._load_json()

    def _load_json(self):
        j_p = Path(self._json_path)
        if not j_p.is_absolute():
            j_p = Path(Path(mutil.get_root()), j_p)
        if not j_p.exists():
            msg = f"Unable to find json file: '{self._json_path}'"
            logger.error(msg)
            raise FileNotFoundError(msg)
        with open(j_p) as j_file:
            json_data = json.load(j_file)
        if not self._is_valid_json(json_data):
            msg = "ParserLinks: Json data failed validation"
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
        if data[key] != 'namespace_url':
            return False
        key = 'url_base'
        if not key in data:
            return False
        key = 'version'
        if not key in data:
            return False
        min_ver = Version(0, 1, 3)
        json_ver = Version.parse(data[key])
        if json_ver < min_ver:
            return False
        key = 'data'
        if not key in data:
            return False
        if not isinstance(data[key], list):
            return False
        return True

    def get_links(self) -> List[urldata]:
        key = 'get_links'
        if key in self._cache:
            return self._cache[key]
        url_base = self._json_data['url_base']
        url_root = self._json_data['url']
        data: List[dict] = self._json_data['data']
        result: List[urldata] = []
        # add root url so module_links.json is written in uno_obj folder.
        m = pattern_http.match(url_root)
        if not m:
            url_root = url_base + '/' + url_root
        result.append(urldata(name='star', href=url_root))
        m = None
        for itm in data:
            name = itm['name']
            href = itm['href']
            m = pattern_http.match(href)
            if not m:
                href = url_base + '/' + href
            result.append(urldata(name=name, href=href))
        self._cache[key] = result
        return self._cache[key]


class WriterLinks:
    def __init__(self, parser: ParserLinks) -> None:
        self._parser = parser

    def _process_direct(self, url_data: urldata, **kwargs) -> Tuple[bool, str]:
        kargs = kwargs.copy()
        kargs['url'] = url_data.href
        result = True
        try:
            mod.parse(**kargs)
        except Exception:
            result = False
        return result, url_data.name

    def Write(self, **kwargs):
        links = self._parser.get_links()
        # for lnk in links:
        #     state, name  = self._process_direct(lnk, **kwargs)
        #     if state:
        #         logger.info(f"Success processing: {name}")
        #     else:
        #         logger.error(f"Failed processing: {name}")
        # return
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(self._process_direct, link, **kwargs)
                       for link in links]
            for f in concurrent.futures.as_completed(results):
                state, name = f.result()
                if state:
                    logger.info(f"Success processing: {name}")
                else:
                    logger.error(f"Failed processing: {name}")


def _main():
    global logger
    if logger is None:
        log_args = {
            'log_file': 'linkproc.log',
            'level': logging.DEBUG
        }
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    data_link = "resources/star.json"
    p = ParserLinks(json_path=data_link)
    w = WriterLinks(parser=p)
    w.Write()

# region Parse method


def get_kwargs_from_args(args: argparse.ArgumentParser) -> dict:
    """
    Converts argparse args into dictionary that can be passed to ``parse()``

    Args:
        args (argparse.ArgumentParser): args

    Returns:
        dict: dictionary that contain key values matching ``parser()`` args.
    """
    # see: https://tinyurl.com/y8rs4ux5
    mod_d = mod.get_kwargs_from_args(args)
    d = {
        "json_file": args.json_file,
        "log_file": args.log_file,
        "verbose": args.verbose
    }
    if args.write_path:
        d['write_path'] = args.write_path
    mod_d.update(d)
    return mod_d


def parse(**kwargs):
    """
    Parses data, and runs commands

    Keyword Arguments:
        json_file (str, optional): Json file to parse. Default ``resources/star.json``
        cache (bool, optional): Determines caching. Default ``False``.
        print_clear (bool, optional): Determines clearing of terminal
            when otuput to terminal. Default ``False``.
        print_json (bool, optional): Print json to termainl. Default ``False``.
        write_json (bool, optional): Write json file into obj_uno subfolder. Default ``False``.
        write_path (str, optional): The root path to write data files (json, tmpl) into. Defaut set in config ``uno_base_dir`` property.
        verbose (bool, optional): Verobose output. Default ``False``.
        recursive (bool, optional): Recursivly process modules. If url contains links other modules they will be processed.
            Default ``False``
        log_file (str, optional): Log File
    """
    global logger
    json_file = str(Path(mutil.get_root(), 'resources', 'star.json'))
    _log_file = 'linkproc.log' if kwargs.get(
        'log_file', None) is None else str(kwargs.get('log_file'))
    _verbose = bool(kwargs.get('verbose', False))

    if logger is None:
        log_args = {}
        log_args['log_file'] = _log_file
        if _verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    j_path = kwargs.get('json_file', None)
    if j_path is None:
        j_path = json_file
    p = ParserLinks(json_path=j_path)
    w = WriterLinks(parser=p)
    kargs = kwargs.copy()
    if 'json_file' in kargs:
        del kargs['json_file']
    w.Write(**kargs)


def set_cmd_args(parser: argparse.ArgumentParser) -> None:
    json_file = str(Path(mutil.get_root(), 'resources', 'star.json'))
    parser.add_argument(
        '-f', '--json-file',
        help="Source Json file. Default 'resources/star.json'",
        type=str,
        dest='json_file',
        required=False,
        default=json_file)
    mod.set_cmd_args(parser)


def set_cmd_args_local(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use. Defaults to const.log',
        type=str,
        required=False)
# endregion Parse method

# region Main


def main():
    global logger
    # region Parser

    parser = argparse.ArgumentParser(description='interface')
    set_cmd_args(parser)
    set_cmd_args_local(parser)

    args = parser.parse_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'linkproc.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    # endregion Parser
    if len(sys.argv) > 1:
        logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing File %s' % args.json_file)

    p = ParserLinks(json_path=args.json_file)
    w = WriterLinks(parser=p)
    w.Write('r', 'j')

# endregion Main

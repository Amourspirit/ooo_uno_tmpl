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
import re
import subprocess
import json
import logging
import concurrent.futures
from collections import namedtuple
from typing import List, Union
from pathlib import Path
from verr import Version
_app_root = os.environ.get('project_root', str(
    Path(__file__).parent.parent.parent))
if not _app_root in sys.path:
    sys.path.insert(0, _app_root)
import parser.base as base
from logger.log_handle import get_logger
from parser import __version__, JSON_ID

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


class ParserInterface:
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
        if data[key] != 'module_links':
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
        if not isinstance(data[key], dict):
            return False
        return True

    def get_links(self) -> List[urldata]:
        key = 'get_links'
        if key in self._cache:
            return self._cache[key]
        result: List[urldata] = []
        data = self._json_data['data']
        if not 'classes' in data:
            return result
        classes = data['classes']
        
        url_base = self._json_data['url_base']
        links: List[dict] = classes.get('interface', [])
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


class WriterInterface:
    def __init__(self, parser: ParserInterface) -> None:
        self._parser: ParserInterface = parser
        self._proc = Path(self._parser.app_root, 'parser', 'xsrc.py')

    def _process_link(self, url_data: urldata) -> bool:
        cmd_str = f"{self._proc} -t -j -u {url_data.href}"
        logger.info('Running subprocess: %s', cmd_str)
        cmd = [sys.executable] + cmd_str.split()
        res = subprocess.run(cmd)
        result = f"{url_data.name}, Success"
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            result = f"{url_data.name}, Fail"
            logger.error(res.stderr)
        return result

    def Write(self):
        links = self._parser.get_links()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(self._process_link, link)
                       for link in links]
            for f in concurrent.futures.as_completed(results):
                logger.info(f.result())


def main():
    global logger
    # region Parser
    # json_file = "uno_obj/chart2/module_links.json"
    # json_file = "uno_obj/chart2/data/module_links.json"
    parser = argparse.ArgumentParser(description='interface')
    parser.add_argument(
        '-f', '--json-file',
        help='Source Url',
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
        help='Log file to use. Defaults to linkproc.log',
        type=str,
        required=False)

    args = parser.parse_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'enum_parser.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    # endregion Parser
    if len(sys.argv) > 1:
        logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing File %s' % args.json_file)

    p = ParserInterface(json_path=args.json_file)
    w = WriterInterface(parser=p)
    w.Write()


if __name__ == "__main__":
    main()

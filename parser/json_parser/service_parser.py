#!/usr/bin/env python
# coding: utf-8
"""
Module reads a json file of links that contain links to enum pages
This module then parses each link and calls the correct module to process each link.
"""
# region imports
import os
import sys
import logging
from typing import Callable, Dict, List, Tuple, Union
from pathlib import Path
from verr import Version
_app_root = os.environ.get('project_root', str(
    Path(__file__).parent.parent.parent))
if not _app_root in sys.path:
    sys.path.insert(0, _app_root)
import parser.base as base
import parser.service as service
from parser.json_parser import base_parser as bp
from logger.log_handle import get_logger

# endregion imports

# region Logger
logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger
    logger = l
    bp._set_loggers(l)
    service._set_loggers(l)


_set_loggers(None)
# endregion Logger


# region IParser Class

class Parser(bp.Parser):
    def __init__(self, json_path: Union[str, Path]) -> None:
        super().__init__(json_path=json_path)

    def get_min_version(self) -> Version:
        return Version(0, 1, 8)

    def get_section_name(self) -> str:
        return 'service'

    def get_is_classes_data(self) -> bool:
        return True


# endregion IParser Class

# region IWriter class


class Writer(bp.Writer):
    def __init__(self, parser: bp.IParser) -> None:
       super().__init__(parser=parser)

    def get_parser_name(self) -> str:
        return 'service.py'

    def get_parse_fn(seff) -> Callable:
        return service.parse


# endregion IWriter class


# region Parse method

def _get_parsed_kwargs(**kwargs) -> Dict[str, str]:
    required = ("json_file",)
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


def parse(**kwargs):
    """
    Parses data, alternative to running on command line.

    Keyword Arguments:
        json_file (str): file to parse
        url (str): url to parse
        sort (str, optional): Sorting of results. Default ``True``
        cache (str, optional): Caching. Default ``False``
        clear_on_print (str, optional): Clearing of terminal when otuput to terminal. Default ``False``
        include_desc (str, optional): Description will be outputed in template. Default ``True``
        json_out (bool, optional): returns json to caller if ``True``. Default ``False``
        long_names (str, optional): Long names. Default set in config ``use_long_import_names`` property.
            Toggles values set in config.
        write_template_long (str, optional): Writes a long format template.
            Requires write_template is set. Default ``False``
        copy_clipboard (str, optional): Copy to clipboard. Default ``False``
        print_json (str, optional): Print json to termainl. Default ``False``
        print_template (str, optional): Print template to terminal. Default ``False``
        write_template (str, optional): Write template file into obj_uno subfolder. Default ``False``
        write_json (str, optional): Write json file into obj_uno subfolder. Default ``False``
        write_path (str, optional): The root path to write data files (json, tmpl) into. Defaut set in config ``uno_base_dir``
        allow_known_json (bool, optional): Allow Known Json to be used. Default ``True``
        verbose (str, optional): Verobose output.
        log_file (str, optional): Log File
    """
    global logger
    verbose = bool(kwargs.get('verbose', False))
    log_file = kwargs.get('log_file', None)

    if logger is None:
        log_args = {}
        if log_file:
            log_args['log_file'] = log_file
        else:
            log_args['log_file'] = 'service_parse.log'
        if verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    kargs = kwargs.copy()
    kargs['iparser'] = Parser
    kargs['iwriter'] = Writer
    bp.parse(**kargs)

# endregion Parse method
def _main():
    # /home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/tmp/module_links.json
    parse(write_json=True, write_template=True,
          json_file='/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno_tmpl/tmp/module_links.json')

def main():
    global logger
    args = bp.get_cmd_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'service_parse.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    if len(sys.argv) > 1:
        logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing File %s' % args.json_file)

    p = Parser(json_path=args.json_file)
    w = Writer(parser=p)
    w.Write(write_json=True, write_template=True)


if __name__ == "__main__":
    main()

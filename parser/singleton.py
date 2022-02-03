#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains a singleton class
"""
import argparse
import os
import sys
import logging
from pathlib import Path
from typing import Union
try:
    import base
except ModuleNotFoundError:
    import parser.base as base
try:
    import xsrc
except ModuleNotFoundError:
    import parser.xsrc as xsrc
from logger.log_handle import get_logger
logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger
    logger = l
    base._set_loggers(l)
    xsrc._set_loggers(l)


_set_loggers(None)

class Parser(xsrc.Parser):
    pass

class Writer(xsrc.Writer):
    def _get_json_type(sefl) -> str:
        return "singleton"

    def _get_template_ext(self) -> str:
        return base.APP_CONFIG.template_singleton_ext

    def _get_template_dyn(self) -> Union[str, None]:
        return 'singleton_dyn.tmpl'
    
    def _get_template_name(self) -> str:
        """
        Gets the template name without extension or appended __stub

        Returns:
            str: singleton
        """
        return 'singleton'

# region Parser


def get_kwargs_from_args(args: argparse.ArgumentParser) -> dict:
    return xsrc.get_kwargs_from_args(args)


def set_cmd_args(parser: argparse.ArgumentParser) -> None:
    return xsrc.set_cmd_args(parser)
# endregion Parser

def parse(**kwargs) -> Union[str, None]:
    """
    Parses data, alternative to running on command line.

    Keyword Arguments:
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
        allow_known_json (bool, optional): Allow Known Json to be used. Default ``True``
        verbose (str, optional): Verobose output.
        log_file (str, optional): Log File
    
    Returns:
        Union[str, None]: Returns json string if json_out is ``True``
    """
    kargs = kwargs.copy()
    kargs['class_parser'] = Parser
    kargs['class_writer'] = Writer
    return xsrc.parse(**kargs)


def _main():
    os.system('cls' if os.name == 'nt' else 'clear')
    url = 'https://api.libreoffice.org/docs/idl/ref/singletoncom_1_1sun_1_1star_1_1sdb_1_1DataAccessDescriptorFactory.html'  # singleton
    kwargs = {
        "url": url,
        "log_file": "debug.log",
        'verbose': True,
        "write_json": True
    }
    # sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    # main()
    parse(**kwargs)

def main():
    global logger
    parser = argparse.ArgumentParser(description='singleton')
    xsrc.set_cmd_args(parser)
    xsrc.set_cmd_args_local(parser)
    args = parser.parse_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'singleton.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    if args.print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)
    args_dict = get_kwargs_from_args(args)

    if args.print_template is False and args.print_json is False:
        print('')
    parse(**args_dict)


if __name__ == '__main__':
    main()

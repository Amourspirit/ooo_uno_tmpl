#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains a singleton class
"""
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
        return "service"

    def _get_template_ext(self) -> str:
        return base.APP_CONFIG.template_singleton_ext
    
    def _get_template_name(self) -> str:
        """
        Gets the template name without extension or appended __stub

        Returns:
            str: service
        """
        return 'service'


def parse(*args, **kwargs):
    """
    Parses data, alternative to running on command line.

    Other Arguments:
        'no_sort' (str, optional): Short form ``'s'``. No sorting of results. Default ``False``
        'no_cache' (str, optional): Short form ``'x'``. No caching. Default ``False``
        'no_print_clear (str, optional): Short form ``'p'``. No clearing of terminal
            when otuput to terminal. Default ``False``
        'no_desc' (str, optional): Short from ``'d'``. No description will be outputed in template. Default ``False``
        'long_template' (str, optional): Short form ``'g'``. Writes a long format template.
            Requires write_template is set. Default ``False``
        'clipboard' (str, optional): Short form ``'c'``. Copy to clipboard. Default ``False``
        'print_json' (str, optional): Short form ``'n'``. Print json to termainl. Default ``False``
        'print_template' (str, optional): Short form ``'m'``. Print template to terminal. Default ``False``
        'write_template' (str, optional): Short form ``'t'``. Write template file into obj_uno subfolder. Default ``False``
        'write_json' (str, optional): Short form ``'j'``. Write json file into obj_uno subfolder. Default ``False``
        'verbose' (str, optional): Short form ``'v'``. Verobose output.

    Keyword Arguments:
        url (str): Short form ``u``. url to parse
        log_file (str, optional): Short form ``L``. Log File
    """
    kargs = kwargs.copy()
    kargs['class_parser'] = Parser
    kargs['class_writer'] = Writer
    xsrc.parse(*args, **kargs)


def _main():
    os.system('cls' if os.name == 'nt' else 'clear')
    url = 'https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1MediaDescriptor.html'
    args = ('v', 'n')
    kwargs = {
        "u": url,
        "log_file": "debug.log"
    }
    # sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    # main()
    parse(*args, **kwargs)

def main():
    global logger
    args = xsrc.get_cmd_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'singleton.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)

    proc = xsrc.Processer(
        p=Parser,
        w=Writer,
        url=args.url,
        sort=args.sort,
        print_template=args.print_template,
        print_json=args.print_json,
        copy_clipboard=args.clipboard,
        write_template=args.write_template,
        write_json=args.write_json,
        clear_on_print=(not args.no_print_clear),
        write_template_long=args.long_format,
        include_desc=args.desc
    )

    if args.print_template is False and args.print_json is False:
        print('')
    proc.process()


if __name__ == '__main__':
    main()

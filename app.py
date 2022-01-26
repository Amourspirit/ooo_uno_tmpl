#!/usr/bin/env python
# region Imports
from dataclasses import dataclass
import logging
import os
import sys
import argparse
from typing import Type
from pathlib import Path
from data_manage.controller import json_controler
from data_manage.controller.database_controler import DatabaseControler
from data_manage.controller.component_controler import ComponentControler
from data_manage.controller.namespace_controler import NamespaceControler
from data_manage.controller.module_links_controler import ModuleLinksControler
from data_manage.controller.star_ns_controller import StarNsControler
from logger.log_handle import get_logger
from parser import const as url_parser_const, enm as url_parser_enum, ex as url_parser_ex, xsrc as url_parser_interface, service as url_parser_service, singleton as url_parser_singleton, struc as url_parser_struct, typedef as url_parser_typedef, star as json_parser_star
from config import AppConfig, read_config
from parser.json_parser import linkproc
from runners.touch_files import TouchFiles
from runners.compile.base_compile import BaseCompile
from runners.compile.compile_const_links import CompileConstLinks
from runners.compile.compile_enum_links import CompileEnumLinks
from runners.compile.compile_ex_lniks import CompileExLinks
from runners.compile.compile_interface_links import CompileInterfaceLinks
from runners.compile.compile_service_links import CompileServiceLinks
from runners.compile.compile_singleton_links import CompileSingletonLinks
from runners.compile.compile_struct_links import CompileStructLinks
from runners.compile.compile_typedef_links import CompileTypeDefLinks
from runners.make import Make
from runners.data_class import CompileLinkArgs
# endregion Imports


# region Logger
logger = None

# endregion Logger


# region Main
# region    Question Yes No
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    # https://tinyurl.com/yyg38fp2
    # https://tinyurl.com/y2pv2cdh
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write(
                "Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")
# endregion Question Yes No

# region    Main Testing


def _main():
    # ns = 'com.sun.star.form.component.DatabaseTextField'
    # ns = 'com.sun.star.form.component.RichTextControl'
    # ns = 'com.sun.star.form.FormController'
    # ns = 'com.sun.star.form.DataAwareControlModel'
    # ns = 'com.sun.star.text.TextRange'
    # args = 'data db-json -n com.sun.star.form.control.GridControl'
    url = 'https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1Paragraph.html'
    args = 'compile compile-batch -g'
    sys.argv.extend(args.split())
    main()


def _touch():
    global logger

    if logger is None:
        log_args = {
            "log_file": "debug.log",
            "level": logging.DEBUG
        }
        logger = get_logger(logger_name=Path(__file__).stem, **log_args)
    config = read_config('./config.json')
    t = TouchFiles(config=config, log=logger)
    t._touch_struct()
# endregion Main Testing

# region Logging


def _log_start_action() -> None:
    if len(sys.argv) > 1:
        logger.info('Executing command: %s', sys.argv[1:])
    else:
        logger.info('Running with no args.')


def _log_end_action() -> None:
    logger.info('Finished!')
# endregion Logging

# region parser
# region    Parser UTIL Methods
def args_remove_options(parser, options):
    # https://tinyurl.com/yagn2yvj
    for option in options:
        for action in parser._actions:
            if vars(action)['option_strings'][0] == option:
                parser._handle_conflict_resolve(None,[(option,action)])
                break
# endregion Parser UTIL Methods
# region    SET ARGS
# region        Create Parsers


def _create_parser(name: str) -> argparse.ArgumentParser:
    return argparse.ArgumentParser(description=name)

# endregion     Create Parsers
# region        Url Parsers


def _args_url_const(parser: argparse.ArgumentParser) -> None:
    url_parser_const.set_cmd_args(parser)

def _args_url_enum(parser: argparse.ArgumentParser) -> None:
    url_parser_enum.set_cmd_args(parser)

def _args_url_exception(parser: argparse.ArgumentParser) -> None:
    url_parser_ex.set_cmd_args(parser)

def _args_url_interface(parser: argparse.ArgumentParser) -> None:
    url_parser_interface.set_cmd_args(parser)

def _args_url_service(parser: argparse.ArgumentParser) -> None:
    url_parser_service.set_cmd_args(parser)

def _args_url_singleton(parser: argparse.ArgumentParser) -> None:
    url_parser_singleton.set_cmd_args(parser)

def _args_url_struct(parser: argparse.ArgumentParser) -> None:
    url_parser_struct.set_cmd_args(parser)

def _args_url_typedef(parser: argparse.ArgumentParser) -> None:
    url_parser_typedef.set_cmd_args(parser)




# endregion     Url Parsers
# region        Compile Links


def _args_links_general(parser: argparse.ArgumentParser, name: str) -> None:
    parser_group = parser.add_mutually_exclusive_group()
    parser_group.add_argument(
        '-a', '--all',
        help=f"Compile all {name} recursivly",
        action='store_true',
        dest='cmd_all',
        default=False
    )
    parser_group.add_argument(
        '-p', '--path',
        help='Compile a specific path',
        action='store',
        dest='path',
        type=str
    )
    parser.add_argument(
        '--data',
        help='Write to data folder',
        action='store_true',
        dest='write_data_dir',
        default=False)
    parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )

def _args_links_ex(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='exceptions')


def _args_links_enum(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='enums')


def _args_links_const(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='constants')


def _args_links_struct(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='struct')


def _args_links_interface(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='interface')


def _args_links_singleton(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='singleton')


def _args_links_service(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='service')


def _args_links_typedef(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='typedef')


def _args_links_batch(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '--data',
        help='Write to data folder',
        action='store_true',
        dest='write_data_dir',
        default=False)
    # grp = parser.add_mutually_exclusive_group()
    parser_group = parser.add_argument_group()
    parser_group.add_argument(
        '-a', '--all',
        help=f"Compile all groups recursivly",
        action='store_true',
        dest='cmd_all',
        default=False
    )
    opt_group = parser.add_argument_group()
    opt_group.add_argument(
        '-s', '--struct',
        help=f"Compile all struct recursivly",
        action='store_true',
        dest='all_struct',
        default=False
    )
    opt_group.add_argument(
        '-g', '--singleton',
        help=f"Compile all singleton recursivly",
        action='store_true',
        dest='all_singleton',
        default=False
    )
    opt_group.add_argument(
        '-r', '--service',
        help=f"Compile all service recursivly",
        action='store_true',
        dest='all_service',
        default=False
    )
    opt_group.add_argument(
        '-c', '--const',
        help=f"Compile all const recursivly",
        action='store_true',
        dest='all_const',
        default=False
    )
    opt_group.add_argument(
        '-e', '--enum',
        help=f"Compile all enum recursivly",
        action='store_true',
        dest='all_enum',
        default=False
    )
    opt_group.add_argument(
        '-x', '--exception',
        help=f"Compile all exception recursivly",
        action='store_true',
        dest='all_exception',
        default=False
    )
    opt_group.add_argument(
        '-i', '--interface',
        help=f"Compile all interface recursivly",
        action='store_true',
        dest='all_interface',
        default=False
    )
    opt_group.add_argument(
        '-t', '--typedef',
        help=f"Compile all typedef recursivly",
        action='store_true',
        dest='all_typedef',
        default=False
    )
    parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )
# endregion     Compile Links
# region        Touch Parser


def _args_touch(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-s', '--struct',
        help='Touch all struct files',
        action='store_true',
        dest='struct_all',
        default=False
    )
    parser.add_argument(
        '-g', '--singleton',
        help='Touch all singleton files',
        action='store_true',
        dest='singleton_all',
        default=False
    )
    parser.add_argument(
        '-r', '--service',
        help='Touch all service files',
        action='store_true',
        dest='service_all',
        default=False
    )
    parser.add_argument(
        '-c', '--const',
        help='Touch all const files',
        action='store_true',
        dest='const_all',
        default=False
    )
    parser.add_argument(
        '-e', '--enum',
        help='Touch all enum files',
        action='store_true',
        dest='enum_all',
        default=False
    )
    parser.add_argument(
        '-x', '--exception',
        help='Touch all enum files',
        action='store_true',
        dest='ex_all',
        default=False
    )
    parser.add_argument(
        '-i', '--interface',
        help='Touch all interface files',
        action='store_true',
        dest='interface_all',
        default=False
    )
    parser.add_argument(
        '-t', '--typedef',
        help='Touch all interface files',
        action='store_true',
        dest='typedef_all',
        default=False
    )
    parser.add_argument(
        '-p', '--python',
        help='Touch python files instead of template files',
        action='store_true',
        dest='python_files',
        default=False
    )
    parser.add_argument(
        '--cache-files',
        help='Touch cached files. Resets cache file expire times',
        action='store_true',
        dest='cache_files',
        default=False
    )
# endregion     Touch Parser

# region        Module Links Parser

def _args_module_links(parser: argparse.ArgumentParser) -> None:
    # usually run with: link-json mod-links --data -r -j -a

    parser.add_argument(
        '-a', '--all',
        help='Compile module_link json files',
        action='store_true',
        dest='mod_links_all',
        default=False
    )
    linkproc.set_cmd_args(parser)
    
    parser.add_argument(
        '--data',
        help='Write to data folder',
        action='store_true',
        dest='write_data_dir',
        default=False)
    args_remove_options(parser, ['-u', '--url'])

# endregion     Module Links Parser
# region        Star Links Parser


def _args_links_parser_url(parser: argparse.ArgumentParser) -> None:
    json_parser_star.set_cmd_args(parser)
# endregion     Star Linkes Parser
# region        Make Parser


def _args_make(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-f', '--force-compile',
        help='Force Compile of templates',
        action='store_true',
        dest='force_compile',
        default=False)
    parser.add_argument(
        '-c', '--clean-scratch',
        help='Wipes all files in scratch',
        action='store_true',
        dest='clean_scratch',
        default=False)
    parser.add_argument(
        '-p', '--processes',
        help='Number of Process to us for make.',
        action='store',
        dest='processes',
        type=int,
        default=4)
# endregion     Make Parser
# region        data args


def _args_data_init(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-i', '--init-db',
        help='Initialize database',
        action='store_true',
        dest='init_db',
        default=False
    )


def _args_data_url(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-u', '--url',
        help='Get url for a full namespace.',
        action='store',
        dest='ns_url',
        default=None
    )


def _args_data_component(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-n', '--namespace',
        help='Genereate component info for a given namespace wildcards %% and _ suporrted',
        action='store',
        dest='namespace',
        required=True
    )
    parser.add_argument(
        '-j', '--json',
        help='Output in json format',
        action='store_true',
        dest='as_json',
        default=False
    )

def _args_data_update(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-a', '--write-all',
        help='Write data from json files in database. Update/insert',
        action='store_true',
        dest='write_all',
        default=False
    )


def _args_data_json(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-n', '--namespace',
        help='Genereate Json for a given namespace',
        action='store',
        dest='namespace',
        default=None
    )


def _args_data_star(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-s', '--write-star',
        help='Write all Star import file into data directory',
        action='store_true',
        dest='write_star_ns',
        default=False
    )

def _args_data_rel(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-n', '--namespace',
        help='Full Namesapce. Genereate Relative info for a given namespace.',
        action='store',
        dest='namespace',
        required=True
    )
    parser.add_argument(
        '-r', '--relative',
        help="Short ns such as 'com.sun.star.text'. Relative Namespace",
        action='store',
        dest='rel',
        required=True
    )
    parser.add_argument(
        '-f', '--as-rel-from',
        help='Get as realitive from import strings',
        action='store_true',
        dest='ns_import_from',
        default=False
    )
    parser.add_argument(
        '-l', '--as-long',
        help='Get as realitive im',
        action='store_true',
        dest='ns_import_from_long',
        default=False
    )
    parser.add_argument(
        '-j', '--json',
        help='Output in json format',
        action='store_true',
        dest='as_json',
        default=False
    )
# region            Imports


def _args_data_imports(parser: argparse.ArgumentParser) -> None:
    data_group = parser.add_argument_group()
    # data_imports_group_rel = data_imports_group.add_argument_group()
    data_group.add_argument(
        '-n', '--namespace',
        help='Genereate Namespace Data for a given namespace object',
        action='store',
        dest='ns_import_name',
        default=None
    )
    data_group.add_argument(
        '-j', '--json',
        help='Output in json format',
        action='store_true',
        dest='as_json',
        default=False
    )
    data_group.add_argument(
        '-c', '--child',
        help='Process only direct children if namespace',
        action='store_true',
        dest='ns_import_child',
        default=False
    )
    data_group.add_argument(
        '-r', '--as-rel-from',
        help='Get as realitive from import strings',
        action='store_true',
        dest='ns_import_from',
        default=False
    )
    data_group.add_argument(
        '-l', '--as-long',
        help='Get as realitive im',
        action='store_true',
        dest='ns_import_from_long',
        default=False
    )
    exclusive_group = data_group.add_mutually_exclusive_group()
    exclusive_group.add_argument(
        '-t', '--typing',
        help='Only imports that require typing',
        action='store_true',
        dest='import_typing',
        default=False
    )
    exclusive_group.add_argument(
        '-f', '--no-typing',
        help='Only imports that do NOT require typing',
        action='store_true',
        dest='import_no_typing',
        default=False
    )


def _args_data_imports_child(parser: argparse.ArgumentParser) -> None:
    data_group = parser.add_argument_group()
    # data_imports_group_rel = data_imports_group.add_argument_group()
    data_group.add_argument(
        '-n', '--namespace',
        help='Genereate Namespace Data for a given namespace object',
        action='store',
        dest='namespace',
        default=None
    )
    data_group.add_argument(
        '-r', '--as-rel-from',
        help='Get as realitive from import strings',
        action='store_true',
        dest='ns_import_from',
        default=False
    )
    data_group.add_argument(
        '-l', '--as-long',
        help='Get as realitive im',
        action='store_true',
        dest='ns_import_from_long',
        default=False
    )
    data_group.add_argument(
        '-j', '--json',
        help='Output in json format',
        action='store_true',
        dest='as_json',
        default=False
    )


def _args_data_imports_extends_tree(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-n', '--namespace',
        help='Genereate Namespace Data for a given namespace object',
        action='store',
        dest='namespace',
        default=None
    )


def _args_data_imports_extends_flat(parser: argparse.ArgumentParser) -> None:
    data_group = parser.add_mutually_exclusive_group()
    parser.add_argument(
        '-n', '--namespace',
        help='Genereate flat unique namespace data for a given namespace object',
        action='store',
        dest='namespace',
        default=None
    )
    data_group.add_argument(
        '-i', '--flat-imports',
        help='Genereate imports if format of from ... import ... as ...',
        action='store_true',
        dest='ns_from_imports',
        default=False
    )
    data_group.add_argument(
        '-e', '--extends-short',
        help='Generates line of short extends such as: XTextRange, XInterface',
        action='store_true',
        dest='ns_extends_short',
        default=False
    )
    data_group.add_argument(
        '-x', '--extends-long',
        help='Generates line of short extends such as: text_x_text_range_i, uno_x_interface_i',
        action='store_true',
        dest='ns_extends_long',
        default=False
    )
    parser.add_argument(
        '-c', '--child',
        help='Process only direct children if namespace',
        action='store_true',
        dest='ns_child',
        default=False
    )
    parser.add_argument(
        '-j', '--json',
        help='Output in json format',
        action='store_true',
        dest='as_json',
        default=False
    )
# endregion         Imports
# endregion     data args
# region        General Args


def _args_general(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use',
        action='store',
        dest='log_file',
        type=str,
        default=None)
# endregion     General Args
# endregion SET ARGS

# region ARGS COMMANDS

# region    Args Helpers


def _get_compile_args(args: argparse.Namespace, config: AppConfig) -> CompileLinkArgs:
    path = getattr(args, 'path', None)
    cmd_line_process = getattr(args, 'cmd_line_process', True)
    c_args = CompileLinkArgs(
        config=config,
        path=path,
        use_sub_process=cmd_line_process,
        log=logger
    )
    return c_args
# endregion     Args Helpers
# region    Make


def _args_action_make(args: argparse.Namespace, config: AppConfig) -> None:
    _log_start_action()
    try:
        _ = Make(config=config, force_compile=args.force_compile,
                 clean=args.clean_scratch, processes=args.processes)
    except Exception as e:
        logger.error(e)
    _log_end_action()
# endregion Make
# region    Compile Links Command


def _args_action_compile_links(args: argparse.Namespace, compiler: Type[BaseCompile], config: AppConfig) -> None:
    _log_start_action()
    c_args = _get_compile_args(args=args, config=config)
    c_args.use_sub_process = args.cmd_line_process
    if args.write_data_dir:
        c_args.out_dir = config.data_dir
        c_args.write_template = False
        c_args.allow_known_json = False
    # if args.cmd_all or args.args.path:
    compiler(args=c_args)
    _log_end_action()


def _args_action_links_ex(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileExLinks, config)


def _args_action_links_enum(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileEnumLinks, config)


def _args_action_links_const(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileConstLinks, config)


def _args_action_links_struct(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileStructLinks, config)


def _args_action_links_interface(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileInterfaceLinks, config)


def _args_action_links_singleton(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileSingletonLinks, config)


def _args_action_links_service(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileServiceLinks, config)


def _args_action_links_typedef(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileTypeDefLinks, config)
    _log_start_action()


def _args_action_links_batch(args: argparse.Namespace, config: AppConfig) -> None:
    fn_map = {
        "exception": _args_action_links_ex,
        "enum": _args_action_links_enum,
        "const": _args_action_links_const,
        "struct": _args_action_links_struct,
        "interface": _args_action_links_interface,
        "singleton": _args_action_links_singleton,
        "service": _args_action_links_service,
        "typedef": _args_action_links_typedef
    }
    if args.cmd_all:
        for _, fn in fn_map.items():
            fn(args=args, config=config)
        return
    if args.all_struct:
        fn_map['struct'](args=args, config=config)
    if args.all_singleton:
        fn_map['singleton'](args=args, config=config)
    if args.all_service:
        fn_map['service'](args=args, config=config)
    if args.all_const:
        fn_map['const'](args=args, config=config)
    if args.all_enum:
        fn_map['enum'](args=args, config=config)
    if args.all_exception:
        fn_map['exception'](args=args, config=config)
    if args.all_interface:
        fn_map['interface'](args=args, config=config)
    if args.all_typedef:
        fn_map['typedef'](args=args, config=config)


def _args_process_compile_cmd_data(args: argparse.Namespace, config: AppConfig) -> None:
    if args.write_data_dir:
        args.write_path = config.data_dir
    if args.command_data == 'ex':
        _args_action_links_ex(args=args, config=config)
    elif args.command_data == 'enum':
        _args_action_links_enum(args=args, config=config)
    elif args.command_data == 'const':
        _args_action_links_const(args=args, config=config)
    elif args.command_data == 'struct':
        _args_action_links_struct(args=args, config=config)
    elif args.command_data == 'interface':
        _args_action_links_interface(args=args, config=config)
    elif args.command_data == 'singleton':
        _args_action_links_singleton(args=args, config=config)
    elif args.command_data == 'service':
        _args_action_links_service(args=args, config=config)
    elif args.command_data == 'typedef':
        _args_action_links_typedef(args=args, config=config)
    elif args.command_data == 'compile-batch':
        _args_action_links_batch(args=args, config=config)
# endregion Compile Links Command
# region    Touch


def _args_action_touch(args: argparse.Namespace, config: AppConfig) -> None:
    _log_start_action()
    TouchFiles(
        config=config,
        touch_struct=args.struct_all,
        touch_const=args.const_all,
        touch_enum=args.enum_all,
        touch_ex=args.ex_all,
        touch_interface=args.interface_all,
        touch_typedef=args.typedef_all,
        touch_singleton=args.singleton_all,
        touch_service=args.service_all,
        touch_py_files=args.python_files,
        touch_cache_files=args.cache_files
    )
    _log_end_action()
# endregion Touch

# region    data Command
# region        Init


def _args_action_db_init(args: argparse.Namespace, config: AppConfig) -> None:
    dbc = DatabaseControler(
        config=config,
        init_db=args.init_db
    )
    if args.init_db:
        if not query_yes_no(f"Are you sure you want initialize the database '{config.db_mod_info}'?", 'no'):
            return
    dbc.results()
# endregion     Init
# region        Update


def _args_action_db_update(args: argparse.Namespace, config: AppConfig) -> None:
    mlc = ModuleLinksControler(
        config=config,
        write_all=args.write_all
    )
    mcc = ComponentControler(
        config=config,
        write_all=args.write_all
    )
    if args.write_all or args.update_all:
        if not query_yes_no(f"Are you sure you want to read all json files and write data in database?", 'no'):
            return
    _ = mlc.results()
    _ = mcc.results()
# endregion     Update
# region        Namespace


def _args_action_db_extends_tree(args: argparse.Namespace, config: AppConfig) -> None:
    qc = NamespaceControler(
        config=config,
        ns_name=args.namespace
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


def _args_action_db_extends_flat(args: argparse.Namespace, config: AppConfig) -> None:
    if args.namespace:
        if args.ns_from_imports:
            qc = NamespaceControler(
                config=config,
                ns_flat_frm=args.namespace,
                b_child=args.ns_child,
                b_json=args.as_json
            )
        elif args.ns_extends_short:
            qc = NamespaceControler(
                config=config,
                extends_short=args.namespace,
                b_child=args.ns_child,
                b_json=args.as_json
            )
        elif args.ns_extends_long:
            qc = NamespaceControler(
                config=config,
                extends_long=args.namespace,
                b_child=args.ns_child,
                b_json=args.as_json
            )
        else:
            qc = NamespaceControler(
                config=config,
                ns_flat=args.namespace,
                b_child=args.ns_child,
                b_json=args.as_json
            )
        qc_result = qc.results()
        if qc_result:
            print(qc_result)


def _args_action_db_qry(args: argparse.Namespace, config: AppConfig) -> None:
    qc = NamespaceControler(
        config=config,
        ns_link=args.ns_url
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


def _args_action_db_imports(args: argparse.Namespace, config: AppConfig) -> None:
    require_typing = None
    if args.import_typing:
        require_typing = True
    elif args.import_no_typing:
        require_typing = False
    qc = NamespaceControler(
        config=config,
        ns_import=args.ns_import_name,
        b_child=args.ns_import_child,
        b_typing=require_typing,
        b_from=args.ns_import_from,
        b_from_long=args.ns_import_from_long,
        b_json=args.as_json
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


def _args_action_db_imports_typing_child(args: argparse.Namespace, config: AppConfig) -> None:
    qc = NamespaceControler(
        config=config,
        ns_import_typing_child=args.namespace,
        b_from=args.ns_import_from,
        b_from_long=args.ns_import_from_long,
        b_json=args.as_json
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


def _args_action_db_component(args: argparse.Namespace, config: AppConfig) -> None:
    qc = NamespaceControler(
        config=config,
        ns_commponent=args.namespace,
        b_json=args.as_json
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


def _args_action_db_rel(args: argparse.Namespace, config: AppConfig) -> None:
    qc = NamespaceControler(
        config=config,
        ns_rel=args.namespace,
        ns_rel_to=args.rel,
        b_from=args.ns_import_from,
        b_from_long=args.ns_import_from_long,
        b_json=args.as_json
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)
# endregion     Namespace
# region        Json


def _args_action_db_json(args: argparse.Namespace, config: AppConfig) -> None:
    qc = json_controler.JsonController(
        config=config,
        namespace=args.namespace
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)
# endregion     Json
# region        Star


def _args_action_db_star(args: argparse.Namespace, config: AppConfig) -> None:
    if args.write_star_ns:
        if not query_yes_no(f"Are you sure write all star namespace import files into {config.data_dir}?", 'no'):
            return
    qc = StarNsControler(
        config=config,
        logger=logger,
        write_star_ns=args.write_star_ns
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)
# endregion     Star

def _args_process_data_cmd_data(args: argparse.Namespace, config: AppConfig) -> None:
    if args.command_data == 'init':
        _args_action_db_init(args=args, config=config)
    elif args.command_data == 'update':
        _args_action_db_update(args=args, config=config)
    elif args.command_data == 'extends-tree':
        _args_action_db_extends_tree(args=args, config=config)
    elif args.command_data == 'extends-flat':
        _args_action_db_extends_flat(args=args, config=config)
    elif args.command_data == 'url':
        _args_action_db_qry(args=args, config=config)
    elif args.command_data == 'imports':
        _args_action_db_imports(args=args, config=config)
    elif args.command_data == 'imports-typing-child':
        _args_action_db_imports_typing_child(args=args, config=config)
    elif args.command_data == 'json':
        _args_action_db_json(args=args, config=config)
    elif args.command_data == 'component':
        _args_action_db_component(args=args, config=config)
    elif args.command_data == 'rel':
        _args_action_db_rel(args=args, config=config)
    elif args.command_data == 'star':
        _args_action_db_star(args=args, config=config)

# endregion data Command

# region    Link Json Command

def _args_action_module_links(args: argparse.Namespace, config: AppConfig) -> None:
    _log_start_action()
    if args.mod_links_all:
        # usually run with: link-json mod-links --data -r -j -a
        if not query_yes_no(f"Are you sure you want to rebuild all {config.module_links_file} files?", 'no'):
            return
        if args.write_data_dir:
            write_path = config.data_dir
        else:
            write_path = None
        parsed_args = linkproc.get_kwargs_from_args(args)
        parsed_args['write_path'] = write_path
        linkproc.parse(**parsed_args)
        return
    _log_end_action()

def _args_action_link_json_star_links(args: argparse.Namespace) -> None:
    d_args = json_parser_star.get_kwargs_from_args(args)
    json_parser_star.parse(**d_args)

def _args_process_link_json_cmd_data(args: argparse.Namespace, config: AppConfig) -> None:
    if args.command_data == 'mod-links':
        _args_action_module_links(args=args, config=config)
    elif args.command_data == 'star-links':
        _args_action_link_json_star_links(args=args)
# endregion Link Json Command

# region    Url Parsers

def _args_action_url_const(args: argparse.Namespace) -> None:
    d_args = url_parser_const.get_kwargs_from_args(args)
    url_parser_const.parse(**d_args)

def _args_action_url_enum(args: argparse.Namespace) -> None:
    d_args = url_parser_enum.get_kwargs_from_args(args)
    url_parser_enum.parse(**d_args)

def _args_action_url_exception(args: argparse.Namespace) -> None:
    d_args = url_parser_ex.get_kwargs_from_args(args)
    url_parser_ex.parse(**d_args)

def _args_action_url_interface(args: argparse.Namespace) -> None:
    d_args = url_parser_interface.get_kwargs_from_args(args)
    url_parser_interface.parse(**d_args)


def _args_action_url_service(args: argparse.Namespace) -> None:
    d_args = url_parser_service.get_kwargs_from_args(args)
    url_parser_service.parse(**d_args)


def _args_action_url_singleton(args: argparse.Namespace) -> None:
    d_args = url_parser_singleton.get_kwargs_from_args(args)
    url_parser_singleton.parse(**d_args)

def _args_action_url_struct(args: argparse.Namespace) -> None:
    d_args = url_parser_struct.get_kwargs_from_args(args)
    url_parser_struct.parse(**d_args)

def _args_action_url_typedef(args: argparse.Namespace) -> None:
    d_args = url_parser_typedef.get_kwargs_from_args(args)
    url_parser_typedef.parse(**d_args)

def _args_process_url_parser_cmd_data(args: argparse.Namespace) -> None:
    if args.command_data == 'const':
        _args_action_url_const(args=args)
    elif args.command_data == 'enum':
        _args_action_url_enum(args=args)
    elif args.command_data == 'exception':
        _args_action_url_exception(args=args)
    elif args.command_data == 'interface':
        _args_action_url_interface(args=args)
    elif args.command_data == 'service':
        _args_action_url_service(args=args)
    elif args.command_data == 'singleton':
        _args_action_url_singleton(args=args)
    elif args.command_data == 'struct':
        _args_action_url_struct(args=args)
    elif args.command_data == 'typedef':
        _args_action_url_typedef(args=args)
# endregion Url Parsers



def _args_process_cmd(args: argparse.Namespace, config: AppConfig) -> None:
    if args.command == 'make':
        _args_action_make(args=args, config=config)
    elif args.command == 'exception':
        _args_action_links_ex(args=args)
    elif args.command == 'enum':
        _args_action_links_enum(args=args)
    elif args.command == 'const':
        _args_action_links_const(args=args)
    elif args.command == 'struct':
        _args_action_links_struct(args=args)
    elif args.command == 'interface':
        _args_action_links_interface(args=args)
    elif args.command == 'singleton':
        _args_action_links_singleton(args=args)
    elif args.command == 'service':
        _args_action_links_service(args=args)
    elif args.command == 'typedef':
        _args_action_links_typedef(args=args)
    elif args.command == 'touch':
        _args_action_touch(args=args, config=config)
    elif args.command == 'link-json':
        _args_process_link_json_cmd_data(args=args, config=config)
    elif args.command == 'data':
        _args_process_data_cmd_data(args=args, config=config)
    elif args.command == 'compile':
        _args_process_compile_cmd_data(args=args, config=config)
    elif args.command == 'url-parse':
        _args_process_url_parser_cmd_data(args=args)

# endregion ARGS COMMANDS
# endregion parser


def main():
    global logger
    # region Config
    config = read_config('./config.json')
    os.environ['config_cache_dir'] = config.cache_dir
    os.environ['config_cache_duration'] = str(config.cache_duration)
    os.environ['project_root'] = str(Path(__file__).parent)
    os.environ['config_resource_dir'] = config.resource_dir
    os.environ['config_db_mod_info'] = config.db_mod_info
    # endregion Config

    # region create parsers
    parser = _create_parser('main')
    subparser = parser.add_subparsers(dest='command')
    # region    make
    make_parser = subparser.add_parser(name='make')
    # endregion make
    
    # region    compile
    compile_subparser = subparser.add_parser(name='compile')
    compile = compile_subparser.add_subparsers(dest='command_data')
    links_const_parser = compile.add_parser(name='const')
    links_enum_parser = compile.add_parser(name='enum')
    links_ex_parser = compile.add_parser(name='exception')
    links_interface_parser = compile.add_parser(name='interface')
    links_service_parser = compile.add_parser(name='service')
    links_singleton_parser = compile.add_parser(name='singleton')
    links_struct_parser = compile.add_parser(name='struct')
    links_typedef_parser = compile.add_parser(name='typedef')
    links_batch_parser = compile.add_parser(name='compile-batch')
    # endregion compile

    # region    url-parse
    url_parser_subparser = subparser.add_parser(name='url-parse')
    url_parser = url_parser_subparser.add_subparsers(dest='command_data')
    url_const = url_parser.add_parser(name='const')
    url_enum = url_parser.add_parser(name='enum')
    url_exception = url_parser.add_parser(name='exception')
    url_interface = url_parser.add_parser(name='interface')
    url_service = url_parser.add_parser(name='service')
    url_singleton = url_parser.add_parser(name='singleton')
    url_struct = url_parser.add_parser(name='struct')
    url_typedef = url_parser.add_parser(name='typedef')
    # endregion url-parse
    
    # region    touch
    touch = subparser.add_parser(name='touch')
    # endregion touch

    # region    link-json
    link_json_subparser = subparser.add_parser(name='link-json')
    link_json_parser = link_json_subparser.add_subparsers(dest='command_data')
    link_json_mod_links = link_json_parser.add_parser(name='mod-links')
    link_json_star_links = link_json_parser.add_parser(name='star-links')
    # endregion link-json

    # region    data
    data_subparser = subparser.add_parser(name='data')
    data = data_subparser.add_subparsers(dest='command_data')
    data_update = data.add_parser(name='update')
    data_init = data.add_parser(name='init')
    data_extends_flat = data.add_parser(name='extends-flat')
    data_extends_tree = data.add_parser(name='extends-tree')
    data_imports = data.add_parser(name='imports')
    data_imports_typing_child = data.add_parser(name='imports-typing-child')
    data_url = data.add_parser(name='url')
    data_json = data.add_parser(name='json')
    data_component = data.add_parser(name='component')
    data_rel = data.add_parser(name='rel')
    data_star = data.add_parser(name='star')
    # endregion data

    # endregion create parsers

    # region Set Args

    # region compile links args
    _args_links_const(parser=links_const_parser)
    _args_links_enum(parser=links_enum_parser)
    _args_links_ex(parser=links_ex_parser)
    _args_links_interface(parser=links_interface_parser)
    _args_links_service(parser=links_service_parser)
    _args_links_singleton(parser=links_singleton_parser)
    _args_links_struct(parser=links_struct_parser)
    _args_links_typedef(parser=links_typedef_parser)
    _args_links_batch(parser=links_batch_parser)
    # endregion compile links args

    # region url parser
    _args_url_const(parser=url_const)
    _args_url_enum(parser=url_enum)
    _args_url_exception(parser=url_exception)
    _args_url_interface(parser=url_interface)
    _args_url_service(parser=url_service)
    _args_url_singleton(parser=url_singleton)
    _args_url_struct(parser=url_struct)
    _args_url_typedef(parser=url_typedef)
    # endregion url parser

    # region Link Json args
    _args_module_links(parser=link_json_mod_links)
    _args_links_parser_url(parser=link_json_star_links)
    
    # endregion Link Json args

    # region Other Args
    _args_general(parser=parser)
    _args_touch(parser=touch)
    _args_make(parser=make_parser)
    # endregion Other Args

    # region data args
    _args_data_init(parser=data_init)
    _args_data_url(parser=data_url)
    _args_data_update(parser=data_update)
    _args_data_json(parser=data_json)
    _args_data_imports(parser=data_imports)
    _args_data_imports_child(parser=data_imports_typing_child)
    _args_data_imports_extends_tree(parser=data_extends_tree)
    _args_data_imports_extends_flat(parser=data_extends_flat)
    _args_data_component(parser=data_component)
    _args_data_rel(parser=data_rel)
    _args_data_star(parser=data_star)
    # endregion data args
    # endregion Set Args

    # region Read Args
    args = parser.parse_args()
    # endregion Read Args

    # region logger
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'app.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        logger = get_logger(logger_name=Path(__file__).stem, **log_args)
    # endregion logger

    _args_process_cmd(args=args, config=config)


if __name__ == '__main__':
    # _touch()
    main()

# endregion Main

#!/usr/bin/env python
"""
OOO_UNO_TMPL

Libre Office API to Python code generator.
Parses Libre Office API website and converts to Python classes and types.
Libre Office API consist of more than 4300 classes and types.


Requirements:
    see: docs/setup_env.rst


Getting Started:

    This project already has data compiled of the entire LO API.
    The file are compiled as *.JSON files, *.tmpl *.dyn, *.tpyi files in project root directory 'lo'.

    API file generation groups api into the following categories:
        const:      Constant classes
        enum:       Enumeration classes
        exception:  Error classes
        interface:  Interface abstract classes
        service:    Service abstract classes
        struct:     Structure classes
        typedef:    Type aliases

    Template files require compiling to generate python files.
    Compiling template files is done on the command line via the 'make' option.


Make Command:
    make does not require any arguments by default.
    running 'python -m app make' will build all templates that require building.
    
        *.tmpl, *.dyn and *.tpyi files that do not have corresponding *.py, *.dynpy and *.pyipy files respectively
        are included in make.
        
        *.tmpl, *.dyn and *.tpyi files that have a newer modification date then corresponding *.py, *.dynpy and *.pyipy
        files respectively are included in make.

    '$ python -m app make -h' will show help for make.
    make processes all template and json file in 'lo' directory recursively.
    make compiles any templates that have not yet been compiled.
    make takes care of generating inplace *.py, *.dynpy and *.pyipy files in lo sub directories
    make takes care of writing to ooobuild/lo and ooobuild/dyn directories and sub directories
    make writes the output python file for each template out to 'ooobuild'
        directory keeping the same directory structure.
    make by default will only compile templates that have been
        updated since compile was last run.
    make writes output to app.log in the project root directory.
    Compiled files are written in place.
        For Example: 'lo/uno/XInterface.tmpl' once compiled
            creates 'lo/uno/XInterface.py'.
    In place compiled files such as 'lo/uno/XInterface.py' are cheetah
        classes that are then written into that actual
        python representation of the tmpl file.
    On first run expect make to take some time to process as all templates must
        be compiled and written on first run.


Sequence of Build:
    star.json links are parsed to generate all module_links.json files.
    module_links.json files are parsed to obtain and write all component
        template files and json files.

    Templates rely on 'resources/mod_info.sqlite' database for build.
        When templates are regenerated with updated data then
        database should also be updated.


    star.json is the jumping off point for reading all api data.
    star.json is located at `resources/star.json'.
    star.json contains links to all modules of LO api.
    star.json file can be regenerated using link-json star-links
        command line options.

    A module_links.json file is created for each namespace.
    module_links.json files are written into every sub directory of 'lo'.
    module_links.json files can regenerated using link-json mod-links
        command line options.
        For instance: $ python -m app link-json mod-links --recursive --write-json --all
        Writes a module_links.json files recursively into the lo dir. Each dir represents a namespace of the LO API>


Compile Templates:
    Note:
        Before Compile is run database must be up to date.
        If a new version of LO API is being compiled then database will need to be regenerated.
        See Regeneration of Database.
        By default database does not need to be created/updated unless underlying
        template json data changes.
        
        By default all links are already compiled and the resulting *.json, *.tmpl, *.dyn, *.tpyi
        files are located in the lo dir.
    
    Compiling reads `module_links.json` files to get url's of components.
    Compiling then request url and parses html and converts in to template and json data
    that are written out to lo dir.
    Compiling all essentially parsers over 4300 urls.
        By default caching is built in so that given url is not parsed if it is in the cache.
        The cache dir is in the systems tmp dir.
            The name of the sub dir in tmp dir is set in config.json cache_dir property.
        The cache duration in seconds is set in config.json cache_duration property.
        Note that the system tmp dir is cleared on most os's when the system is rebooted.
    
    The compile option allow for some, many or all templates to be created or overwritten.
        The following command will compile all enum classes:
            $ python -m app compile enum --all
        
        The following command will compile all ( over 4300 ) classes:
            $ python -m app compile batch --all


Type of Templates:
    There are currently three types of templates outputted into lo dir, *.tmpl, *.dyn and *.tpyi.
    
    *.tmpl templates files are converted into corresponding *.py files and are written into
    ooobuild/lo sub directories
    
    *.dyn template files are converted into corresponding *.dynpy files and are written into
    ooobuild/dyn sub directories
    
    *.tpyi template files are converted into corresponding *.pyipy files and are written into
    ooobuild/star/_pyi sub directories
    
    By default *.tmpl *.dyn, *.tpyi files are just stubs that don't contain any actual data.
    The template files read from corresponding json files and converts data into actual LibreOffice classes as py files.


Touch Files:
    The touch command line option allows for setting of various files modification date to current system date and time.
    
    On advantage of touching files is it prevents the need to compile components again if the underlying data has not change.
        Essentially the underlying data will not change unless the LO api has changed.
    
    Touching files can be used to force make to include or exclude making of files.
        If tmpl files are touched then make will rebuild any *.tmpl file when run again.
        If dyn files are touched then make will rebuild any *.dyn file when run again.
        If tpyi files are touched then make will rebuild any *.tpyi file when run again.
        If py files are touched then make will exclude any corresponding *.tmpl template files.
        If dynpy files are touched then make will exclude any corresponding *.dyn template files.
        If pyipy files are touched then make will exclude any corresponding *.pyipy template files.

    Example:
        The following commands force make to rebuild all enum tmpl files:
            $ python -m app touch --enum --option tmpl
            $ python -m app make
    
    Touch can be used to reset cached data created by compile as well.
    To update all cached data in the system tmp sub dir run:
        $ python -m app touch --cache-files
        
        Note on cached files:
            Because cached files are stored in system temp dir the cached files will be deleted on reboot.
            If you need to restore after reboot then it is recommend to keep a zip file of the cached dir.
            The name of the dir in the system tmp dir is determined by the cache_dir option in config.json, Default is ooo_uno_tmpl.
            After reboot copy you zip file into system tmp dir and extract it.
            Next run the above touch command to reset the date of the cached files.
            If the entire api is cached then expect the cache dir to contain over 7500 files.


url-links:
    url-links allow the compiling of a single url. Sort of like compile with more options and
    only for a single url. Mostly use for testing and debugging.
    
    Note the url is expected to match the type of command.
    
    Example:
        The following command will compile template and write json data for XInterface into lo/uno dir.
            $ python -m app url-parse interface --write-template --write-json --url https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html


Modifying Templates:
    Code generation templates are found in the template directory.
    *.tmpl files are cheetah template files.
    Template files starting with _base_ can be modified.
    Changes to files starting with _base_ are automatically picked up on next
        command line make (python app.py make)
    Any modification to *.tmpl files in the template directory requires
        make to be run on the command line in the template directory.
        Eg: user@user-pc:~/Projects/ooo_uno_tmpl/template$ make


Output Other Namespaces:
    The make command outputs ooobuild/lo, ooobuild/dyn and ooobuild/star namespace and files.
    
    Outputting ooobuild/csslo:
        $ python -m app data star --css-lo
    
    Outputting ooobulid/cssdyn:
        $ python -m app data star --css-dyn
    
    Outputting ooobulid/star:
        $ python -m app data star --css-pyi

    Note:
        Other Namespaces requires resources/mod_info.sqlite' database.

Regeneration of Database:
    'resources/mod_info.sqlite' database is required for templates to build.
    Database must exist before make command line option is invoked.
    
    Database is built from various json files that are generated in 'ooodata' directory.
    1. Write all module_links.json into ooodata directory.
        This is done by running the following on the command line.
        $ python app.py link-json mod-links --data --all --recursive --write-json
        The --data flag instructs to write into data directory.
    2. Write all component json files into ooodata directory.
        This is done by running the following on the command line.
        python app.py compile batch --data --all
        The --data flag instructs app to write into ooodata directory.
        It is important to check Logs for ERROR after this command.
        There may be timeout or connections issues, etc,
        such as `('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))`
        For Connections issues run the command again, such as,
        python app.py compile batch --data -i
        The caching will kick in and only items not in the cache will be downloaded again.
    3. Created database if it does not exist.
        This is done by running the following on the command line.
        python app.py data init --init-db
        If database is already existing this command has no effect.
    4. Update database with 'ooodata/**/*.json' files.
        This is done by running the following on the command line.
        python app.py data update --write-all
        Command reads 'ooodata' folder and add/updates database.
        Any preexisting data in the database will be updated.


Other Notes:
    App Configuration:
        The config.json for app is located in src/cfg/config.json
    
    App Version:
        App version is set in src/__init__py
    
    Other Config:
        src/parsers/config directory contains special configuration files.
        
        known_extends.json:
            This file contains overrides for the extends of matching components.
            If a match is found in this file then the resulting output of json
            data of the parser will contain extends for the found match.

            There is a special use case as seen com.sun.star.uno.Exception.
                When extend ends in ._ it will be treated as a python extend.
                In short build.lo.uno.Exception extends Exception (builtins.Exception)

        known_json.json.
            This file contains matches to components that will use predetermined json
            output that is to be written into lo/**/*.json files.
            In short this means a matched file will ignore parsed html and use
            matched known instead.

            Note when parsers that participate have an option to ignore known_json.json.
            This option is used by app.py when writing data into data dir.
            The data dir is used to create/update database.
    
    The underlying parsers that convert html into json and template are located in 
    the src/parser directory.

Regeneration of a new LO API version.
    When a new version of the LO API is published it may have removed or added classes.
    For this reason new version must be generated from a clean slate.

    Cleaning before regeneration:
        Remove database.
            delete 'resources/mod_info.sqlite'
        Remove entire contents of ooobuild dir.
        Remove entire contents of ooodata dir except for ``ooobuild/star/__init__.py``
            Although there is a backup in ``resources/project/pyi_files/__init__.py``
        Remove entire contents of lo dir.
        Make sure cache_dir (set in config) is removed from system tmp dir.
            Defaults to "ooo_uno_tmpl"
            EG: $ rm -rf /tmp/ooo_uno_tmpl

    Regeneration steps:
        1. Set config to new version of LO API.
            config.json is found in src/cfg/
            config property is libre_office_ver
        2. Clean as shown in previous step.
        3. Generate generate module_links.json into ooodata.
            $ python app.py link-json mod-links --data --all --recursive --write-json
        4. Generate generate json ooodata.
            $ python -m app compile batch --all --data
            This will parse the entire LO API:
                Cache will be created in system tmp dir.
                Json data will be written into ooodata and sub directories.
                each json file represents a class.

                It is important to check Logs for ERROR after this command.
                There may be timeout or connections issues, etc,
                such as `('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))`
                For Connections issues run the command again, such as,
                python app.py compile batch --data -i
                The caching will kick in and only items not in the cache will be downloaded again.
        5. Generate database.
            $ python -m app data init --init-db
        6. Write data into database.
            $ python -m app data update --write-all
            This command read the json data in ooodata and writes data into database.
        7. Generate all module_link.json file into lo dir.
            $ python -m app link-json mod-links --recursive --write-json --all
            This creates a module_link.json file for each module in lo dir.
        8. Write all templates and template json data into lo dir.
            $ python -m app compile batch --all
        8. Generate python output.
            $ python -m app make
            This will generate all the python file from template in the lo dir.
            The output will is written into ooobuild dir.
        9. Generate csslo namespace and python files.
            $ python -m app data star --css-lo
        10. Generate cssdyn namespace and python files.
            $ python -m app data star --css-dyn
        11. Old: Generate star sub namespaces and python files.
            This was done in older version that wrote typings into ``star/_pyi/``.
            The config.json properties still allow for this but are not used by default.
            The config properties that control this are ``pyi_dir``, ``pyi_write_imports_in_init`` and ``pyi_write_star_dir_old_style``.
            Also Note: The template for enum pyi files is currently set to use the new protocol style.

            The command to generate star sub namespaces and python files is:
            $ python -m app data star --css-pyi
"""

# region Imports
import logging
import os
import sys
import argparse
from typing import Type
from pathlib import Path

from src.cfg.config import AppConfig
from src.cmds import uno_lnk
from src.data_manage.controller import json_controler
from src.data_manage.controller.component_controler import ComponentControler
from src.data_manage.controller.database_controler import DatabaseControler
from src.data_manage.controller.module_links_controler import ModuleLinksControler
from src.data_manage.controller.namespace_controler import NamespaceControler
from src.data_manage.controller.star_ns_controller import StarNsControler
from src.logger.log_handle import get_logger
from src.parser import (
    const as url_parser_const,
    enm as url_parser_enum,
    ex as url_parser_ex,
    xsrc as url_parser_interface,
    service as url_parser_service,
    singleton as url_parser_singleton,
    struc as url_parser_struct,
    typedef as url_parser_typedef,
    star as json_parser_star,
)
from src.parser.json_parser import linkproc
from src.runners.compile.base_compile import BaseCompile
from src.runners.compile.compile_const_links import CompileConstLinks
from src.runners.compile.compile_enum_links import CompileEnumLinks
from src.runners.compile.compile_ex_lniks import CompileExLinks
from src.runners.compile.compile_interface_links import CompileInterfaceLinks
from src.runners.compile.compile_service_links import CompileServiceLinks
from src.runners.compile.compile_singleton_links import CompileSingletonLinks
from src.runners.compile.compile_struct_links import CompileStructLinks
from src.runners.compile.compile_typedef_links import CompileTypeDefLinks
from src.runners.data_class import CompileLinkArgs
from src.runners.make import Make
from src.runners.touch_files import TouchFiles
from src.utilities import util as mutil

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
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


# endregion Question Yes No

# region    Main Testing


def _main():
    # ns = 'com.sun.star.form.component.DatabaseTextField'
    # ns = 'com.sun.star.form.component.RichTextControl'
    # ns = 'com.sun.star.form.FormController'
    # ns = 'com.sun.star.form.DataAwareControlModel'
    # ns = 'com.sun.star.text.TextRange'
    # args = 'data db-json -n com.sun.star.form.control.GridControl'
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1SubIncrement.html'
    url = "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1Settings.html"
    args = "url-parse service -t -u "
    args += url
    sys.argv.extend(args.split())
    main()


# endregion Main Testing

# region Logging


def _log_start_action() -> None:
    if len(sys.argv) > 1:
        logger.info("Executing command: %s", sys.argv[1:])
    else:
        logger.info("Running with no args.")


def _log_end_action() -> None:
    logger.info("Finished!")


# endregion Logging

# region parser
# region    Parser UTIL Methods
def args_remove_options(parser, options):
    # https://tinyurl.com/yagn2yvj
    for option in options:
        for action in parser._actions:
            if vars(action)["option_strings"][0] == option:
                parser._handle_conflict_resolve(None, [(option, action)])
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
        "-a", "--all", help=f"Compile all {name} recursivly", action="store_true", dest="cmd_all", default=False
    )
    parser_group.add_argument("-p", "--path", help="Compile a specific path", action="store", dest="path", type=str)
    parser.add_argument(
        "--data", help="Write to data folder", action="store_true", dest="write_data_dir", default=False
    )
    # parser.add_argument(
    #     '-u', '--run-as-cmdline',
    #     help='Run as command line suprocess. Default False',
    #     action='store_true',
    #     dest='cmd_line_process',
    #     default=False
    # )


def _args_links_ex(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name="exceptions")


def _args_links_enum(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name="enums")


def _args_links_const(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name="constants")


def _args_links_struct(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name="struct")


def _args_links_interface(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name="interface")


def _args_links_singleton(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name="singleton")


def _args_links_service(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name="service")


def _args_links_typedef(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name="typedef")


def _args_links_batch(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--data", help="Write to data folder", action="store_true", dest="write_data_dir", default=False
    )
    # grp = parser.add_mutually_exclusive_group()
    parser_group = parser.add_argument_group()
    parser_group.add_argument(
        "-a", "--all", help=f"Compile all groups recursivly", action="store_true", dest="cmd_all", default=False
    )
    opt_group = parser.add_argument_group()
    opt_group.add_argument(
        "-s", "--struct", help=f"Compile all struct recursivly", action="store_true", dest="all_struct", default=False
    )
    opt_group.add_argument(
        "-g",
        "--singleton",
        help=f"Compile all singleton recursivly",
        action="store_true",
        dest="all_singleton",
        default=False,
    )
    opt_group.add_argument(
        "-r",
        "--service",
        help=f"Compile all service recursivly",
        action="store_true",
        dest="all_service",
        default=False,
    )
    opt_group.add_argument(
        "-c", "--const", help=f"Compile all const recursivly", action="store_true", dest="all_const", default=False
    )
    opt_group.add_argument(
        "-e", "--enum", help=f"Compile all enum recursivly", action="store_true", dest="all_enum", default=False
    )
    opt_group.add_argument(
        "-x",
        "--exception",
        help=f"Compile all exception recursivly",
        action="store_true",
        dest="all_exception",
        default=False,
    )
    opt_group.add_argument(
        "-i",
        "--interface",
        help=f"Compile all interface recursivly",
        action="store_true",
        dest="all_interface",
        default=False,
    )
    opt_group.add_argument(
        "-t",
        "--typedef",
        help=f"Compile all typedef recursivly",
        action="store_true",
        dest="all_typedef",
        default=False,
    )
    # parser.add_argument(
    #     '-u', '--run-as-cmdline',
    #     help='Run as command line suprocess. Default False',
    #     action='store_true',
    #     dest='cmd_line_process',
    #     default=False
    # )


# endregion     Compile Links
# region        Touch Parser


def _args_touch(parser: argparse.ArgumentParser, config: AppConfig) -> None:
    parser.add_argument(
        "-s",
        "--struct",
        help=f"Touch all struct files in {config.uno_obj_dir} direcotry recursivly.",
        action="store_true",
        dest="struct_all",
        default=False,
    )
    parser.add_argument(
        "-g",
        "--singleton",
        help=f"Touch all singleton files in {config.uno_obj_dir} direcotry recursivly.",
        action="store_true",
        dest="singleton_all",
        default=False,
    )
    parser.add_argument(
        "-r",
        "--service",
        help=f"Touch all service files in {config.uno_obj_dir} direcotry recursivly.",
        action="store_true",
        dest="service_all",
        default=False,
    )
    parser.add_argument(
        "-c",
        "--const",
        help=f"Touch all const files in {config.uno_obj_dir} direcotry recursivly.",
        action="store_true",
        dest="const_all",
        default=False,
    )
    parser.add_argument(
        "-e",
        "--enum",
        help=f"Touch all enum files in {config.uno_obj_dir} direcotry recursivly.",
        action="store_true",
        dest="enum_all",
        default=False,
    )
    parser.add_argument(
        "-x",
        "--exception",
        help=f"Touch all exception files in {config.uno_obj_dir} direcotry recursivly.",
        action="store_true",
        dest="ex_all",
        default=False,
    )
    parser.add_argument(
        "-i",
        "--interface",
        help=f"Touch all interface files in {config.uno_obj_dir} direcotry recursivly.",
        action="store_true",
        dest="interface_all",
        default=False,
    )
    parser.add_argument(
        "-t",
        "--typedef",
        help=f"Touch all typedef files in {config.uno_obj_dir} direcotry recursivly.",
        action="store_true",
        dest="typedef_all",
        default=False,
    )
    touch_help = f"touch *.py, *tmpl, *{config.template_dyn_ext}, *{config.template_dyn_py_ext}, *{config.template_pyi_ext}, *{config.template_pyi_py_ext}, files (default: %(default)s)"
    parser.add_argument(
        "-o",
        "--option",
        default="tmpl",
        const="tmpl",
        nargs="?",
        choices=["py", "dyn", "dynpy", "tmpl", "tpyi", "pyipy"],
        help=touch_help,
    )
    parser.add_argument(
        "--cache-files",
        help="Touch cached files in the system tmp dir and resets cache file expire times.",
        action="store_true",
        dest="cache_files",
        default=False,
    )


# endregion     Touch Parser

# region        Module Links Parser


def _args_module_links(parser: argparse.ArgumentParser) -> None:
    # usually run with: link-json mod-links --data -r -j -a

    parser.add_argument(
        "-a", "--all", help="Compile module_link json files", action="store_true", dest="mod_links_all", default=False
    )
    linkproc.set_cmd_args(parser)

    parser.add_argument(
        "--data", help="Write to data folder", action="store_true", dest="write_data_dir", default=False
    )
    args_remove_options(parser, ["-u", "--url"])


# endregion     Module Links Parser
# region        Star Links Parser


def _args_links_parser_url(parser: argparse.ArgumentParser) -> None:
    json_parser_star.set_cmd_args(parser)


# endregion     Star Linkes Parser
# region        Make Parser


def _args_make(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-f",
        "--force-compile",
        help="Force Compile of templates",
        action="store_true",
        dest="force_compile",
        default=False,
    )
    # parser.add_argument(
    #     '-c', '--clean-scratch',
    #     help='Wipes all files in scratch',
    #     action='store_true',
    #     dest='clean_scratch',
    #     default=False)
    parser.add_argument(
        "-p",
        "--processes",
        help="Number of Process to us for make.",
        action="store",
        dest="processes",
        type=int,
        default=4,
    )


# endregion     Make Parser
# region        data args


def _args_data_init(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-i", "--init-db", help="Initialize database", action="store_true", dest="init_db", default=False
    )


def _args_data_url(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-n", "--namespace", help="Get url for a full namespace.", action="store", dest="ns_url", default=None
    )


def _args_data_component(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-n",
        "--namespace",
        help="Genereate component info for a given namespace wildcards %% and _ suporrted",
        action="store",
        dest="namespace",
        required=True,
    )
    parser.add_argument(
        "-j", "--json", help="Output in json format", action="store_true", dest="as_json", default=False
    )


def _args_data_update(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-a",
        "--write-all",
        help="Write data from json files in database. Update/insert",
        action="store_true",
        dest="write_all",
        default=False,
    )


def _args_data_json(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-n",
        "--namespace",
        help="Generate Json for a given namespace, ignores direct extends and uses child flattened extends but includes original extends methods and properties.",
        action="store",
        dest="namespace",
        default=None,
    )


def _args_data_star(parser: argparse.ArgumentParser, config: AppConfig) -> None:
    opt_group = parser.add_mutually_exclusive_group()
    css_dir_lo = config.build_dir + os.sep + os.sep.join(config.com_sun_star_lo)
    css_dir_dyn = config.build_dir + os.sep + os.sep.join(config.com_sun_star_dyn)
    css_dir_pyi = config.build_dir + os.sep + os.sep.join(config.com_sun_star_pyi)
    opt_group.add_argument(
        "-l",
        "--css-lo",
        help=f"Writes imports for all '{config.build_dir}/{config.uno_obj_dir}' files into  {css_dir_lo}... __init__.py files.",
        action="store_true",
        dest="write_lo",
        default=False,
        required=False,
    )
    opt_group.add_argument(
        "-d",
        "--css-dyn",
        help=f"Writes imports for all '{config.build_dir}/{config.dyn_dir}' files into  {css_dir_dyn}... __init__.py files.",
        action="store_true",
        dest="write_dyn",
        default=False,
        required=False,
    )
    star_group = parser.add_argument_group()
    star_group.add_argument(
        "-i",
        "--css-pyi",
        help=f"Writes imports for all '{config.build_dir}/{os.sep.join(config.pyi_dir)}' files into  {css_dir_pyi}... __init__.pyi files.",
        action="store_true",
        dest="write_pyi",
        default=False,
        required=False,
    )
    star_group.add_argument(
        "-w",
        "--no-write-init",
        help=f"Writes star/__init__.py",
        action="store_false",
        dest="write_star_init",
        default=True,
        required=False,
    )
    parser.add_argument(
        "-r", "--no-rel-import", help=f"No relative import", action="store_false", dest="rel_import", default=True
    )


def _args_data_rel(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-n",
        "--namespace",
        help="Full Namesapce. Genereate Relative info for a given namespace.",
        action="store",
        dest="namespace",
        required=True,
    )
    parser.add_argument(
        "-r",
        "--relative",
        help="Short ns such as 'com.sun.star.text'. Relative Namespace",
        action="store",
        dest="rel",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--as-rel-from",
        help="Get as realitive from import strings",
        action="store_true",
        dest="ns_import_from",
        default=False,
    )
    parser.add_argument(
        "-l", "--as-long", help="Get as realitive im", action="store_true", dest="ns_import_from_long", default=False
    )
    parser.add_argument(
        "-j", "--json", help="Output in json format", action="store_true", dest="as_json", default=False
    )


# region            Imports


def _args_data_imports(parser: argparse.ArgumentParser) -> None:
    data_group = parser.add_argument_group()
    # data_imports_group_rel = data_imports_group.add_argument_group()
    data_group.add_argument(
        "-n",
        "--namespace",
        help="Genereate Namespace Data for a given namespace object",
        action="store",
        dest="ns_import_name",
        default=None,
    )
    data_group.add_argument(
        "-j", "--json", help="Output in json format", action="store_true", dest="as_json", default=False
    )
    data_group.add_argument(
        "-c",
        "--child",
        help="Process only direct children if namespace",
        action="store_true",
        dest="ns_import_child",
        default=False,
    )
    data_group.add_argument(
        "-r",
        "--as-rel-from",
        help="Get as realitive from import strings",
        action="store_true",
        dest="ns_import_from",
        default=False,
    )
    data_group.add_argument(
        "-l", "--as-long", help="Get as realitive im", action="store_true", dest="ns_import_from_long", default=False
    )
    exclusive_group = data_group.add_mutually_exclusive_group()
    exclusive_group.add_argument(
        "-t",
        "--typing",
        help="Only imports that require typing",
        action="store_true",
        dest="import_typing",
        default=False,
    )
    exclusive_group.add_argument(
        "-f",
        "--no-typing",
        help="Only imports that do NOT require typing",
        action="store_true",
        dest="import_no_typing",
        default=False,
    )


def _args_data_imports_child(parser: argparse.ArgumentParser) -> None:
    data_group = parser.add_argument_group()
    # data_imports_group_rel = data_imports_group.add_argument_group()
    data_group.add_argument(
        "-n",
        "--namespace",
        help="Genereate Namespace Data for a given namespace object",
        action="store",
        dest="namespace",
        default=None,
    )
    data_group.add_argument(
        "-r",
        "--as-rel-from",
        help="Get as realitive from import strings",
        action="store_true",
        dest="ns_import_from",
        default=False,
    )
    data_group.add_argument(
        "-l", "--as-long", help="Get as realitive im", action="store_true", dest="ns_import_from_long", default=False
    )
    data_group.add_argument(
        "-j", "--json", help="Output in json format", action="store_true", dest="as_json", default=False
    )


def _args_data_imports_extends_tree(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-n",
        "--namespace",
        help="Genereate Namespace Data for a given namespace object",
        action="store",
        dest="namespace",
        default=None,
    )


def _args_data_imports_extends_flat(parser: argparse.ArgumentParser) -> None:
    data_group = parser.add_mutually_exclusive_group()
    parser.add_argument(
        "-n",
        "--namespace",
        help="Genereate flat unique namespace data for a given namespace object",
        action="store",
        dest="namespace",
        default=None,
    )
    data_group.add_argument(
        "-i",
        "--flat-imports",
        help="Genereate imports if format of from ... import ... as ...",
        action="store_true",
        dest="ns_from_imports",
        default=False,
    )
    data_group.add_argument(
        "-e",
        "--extends-short",
        help="Generates line of short extends such as: XTextRange, XInterface",
        action="store_true",
        dest="ns_extends_short",
        default=False,
    )
    data_group.add_argument(
        "-x",
        "--extends-long",
        help="Generates line of short extends such as: text_x_text_range_i, uno_x_interface_i",
        action="store_true",
        dest="ns_extends_long",
        default=False,
    )
    parser.add_argument(
        "-c",
        "--child",
        help="Process only direct children if namespace",
        action="store_true",
        dest="ns_child",
        default=False,
    )
    parser.add_argument(
        "-j", "--json", help="Output in json format", action="store_true", dest="as_json", default=False
    )


# endregion         Imports
# endregion     data args
# region        General Args


def _args_general(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("-v", "--verbose", help="verbose logging", action="store_true", dest="verbose", default=False)
    parser.add_argument(
        "-L", "--log-file", help="Log file to use", action="store", dest="log_file", type=str, default=None
    )


# endregion     General Args

# region        cmd link
def _args_cmd_link(parser: argparse.ArgumentParser) -> None:
    add_grp = parser.add_argument_group()
    add_grp.add_argument(
        "-a",
        "--add",
        help="Add uno links to virtual environment.",
        action="store_true",
        dest="add",
        default=False,
    )

    add_grp.add_argument(
        "-s",
        "--uno-src",
        help="Optional source directory that contains uno.py and unohelper.py. If ommited then defaults are used.",
        action="store",
        dest="src_dir",
        default=None,
    )
    parser.add_argument(
        "-r",
        "--remove",
        help="Remove uno links to virtual environment.",
        action="store_true",
        dest="remove",
        default=False,
    )


# endregion     cmd link
# endregion SET ARGS

# region ARGS COMMANDS

# region    Args Helpers


def _get_compile_args(args: argparse.Namespace, config: AppConfig) -> CompileLinkArgs:
    path = getattr(args, "path", None)
    # cmd_line_process = getattr(args, 'cmd_line_process', True)
    c_args = CompileLinkArgs(config=config, path=path, use_sub_process=False, log=logger)
    return c_args


# endregion     Args Helpers
# region    Make


def _args_action_make(args: argparse.Namespace, config: AppConfig) -> None:
    _log_start_action()
    try:
        _ = Make(config=config, log=logger, force_compile=args.force_compile, clean=False, processes=args.processes)
    except Exception as e:
        logger.error(e)
    _log_end_action()


# endregion Make
# region    Compile Links Command


def _args_action_compile_links(args: argparse.Namespace, compiler: Type[BaseCompile], config: AppConfig) -> None:
    _log_start_action()
    c_args = _get_compile_args(args=args, config=config)
    c_args.use_sub_process = False  # args.cmd_line_process
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
        "typedef": _args_action_links_typedef,
    }
    if args.cmd_all:
        for _, fn in fn_map.items():
            fn(args=args, config=config)
        return
    if args.all_struct:
        fn_map["struct"](args=args, config=config)
    if args.all_singleton:
        fn_map["singleton"](args=args, config=config)
    if args.all_service:
        fn_map["service"](args=args, config=config)
    if args.all_const:
        fn_map["const"](args=args, config=config)
    if args.all_enum:
        fn_map["enum"](args=args, config=config)
    if args.all_exception:
        fn_map["exception"](args=args, config=config)
    if args.all_interface:
        fn_map["interface"](args=args, config=config)
    if args.all_typedef:
        fn_map["typedef"](args=args, config=config)


def _args_process_compile_cmd_data(args: argparse.Namespace, config: AppConfig) -> None:
    if args.write_data_dir:
        args.write_path = config.data_dir
    if args.command_data == "exception":
        _args_action_links_ex(args=args, config=config)
    elif args.command_data == "enum":
        _args_action_links_enum(args=args, config=config)
    elif args.command_data == "const":
        _args_action_links_const(args=args, config=config)
    elif args.command_data == "struct":
        _args_action_links_struct(args=args, config=config)
    elif args.command_data == "interface":
        _args_action_links_interface(args=args, config=config)
    elif args.command_data == "singleton":
        _args_action_links_singleton(args=args, config=config)
    elif args.command_data == "service":
        _args_action_links_service(args=args, config=config)
    elif args.command_data == "typedef":
        _args_action_links_typedef(args=args, config=config)
    elif args.command_data == "batch":
        _args_action_links_batch(args=args, config=config)


# endregion Compile Links Command
# region    Touch


def _args_action_touch(args: argparse.Namespace, config: AppConfig) -> None:
    touch_py_files = False
    touch_dyn_files = False
    touch_dyn_py_files = False
    touch_pyi_files = False
    touch_pyi_py_files = False
    if args.option == "dyn":
        touch_dyn_files = True
    elif args.option == "dynpy":
        touch_dyn_py_files = True
    elif args.option == "py":
        touch_dyn_files = True
    elif args.option == "tpyi":
        touch_pyi_files = True
    elif args.option == "pyipy":
        touch_pyi_py_files = True

    _log_start_action()

    TouchFiles(
        config=config,
        log=logger,
        touch_struct=args.struct_all,
        touch_const=args.const_all,
        touch_enum=args.enum_all,
        touch_ex=args.ex_all,
        touch_interface=args.interface_all,
        touch_typedef=args.typedef_all,
        touch_singleton=args.singleton_all,
        touch_service=args.service_all,
        touch_py_files=touch_py_files,
        touch_dyn_files=touch_dyn_files,
        touch_dyn_py_files=touch_dyn_py_files,
        touch_pyi_files=touch_pyi_files,
        touch_pyi_py_files=touch_pyi_py_files,
        touch_cache_files=args.cache_files,
    )
    _log_end_action()


# endregion Touch

# region    data Command
# region        Init


def _args_action_db_init(args: argparse.Namespace, config: AppConfig) -> None:
    dbc = DatabaseControler(config=config, init_db=args.init_db)
    if args.init_db:
        if not query_yes_no(f"Are you sure you want initialize the database '{config.db_mod_info}'?", "no"):
            return
    dbc.results()


# endregion     Init
# region        Update


def _args_action_db_update(args: argparse.Namespace, config: AppConfig) -> None:
    mlc = ModuleLinksControler(config=config, write_all=args.write_all)
    mcc = ComponentControler(config=config, write_all=args.write_all)
    if args.write_all or args.update_all:
        if not query_yes_no(f"Are you sure you want to read all json files and write data in database?", "no"):
            return
    _ = mlc.results()
    _ = mcc.results()


# endregion     Update
# region        Namespace


def _args_action_db_extends_tree(args: argparse.Namespace, config: AppConfig) -> None:
    qc = NamespaceControler(config=config, ns_name=args.namespace)
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


def _args_action_db_extends_flat(args: argparse.Namespace, config: AppConfig) -> None:
    if args.namespace:
        if args.ns_from_imports:
            qc = NamespaceControler(
                config=config, ns_flat_frm=args.namespace, b_child=args.ns_child, b_json=args.as_json
            )
        elif args.ns_extends_short:
            qc = NamespaceControler(
                config=config, extends_short=args.namespace, b_child=args.ns_child, b_json=args.as_json
            )
        elif args.ns_extends_long:
            qc = NamespaceControler(
                config=config, extends_long=args.namespace, b_child=args.ns_child, b_json=args.as_json
            )
        else:
            qc = NamespaceControler(config=config, ns_flat=args.namespace, b_child=args.ns_child, b_json=args.as_json)
        qc_result = qc.results()
        if qc_result:
            print(qc_result)


def _args_action_db_qry(args: argparse.Namespace, config: AppConfig) -> None:
    qc = NamespaceControler(config=config, ns_link=args.ns_url)
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
        b_json=args.as_json,
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
        b_json=args.as_json,
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


def _args_action_db_component(args: argparse.Namespace, config: AppConfig) -> None:
    qc = NamespaceControler(config=config, ns_commponent=args.namespace, b_json=args.as_json)
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
        b_json=args.as_json,
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


# endregion     Namespace
# region        Json


def _args_action_db_json(args: argparse.Namespace, config: AppConfig) -> None:
    qc = json_controler.JsonController(config=config, namespace=args.namespace)
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


# endregion     Json
# region        Star


def _args_action_db_star(args: argparse.Namespace, config: AppConfig) -> None:
    if args.write_lo or args.write_dyn or args.write_pyi:
        if not query_yes_no(f"Are you sure write all star namespace import files into {config.data_dir}?", "no"):
            return
    qc = StarNsControler(
        config=config,
        logger=logger,
        write_lo=args.write_lo,
        write_dyn=args.write_dyn,
        write_pyi=args.write_pyi,
        rel_import=args.rel_import,
        write_pyi_star_init=args.write_star_init,
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


# endregion     Star


def _args_process_data_cmd_data(args: argparse.Namespace, config: AppConfig) -> None:
    if args.command_data == "init":
        _args_action_db_init(args=args, config=config)
    elif args.command_data == "update":
        _args_action_db_update(args=args, config=config)
    elif args.command_data == "extends-tree":
        _args_action_db_extends_tree(args=args, config=config)
    elif args.command_data == "extends-flat":
        _args_action_db_extends_flat(args=args, config=config)
    elif args.command_data == "url":
        _args_action_db_qry(args=args, config=config)
    elif args.command_data == "imports":
        _args_action_db_imports(args=args, config=config)
    elif args.command_data == "imports-typing-child":
        _args_action_db_imports_typing_child(args=args, config=config)
    elif args.command_data == "json":
        _args_action_db_json(args=args, config=config)
    elif args.command_data == "component":
        _args_action_db_component(args=args, config=config)
    elif args.command_data == "rel":
        _args_action_db_rel(args=args, config=config)
    elif args.command_data == "star":
        _args_action_db_star(args=args, config=config)


# endregion data Command

# region    Link Json Command


def _args_action_module_links(args: argparse.Namespace, config: AppConfig) -> None:
    _log_start_action()
    if args.mod_links_all:
        # usually run with: link-json mod-links --data -r -j -a
        if not query_yes_no(f"Are you sure you want to rebuild all {config.module_links_file} files?", "no"):
            return
        if args.write_data_dir:
            write_path = config.data_dir
        else:
            write_path = None
        parsed_args = linkproc.get_kwargs_from_args(args)
        parsed_args["write_path"] = write_path
        linkproc.parse(**parsed_args)
        return
    _log_end_action()


def _args_action_link_json_star_links(args: argparse.Namespace) -> None:
    d_args = json_parser_star.get_kwargs_from_args(args)
    json_parser_star.parse(**d_args)


def _args_process_link_json_cmd_data(args: argparse.Namespace, config: AppConfig) -> None:
    if args.command_data == "mod-links":
        _args_action_module_links(args=args, config=config)
    elif args.command_data == "star-links":
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
    if args.command_data == "const":
        _args_action_url_const(args=args)
    elif args.command_data == "enum":
        _args_action_url_enum(args=args)
    elif args.command_data == "exception":
        _args_action_url_exception(args=args)
    elif args.command_data == "interface":
        _args_action_url_interface(args=args)
    elif args.command_data == "service":
        _args_action_url_service(args=args)
    elif args.command_data == "singleton":
        _args_action_url_singleton(args=args)
    elif args.command_data == "struct":
        _args_action_url_struct(args=args)
    elif args.command_data == "typedef":
        _args_action_url_typedef(args=args)


# endregion Url Parsers


def _args_action_cmd_link(args: argparse.Namespace) -> None:
    if not (args.add or args.remove):
        raise Exception("No action requested, add --add or --remove")
    if args.add:
        uno_lnk.add_links(args.src_dir)
    elif args.remove:
        uno_lnk.remove_links()


def _args_process_cmd(args: argparse.Namespace, config: AppConfig) -> None:
    if args.command == "make":
        _args_action_make(args=args, config=config)
    elif args.command == "touch":
        _args_action_touch(args=args, config=config)
    elif args.command == "link-json":
        _args_process_link_json_cmd_data(args=args, config=config)
    elif args.command == "data":
        _args_process_data_cmd_data(args=args, config=config)
    elif args.command == "compile":
        _args_process_compile_cmd_data(args=args, config=config)
    elif args.command == "url-parse":
        _args_process_url_parser_cmd_data(args=args)
    elif args.command == "cmd-link":
        _args_action_cmd_link(args=args)


# endregion ARGS COMMANDS
# endregion parser


def main():
    global logger
    # region Config
    os.environ["project_root"] = str(Path(__file__).parent)
    config = mutil.get_app_cfg()
    os.environ["config_cache_dir"] = config.cache_dir
    os.environ["config_cache_duration"] = str(config.cache_duration)
    os.environ["config_resource_dir"] = config.resource_dir
    os.environ["config_db_mod_info"] = config.db_mod_info
    os.environ["config_uno_obj_dir"] = config.uno_obj_dir
    os.environ["config_dyn_dir"] = config.dyn_dir
    os.environ["config_helper_ns"] = config.helper_ns
    os.environ["config_helper_mod"] = config.helper_mod
    os.environ["config_enum_mod"] = config.enum_mod
    os.environ["config_oenv_ns"] = config.env
    # endregion Config

    # region create parsers
    parser = _create_parser("main")
    subparser = parser.add_subparsers(dest="command")
    # region    make
    make_parser = subparser.add_parser(
        name="make", help=f"Once files have been compiled (written to {config.uno_obj_dir})"
    )
    # endregion make

    # region    compile
    compile_subparser = subparser.add_parser(
        name="compile",
        help=f"Batch compiles html urls found {config.module_links_file} files into json and tmpl files.",
    )
    compile = compile_subparser.add_subparsers(dest="command_data")
    links_const_parser = compile.add_parser(
        name="const", help=f"Compile Const components found in {config.module_links_file} files."
    )
    links_enum_parser = compile.add_parser(
        name="enum", help=f"Compile enum components found in {config.module_links_file} files."
    )
    links_ex_parser = compile.add_parser(
        name="exception", help=f"Compile exception components found in {config.module_links_file} files."
    )
    links_interface_parser = compile.add_parser(
        name="interface", help=f"Compile interface components found in {config.module_links_file} files."
    )
    links_service_parser = compile.add_parser(
        name="service", help=f"Compile service components found in {config.module_links_file} files."
    )
    links_singleton_parser = compile.add_parser(
        name="singleton", help=f"Compile singleton components found in {config.module_links_file} files."
    )
    links_struct_parser = compile.add_parser(
        name="struct", help=f"Compile struct components found in {config.module_links_file} files."
    )
    links_typedef_parser = compile.add_parser(
        name="typedef", help=f"Compile typedef components found in {config.module_links_file} files."
    )
    links_batch_parser = compile.add_parser(name="batch", help="Batch compile one or more at once")
    # endregion compile

    # region    url-parse
    url_parser_subparser = subparser.add_parser(
        name="url-parse",
        help=f"Parse url of a component into template/json files (compile single class). Outputs to {config.uno_obj_dir} directory.",
    )
    url_parser = url_parser_subparser.add_subparsers(dest="command_data")
    url_const = url_parser.add_parser(name="const", help="Parse url to a const component into template/json file.")
    url_enum = url_parser.add_parser(name="enum", help="Parse url to a enum component into template/json file.")
    url_exception = url_parser.add_parser(
        name="exception", help="Parse url to a exception component into template/json file."
    )
    url_interface = url_parser.add_parser(
        name="interface", help="Parse url to a interface component into template/json file."
    )
    url_service = url_parser.add_parser(
        name="service", help="Parse url to a service component into template/json file."
    )
    url_singleton = url_parser.add_parser(
        name="singleton", help="Parse url to a singleton component into template/json file."
    )
    url_struct = url_parser.add_parser(name="struct", help="Parse url to a struct component into template/json file.")
    url_typedef = url_parser.add_parser(
        name="typedef", help="Parse url to a typedef component into template/json file."
    )
    # endregion url-parse

    # region    touch
    touch = subparser.add_parser(name="touch", help="Touches files updating their modifiled date")
    # endregion touch

    # region    link-json
    link_json_subparser = subparser.add_parser(
        name="link-json", help=f"Generate json link files such as {config.module_links_file} files or star.json file."
    )
    link_json_parser = link_json_subparser.add_subparsers(dest="command_data")
    link_json_mod_links = link_json_parser.add_parser(
        name="mod-links",
        help=f"Reads a namespace_url type json file such as resources/star.json and writes {config.module_links_file} files.",
    )
    link_json_star_links = link_json_parser.add_parser(
        name="star-links", help="Generates a namespace_url type json file such as resources/star.json."
    )
    # endregion link-json

    # region    data
    data_subparser = subparser.add_parser(name="data", help="Various database commands and queries.")
    data = data_subparser.add_subparsers(dest="command_data")
    data_init = data.add_parser(
        name="init",
        help=f"Create a new database if it does not yet exits. Default location is '{config.resource_dir}/{config.db_mod_info}'.",
    )
    data_update = data.add_parser(
        name="update",
        help=f"Read json data from '{config.data_dir}' directory and write relevant data into '{config.resource_dir}/{config.db_mod_info}' database. Will add data if not existing. Requires that json file have been generated in '{config.data_dir}' directory.",
    )
    data_component = data.add_parser(name="component", help="Queries database for component info.")
    data_url = data.add_parser(name="url", help="Queries database and gets info such as url for a namespace.")
    data_rel = data.add_parser(name="rel", help="Generated relative import info for given namespaces.")
    data_json = data.add_parser(
        name="json",
        help="Generates json file, ignores direct extends and uses child flattened extends but includes original extends methods and properties. Used for MRO issues.",
    )
    data_extends_tree = data.add_parser(
        name="extends-tree", help="Queries database and gets extends tree format for a given namespace."
    )
    data_extends_flat = data.add_parser(
        name="extends-flat",
        help="Queries database and gets extends flat formats for a given namespace. Can get flat child extends as well.",
    )
    data_imports = data.add_parser(
        name="imports", help="Queries database and gets import information for a given namespace."
    )
    data_imports_typing_child = data.add_parser(
        name="imports-typing-child", help="Queries database and get import information for imports typing child."
    )
    data_star = data.add_parser(
        name="star",
        help=f"Writes imports for all '{config.build_dir}/{config.uno_obj_dir}' files into  com.sun.star... __init__.py files.",
    )
    # endregion data

    # region command link
    if os.name != "nt":
        # linking is not useful in Windows.
        cmd_link = subparser.add_parser(
            name="cmd-link",
            help="Add/Remove links in virtual environments to uno files.",
        )
        _args_cmd_link(parser=cmd_link)
    # endregion command link

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
    _args_touch(parser=touch, config=config)
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
    _args_data_star(parser=data_star, config=config)
    # endregion data args
    # endregion Set Args

    # region Read Args
    args = parser.parse_args()
    # endregion Read Args

    # region logger
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args["log_file"] = args.log_file
        else:
            log_args["log_file"] = "app.log"
        if args.verbose:
            log_args["level"] = logging.DEBUG
        logger = get_logger(logger_name=Path(__file__).stem, **log_args)
    # endregion logger

    _args_process_cmd(args=args, config=config)


if __name__ == "__main__":
    # _touch()
    main()

# endregion Main

#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains links to modules.
Modules data is writen in json format into namespace converted to directories.
This file writes module_links.json files.
"""
# region Imports
import sys
import os
import argparse
import re
import logging
from dataclasses import dataclass
from abc import abstractmethod
from typing import Dict, List,  Union
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RequireArgs, RuleCheckAllKw, TypeCheckKw, TypeCheck
from kwhelp import rules
from pathlib import Path
from ..common.config import APP_CONFIG
from ..common.util import Util
from ..common import log_load
from ..web.block_obj import BlockObj
from ..web.soup_obj import SoupObj
from ..web.url_obj import UrlObj
from ...logger.log_handle import get_logger
from ...parser import __version__, JSON_ID
from ...utilities import util as mutil
# try:
#     import base
# except ModuleNotFoundError:
#     import parser.base as base
# endregion Imports

# region Logging
logger: logging.Logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger
    log = log_load.Log()
    log.logger = l
    logger = log.logger

_set_loggers(None)
# endregion Logging

# region Data Classes


@dataclass
class Link:
    href: str
    type: str
    name: str
# endregion Data Classes

# region API Classes


class ApiTables(BlockObj):
    @TypeCheck(SoupObj, ftype=DecFuncEnum.METHOD)
    def __init__(self, soup: SoupObj):
        self._soup = soup
        super().__init__(soup)
        self._data = None

    def get_obj(self) -> ResultSet:
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        self._data = soup.find_all('table', class_='memberdecls')
        return self._data


class ApiTableFindBase(BlockObj):
    """Abstract Class for finding tables"""
    @TypeCheck(ApiTables, ftype=DecFuncEnum.METHOD)
    def __init__(self, tables: ApiTables):
        self._tables = tables
        super().__init__(self._tables.soup)
        self._data = None
        self._has_data = None

    def get_obj(self) -> Union[Tag, None]:
        """
        Gets Table as Tag if match if found

        Returns:
            Union[Tag, None]: Table if found; Otherwise,  ``None``
        """
        if not self._data is None:
            return self._data
        if self._has_data is False:
            return None
        tables = self._tables.get_obj()
        for tbl in tables:
            if self._find_table(tbl):
                self._data = tbl
                self._has_data = True
                logger.debug(
                    "ApiTableFindBase.get_obj() Found table: %s", self._get_heading_text())
                break
        if self._has_data is None:
            logger.debug(
                "ApiTableFindBase.get_obj() Did not find table: %s", self._get_heading_text())
            self._has_data = False
        return self._data

    @abstractmethod
    def _get_heading_text(self) -> str:
        """Gets name such as service"""

    def _find_table(self, t: Tag) -> bool:
        t_heading = t.find('tr', class_='heading')
        if not t_heading:
            return False
        text = t_heading.text.strip().lower()
        return text == self._get_heading_text()


class ApiConstantsBlock(ApiTableFindBase):

    def _get_heading_text(self) -> str:
        return 'constant groups'


class ApiClassBlock(ApiTableFindBase):

    def _get_heading_text(self) -> str:
        return 'classes'


class ApiEnumBlock(ApiTableFindBase):

    def _get_heading_text(self) -> str:
        return 'enumerations'


class ApiModulesBlock(ApiTableFindBase):

    def _get_heading_text(self) -> str:
        return 'modules'


class ApiTypeDefsBlock(ApiTableFindBase):

    def _get_heading_text(self) -> str:
        return 'typedefs'


class ApiTableLinks:
    def __init__(self, table_block: ApiTableFindBase) -> List[Link]:
        self._table_block = table_block
        self._data = None

    def get_obj(self) -> List[Link]:
        if not self._data is None:
            return self._data
        self._data = []
        tag_tbl = self._table_block.get_obj()
        if not tag_tbl:
            return self._data
        tag_tr = tag_tbl.find_all('tr', class_=re.compile(r"memitem:*"))
        if not tag_tr:
            return self._data
        for tr in tag_tr:
            tag_left: Tag = tr.find('td', class_='memItemLeft')
            if not tag_left:
                logger.warning("ApiTableLinks.get_obj() Unable to find type in %s",
                               self._table_block._get_heading_text().capitalize())
                continue
            _type = tag_left.text.strip()
            tag_right: Tag = tr.find('td', class_='memItemRight')
            if not tag_right:
                logger.warning("ApiTableLinks.get_obj() Unable to find Name for type: %s in %s",
                               _type, self._table_block._get_heading_text().capitalize())
                continue
            tag_a = tag_right.select_one('a')
            if not tag_a:
                logger.warning("ApiTableLinks.get_obj() Unable to find Link for type: %s in %s",
                               _type, self._table_block._get_heading_text().capitalize())
                continue
            href = tag_a.get('href', None)
            if not href:
                logger.warning("ApiTableLinks.get_obj() Unable to find Href in Link for type: %s in %s",
                               _type, self._table_block._get_heading_text().capitalize())
                continue
            name = tag_a.text.strip().replace('::', '.')
            self._data.append(
                Link(
                    href=href,
                    type=_type,
                    name=name
                )
            )
        return self._data


class ApiData:
    # region constructor
    @TypeCheck((str, SoupObj), bool, ftype=DecFuncEnum.METHOD)
    def __init__(self, url_soup: Union[str, SoupObj], allow_cache: bool):
        if isinstance(url_soup, str):
            self._url = url_soup
            self._soup_obj = SoupObj(
                url=url_soup, allow_cache=allow_cache, has_name=False)
        else:
            self._url = url_soup.url
            self._soup_obj = url_soup
            self._soup_obj.allow_cache = allow_cache
        self._api_tables: ApiTables = None
        self._api_constants_block: ApiConstantsBlock = None
        self._api_class_block: ApiClassBlock = None
        self._api_modules_block: ApiModulesBlock = None
        self._api_enum_block: ApiEnumBlock = None
        self._api_type_defs_block: ApiTypeDefsBlock = None
        self._api_constants_links: ApiTableLinks = None
        self._api_class_links: ApiTableLinks = None
        self._api_modules_links: ApiTableLinks = None
        self._api_enum_links: ApiTableLinks = None
        self._api_type_defs_links: ApiTableLinks = None
    # endregion constructor

    # region Properties
    @property
    def soup_obj(self) -> SoupObj:
        return self._soup_obj

    @property
    def url_obj(self) -> UrlObj:
        return self._soup_obj.url_obj

    @property
    def api_tables(self) -> ApiTables:
        """Gets tables on a page"""
        if self._api_tables is None:
            self._api_tables = ApiTables(self._soup_obj)
        return self._api_tables

    @property
    def api_constants_block(self) -> ApiConstantsBlock:
        """Gets Table representing Constants on a page"""
        if self._api_constants_block is None:
            self._api_constants_block = ApiConstantsBlock(self.api_tables)
        return self._api_constants_block

    @property
    def api_class_block(self) -> ApiClassBlock:
        """Gets Table representing Constants on a page"""
        if self._api_class_block is None:
            self._api_class_block = ApiClassBlock(self.api_tables)
        return self._api_class_block

    @property
    def api_modules_block(self) -> ApiModulesBlock:
        """Gets Table representing Modules on a page"""
        if self._api_modules_block is None:
            self._api_modules_block = ApiModulesBlock(self.api_tables)
        return self._api_modules_block

    @property
    def api_enum_block(self) -> ApiEnumBlock:
        """Gets Table representing Enums ona page"""
        if self._api_enum_block is None:
            self._api_enum_block = ApiEnumBlock(self.api_tables)
        return self._api_enum_block

    @property
    def api_type_defs_block(self) -> ApiTypeDefsBlock:
        """Gets Table representing Enums ona page"""
        if self._api_type_defs_block is None:
            self._api_type_defs_block = ApiTypeDefsBlock(self.api_tables)
        return self._api_type_defs_block

    @property
    def api_constants_links(self) -> ApiTableLinks:
        """Gets Data representing Constant Links on a page"""
        if self._api_constants_links is None:
            self._api_constants_links = ApiTableLinks(self.api_constants_block)
        return self._api_constants_links

    @property
    def api_class_links(self) -> ApiTableLinks:
        """Gets Data representing Class Links on a page"""
        if self._api_class_links is None:
            self._api_class_links = ApiTableLinks(self.api_class_block)
        return self._api_class_links

    @property
    def api_modules_links(self) -> ApiTableLinks:
        """Gets Data representing Module Links on a page"""
        if self._api_modules_links is None:
            self._api_modules_links = ApiTableLinks(self.api_modules_block)
        return self._api_modules_links

    @property
    def api_enum_links(self) -> ApiTableLinks:
        """Gets Data representing Module Links on a page"""
        if self._api_enum_links is None:
            self._api_enum_links = ApiTableLinks(self.api_enum_block)
        return self._api_enum_links

    @property
    def api_type_defs_links(self) -> ApiTableLinks:
        """Gets Data representing Module Links on a page"""
        if self._api_type_defs_links is None:
            self._api_type_defs_links = ApiTableLinks(self.api_type_defs_block)
        return self._api_type_defs_links
    # endregion Properties

# endregion API Classes

# region Parser Class


class ParserMod:
    @RequireArgs('url', ftype=DecFuncEnum.METHOD, opt_logger=logger)
    @TypeCheckKw(arg_info={'cache': 0}, types=[bool], ftype=DecFuncEnum.METHOD, opt_logger=logger)
    @RuleCheckAllKw(arg_info={'url': rules.RuleStrNotNullEmptyWs}, ftype=DecFuncEnum.METHOD, opt_logger=logger)
    def __init__(self, url: str, **kwargs) -> None:
        self._url: str = url
        self._allow_cache: bool = kwargs.get('cache', True)
        self._api_data = ApiData(
            url_soup=self._url, allow_cache=self._allow_cache)
        self._cache = {}

    def _get_module_links(self) -> List[Dict[str, str]]:
        module_links = self._api_data.api_modules_links.get_obj()
        links = []
        if module_links:
            for link in module_links:
                links.append(
                    {
                        "name": link.name,
                        "href": link.href
                    }
                )
        logger.debug("ParserMod.get_data() %d moduled links.",
                     len(module_links))
        return links

    def _get_enum_links(self) -> List[Dict[str, str]]:
        enum_links = self._api_data.api_enum_links.get_obj()
        links = []
        if enum_links:
            for link in enum_links:
                links.append(
                    {
                        "name": link.name,
                        "href": link.href
                    }
                )
        logger.debug("ParserMod.get_data() %d enum links.", len(enum_links))
        return links

    def _get_type_def_links(self) -> List[Dict[str, str]]:
        type_def_links = self._api_data.api_type_defs_links.get_obj()
        links = []
        if type_def_links:
            for link in type_def_links:
                links.append(
                    {
                        "name": link.name,
                        "href": link.href
                    }
                )
        logger.debug("ParserMod.get_data() %d type_def links.",
                     len(type_def_links))
        return links

    def _get_const_links(self) -> List[Dict[str, str]]:
        const_links = self._api_data.api_constants_links.get_obj()
        links = []
        if const_links:
            for link in const_links:
                links.append(
                    {
                        "name": link.name,
                        "href": link.href
                    }
                )
        logger.debug("ParserMod.get_data() %d type_def links.",
                     len(const_links))
        return links

    def _get_class_links(self):
        class_links = self._api_data.api_class_links.get_obj()
        results = {}
        for link in class_links:
            if not link.type in results:
                results[link.type] = []
            results[link.type].append(
                {
                    "name": link.name,
                    "href": link.href
                }
            )
        logger.debug("ParserMod.get_data() %d Class links.",
                     len(class_links))
        return results

    def get_data(self) -> Dict[str, str]:
        key = 'get_data'
        if key in self._cache:
            return self._cache[key]
        results = {
            "modules": self._get_module_links(),
            "enums": self._get_enum_links(),
            "constants": self._get_const_links(),
            "typedef": self._get_type_def_links(),
            "classes": self._get_class_links()
        }
        self._cache[key] = results
        return self._cache[key]

    @property
    def api_data(self) -> ApiData:
        """Gets api_data value"""
        return self._api_data
# endregion Parser Class

# region Writer Class


class WriterMod():
    @TypeCheckKw(arg_info={
        "write_json": 0,
        "print_json": 0,
        "clear_on_print": 0
    },
        types=[bool],
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, parser: ParserMod, **kwargs) -> None:
        self._parser: ParserMod = parser
        self._print_json: bool = kwargs.get('print_json', True)
        self._write_json: bool = kwargs.get('write_json', False)
        self._clear_on_print: bool = kwargs.get('clear_on_print', True)
        self._clear_on_print: bool = kwargs.get('clear_on_print', True)
        self._write_path: Union[str, None] = kwargs.get('write_path', None)
        self._path_dir = Path(__file__).parent
        self._cache = {}

    def write(self):
        try:
            if self._clear_on_print and self._print_json:
                logger.debug('Printing to terminal')
                os.system('cls' if os.name == 'nt' else 'clear')
            if self._print_json:
                print(self._get_json())
            if self._write_json:
                self._write_to_json()
        except Exception as e:
            logger.exception(e)

    def _get_json(self) -> str:
        key = '_get_json'
        if key in self._cache:
            return self._cache[key]
        # name = f"{self._parser.api_data.url_obj.namespace_str}.{self._parser.api_data.url_obj.name}"
        name = self._parser.api_data.url_obj.namespace_str
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            # "timestamp": str(Util.get_timestamp_utc()),
            "libre_office_ver": APP_CONFIG.libre_office_ver,
            "name": name,
            "namespace": name,
            "type": "module_links",
            "url_base": self._parser.api_data.url_obj.url_base,
            "data": self._parser.get_data()
        }
        str_jsn = Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._cache[key] = str_jsn
        return self._cache[key]

    def _write_to_json(self):
        jsn_p = self._get_uno_obj_path()
        jsn_str = self._get_json()
        with open(jsn_p, 'w') as f:
            f.write(jsn_str)
        logger.info("Created file: %s", jsn_p)

    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        if self._write_path:
            write_path = self._write_path
        else:
            write_path = APP_CONFIG.uno_base_dir
        uno_obj_path = Path(mutil.get_root(), write_path)
        name_parts: List[str] = self._parser.api_data.url_obj.namespace
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append('module_links.json')
        obj_path = uno_obj_path.joinpath(*path_parts)
        Util.mkdirp(dest_dir=obj_path.parent)
        self._cache[key] = obj_path
        return self._cache[key]
# endregion Writer Class


def work(url: str, **kwargs):
    logger.info('Parsing Url %s', url)
    recursive = bool(kwargs.get('recursive', False))
    p = ParserMod(url=url, **kwargs)
    w = WriterMod(parser=p, **kwargs)
    w.write()
    if recursive:
        data = p.get_data()
        base_url = p.api_data.url_obj.url_base
        key = 'modules'
        if key in data:
            mods: List[dict] = data[key]
            for mod in mods:
                href: str = mod['href']
                _url = f"{base_url}/{href}"
                work(url=_url, **kwargs)

# region Parse method


def get_kwargs_from_args(args: argparse.ArgumentParser) -> dict:
    """
    Converts argparse args into dictionary that can be passed to ``parse()``

    Args:
        args (argparse.ArgumentParser): args

    Returns:
        dict: dictionary that contain key values matching ``parser()`` args.
    """
    defaults = {
        "url": None,
        "cache": True,
        "write_path": None,
        "print_clear": True,
        "print_json": False,
        "write_json": False,
        "verbose": False
    }
    # d = {
    #     "url": args.url,
    #     "cache": args.cache,
    #     "print_clear": args.print_clear,
    #     "print_json": args.print_json,
    #     "write_json": args.write_json,
    #     "log_file": args.log_file,
    #     "verbose": args.verbose
    # }
    # if args.write_path:
    #     d['write_path'] = args.write_path
    command_line_args = {k: v for k, v in vars(args).items()}
    defaults.update(command_line_args)
    return defaults


def parse(**kwargs):
    """
    Parses data, alternative to running on command line.

    Keyword Arguments:
        url (str): Url to parse
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
    _url = str(kwargs['url'])
    _cache = bool(kwargs.get('cache', False))
    _print_clear = bool(kwargs.get('print-clear', False))
    _print_json = bool(kwargs.get('print_json', False))
    _write_json = bool(kwargs.get('write_json', False))
    _write_path = kwargs.get('write_path', None)
    _verbose = bool(kwargs.get('verbose', False))
    _recursive = bool(kwargs.get('recursive', False))
    _log_file = 'mod.log' if kwargs.get(
        'log_file', None) is None else str(kwargs.get('log_file'))

    if logger is None:
        log_args = {}
        log_args['log_file'] = _log_file
        if _verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    work(
        url=_url,
        cache=_cache,
        print_json=_print_json,
        write_json=_write_json,
        clear_on_print=_print_clear,
        recursive=_recursive,
        write_path=_write_path
    )


def set_cmd_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=True)
    parser.add_argument(
        '-o', '--out',
        help=f"Out path of templates and json data. Default: '{APP_CONFIG.uno_base_dir}'",
        type=str,
        dest='write_path',
        default=None,
        required=False)
    parser.add_argument(
        '-x', '--no-cache',
        help='No caching',
        action='store_false',
        dest='cache',
        default=True)
    parser.add_argument(
        '-p', '--no-print-clear',
        help='No clearing of terminal when output to terminal.',
        action='store_false',
        dest='print_clear',
        default=True)
    parser.add_argument(
        '-n', '--print-json',
        help='Print json to terminal',
        action='store_true',
        dest='print_json',
        default=False)
    parser.add_argument(
        '-j', '--write-json',
        help='Write json file into obj_uno subfolder',
        action='store_true',
        dest='write_json',
        default=False)
    parser.add_argument(
        '-r', '--recursive',
        help='Recursivly process modules. If url contains links other modules they will be processed',
        action='store_true',
        dest='recursive',
        default=False)


def set_cmd_args_local(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use. Defaults to mod.log',
        type=str,
        required=False)
# endregion Parse method


def _main():
    # url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html'
    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html'
    sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    main()


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
            log_args['log_file'] = 'mod.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    # endregion Parser
    if not args.print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    logger.info('Executing command: %s', sys.argv[1:])
    args_dict = get_kwargs_from_args(args)
    parse(**args_dict)


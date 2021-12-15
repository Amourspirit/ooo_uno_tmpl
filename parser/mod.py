#!/usr/bin/env python
# region Imports
import sys
import os
import argparse
import base
import re
import logging
from dataclasses import dataclass
from abc import abstractmethod
from typing import Dict, List, Tuple, Union
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, TypeCheckKw, TypeCheck
from kwhelp import rules
from pathlib import Path
from logger.log_handle import get_logger
from parser import __version__, JSON_ID
# endregion Imports

# region Logging
logger: logging.Logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l

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


class ApiTables(base.BlockObj):
    @TypeCheck(base.SoupObj, ftype=DecFuncEnum.METHOD)
    def __init__(self, soup: base.SoupObj):
        self._soup = soup
        super().__init__(soup)
        self._data = None

    def get_obj(self) -> ResultSet:
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        self._data = soup.find_all('table', class_='memberdecls')
        return self._data


class ApiTableFindBase(base.BlockObj):
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

class ApiTableLinks:
    def __init__(self, table_block: ApiTableFindBase) -> List[Link]:
        self._table_block = table_block
        self._data = None
    
    def get_obj(self):
        if not self._data is None:
            return self.Data
        self._data = []
        tag_tbl =self._table_block.get_obj()
        if not tag_tbl:
            return self._data
        tag_tr = tag_tbl.find_all('tr', class_=re.compile(r"memitem:*"))
        if not tag_tr:
            return self._data
        for tr in tag_tr:
            tag_left: Tag = tr.find('td', class_='memItemLeft')
            if not tag_left:
                logger.warning("ApiTableLinks.get_obj() Unable to find type in %s", self._table_block._get_heading_text().capitalize())
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
    @TypeCheck((str, base.SoupObj), bool, ftype=DecFuncEnum.METHOD)
    def __init__(self, url_soup: Union[str, base.SoupObj], allow_cache: bool):
        if isinstance(url_soup, str):
            self._url = url_soup
            self._soup_obj = base.SoupObj(
                url=url_soup, allow_cache=allow_cache)
        else:
            self._url = url_soup.url
            self._soup_obj = url_soup
            self._soup_obj.allow_cache = allow_cache
        self._api_tables: ApiTables = None
        self._api_constants_block: ApiConstantsBlock = None
        self._api_class_block: ApiClassBlock = None
        self._api_modules_block: ApiModulesBlock = None
        self._api_enum_block: ApiEnumBlock = None
        self._api_constants_links: ApiTableLinks = None
        self._api_class_links: ApiTableLinks = None
        self._api_modules_links: ApiTableLinks = None
        self._api_enum_links: ApiTableLinks = None
    # endregion constructor
    
    # region Properties
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
    # endregion Properties

# endregion API Classes

def main():
    global logger
    if logger is None:
        log_args = {
            'log_file': 'mod.log',
            'level': logging.DEBUG
        }
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    os.system('cls' if os.name == 'nt' else 'clear')
    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html'
    data = ApiData(url_soup=url, allow_cache=True)
    module_links = data.api_modules_links.get_obj()
    class_links = data.api_class_links.get_obj()
    const_links = data.api_constants_links.get_obj()
    enum_links = data.api_enum_links.get_obj()
    print(enum_links)

if __name__ == '__main__':
    main()
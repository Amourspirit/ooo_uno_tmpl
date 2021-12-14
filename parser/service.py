#!/usr/bin/env python
from abc import abstractmethod
import os
import sys
import argparse
import logging
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
import re
import base
from typing import Dict, List, Set, Union
from bs4.element import PageElement, ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, SubClass, TypeCheck, TypeCheckKw
from pathlib import Path
from logger.log_handle import get_logger
from parser.enm import main
from dataclasses import dataclass
from parser import __version__, JSON_ID

logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l


_set_loggers(None)


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
                logger.debug("ApiTableFindBase.get_obj() Found table: %s", self._get_a_name())
                break
        if self._has_data is None:
            logger.debug(
                "ApiTableFindBase.get_obj() Did not find table: %s", self._get_a_name())
            self._has_data = False
        return self._data

    @abstractmethod
    def _get_a_name(self) -> str:
        """Gets name such as service"""
    
    def _find_table(self, t: Tag) -> bool:
        t_heading = t.find('tr', class_='heading')
        if not t_heading:
            return False
        t_a = t_heading.find('a',  attrs={"name": self._get_a_name()})
        if t_a:
            return True
        return False


class ApiIncludedServicesBlock(ApiTableFindBase):

    def _get_a_name(self) -> str:
        return 'services'


class ApiExportedInterfacesBlock(ApiTableFindBase):

    def _get_a_name(self) -> str:
        return 'interfaces'

class ApiComponentExtends:
    @SubClass(ApiTableFindBase, ftype=DecFuncEnum.METHOD)
    def __init__(self, table: ApiTableFindBase):
        self._table = table
        self._data = None
    
    def _get_rows(self) -> List[Tag]:
        results = []
        tag = self._table.get_obj()
        if not tag:
            return results
        rs = tag.select('tr')
        for r in rs:
            class_ : List[str] = r.get('class', None)
            if not class_:
                continue
            if 'inherit_header' in class_:
                # Exported interfaces are alos included in the same table
                # to filter out these stop when row with class including
                # inherit_header is found.
                break
            if class_[0].startswith('memitem:'):
                results.append(r)
        return results
    
    def get_obj(self) -> List[str]:
        if not self._data is None:
            return self._data
        results = []
        rows = self._get_rows()
        for row in rows:
            tag = row.find('td', class_='memItemRight')
            if not tag:
                continue
            try:
                s: str = tag.text
                s = s.replace("::", ".")
                results.append(base.Util.get_clean_ns(input=s, ltrim=True))
            except Exception as e:
                logger.debug('ApiComponentExtends.get_obj() parsing error. continuing...')
                continue
        self._data = results
        return self._data
class ApiData:
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
        self._api_included_services_block: ApiIncludedServicesBlock = None
        self._api_exported_interfaces_block: ApiExportedInterfacesBlock = None
        self._api_services: ApiComponentExtends = None
        self._api_interfaces: ApiComponentExtends = None

    @property
    def soup(self) -> base.SoupObj:
        """Gets soup value"""
        return self._soup_obj

    @property
    def api_tables(self) -> ApiTables:
        """Gets api_tables value"""
        if self._api_tables is None:
            self._api_tables = ApiTables(self._soup_obj)
        return self._api_tables
    
    @property
    def api_included_services_block(self) -> ApiIncludedServicesBlock:
        """Gets api_tables value"""
        if self._api_included_services_block is None:
            self._api_included_services_block = ApiIncludedServicesBlock(self.api_tables)
        return self._api_included_services_block

    @property
    def api_exported_interfaces_block(self) -> ApiExportedInterfacesBlock:
        """Gets api_tables value"""
        if self._api_exported_interfaces_block is None:
            self._api_exported_interfaces_block = ApiExportedInterfacesBlock(
                self.api_tables)
        return self._api_exported_interfaces_block

    @property
    def api_services(self) -> ApiComponentExtends:
        if self._api_services is None:
            self._api_services = ApiComponentExtends(self.api_included_services_block)
        return self._api_services

    @property
    def api_interfaces(self) -> ApiComponentExtends:
        if self._api_interfaces is None:
            self._api_interfaces = ApiComponentExtends(
                self.api_exported_interfaces_block)
        return self._api_interfaces

class ParserService(base.ParserBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._api_data = ApiData(
            url_soup=self.url,
            allow_cache=self.allow_cache
            )
        self._cache = {}

    def get_parser_args(self) -> dict:
        args = {
            "sort": self.sort
        }
        return args
    
    def _get_extends(self) -> List[str]:
        extends = []
        service_e = self._api_data.api_services.get_obj()
        extends.extend(service_e)
        interface_e = self._api_data.api_interfaces.get_obj()
        extends.extend(interface_e)
        return extends

    def get_info(self) -> Dict[str, object]:
        key = 'get_info'
        if key in self._cache:
            return self._cache[key]
        ns = self._api_data.soup.url_obj
        result = {
            'name': ns.name,
            'namespace': ns.namespace_str,
            'extends': self._get_extends(),
            "url": ns.url
        }
        self._cache[key] = result
        return self._cache[key]

def main():
    global logger
    
    if logger is None:
        log_args = {
            "log_file": "service.log",
            "level": logging.DEBUG
        }
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    # url = "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1AccessibleIconChoiceControl.html"
    # url = "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1AnimatedImagesControlModel.html"
    # url = "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1SpinningProgressControlModel.html"
    url = "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1AccessibleCheckBox.html"
    p = ParserService(
        url=url,
        sort=True,
        cache=True
        )
    data = p.get_info()
    print(data)

if __name__ == '__main__':
    main()

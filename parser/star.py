#!/usr/bin/env python
from dataclasses import dataclass
import os
import sys
import argparse
import base
import re
import logging
from typing import Dict, List, Tuple, Union
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, RequireArgs, TypeCheckKw, TypeCheck
from kwhelp import rules
from collections import namedtuple
from pathlib import Path
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
from logger.log_handle import get_logger
from parser import __version__, JSON_ID

logger:logging.Logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l


_set_loggers(None)

@dataclass
class LinkInfo:
    Name: str
    href: str
    desc: str
    class_name: str

class ApiModuleBlock(base.BlockObj):
    @TypeCheck(base.SoupObj, ftype=DecFuncEnum.METHOD)
    def __init__(self, soup: base.SoupObj):
        self._soup = soup
        super().__init__(soup)
        self._data = None
    
    def get_obj(self) -> Tag:
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        tag = soup.select_one('body > div.contents > table')
        if not tag:
            msg = "ApiModuleBlock.get_obj() failed to get html data"
            logger.error(msg)
            raise Exception(msg)
        self._data = tag
        return self._data

class ApiLink:
    def __init__(self, api_module_block: ApiModuleBlock):
        self._api_module_block = api_module_block
        self._data = None
    
    def _get_name_rows(self) -> ResultSet:
        tag = self._api_module_block.get_obj()
        results = tag.find_all('tr', class_=re.compile(
            r"memitem:namespacecom_1_1sun_1_1star.*"
        ))
        return results
    
    def _get_tr_class(self, tag: Tag) -> str:
        t = tag.select_one('tr')
        return t['class']
    
    def _get_link(self, tag: Tag) -> Tuple[str, str]:
        a:Tag = tag.find('a', class_='el')
        name = a.text.strip()
        href = a['href']
        return name, href
    
    def _get_name_info(self) -> List[LinkInfo]:
        rs = self._get_name_rows()
        result = []
        for tag in rs:
            class_ = tag['class'][0]
            a_name, a_href = self._get_link(tag)
            result.append(LinkInfo(
                Name=a_name,
                href=a_href,
                desc='',
                class_name=class_
            ))
        return result
    
    def _get_desc(self, class_:str) -> str:
        try:
            full_class = 'memdesc:' + class_
            tag = self._api_module_block.get_obj()
            tr: Tag = tag.find('tr', class_=full_class)
            td: Tag = tr.find('td', class_='mdescRight')
            return " ".join(td.text.strip().splitlines())
        except Exception as e:
            logger.error("ApiLink._get_desc() Error %s", e)
            return ''
    
    def get_obj(self) -> List[LinkInfo]:
        if not self._data is None:
            return self._data
        ni_lst: List[LinkInfo] = self._get_name_info()
        for ni in ni_lst:
            class_ = base.Util.get_last_part(input=ni.class_name, sep=':')
            ni.desc = self._get_desc(class_)
        self._data = ni_lst
        return self._data
class ApiData:
    @TypeCheck((str, base.SoupObj), ftype=DecFuncEnum.METHOD)
    def __init__(self, url_soup: Union[str, base.SoupObj]):
        if isinstance(url_soup, str):
            self._url = url_soup
            self._soup_obj = base.SoupObj(url_soup)
        else:
            self._url = url_soup.url
            self._soup_obj = url_soup

        self._api_module_block: ApiModuleBlock = None
        self._api_link: ApiLink = None
    
    @property
    def api_module_block(self) -> ApiModuleBlock:
        """Gets api_module_block value"""
        if self._api_module_block is None:
            self._api_module_block = ApiModuleBlock(self._soup_obj)
        return self._api_module_block
    
    @property
    def api_link(self) -> ApiLink:
        """Gets api_link value"""
        if self._api_link is None:
            self._api_link = ApiLink(self.api_module_block)
        return self._api_link

def main():
    global logger
    log_args = {
        'log_file': 'debug.log',
        'level': logging.DEBUG
    }
    _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html'
    
    api_data = ApiData(url)
    
    print(api_data.api_link.get_obj())
    
if __name__ == '__main__':
    main()

# body > div.contents > table > tbody > tr.memitem\:namespacecom_1_1sun_1_1star_1_1accessibility > td.memItemRight > a

# modules can contain other modules such as with chart2: https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html


#!/usr/bin/env python
# coding: utf-8
"""
Process link to star namesapec that contains links to modules
"""
# region Imports
from dataclasses import dataclass
import sys
import argparse
import base
import re
import logging
from typing import Dict, List, Tuple, Union
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, TypeCheckKw, TypeCheck
from kwhelp import rules
from pathlib import Path
from logger.log_handle import get_logger
from parser import __version__, JSON_ID
# endregion Imports

# region Logging
logger:logging.Logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l


_set_loggers(None)
# endregion Logging

# region Data Classes
@dataclass
class LinkInfo:
    Name: str
    href: str
    desc: str
    class_name: str
# endregion Data Classes

# region API Classes
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
    
    def _get_desc(self, class_:str, name:str) -> str:
        try:
            full_class = 'memdesc:' + class_
            tag = self._api_module_block.get_obj()
            tr: Tag = tag.find('tr', class_=full_class)
            td: Tag = tr.find('td', class_='mdescRight')
            return " ".join(td.text.strip().splitlines())
        except Exception as e:
            logger.warning(
                'ApiLink._get_desc() No description found for: %s', name)
            return ''
    
    def get_obj(self) -> List[LinkInfo]:
        if not self._data is None:
            return self._data
        ni_lst: List[LinkInfo] = self._get_name_info()
        for ni in ni_lst:
            class_ = base.Util.get_last_part(input=ni.class_name, sep=':')
            ni.desc = self._get_desc(class_, ni.Name)
        self._data = ni_lst
        return self._data
class ApiData:
    @TypeCheck((str, base.SoupObj), bool, ftype=DecFuncEnum.METHOD)
    def __init__(self, url_soup: Union[str, base.SoupObj], allow_cache:bool):
        if isinstance(url_soup, str):
            self._url = url_soup
            self._soup_obj = base.SoupObj(
                url=url_soup,
                allow_cache=allow_cache,
                has_name=False
                )
        else:
            self._url = url_soup.url
            self._soup_obj = url_soup
            self._soup_obj.allow_cache = allow_cache

        self._api_module_block: ApiModuleBlock = None
        self._api_link: ApiLink = None

    # region Properties
    @property
    def soup_obj(self) -> base.SoupObj:
        return self._soup_obj

    @property
    def url_obj(self) -> base.UrlObj:
        return self._soup_obj.url_obj

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
    # endregion Properties

# endregion API Classes

# region Parser Class
class ParserStar:
    @TypeCheckKw(arg_info={'cache': 0}, types=[bool], ftype=DecFuncEnum.METHOD)
    @RuleCheckAllKw(arg_info={'url': rules.RuleStrNotNullEmptyWs}, ftype=DecFuncEnum.METHOD)
    def __init__(self, url: str,**kwargs) -> None:
        self._url: str = url
        self._allow_cache: bool = kwargs.get('cache', True)
        self._api_data = ApiData(
            url_soup=self._url, allow_cache=self._allow_cache)
        self._cache = {}
        
    
    def get_data(self) -> Dict[str, str]:
        key = 'get_data'
        if key in self._cache:
            return self._cache[key]
        data = self._api_data.api_link.get_obj()
        results = []
        for itm in data:
            result = {
                "name": itm.Name,
                "href": itm.href,
                "desc": itm.desc
            }
            results.append(result)
        self._cache[key] = results
        return self._cache[key]

    @property
    def api_data(self) -> ApiData:
        """Gets api_data value"""
        return self._api_data
# endregion Parser Class

# region Writer Class
class WriteStar:
    @TypeCheckKw(arg_info={
        "write_json": 0,
        "print_json": 0,
        "clear_on_print": 0
    },
        types=[bool],
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, parser: ParserStar, **kwargs) -> None:
        self._parser: ParserStar = parser
        self._print_json: bool = kwargs.get('print_json', True)
        self._write_json: bool = kwargs.get('write_json', False)
        self._clear_on_print: bool = kwargs.get('clear_on_print', True)
        self._file_name: bool = kwargs.get('filename', 'star.json')
        self._dir_name: bool = kwargs.get('dirname', 'resources')
        self._path_dir = Path(__file__).parent
        self._cache = {}
        
    def write(self):
        try:
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
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "timestamp": str(base.Util.get_timestamp_utc()),
            "name": 'star links',
            "namespace": self._parser.api_data.url_obj.namespace_str,
            "type": "namespace_url",
            "url_base": self._parser.api_data.url_obj.url_base,
            "url": self._parser.api_data.url_obj.url,
            "data": self._parser.get_data()
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._cache[key] = str_jsn
        return self._cache[key]

    def _get_path(self) -> Path:
        key = '_get_path'
        if key in self._cache:
            return self._cache[key]
        dir_path = Path(self._path_dir.parent, self._dir_name)
        base.Util.mkdirp(dir_path)
        self._cache[key] = dir_path.joinpath(self._file_name)
        return self._cache[key]

    def _write_to_json(self):
        jsn_p = self._get_path()
        jsn_str = self._get_json()
        with open(jsn_p, 'w') as f:
            f.write(jsn_str)
        logger.info("Created file: %s", jsn_p)

# region Writer Class

# region Main

def main():
    global logger
    
    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star.html'
    file_name = 'star.json'
    dir_name = 'resources'
    # region Parser
    parser = argparse.ArgumentParser(description='star')
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=False,
        default=url)
    parser.add_argument(
        '-f', '--file-name',
        help='Dest file',
        type=str,
        dest='file_name',
        required=False,
        default=file_name)
    parser.add_argument(
        '-d', '--dir-name',
        help='Dest directory',
        type=str,
        dest='dir_name',
        required=False,
        default=dir_name)
    parser.add_argument(
        '-x', '--no-cache',
        help='No caching',
        action='store_false',
        dest='cache',
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
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use. Defaults to app.log',
        type=str,
        required=False)
    args = parser.parse_args()
    # endregion Parser
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    if len(sys.argv) > 1:
        logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)
    p = ParserStar(
        url=args.url,
        cache=args.cache,
        filename=args.file_name,
        dirname=args.dir_name
        )
    
    w = WriteStar(
        parser=p,
        write_json=args.write_json,
        print_json=args.print_json
        )
    w.write()

# endregion Main

if __name__ == '__main__':
    main()

# body > div.contents > table > tbody > tr.memitem\:namespacecom_1_1sun_1_1star_1_1accessibility > td.memItemRight > a

# modules can contain other modules such as with chart2: https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html


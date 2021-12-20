# coding: utf-8
"""
Module for reading and parsing area data for a component
Module logger must be set before calling any class or function.
eg: import area
    area.logger = mylogger
"""
from dataclasses import dataclass
import os
import sys
import requests
import logging
import shutil  # to save it locally
import numpy
from pathlib import Path
from typing import Any, Awaitable, Dict, List, Optional, Set, Tuple, Union
import asyncio
import time
from PIL import Image
from bs4.element import ResultSet, Tag
APP_ROOT:str = os.environ.get('project_root', str(Path(__file__).parent.parent.parent))
if not APP_ROOT in sys.path:
    sys.path.insert(0, APP_ROOT)
from parser import base

logger: logging.Logger = None

@dataclass
class Area:
    name: str
    href: str
    x1: int
    y1: int
    x2: int
    y2: int
    title: str = ''

class ApiDyContent(base.BlockObj):
    """Gets dyncontent block that contains area data and image data"""
    def __init__(self, block: base.BlockObj):
        self._block = block
        super().__init__(self._block.soup)
        self._data = False

    def _log_missing(self):
        logger.warning(
            "ApiDyContent.get_obj() Failed to get find data. Url: %s", self.url_obj.url)

    def get_obj(self) -> Union[Tag, None]:
        """Gets dyncontent block that contains area data and image data"""
        if not self._data is False:
            return self._data
        tag: Tag = self._block.get_obj()
        if not tag:
            logger.warning(
                "ApiAreaBlock.get_obj() Failed to get data from self._block. Url: %s", self.url_obj.url)
            return self._data
        tag_dyn = tag.find('div', class_='dyncontent')
        if not tag_dyn:
            self._log_missing()
            return self._data
        self._data = tag_dyn
        return self._data

class ApiAreaBlock(base.BlockObj):
    def __init__(self, block: ApiDyContent):
        self._block: ApiDyContent = block
        super().__init__(self._block.soup)
        self._data = False
    
    def _log_missing(self):
        logger.warning(
            "ApiAreaBlock.get_obj() Failed to get find data. Url: %s", self.url_obj.url)
        
    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        tag: Tag = self._block.get_obj()
        if not tag:
            self._log_missing()
            return self._data
        tag_map = tag.find('map')
        if not tag_map:
            self._log_missing()
            return self._data
        self._data = tag_map
        return self._data


class ApiImage(base.BlockObj):
    """Gets url of image that represents map"""
    def __init__(self, block: ApiDyContent):
        self._block: ApiDyContent = block
        super().__init__(self._block.soup)
        self._data = False

    def _log_missing(self, for_str: Optional[str] = None):
        if for_str:
            f_str = f" for {for_str}"
        else:
            f_str = ''
        logger.warning(
            "ApiImage.get_obj() Failed to get find data%s. Url: %s", f_str, self.url_obj.url)
        
    def get_obj(self) -> Union[str, None]:
        """Gets url of image that represents map"""
        if not self._data is False:
            return self._data
        self._data = None
        tag: Tag = self._block.get_obj()
        if not tag:
            self._log_missing()
            return self._data
        tag_img = tag.find('img')
        if not tag_img:
            self._log_missing()
            return self._data
        src = tag.img.get('src', None)
        if src is None:
            self._log_missing('image src')
            return self._data
        m = base.pattern_http.match(src)
        if m:
            self._data = src
        else:
            self._data = self.url_obj.url_base + '/' + src
        return self._data


class ApiArea(base.BlockObj):
    """List of area items"""

    def __init__(self, block: ApiAreaBlock):
        self._block: ApiAreaBlock = block
        super().__init__(self._block.soup)
        self._data = None

    def _log_missing(self, for_str: Optional[str] = None):
        if for_str:
            f_str = f" for {for_str}"
        else:
            f_str = ''
        logger.warning(
            "ApiArea.get_obj() Failed to get find data%s. Url: %s", f_str, self.url_obj.url)

    def get_obj(self) -> List[Area]:
        """List of area items"""
        if not self._data is None:
            return self._data
        self._data = []
        tag = self._block.get_obj()
        if not tag:
            self._log_missing('ApiAreaBlock instance')
            return self._data
        rs = tag.select('area')
        if not rs:
            self._log_missing('area tags')
            return self._data
        for el in rs:
            href = el.get('href', None)
            if not href:
                self._log_missing('area href')
                continue
            name = el.get('alt', None)
            if not name:
                self._log_missing('area alt')
                continue
            coords = el.get('coords', None)
            if not coords:
                self._log_missing('area cords')
                continue
            title = el.get('title', '')
            a_coords = coords.split(',')
            if len(a_coords) != 4:
                logger.warning(
                    "ApiArea.get_obj() Bad Coords for %s. Url: %s", name, self.url_obj.url)
                continue
            x1 = int(a_coords[0].strip())
            y1 = int(a_coords[1].strip())
            x2 = int(a_coords[2].strip())
            y2 = int(a_coords[3].strip())
            m = base.pattern_http.match(href)
            if not m:
                href = self.url_obj.url_base + '/' + href
            area = Area(name=name,href=href,x1=x1,y1=y1,x2=x2,y2=y2,title=title)
            self._data.append(area)

class AreaFilter:
    def __init__(self, alst: List[Area], is_inherited: bool) -> None:
        self._lst = alst
        self._is_inherited = is_inherited
        self._first: Area = None if len(self._lst) == 0 else self._lst[0]
        
    def get_inherited(self) -> Union[List[Area], None]:
        if self._is_inherited is False:
            return None
        if self._first is None:
            return None
        d_lst = self._list_dict(lst=self._lst)
        match_lst = d_lst[self._first.y1]
        in_lst = [area for area in match_lst] # make a copy
        # remove first first group
        # del d_lst[self._first.y1]
        
        # get a list of all other upper area items.
        upper: List[Area] = []
        keys = list(d_lst.keys()) # list of y1
        for k in keys:
            if k < self._first.y1:
                upper.extend(d_lst[k])
        if len(upper) == 0:
            return match_lst
        # search for name in upper that are in inherited.
        # if found then remove from inherited.
        unique_names: Set[str] = set()
        for area in upper:
            unique_names.add(area.name)
        remove_indexes: List[int] = []
        for i, area in enumerate(match_lst):
            if area.name in unique_names:
                remove_indexes.append(i)
        if len(remove_indexes) == 0:
            return match_lst
        remove_indexes.sort(reverse=True)
        for i in remove_indexes:
            match_lst.pop(i)
        return match_lst

    def _list_dict(self, lst: List[Area]) -> Dict[int, List[Area]]:
        d = {}
        for area in lst:
            if not area.y1 in d:
                d[area.y1] = []
            d[area.y1].append(area)
        return d
    
    def _get_group_by(self, lst:List[Area]) -> List[List[Area]]:
        # use y1 as key to get all items that are on same row level
        d = self._list_dict(lst)
        result: List[List[Area]] = []
        for _, v in d.items():
            result.append(v)
        return result
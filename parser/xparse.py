#!/usr/bin/env python
import os
import sys
import argparse
from typing import Dict, List
from bs4 import BeautifulSoup
from bs4.element import NavigableString, PageElement, ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, RequireArgs
from kwhelp import rules
from collections import namedtuple
from base import TYPE_MAP, TagsStrObj, WriteBase, ParserBase, SoupObj, UrlObj, BlockObj, str_clean
from pathlib import Path
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
from logger.log_handle import get_logger
from parser.enm import main
from dataclasses import dataclass
from enum import IntEnum
logger = get_logger(Path(__file__).stem)

class DirectionEnum(IntEnum):
    IN = 1
    OUT = 2

@dataclass
class MethodBlockInfo:
    tag_id: Tag
    tag_title: Tag
    tag_main: Tag

@dataclass
class ParamInfo:
    dir_info: DirectionEnum
    name: str
    type_info: str
    

class MethodBlock:
    def __init__(self, block: Tag, blocks: 'MethodBlocks'):
        self._block: Tag = block
        self._blocks: MethodBlocks = blocks
        self._data = None

    def _get_next_sibling(self, el:PageElement) -> PageElement:
        # get the next sibling recursivly because
        # BeautifulSoup will also find whitesapce on next_sibling
        if not isinstance(el, PageElement):
            raise TypeError(f"MethodBlock._get_next_sibling() el is not a PageElement")
        next = el.next_sibling
        # https://stackoverflow.com/questions/10711116/strip-spaces-tabs-newlines-python
        # use split join to remove whitespace and new line
        s = ''.join(str(next).split())
        if s == '':
            next = self._get_next_sibling(next)
        return next

    def get_obj(self) -> MethodBlockInfo:
        # BeautifulSoup will also find whitesapce on next_sibling
        # https://stackoverflow.com/questions/5690686/using-nextsibling-from-beautifulsoup-outputs-nothing
        if self._data:
            return self._data
        tag = self._block # a tag with id
        try:
            title: PageElement = self._get_next_sibling(tag)
            main = self._get_next_sibling(title)
            mi = MethodBlockInfo(
                tag_id=tag,
                tag_title=title,
                tag_main=main
            )
        except Exception as e:
            logger.error(e)
            raise e
        self._data = mi
        return self._data

    def is_valid(self) -> bool:
        if not self._block:
            return False
        tag = self._block
        _id = tag.attrs.get('id', None)
        if not _id:
            return False
        if str(_id).lower() == 'details':
            return False
        return True
        

    @property
    def blocks(self) -> 'MethodBlocks':
        """
        Gets MethodBlocks instance that generated this instance.
        """
        return self._blocks
    

class MethodBlocks(BlockObj):
    """Get all methods"""

    def __init__(self, soup: SoupObj):
        super().__init__(soup=soup)
        self._obj_data = None
        self._index = 0
        self._len = 0

    def get_obj(self) -> ResultSet:
        """
        Gets all items, methods etc

        Returns:
            ResultSet: List of items
        """
        if self._obj_data:
            return self._obj_data
        # _cls = 'memitem'
        self._obj_data = self._soup.soup.select("a[id]")
        
        return self._obj_data
    
    def _get_next(self) -> MethodBlock:
        if self._index >= self._len:
            self._index = 0
            self._cur_obj = None
            raise StopIteration
        itm = self._obj_data[self._index]
        self._index += 1
        mb = MethodBlock(block=itm, blocks=self)
        if not mb.is_valid():
            mb = self._get_next()
        return mb

    def __iter__(self):
        # if not self._obj_data:
        #     self.get_obj()
        #     self._len = len(self._obj_data)
        return self
    
    def __next__(self) -> MethodBlock:
        if not self._obj_data:
            self.get_obj()
            self._len = len(self._obj_data)
        return self._get_next()

# body > div.contents > div:nth-child(18) > div.memproto > table > tbody > tr > td.memname

class MethodName:
    def __init__(self, block: MethodBlock):
        self._block: MethodBlock = block
    
    def get_obj(self) -> str:
        info = self._block.get_obj()
        name:str = info.tag_title.contents[1]
        name = name.replace('(', '').replace(')', '').strip()
        return name

class ParamNameReturnBlock:
    """
    Responsible for parsing the first param of a method.
    Only the first param.
    The first param alos contains return type if there is one.
    """
    def __init__(self, block: Tag):
        self._block = block
        self._data = None
        self._type_info = None
    
    def get_obj(self) -> Dict[str, object]:
        """
        Gets a dictionary that represents the first parameter and return type of
        a method

        Returns:
            Dict[str, object]: {
                "returns: "the python return type of the method",
                "name": "Optional, Name of the first param of the method",
                "param_type": "Optional, Python type of the first parameter",
                "direction": "Optional, The direction of the firt parameter. ``DirectionEnum`` value",
                
            }
        """
        if self._data:
            return self._data
        parts = str(self._block.find('td', class_='memname').contents[0]).split()
        returns = TYPE_MAP.get(parts[0], parts[0])
        result = {
            "returns": str_clean(returns)
        }
        if self.is_valid():
            # get first param if it exist
            # there is a pramname td even for methods with no parameters
            p_name = ParamNameBlock(block=self._block)
            p_name_str = p_name.get_obj()
            if p_name:
                result['name'] = p_name_str
                parm_type = self._get_type_info()
                result.update(parm_type.get_obj())
        self._data = result
        return self._data

    def _get_type_info(self):
        if not self._type_info:
            self._type_info = ParamTypeBlock(block=self._block)
        return self._type_info

    def is_valid(self) -> bool:
        p_type = self._get_type_info()
        data = p_type.get_obj()
        return 'param_type' in data

class ParamNameBlock:
    """
    Responsible for getting parameter name for a method.
    """
    def __init__(self, block: Tag):
        self._block = block
        self._data = None
    
    def get_obj(self) -> str:
        """
        Get the name of the parameter

        Returns:
            str: Name of parameter if found; Otherwise, empty string.
        """
        if self._data:
            return self._data
        tag = self._block.find('td', class_='paramname')
        result = ''
        if tag:
            name = tag.find('em')
            if name:
                result = str_clean(name.text.strip())
            else:
                result = tag.text.strip()
                result = str_clean(result)
        self._data = result
        return self._data

class ParamTypeBlock:
    """
    Responsible for parsing param type only.
    Processes values such as:
        sequence< char >
        [in] string
    """
    def __init__(self, block: Tag):
        self._block = block
        self._data = None
        
    def get_obj(self) -> Dict[str, object]:
        """
        Gets a dictionary that represents parmeter type info
        Returns:
            Dict[str, object]: {
                "param_type": "Optional, Python type of the first parameter",
                "direction": "Optional, The direction of the firt parameter. ``DirectionEnum`` value",
                
            }
        """
        if self._data:
            return self._data
        self._data = self._parse_param()
        return self._data
    
    def _parse_param(self) -> dict:
        tag = self._block.find('td', class_='paramtype')
        result = {}
        if not tag:
            return result
        # [out] sequence< char > or [in] string
        type_str = tag.text.strip()
        parts = type_str.split()
        result['direction'] = DirectionEnum.IN
        if parts[0].startswith('['):
            s_dir = parts[0].replace(
                '[', '').replace(']', '').strip().lower()
            if s_dir == 'out':
                result['direction'] = DirectionEnum.OUT
            del parts[0]
        result.update(self._parse_param_type(parts=parts))
        return result

    def _parse_param_type(self, parts: List[str]) -> dict:
        result = {}
        # ['sequence<', 'char', '>']
        # or
        # ['string']
        if len(parts) == 1:
            result['param_type'] = TYPE_MAP.get(parts[0], str_clean(parts[0]))
        if len(parts) == 3:
            seq = parts[0].replace('<', '').strip()
            seq_type = TYPE_MAP.get(seq, 'list')
            s_type = TYPE_MAP.get(parts[1], str_clean(parts[1]))
            if seq_type == 'list':
                result['param_type'] = f"List[{s_type}]"
            else:
                result['param_type'] = f"{seq_type}[{s_type}]"
        return result


class ParamBlock:
    """
    Gets the name and type of a method parameter
    """
    def __init__(self, block: Tag):
        self._block = block
        self._data = None
        
    def get_obj(self):
        """
        Gets a dictionary that represents name and type of a parameter

        Returns:
            Dict[str, object]: {
                "name": "Optional, Name of the first param of the method",
                "param_type": "Optional, Python type of the first parameter",
                "direction": "Optional, The direction of the firt parameter. ``DirectionEnum`` value",
            }
        """
        if self._data:
            return self._data
        p_name = ParamNameBlock(block=self._block)
        result = {}
        name = p_name.get_obj()
        if name:
            p_type = ParamTypeBlock(block=self._block)
            result = p_type.get_obj()
            result['name'] = name
        self._data = result
        return self._data

class ParamsBlock:
    def __init__(self, block: MethodBlock):
        self._block = block
        self._data = None
    
    def get_obj(self) -> List[ParamInfo]:
        if self._data:
            return self._data
        el = 'table'
        _cls = 'memname'
        info = self._block.get_obj()
        tag = info.tag_main.find(el, class_=_cls)
        rows = tag.findChildren(['th', 'tr'])
        results = []
        row_count = len(rows)
        # handle first row sepertaly as it has different block attribs
        # returns = 'None'
        
        # last row can just be closing of method and containd only ')'
        if row_count > 0:
            first = ParamNameReturnBlock(block=rows[0])
            first_data = first.get_obj()
            # returns = first_data['returns']
            name = first_data.get('name', None)
            if name:
                type_info = first_data.get('param_type', '')
                direction = first_data.get('direction', DirectionEnum.IN)
                p_info = ParamInfo(dir_info=direction,
                                name=name, type_info=type_info)
                results.append(p_info)
        if row_count > 1:
            for i in (1, row_count -1):
                direction = DirectionEnum.IN
                name = ''
                type_info = ''
                p_block = ParamBlock(block=rows[i])
                p_block_data = p_block.get_obj()
                name = p_block_data.get('name', None)
                if name:
                    type_info = p_block_data.get('param_type', '')
                    direction = p_block_data.get('direction', DirectionEnum.IN)
                    p_info = ParamInfo(dir_info=direction,
                                    name=name, type_info=type_info)
                    results.append(p_info)
            
        self._data = results
        return self._data

def main():
    url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XFont.html'
    soup = SoupObj(url=url)
    m_blocks = MethodBlocks(soup=soup)
    for block in m_blocks:
        params = ParamsBlock(block=block)
        p_data = params.get_obj()
        for p in p_data:
            print(p)

if __name__ == '__main__':
    main()
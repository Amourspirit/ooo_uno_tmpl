# coding: utf-8
from typing import List
from bs4.element import ResultSet
from .api_desc_detail_since import ApiDescDetailSince
from ..web.block_obj import BlockObj
from ..web.tag_str_obj import TagsStrObj

class ApiDescDetail(BlockObj):
    """Gets description of a detail block section"""

    def __init__(self, block: BlockObj) -> None:
        self._block: BlockObj = block
        super().__init__(self._block.soup)
        self._data = None
        self._cls = 'memdoc'
        self._el = 'div'

    def get_obj(self) -> List[str]:
        if not self._data is None:
            return self._data
        self._data = []
        tag = self._block.get_obj()
        if not tag:
            return self._data
        lines_found: ResultSet = tag.select(f'{self._el}.{self._cls} > p')
        if not lines_found:
            return self._data
        p_obj = TagsStrObj(tags=lines_found)
        self._data = p_obj.get_lines()
        since_obj = ApiDescDetailSince(self._block)
        since = since_obj.get_obj()
        if since:
            self._data.append('')
            self._data.append('**since**')
            self._data.append('')
            self._data.append(f"    {since}")
        return self._data

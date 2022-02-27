# coding: utf-8
from typing import Union
from bs4.element import Tag
from .api_detail_block import ApiDetailBlock
from ..web.block_obj import BlockObj


class ApiDescBlock(BlockObj):
    """Gets Detailed description block of method or component"""

    def __init__(self, block: ApiDetailBlock) -> None:
        self._block: ApiDetailBlock = block
        super().__init__(self._block.soup)
        self._data = False

    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        tag = self._block.get_obj()
        if not tag:
            return self._data
        desc = tag.findChild('div', class_='memdoc')
        self._data = desc
        return self._data

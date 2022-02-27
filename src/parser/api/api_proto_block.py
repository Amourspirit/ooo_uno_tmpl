# coding: utf-8
from typing import Union
from bs4.element import Tag
from .api_detail_block import ApiDetailBlock
from ..web.block_obj import BlockObj


class ApiProtoBlock(BlockObj):
    """Gets Detailed data block"""

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
        proto = tag.findChild('div', class_='memproto')
        self._data = proto
        self._data

# coding: utf-8
from typing import Union
from bs4.element import Tag
from ..web.block_obj import BlockObj


class ApiDescDetailSince(BlockObj):
    """Gets the Since part if it exist of a detailed block section"""

    def __init__(self, block: BlockObj) -> None:
        self._block: BlockObj = block
        super().__init__(self._block.soup)
        self._data = False

    def get_obj(self) -> Union[str, None]:
        if not self._data is False:
            return self._data
        self._data = None
        tag: Tag = self._block.get_obj()
        if not tag:
            return self._data
        dl_tag = tag.select_one('dl.section.since')
        if not dl_tag:
            return self._data
        dd_tag = dl_tag.find('dd')
        if not dd_tag:
            return self._data
        self._data = dd_tag.text.strip()
        return self._data

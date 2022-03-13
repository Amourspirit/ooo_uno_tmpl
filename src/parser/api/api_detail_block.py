# coding: utf-8
from typing import Union
from bs4.element import Tag
from ..web.soup_obj import SoupObj
from ..web.block_obj import BlockObj


class ApiDetailBlock(BlockObj):
    """Get Details block from block id"""

    def __init__(self, soup: SoupObj, a_id: str) -> None:
        """
        ApiDetailBlock Constructor

        Args:
            soup (base.SoupObj): Soup Obj
            a_id (str): id of block such as ``aa1d747451151fbd244196e6305348dbc``
        """
        super().__init__(soup)
        self._a_d = a_id
        self._data = False

    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        soup = self.soup.soup
        a_tag: Tag = soup.find('a', id=self._a_d)
        if not a_tag:
            return self._data
        self._data = a_tag.find_next('div', class_='memitem')
        return self._data

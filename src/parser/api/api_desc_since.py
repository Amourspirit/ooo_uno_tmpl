# coding: utf-8
from typing import Union
from ..web.soup_obj import SoupObj
from ..web.block_obj import BlockObj


class ApiDescSince(BlockObj):
    """Gets the Since if it exist"""

    def __init__(self, soup: SoupObj):
        super().__init__(soup)
        self._data = False

    def get_obj(self) -> Union[str, None]:
        """
        Gets See alos of Interface

        Returns:
            str: See also. if it exist; Otherwise empty string.
        """
        if not self._data is False:
            return self._data
        self._data = None
        dl_tag = self._soup.soup.select_one('dl.section.since')
        if not dl_tag:
            return self._data
        dd_tag = dl_tag.find('dd')
        if not dd_tag:
            return self._data
        self._data = dd_tag.text.strip()
        return self._data

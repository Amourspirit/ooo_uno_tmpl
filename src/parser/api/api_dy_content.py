# coding: utf-8
import logging
from typing import Union
from bs4.element import Tag
from ..web.soup_obj import SoupObj
from ..web.block_obj import BlockObj
from ..common.log_load import Log
log = Log()

class ApiDyContent(BlockObj):
    """Gets dyncontent block that contains area data and image data"""

    def __init__(self, soup: SoupObj):
        """
        Constructor

        Args:
            block (BlockObj): Block obj containing full page html
        """
        super().__init__(soup)
        self._data = False

    def _log_missing(self):
        log.logger.warning(
            "ApiDyContent.get_obj() Failed to get find data. Url: %s", self.url_obj.url)

    def get_obj(self) -> Union[Tag, None]:
        """Gets dyncontent block that contains area data and image data"""
        if not self._data is False:
            return self._data
        soup = self.soup.soup
        tag_dyn = soup.find('div', class_='dyncontent')
        if not tag_dyn:
            self._log_missing()
            return self._data
        self._data = tag_dyn
        return self._data
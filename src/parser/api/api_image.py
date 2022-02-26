# coding: utf-8
import logging
from typing import Union, Optional
from bs4.element import Tag
from ..web.block_obj import BlockObj
from .api_dy_content import ApiDyContent
from ..common.regx import pattern_http
from ..common import log_load
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger


class ApiImage(BlockObj):
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
        m = pattern_http.match(src)
        if m:
            self._data = src
        else:
            self._data = self.url_obj.url_base + '/' + src
        return self._data

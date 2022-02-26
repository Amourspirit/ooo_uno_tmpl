# coding: utf-8
import logging
from typing import Union
from bs4.element import Tag
from ..web.block_obj import BlockObj
from .api_dy_content import ApiDyContent
from ..common import log_load
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger


class ApiAreaBlock(BlockObj):
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

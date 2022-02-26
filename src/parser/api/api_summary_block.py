# coding: utf-8
import logging
from typing import Union
from bs4.element import Tag
from abc import abstractmethod
from .api_public_members import ApiPublicMembers
from ..web.soup_obj import SoupObj
from ..web.block_obj import BlockObj
from ..common import log_load
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger


class ApiSummaryBlock(BlockObj):
    """
    Abstract class for getting sumary block form ApiPublicMembers
    """

    def __init__(self, block: ApiPublicMembers):
        self._block: ApiPublicMembers = block
        super().__init__(self._block.soup)
        self._data = False

    @abstractmethod
    def _get_match_name(self) -> str:
        """
        Name of a sction to match

        Returns:
            str: section heading name such as ``interfaces``
        """

    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        rs = self._block.get_obj()
        if not rs:
            return self._data
        match_name = self._get_match_name()
        for tag in rs:
            # tag is a table
            # body > div.contents > table > tbody > tr.heading > td > h2 > a
            t: Tag = tag
            a_lnk = t.select_one('tr.heading > td > h2 > a')
            if a_lnk:
                name = a_lnk.get('name', None)
                if name == match_name:
                    self._data = tag
                    break
        if self._data is None and logger.level <= logging.WARNING:
            logger.warning(
                "ApiSummaryBlock.get_obj() No summary block found for '%s'", match_name)
        return self._data

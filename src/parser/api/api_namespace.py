# coding: utf-8
import logging
from typing import List
from bs4.element import Tag
from ..web.soup_obj import SoupObj
from ..web.block_obj import BlockObj
from ..common.log_load import Log
log = Log()


class ApiNamespace(BlockObj):
    """Get the Namespace object for component"""

    def __init__(self, soup: SoupObj):
        super().__init__(soup)
        self._data = None
        self.__namespace_str = None
        self.__namespace = None

    def get_obj(self) -> List[str]:
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        self._data = []
        try:
            tag_div_nav: Tag = soup.select_one('div#nav-path')
            names = tag_div_nav.find_all('li', class_='navelem')
            for name in names:
                self._data.append(name.text.strip())
            return self._data
        except Exception as e:
            log.logger.error(
                "ApiNamespace.get_obj() Error getting Namespace.", exc_info=True)
            raise e

    @property
    def namespace(self) -> List[str]:
        """Gets namespace value"""
        if self.__namespace is None:
            self.__namespace = self.get_obj()
        return self.__namespace

    @property
    def namespace_str(self) -> str:
        if self.__namespace_str is None:
            self.__namespace_str = '.'.join(self.namespace)
        return self.__namespace_str

# coding: utf-8
from typing import Union
from bs4.element import ResultSet
from kwhelp.decorator import TypeCheck, DecFuncEnum
from ..web.soup_obj import SoupObj
from ..web.block_obj import BlockObj


class ApiPublicMembers(BlockObj):
    """Gets all blocks with condensed info such as Public Member Functions"""
    @TypeCheck(SoupObj, ftype=DecFuncEnum.METHOD)
    def __init__(self, soup: SoupObj):
        self._soup = soup
        super().__init__(soup)
        self._data = False

    def get_obj(self) -> Union[ResultSet, None]:
        if not self._data is False:
            return self._data
        self._data = None
        soup = self.soup.soup
        rs = soup.find_all('table', class_='memberdecls')
        self._data = rs
        return self._data

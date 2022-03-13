# coding: utf-8
from bs4.element import ResultSet
from typing import List
from .api_desc_since import ApiDescSince
from .api_depreciated import ApiDepreciated
from ..web.soup_obj import SoupObj
from ..web.block_obj import BlockObj
from ..web.tag_str_obj import TagsStrObj


class ApiDesc(BlockObj):
    """Gets the description"""

    def __init__(self, soup: SoupObj):
        super().__init__(soup)
        self._data = None

    def get_obj(self) -> List[str]:
        """
        Gets description as list of str

        Returns:
            List[str]: description lines
        """
        if self._data:
            return self._data
        lines_found: ResultSet = self.soup.soup.select(
            'body > div.contents > div.textblock > p')
        p_obj = TagsStrObj(tags=lines_found)
        self._data = p_obj.get_lines()
        since_obj = ApiDescSince(self.soup)
        since = since_obj.get_obj()
        if since:
            self._data.append('')
            self._data.append('**since**')
            self._data.append('')
            self._data.append(f"    {since}")
        # .. deprecated::
        dep_obj = ApiDepreciated(self.soup)
        dep = dep_obj.get_obj()
        if dep:
            self._data.append('')
            self._data.append('.. deprecated::')
            self._data.append('')
            self._data.append('    Class is deprecated.')
        return self._data

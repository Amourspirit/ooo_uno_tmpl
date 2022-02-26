# coding: utf-8
from typing import List
from bs4.element import Tag, ResultSet
from .api_summary_block import ApiSummaryBlock
from ..web.block_obj import BlockObj


class ApiSummaryRows(BlockObj):
    """Gets the rows that contain short details and desc for a Function/properyty block"""

    def __init__(self, block: ApiSummaryBlock):
        self._block: ApiSummaryBlock = block
        super().__init__(self._block.soup)
        self._data = None

    def get_obj(self) -> List[Tag]:
        if not self._data is None:
            return self._data
        self._data = []
        tbl_tag: Tag = self._block.get_obj()
        if not tbl_tag:
            return self._data
        rs_rows: ResultSet = tbl_tag.find_all('tr')
        if not rs_rows:
            return self._data
        for row in rs_rows:
            r: Tag = row
            _class = r.get('class', [])
            if len(_class) == 0:
                continue
            class_str = _class[0]
            if class_str == 'inherit_header':
                # Public Member Functions inherited from ...
                break
            if class_str.startswith('memitem:'):
                self._data.append(row)
        return self._data

# coding: utf-8
from typing import Union, List
from bs4.element import Tag, ResultSet
from .api_proto_block import ApiProtoBlock
from ..dataclass.summary_info import SummaryInfo
from ..web.block_obj import BlockObj


class ApiMethodException(BlockObj):
    """Gets errors for a funciton"""
    # have not found an example with more than one exception so assuming
    # singular excpetion
    # returning as a list of str for future consideration

    def __init__(self, block: ApiProtoBlock) -> None:
        self._block: ApiProtoBlock = block
        super().__init__(self._block.soup)
        self._data = False

    def _get_raises_lst(self) -> List[str]:
        # rows for raise a bit messy.
        # see: https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XTimeContainer.html
        # first row of raise will contain only the first exception.
        # if there is another exception then the row text should end with a comma
        row: Tag = None

        def ex_gen():
            nonlocal row
            while row:
                if row is None:
                    break
                text = self._get_raises_text(row)
                s = text
                if text.endswith(","):
                    row = row.find_next_sibling('tr')
                    s = s.rstrip(',')
                else:
                    row = None
                yield s

        results = []
        row = self._get_raises_row()
        if not row:
            return results
        # errs = ex()
        for err in ex_gen():
            results.append(err)
        return results

    def _get_raises_row(self) -> Union[Tag, None]:
        proto = self._block.get_obj()
        rows: ResultSet = proto.find_all('tr')
        result = None
        for row in rows:
            td: Tag = row.select_one('td')
            if td.text.strip().lower() == 'raises':
                result = row
                break
        return result

    def _get_raises_text(self, row: Tag):
        if not row:
            return None
        parts = row.text.rsplit(maxsplit=1)  # in case starts with raises
        s: str = parts.pop()
        s = s.replace('(', '').replace(')', '').replace(
            '::', '.').strip().lstrip('.')
        return s

    def get_obj(self) -> Union[List[str], None]:
        """
        Get name of error that is raises

        Returns:
            Union[str, None]: String containing type of error if it exist; Otherwise, ``None``
        """
        if not self._data is False:
            return self._data
        self._data = None
        # row = self._get_raises_row()
        # if not row:
        #     return self._data
        # self._data = [self._get_raises_text(row)]
        self._data = self._get_raises_lst()
        return self._data

    @property
    def summary_info(self) -> SummaryInfo:
        """Gets summary_info value"""
        return self._block.summary_info

# coding: utf-8
import logging
from typing import List, Optional
from .api_area_block import ApiAreaBlock
from ..web.block_obj import BlockObj
from ..dataclass.ns import Ns
from ..dataclass.area import Area
from ..common.regx import pattern_http
from ..common.constants import URL_SPLIT
from ..common.log_load import Log
log = Log()


class ApiArea(BlockObj):
    """List of area items"""

    def __init__(self, block: ApiAreaBlock):
        self._block: ApiAreaBlock = block
        super().__init__(self._block.soup)
        self._data = None

    def _log_missing(self, for_str: Optional[str] = None):
        if for_str:
            f_str = f" for {for_str}"
        else:
            f_str = ''
        log.logger.warning(
            "ApiArea.get_obj() Failed to get find data%s. Url: %s", f_str, self.url_obj.url)

    def _get_ns(self, name: str, href: str) -> Ns:
        parts = href.split(sep=URL_SPLIT)
        parts[0] = 'com'  # rename interfacecom etc...
        parts.pop()  # drop XShapeDescriptor.html etc...
        ns = ".".join(parts)
        return Ns(name=name, namespace=ns)

    def get_obj(self) -> List[Area]:
        """List of area items"""
        if not self._data is None:
            return self._data
        self._data = []
        tag = self._block.get_obj()
        if not tag:
            self._log_missing('ApiAreaBlock instance')
            return self._data
        rs = tag.select('area')
        if not rs:
            self._log_missing('area tags')
            return self._data
        for el in rs:
            href = el.get('href', None)
            if not href:
                self._log_missing('area href')
                continue
            name = el.get('alt', None)
            if not name:
                self._log_missing('area alt')
                continue
            coords = el.get('coords', None)
            if not coords:
                self._log_missing('area cords')
                continue
            title = el.get('title', '')
            a_coords = coords.split(',')
            if len(a_coords) != 4:
                log.logger.warning(
                    "ApiArea.get_obj() Bad Coords for %s. Url: %s", name, self.url_obj.url)
                continue
            ns = self._get_ns(name=name, href=href)
            x1 = int(a_coords[0].strip())
            y1 = int(a_coords[1].strip())
            x2 = int(a_coords[2].strip())
            y2 = int(a_coords[3].strip())
            m = pattern_http.match(href)
            if not m:
                href = self.url_obj.url_base + '/' + href
            area = Area(name=name, ns=ns, href=href, x1=x1,
                        y1=y1, x2=x2, y2=y2, title=title)
            self._data.append(area)
        return self._data

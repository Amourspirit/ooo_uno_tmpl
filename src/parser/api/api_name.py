# coding: utf-8
# import logging
from bs4.element import Tag
from ..web.block_obj import BlockObj
from ..web.soup_obj import SoupObj
from ..dataclass.name_info import NameInfo
from ..rules.name.i_rules_name import IRulesName
from ..common.log_load import Log
log = Log()

class ApiName(BlockObj):
    """Get the Name object for the interface"""

    def __init__(self, soup: SoupObj, rules_engine: IRulesName = None):
        super().__init__(soup)
        self._data = None
        self._rules_engine = rules_engine

    def get_obj(self) -> NameInfo:
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        try:
            tag_div_nav: Tag = soup.select_one('div#nav-path')
            name = tag_div_nav.find_all(
                'li', class_='navelem')[-1].text.strip()
            ni = NameInfo(name=name, orig_name=name)
            if self._rules_engine:
                self._rules_engine.process_name(ni)

            self._data = ni
            return self._data
        except Exception as e:
            log.logger.error(
                "ApiName.get_obj() Error getting name.", exc_info=True)
            raise e

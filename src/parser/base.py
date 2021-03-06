# coding: utf-8
"""
Base classes and helper functions of various types that are used with different parsers.
"""
# region imports

from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from glob import glob
from kwhelp.decorator import DecFuncEnum, RequireArgs, RuleCheckAllKw
from kwhelp import rules
from pathlib import Path
from typing import List,Union
from .common.constants import URL_SPLIT as URL_SPLIT, APP_ROOT as APP_ROOT
from .common.config import APP_CONFIG as APP_CONFIG
from .common.util import Util as Util, str_clean
from .web.response_obj import ResponseObj
# endregion imports

# region Writer/parser base
class WriteBase(object):
    def __init__(self, **kwargs):
        pass

    def _mkdirp(self, dest_dir):
        Util.mkdirp(dest_dir=dest_dir)

    def _get_project_path(self) -> Path:
        return Path(__file__).parent.parent

    def _get_template_path(self) -> Path:
        project_path = self._get_project_path()
        return project_path.joinpath('template')

    def _get_template_files(self) -> List[str]:
        p = self._get_template_path()
        pattern = str(p) + '/_*.py'
        files = glob(pattern, recursive=False)
        return files


class ParserBase(object):
    @RequireArgs('url', ftype=DecFuncEnum.METHOD)
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "cache": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        self._allow_cache: bool = kwargs.get('cache', True)
        self._indent = '    '
        self._url = kwargs.get('url', '')
        self._raw = ''
        self._sort = kwargs.get('sort', True)
        self._replace_dual_colon = kwargs.get('replace_dual_colon', True)
        self._title_full = None
        self._response_obj = None

    # region internal Non specific methods
    def _get_number(self, input: str) -> Union[str, int, float]:
        if not input:
            return ''
        try:
            return int(input)
        except ValueError:
            pass
        try:
            return int(input, 16)
        except ValueError:
            pass
        try:
            return float(input)
        except ValueError:
            pass
        return input
    # endregion internal Non specific methods

    # region request
    def get_request_text(self, url: str) -> str:
        if self._response_obj is None:
            if self.allow_cache:
                self._response_obj = ResponseObj(url=url)
            else:
                self._response_obj = ResponseObj(url=url, cache_seconds=0)
        return self._response_obj.raw_html

    # endregion request

    # region raw html

    def get_raw_html(self) -> str:
        if not self._url:
            return ''
        if not self._raw:
            self._raw = self.get_request_text(self.url)
        return self._raw

    # endregion raw html

    # region Info
    def _get_full_name(self, soup: BeautifulSoup) -> str:
        """
        Gets full name from nav bar

        Returns:
            str: such as com.sun.star.awt.AdjustmentEvent
        """
        if self._title_full is None:
            nav = soup.find('div', id='nav-path')
            els = nav.find_all('a', class_='el')
            text = ''
            for i, el in enumerate(els):
                if i > 0:
                    text += '.'
                text += el.text.strip()
            # text = nav.text.replace('\n', '.').strip()
            self._title_full = Util.get_clean_classname(text)
        return self._title_full

    def _get_name(self, soup: BeautifulSoup):
        full = self._get_full_name(soup=soup)
        parts = full.split('.')
        return parts[len(parts) - 1]

    def _get_desc(self, soup: BeautifulSoup) -> List[str]:
        lines = []
        contents = soup.find('div', class_='contents')
        if not contents:
            return lines
        block = contents.find('div', class_='textblock')
        if not block:
            return lines
        soup_lines: ResultSet = block.find_all('p')
        if not soup_lines:
            return lines
        for i, ln in enumerate(soup_lines):
            s = ln.text.strip().replace('::', '.')
            if i > 0:
                lines.append("")
            lines.append(s)
        since = self._get_since(block=block)
        if len(since) > 0:
            lines.append('')
            lines.extend(since)
        # result = "\n".join(lines)
        return lines

    def _get_since(self, block: Tag) -> List[str]:
        result = []
        since = block.find('dl', class_='section since')
        if since:
            s = since.find('dd').text.strip()
            result.append("**Since**")
            result.append("")
            result.append(self._indent + s)
        return result
    # endregion Info

    # region Tidy
    def _clean_str(self, input: str) -> str:
        """
        Cleans and encodes string for template replacemnt
        """
        return str_clean(input=input, replace_dual=self._replace_dual_colon)

    # endregion Tidy

    # region Data
    def _get_memitems(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all('div', class_='memitem')

    # endregion Data

    # region util
    def camel_to_snake(self, name: str) -> str:
        """
        Converts Camel case to snake clase

        Args:
            name (str): Camel name

        Returns:
            str: snake case
        """
        return Util.camel_to_snake(name)

    # endregion util

    # region Properties

    @property
    def sort(self) -> bool:
        """Specifies sort

            :getter: Gets sort value.
            :setter: Sets sort value.
        """
        return self._sort

    @sort.setter
    def sort(self, value: bool):
        self._sort = value

    @property
    def url(self) -> str:
        """Specifies url

            :getter: Gets url value.
            :setter: Sets url value.
        """
        return self._url

    @url.setter
    def url(self, value: str):
        self._url = value

    @property
    def allow_cache(self) -> bool:
        """Specifies allow_cache

            :getter: Gets allow_cache value.
            :setter: Sets allow_cache value.
        """
        return self._allow_cache

    @allow_cache.setter
    def allow_cache(self, value: bool):
        self._allow_cache = value
    # endregion Properties

# endregion Writer/parser base

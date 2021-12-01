from typing import List, Union
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
import requests
import re

TYPE_MAP = {
    "short": "int",
    "long": "int",
    "float": "float",
    "double": "float",
    "string": "str",
    "char": "str",
    "boolean": "bool"
}
class WriteBase(object):
    def _mkdirp(self, dest_dir):
        # Python ≥ 3.5
        if isinstance(dest_dir, Path):
            dest_dir.mkdir(parents=True, exist_ok=True)
        else:
            Path(dest_dir).mkdir(parents=True, exist_ok=True)

class ParserBase(object):
    def __init__(self, **kwargs):
        self._indent = '    '
        self._url = kwargs.get('url', '')
        self._raw = ''
        self._sort = kwargs.get('sort', True)
        self._replace_dual_colon = kwargs.get('replace_dual_colon', True)
        self._title_full = None

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
        response = requests.get(url=url)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        html_text = response.text
        return html_text
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
            self._title_full = text
        return self._title_full
    
    def _get_name(self, soup: BeautifulSoup):
        full = self._get_full_name(soup=soup)
        parts = full.split('.')
        return parts[len(parts) - 1]
    
    def _get_desc(self, soup: BeautifulSoup):
        contents = soup.find('div', class_='contents')
        block = contents.find('div', class_='textblock')
        soup_lines:ResultSet = block.find_all('p')
        lines = []
        for i, ln in enumerate(soup_lines):
            s = ln.text.strip()
            if i > 0:
                lines.append("")
            lines.append(s)
        since = self._get_since(block=block)
        if len(since) > 0:
            lines.append('')
            lines.extend(since)
        result = "\n".join(lines)
        return result
    
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
        result = input
        if self._replace_dual_colon:
            result = result.replace("::", ".")
        result = result.replace('\\n', '\\\\\\\\n').replace('\\r', '\\\\\\\\r')
        result = result.replace('"', '\\"')
        return result.strip()

    # endregion Tidy

    # region Data
    def _get_memitems(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find_all('div', class_='memitem')

    # endregion Data

    # region util
    def camel_to_snake(self, name: str)-> str:
        """
        Converts Camel case to snake clase

        Args:
            name (str): Camel name

        Returns:
            str: snake case
        """
        _name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', _name).lower()

    # endregion util

     # region Properties
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

    # endregion Properties
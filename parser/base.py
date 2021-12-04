import os
import sys
import re
import requests
import textwrap
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from glob import glob
from kwhelp.decorator import DecFuncEnum, RuleCheckAll
from kwhelp import rules
from pathlib import Path
from typing import Iterable, List, Union
sys.path.insert(0, os.path.abspath('.'))
from logger.log_handle import get_logger
logger = get_logger(__name__)

TYPE_MAP = {
    "any": "object",
    "short": "int",
    "long": "int",
    "float": "float",
    "double": "float",
    "string": "str",
    "char": "str",
    "boolean": "bool",
    "sequence": "list",
    "void": "None"
}

def str_clean(input: str, **kwargs) -> str:
        """
        Cleans and encodes string for template replacemnt
        
        Keyword Arguments:
            replace_dual (bool, optional): Replace ``::`` with ``.`` Default ``True``
        """
        _replace_dual = bool(kwargs.get('replace_dual', True))
        result = input
        if _replace_dual:
            result = result.replace("::", ".")
        result = result.replace('\\n', '\\\\\\\\n').replace('\\r', '\\\\\\\\r')
        result = result.replace('"', '\\"')
        return result.strip()
class ResponseObj:
    @RuleCheckAll(rules.RuleStrNotNullEmptyWs, ftype=DecFuncEnum.METHOD)
    def __init__(self, url:str):
        self._url = url
        self._text = None
    
    def _get_request_text(self) -> str:
        response = requests.get(url=self._url)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        html_text = response.text
        return html_text
    
    @property
    def url(self) -> str:
        """Specifies url"""
        return self._url
    
    @property
    def raw_html(self) -> str:
        """
        Gets raw html of url
        """
        if not self._text:
            self._text = self._get_request_text()
        return self._text

class SoupObj:
    @RuleCheckAll(rules.RuleStrNotNullEmptyWs, ftype=DecFuncEnum.METHOD)
    def __init__(self, url:str) -> None:
        self._response = ResponseObj(url)
        self._soup = None
    
    @property
    def soup(self) -> BeautifulSoup:
        """Gets soup for this instance"""
        if not self._soup:
            self._soup = BeautifulSoup(self._response.raw_html, 'lxml')
        return self._soup

    @property
    def response(self) -> ResponseObj:
        """Gets this instance response"""
        return self._response
    
    @property
    def url(self) -> str:
        """Specifies url"""
        return self.response.url

class UrlObj:
    """Properties of url"""
    @RuleCheckAll(rules.RuleStrNotNullEmptyWs, ftype=DecFuncEnum.METHOD)
    def __init__(self, url: str):
        """
        Constructor

        Args:
            url (str): Url
        """
        self._url = url
        # similar to: namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925
        self._page_link = self._url.rsplit('/',1)[1]
        self._is_frag = False
        try:
            self._fragment = self._page_link.split('#')[1]
            self._is_frag = True
        except IndexError:
            self._fragment = ''
        self._ns = self._get_ns()
        self._ns_str = None
    
    def _get_ns(self) -> List[str]:
        ns_part = self._page_link.split('.')[0].lower()
        if ns_part.startswith('namespace'):
            ns_part = ns_part[9:]
        return ns_part.split('_1_1')

    @property
    def page_link(self) -> str:
        """
        Gets page link similar to ``namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925``
        """
        return self._page_link

    @property
    def fragment(self) -> str:
        """
        Gets fragment simalar to a3ae28cb49c180ec160a0984600b2b925
        """
        return self._fragment
    
    @property
    def is_fragment(self) -> str:
        """
        Gets if there is a fragment
        """
        return self._is_frag

    @property
    def namespace(self) -> List[str]:
        """
        Gets Namespace in format of ['com', 'sun', 'star', 'style']
        """
        return self._ns

    @property
    def namespace_str(self) -> str:
        """
        Gets namespace in format of 'com.sun.star.style'
        """
        if not self._ns_str:
            self._ns_str = '.'.join(self.namespace)
        return self._ns_str
class BlockObj(ABC):
    """
    Abstract Class.
    
    Represents a Html Block.
    """
    def __init__(self, soup:SoupObj):
        """
        Constructor

        Args:
            soup (SoupObj): soup for this instance
        """
        self._soup = soup
        self._urlobj = UrlObj(url=soup.url)
        self._url = soup.url
    
    @abstractmethod
    def get_obj(self) -> Tag:
        """Get object"""

    @property
    def url(self) -> str:
        """Gets Url"""
        return self._url
    
    @property
    def soup(self) -> SoupObj:
        """Gets SoupObj instance for this instance"""
        return self._soup
    
    @property
    def url_obj(self) -> UrlObj:
        """Gets UrlObj instance for this instance"""
        return self._urlobj

class TagsStrObj:
    """Class that converts list of tags to string"""
    def __init__(self, tags: Iterable[Tag], **kwargs):
        """
        Constructor

        Args:
            tags (Iterable[Tag]): List of tags

        Keyword Arguments:
            clean (bool, optional): If ``True`` then data will be cleaned
                using ``str_clean`` method. Default ``True``
            empty (bool, optional): If ``True`` empty lines will be added
                between other lines. Default ``True``
            indent (int, optional): The number of spaces to indent for 
                methods that return a string. Default ``0``
        """
        self._tags = tags
        self._clean = bool(kwargs.get('clean', True))
        self._empty_lines = bool(kwargs.get('empty', True))
        self._indent_amt = int(kwargs.get('indent', 0))
        
    
    def get_lines(self) -> List[str]:
        """Gets lines for this instance"""
        lines = []
        for i, ln in enumerate(self._tags):
            s = ln.text.strip()
            if self._clean:
                s = str_clean(input=s)
            if i > 0 and self._empty_lines:
                lines.append("")
            lines.append(s)
        return lines
    
    def get_data(self) -> str:
        """Gets Lines as string for this instance"""
        lines =self.get_lines()
        s = "\n".join(lines)
        s = self._indent(s)
        return s

    def get_string_list(self) -> str:
        lines = self._encode_list(self.get_lines())
        c_lines = self._decode_list(str(lines).split(','))
        s = ',\n'.join(c_lines)
        s = self._indent(s)
        return s
    
    def _encode_list(self, lst:List[str]) -> List[str]:
        # \xff and \xfe are BOM chars
        results = []
        for el in lst:
            s = el.replace(',', '\xff')
            results.append(s)
        return results

    def _decode_list(self, lst: List[str]) -> List[str]:
        # \xff and \xfe are BOM chars
        results = []
        for el in lst:
            s = el.replace('\xff', ',')
            results.append(s)
        return results

    def _indent(self, text: str) -> str:
        if self._indent_amt <= 0:
            return text
        indent = ' ' * self._indent_amt
        s = textwrap.indent(text, indent)
        return s
class WriteBase(object):
    def _mkdirp(self, dest_dir):
        # Python ≥ 3.5
        if isinstance(dest_dir, Path):
            dest_dir.mkdir(parents=True, exist_ok=True)
        else:
            Path(dest_dir).mkdir(parents=True, exist_ok=True)
    
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

    def _create_sys_links(self, dest: Path):
        files = self._get_template_files()
        rel = Path('../../template')
        for file in files:
            try:
                p_file = Path(file)
                rel_file = rel.joinpath(p_file.name)
                dst_file = dest / p_file.name
                os.symlink(
                    src=rel_file,
                    dst=dst_file
                )
                msg = f"Created system link: {dst_file} -> {rel_file}"
                logger.info(msg)
            except FileExistsError:
                continue
            except Exception as e:
                logger.error(e)

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
        return str_clean(input=input, replace_dual=self._replace_dual_colon)

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
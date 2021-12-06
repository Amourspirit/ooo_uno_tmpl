import os
import sys
import re
import requests
import textwrap
import json
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from glob import glob
from kwhelp.decorator import DecFuncEnum, RuleCheckAll
from kwhelp import rules
from pathlib import Path
from typing import Iterable, List, Tuple, Union
# this is for VS code debuging
sys.path.insert(0, os.path.abspath('.'))
# this is for command line
sys.path.insert(0, os.path.abspath('..'))

from logger.log_handle import get_logger
logger = get_logger(__name__)

#  \W = [^a-zA-Z0-9_]
py_name_pattern = re.compile('[\W_]+')
py_ns_pattern = re.compile(r'[^a-zA-Z0-9\._]+')

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
    def __init__(self, url: str):
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
    def __init__(self, url: str) -> None:
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


class Util:
    @staticmethod
    def get_clean_name(input: str, sub: str = '') -> str:
        """
        Removes all char from a string except for ``a-zA-Z0-9_``

        Args:
            input (str): string to clean
            sub (str, optional): replacement string for non matching characters.
                Default is empty string.

        Returns:
            str: input with any other chars replaced
        """
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        return py_name_pattern.sub(sub, input)
    
    @staticmethod
    def get_clean_ns(input: str, sub: str='') -> str:
        """
        Removes all char from a string except for ``a-zA-Z0-9_.``

        Args:
            input (str): string to clean
            sub (str, optional): replacement string for non matching characters.
                Default is empty string.

        Returns:
            str: input with any other chars replaced
        """
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        return py_ns_pattern.sub(sub, input)

    """Static Class or helper methods"""
    @staticmethod
    def get_formated_dict_list_str(obj: Union[dict, list], indent=4) -> str:
        """
        Get a formated dictionary or list

        Args:
            obj (Union[dict, list]): Dict or list to get formates string for.
            indent (int, optional): The number of spaces to indent string.. Defaults to ``2``.

        Returns:
            str: string of formated dictionary properties and values
        """
        if not isinstance(obj, dict) and not isinstance(obj, list):
            return "{}"
        _indent = 4 if indent < 0 else indent
        formatted = json.dumps(obj, indent=_indent)
        return formatted

    @staticmethod
    def get_string_list(lines: List[str], indent_amt: int = 0) -> str:
        """
        Converts a list into str.
        Similar to calling str(lines) but handles more edge cases.

        Args:
            lines (List[str]): list to convert
            indent_amt (int, optional): Amount to indent results. Defaults to 0.

        Returns:
            str: List as string.
        """
        _lines = Util._encode_list(lines)
        c_lines = Util._decode_list(str(_lines).split(','))
        s = ',\n'.join(c_lines)
        if indent_amt > 0:
            s = Util.indent(text=s, indent_amt=indent_amt)
        return s

    @staticmethod
    def get_last_part(input: str, sep='.') -> str:
        """
        Splits a string and returns the last part

        Args:
            input (str): string to get last part of.
            sep (str, optional): string used to split. Defaults to ``.``

        Returns:
            str: [description]
        """
        if not input:
            return ''
        _parts = input.rsplit(sep, 1)
        return _parts[0] if len(_parts) == 1 else _parts[1]

    @staticmethod
    def indent(text: str, indent_amt: int = 4) -> str:
        """
        Indents a multi line string

        Args:
            text (str): text to apply indent
            indent_amt (int, optional): Amout of indent. Defaults to 4.

        Returns:
            str: indented text.
        """
        if indent_amt <= 0:
            return text
        indent = ' ' * indent_amt
        s = textwrap.indent(text, indent)
        return s

    @staticmethod
    def camel_to_snake(input: str) -> str:
        """
        Converts Camel case to snake clase

        Args:
            name (str): Camel name

        Returns:
            str: snake case
        """
        _input = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', _input).lower()

    @staticmethod
    def get_rel_import(i_str: str, ns: str) -> Tuple[str, str]:
        logger.debug('Util.get_rel_import')
        logger.debug("i_str: '%s' ns: '%s'",i_str, ns)
        name_ns_str = i_str.rsplit('.', 1)[0] # drop last word
        logger.debug("Namespace from i_str: '%s'", name_ns_str)
        name_ns: List[str] = name_ns_str.split('.')
        logger.debug("i_str Namespace Parts: '%s'", str(name_ns))
        if len(name_ns) == 1:
            # this is a single word
            # assume it is in the same namespace as this import
            logger.debug("'%s', single word. Converting to from import and returning", i_str)
            return (f'.{Util.camel_to_snake(i_str)}', f'{i_str}')
        name = Util.get_last_part(input=i_str)
        camel_name = Util.camel_to_snake(name)
        logger.debug("Name from i_str: '%s'", name)
        ns_parts = ns.split('.')
        if name_ns_str == ns:
            logger.debug("Names are equal: '%s'", ns)
            logger.debug(f"Returning (.{camel_name}', '{name})")
            return (f'.{camel_name}', f'{name}')
        commmon_count = 0
        for i, ns in enumerate(name_ns):
            if ns != ns_parts[i]:
                break
            commmon_count += 1
        if commmon_count > 0:
            logger.debug('found common %d namespace elements', commmon_count)
            common_ns = name_ns[commmon_count:]
            logger.debug("Common elements: '$s'", str(common_ns))
            dot_ext = (len(ns_parts) - commmon_count) + 1
            logger.debug("'.' to prepend is: %d", dot_ext)
            dot = "." * dot_ext
            rel = ".".join(common_ns)
            logger.debug("Realitive part is '%s'", rel)
            str_from = f'{dot}{rel}.{camel_name}'
            logger.debug("From String to return is:'%s'", str_from)
            return (str_from, name)
        # last ditch effort to import via full path
        short = name_ns_str.replace('com.sun.star.', '')
        logger.debug(
            f"Last ditch effort. Returning: (ooo_uno.uno_obj.{short}.{camel_name}', {name})")
        return (f'ooo_uno.uno_obj.{short}.{camel_name}', f'{name}')

    @staticmethod
    def encode_char(input:str, replace:str, en:str = '\xff') -> str:
        """
        Encodes all matching chars in a string with the value of ``en``.
        Chars ``\\xff`` and ``\\xfe`` are BOM

        Args:
            input (str): text to search and replace
            replace (str): char to replace all instances of
            en (str, optional): Value to replace. Defaults to ``\\xff``.

        Returns:
            str: input with chars replace with ``en`` value
        """
        return input.replace(replace, en)

    @staticmethod
    def decode_char(input: str, restore: str, de: str = '\xff') -> str:
        """
        Decodes allmathing chars in a string with the value of ``restore``.
        Chars ``\\xff`` and ``\\xfe`` are BOM

        Args:
            input (str): text to search and restore
            restore (str): char to restore
            de (str, optional): value to decode. Defaults to ``\\xff``.

        Returns:
            str: [description]
        """
        return input.replace(de, restore)
    
    @staticmethod
    def get_py_type(uno_type: str, **kwargs) -> str:
        if not uno_type:
            return ''
        def do_cb(_cb:callable, data):
            if not _cb:
                return
            _cb(data)
    
        add_typeings = bool(kwargs.get('typings', True))
        cb = kwargs.get('cb', None)
        cb_data = {
            "uno_type": uno_type,
            "is_py_type": False,
            "is_wrapper": False,
            "is_typing": False,
            "wdata": {}
        }
        _u_type = uno_type.strip().replace("::", ".")
        # check for # sequence< string >
        parts = _u_type.split(sep='<', maxsplit=1)
        if len(parts) > 1:
            is_pytype = True
            cb_data['is_wrapper'] = True
            clean_wrapper = Util.get_last_part(Util.get_clean_name(parts[0]))
            wrapper = TYPE_MAP.get(clean_wrapper, None)
            if wrapper:
                cb_data['wdata']['is_py_type'] = True
            else:
                is_pytype = False
                cb_data['wdata']['is_py_type'] = False
            type_pre = "typing." if add_typeings else ''
            cb_data['is_typing'] = add_typeings
            cb_data['wdata']['prefix'] = type_pre
            if wrapper:
                # got a match from TYPE_MAP
                # title case the word and add typings
                wrapper = type_pre + wrapper.title()
            else:
                wrapper = type_pre + 'List'
            cb_data['wdata']['wrapper'] = wrapper
            _type = parts[1].replace('>', '').strip()
            _type = Util.get_clean_name(Util.get_last_part(_type))
            map_type = TYPE_MAP.get(_type, None)
            if not map_type:
                is_pytype = False
                map_type = _type
            cb_data['is_py_type'] = is_pytype
            cb_data['type'] = _type
            do_cb(cb, cb_data)
            return f"{wrapper}[{_type}]"
        _u_type_clean = Util.get_clean_name(Util.get_last_part(_u_type))
        result = TYPE_MAP.get(_u_type_clean, None)
        if result:
            cb_data['is_py_type'] = True
            cb_data['type'] = result
            do_cb(cb, cb_data)
            return result
        cb_data['type'] = _u_type_clean
        do_cb(cb, cb_data)
        return _u_type_clean
    
    @staticmethod
    def _encode_list(lst: List[str]) -> List[str]:
        results = []
        for el in lst:
            s = Util.encode_char(el, ',')
            results.append(s)
        return results

    @staticmethod
    def _decode_list(lst: List[str]) -> List[str]:
        results = []
        for el in lst:
            s = Util.decode_char(el, ',')
            results.append(s)
        return results

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
        self._page_link = self._url.rsplit('/', 1)[1]
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

    def __init__(self, soup: SoupObj):
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
        lines = self.get_lines()
        s = "\n".join(lines)
        if self._indent_amt > 0:
            s = Util.indent(text=s, indent_amt=self._indent_amt)
        return s

    def get_string_list(self) -> str:
        lines = self._encode_list(self.get_lines())
        c_lines = self._decode_list(str(lines).split(','))
        s = ',\n'.join(c_lines)
        if self._indent_amt > 0:
            s = Util.indent(text=s, indent_amt=self._indent_amt)
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
        soup_lines: ResultSet = block.find_all('p')
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

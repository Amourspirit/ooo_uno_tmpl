#!/usr/bin/env python
# exception parser
from dataclasses import dataclass
import os
import sys
import argparse
import xsrc
import logging
import re
import base
from typing import Dict, List, Set, Union
from bs4.element import PageElement, ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, RequireArgs, TypeCheck, TypeCheckKw
from kwhelp import rules
from pathlib import Path
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
from logger.log_handle import get_logger
from parser import __version__, JSON_ID

# some exceptions are Depreciated such as IntrospectionException https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1beans_1_1IntrospectionException.html

logger = None
# xsrc.logger = None
# base.logger = None
xsrc.re_component_start = re.compile(r"(exception.*){", re.DOTALL)
xsrc.re_name_info_start = re.compile(r"(exception)\s*[a-zA-Z0-9]+[ :]+")
xsrc.re_name_info_name = re.compile(r"exception\s*(?P<NAME>[a-zA-Z0-9_]+)")

def _set_loggers(l:Union[logging.Logger, None]):
    global logger, xsrc, base
    logger = l
    xsrc.logger = l
    base.logger = l

_set_loggers(None)
@dataclass
class Property:
    name: str
    type: str
    desc: List[str]

# region SDK


class SdkEntends:
    def __init__(self, data: xsrc.SdkData):
        self._sdk_data: xsrc.SdkData = data
        self._ex_lst: List[str] = []
        self._init()

    def _init(self):
        s = self._sdk_data.component_start.get_obj()
        logger.debug("SdkExtends._init() First Line: %s", s)
        # published interface XFont: com::sun::star::uno::XInterface
        s = s.replace('::', ".")
        logger.debug("SdkExtends._init() Replaced :: %s", s)
        parts = s.rsplit(sep=':', maxsplit=1)
        if len(parts) > 1:
            logger.debug(
                "SdkExtends._init() ':' seperator found extends on first line.")
            s = parts[1]
            logger.debug("SdkExtends._init() Processing: '%s'", s)
            s = base.Util.get_clean_ns(input=s, ltrim=True)
            self._ex_lst.append(s)
            logger.debug("SdkExtends._init() Added Extends: '%s'", s)

    @property
    def ex_lst(self) -> List[str]:
        """Gets ex_lst value"""
        return self._ex_lst
# endregion SDK

# region API


class ApiPropertyIds(base.BlockObj):
    @TypeCheck(base.SoupObj, ftype=DecFuncEnum.METHOD)
    def __init__(self, soup: base.SoupObj):
        self._soup = soup
        super().__init__(soup)
        self._data = None

    def get_obj(self) -> List[str]:
        """get a list of all property ids"""
        # https://stackoverflow.com/questions/2830530/matching-partial-ids-in-beautifulsoup
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        # #a5f96e2ff361b33c3fa10fed24a02d6e1
        ctx = soup.select_one('body > div.contents')
        if not ctx:
            msg = "ApiPropertyIds.get_obj() Unable to find contents of page"
            logger.error(msg)
            raise Exception(msg)
        rs: ResultSet = ctx.find_all(
            'a', id=re.compile(r'[a-z0-9]{28,38}'))
        
        results = []
        for r in rs:
            results.append(r['id'].strip())
        self._data = results
        return self._data


class ApiPropertyInfo:
    def __init__(self, id: str, api_data: 'ApiData'):
        self._id = id
        self._api_data: ApiData = api_data
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._prop = None
        self._init()

    def _get_next_sibling(self, el: PageElement) -> PageElement:
        # get the next sibling recursivly because
        # BeautifulSoup will also find whitesapce on next_sibling
        if not isinstance(el, PageElement):
            raise TypeError(
                f"ApiPropertyInfo._get_next_sibling() el is not a PageElement")
        next = el.next_sibling
        # https://stackoverflow.com/questions/10711116/strip-spaces-tabs-newlines-python
        # use split join to remove whitespace and new line
        s = ''.join(str(next).split())
        if s == '':
            next = self._get_next_sibling(next)
        return next

    def _init(self):
        # select a tag for id
        soup = self._api_data.soup_obj.soup
        a = soup.find('a', attrs={'id': self._id})
        if not a:
            logger.debug(
                "ApiPropertyInfo.get_obj() No tag found with ID: %s", self._id)
            return None
        try:
            title = self._get_next_sibling(a)
        except TypeError:
            logger.error(
                "ApiPropertyInfo.get_obj() Not Title object for id: %s", self._id)
            return None
        # name = title.text.strip()
        try:
            item = self._get_next_sibling(title)
        except TypeError:
            logger.error(
                "ApiPropertyInfo.get_obj() No Title object for id: %s", self._id)
            return None
        # item contains type, name and desc
        tn = item.find_next('td', class_='memname')
        parts = tn.text.split()
        name = parts.pop()
        _type = parts.pop().replace("::", ".")
        _py_type = self._get_py_type(_type)
        d = item.find_next('div', class_='memdoc')
        tso = base.TagsStrObj(tags=d)
        lines = tso.get_lines()
        self._prop = Property(name=name, type=_py_type, desc=lines)
    
    def _get_py_type(self, in_type: str) -> str:
        cb_data = None

        def cb(data: dict):
            nonlocal cb_data
            cb_data = data

        n_type = base.TYPE_MAP.get(in_type, None)
        if n_type:
            logger.debug(
                "ApiPropertyInfo._get_py_type() Found python type: %s", n_type)
            return n_type
        n_type = base.Util.get_py_type(uno_type=in_type, cb=cb)
        is_wrapper = cb_data['is_wrapper']
        is_py = cb_data['is_py_type']
        _result = n_type
        if is_wrapper:
            self._requires_typing = True
            logger.debug(
                "ApiPropertyInfo._get_py_type() wrapper arg %s", in_type)
            logger.debug(
                "ApiPropertyInfo._get_py_type() wrapper arg Typing is Required.")
            wdata: dict = cb_data['wdata']
            if not wdata['py_type_inner']:
                logger.debug(
                    "ApiPropertyInfo._get_py_type() wrapper inner requires typing arg %s", in_type)
                self._imports.add(cb_data['long_type'])
                logger.debug(
                    "ApiPropertyInfo._get_py_type() added import %s", cb_data['long_type'])
        else:
            if is_py is False:
                logger.debug(
                    "ApiPropertyInfo._get_py_type() requires typing arg %s", in_type)
                self._requires_typing = True
                self._imports.add(cb_data['long_type'])
                logger.debug(
                    "ApiPropertyInfo._get_py_type() added import %s", cb_data['long_type'])
        return _result

    @property
    def api_data(self) -> 'ApiData':
        """Gets api_data value"""
        return self._api_data

    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        return self._imports

    @property
    def requires_typing(self) -> bool:
        """Gets requires_typing value"""
        return self._requires_typing
    
    @property
    def prop(self) -> Property:
        return self._prop

class ApiProperties:

    def __init__(self, p_ids: ApiPropertyIds, a_data: 'ApiData'):
        self._property_ids = p_ids
        self._a_data = a_data
        self._imports: Set[str] = set()
        self._requires_typing = False
        self._properties: List[Property] = []
        self._init()
    
    def _init(self):
        ids: List[str] = self._property_ids.get_obj()
        for s in ids:
            pi = ApiPropertyInfo(
                id=s, api_data=self._a_data)
            if pi.requires_typing == True:
                self._requires_typing = True
            if len(pi.imports) > 0:
                self._imports.update(pi.imports)
            self._properties.append(pi.prop)

    @property
    def property_ids(self) -> ApiPropertyIds:
        """Gets property_ids value"""
        return self._property_ids

    @property
    def properties(self) -> List[Property]:
        """Gets properties value"""
        return self._properties
    
    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        return self._imports

    @property
    def requires_typing(self) -> bool:
        """Gets requires_typing value"""
        return self._requires_typing

class ApiDesc:
    """Responsible for getting description for an exception"""

    def __init__(self, api_data: 'ApiData'):
        self._api_data = api_data
        self._data = None

    def get_obj(self) -> List[str]:
        """
        Gets Descripton include since.

        Returns:
            List[str]: Description as list of str
        """
        if not self._data is None:
            return self._data
        result: List[str] = []
        soup = self._api_data.soup_obj.soup
        t_block = soup.select_one('body > div.contents > div.textblock')
        if t_block:
            # found description block
            rs = t_block.select("p")
            tso = base.TagsStrObj(rs)
            lines = tso.get_lines()
            if len(lines) > 0:
                result.extend(lines)
            dl_since = t_block.find('dl', class_='since')
            if dl_since:
                dd = dl_since.select_one('dd')
                if dd:
                    result.append('')
                    result.append('**Since**')
                    result.append('')
                    result.append('   ' + dd.text.strip())
        self._data = result
        return self._data

    @property
    def api_data(self) -> 'ApiData':
        """Gets api_data value"""
        return self._api_data


class ApiData:

    @TypeCheck((str, base.SoupObj), bool, ftype=DecFuncEnum.METHOD)
    def __init__(self, url_soup: Union[str, base.SoupObj], allow_cache: bool):
        if isinstance(url_soup, str):
            self._url = url_soup
            self._soup_obj = base.SoupObj(
                url=url_soup, allow_cache=allow_cache)
        else:
            self._url = url_soup.url
            self._soup_obj = url_soup
            self._soup_obj.allow_cache = allow_cache

        self._property_ids = None
        self._api_properties = None

    @property
    def property_ids(self) -> ApiPropertyIds:
        """Gets property_ids value"""
        if self._property_ids is None:
            self._property_ids = ApiPropertyIds(self.soup_obj)
        return self._property_ids

    @property
    def api_properties(self) -> ApiProperties:
        """Gets api_properties value"""
        if self._api_properties is None:
            self._api_properties = ApiProperties(self.property_ids, self)
        return self._api_properties

    @property
    def soup_obj(self) -> base.SoupObj:
        """Gets soup_obj value"""
        return self._soup_obj

# endregion API


class ParserEx(base.ParserBase):
    # region Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._sdk_data = xsrc.SdkData(
            url=self.url,
            allow_cache=self._allow_cache
            )
        soup = self._sdk_data.api_sdk_link.soup
        self._api_data = ApiData(url_soup=soup, allow_cache=self._allow_cache)
        self._imports: Set[str] = set()
        self._requires_typing = False
        self._cache = {}
    # endregion Constructor

    def get_parser_args(self) -> dict:
        args = {
            "sort": self.sort
        }
        return args

    def get_formated_data(self, indent=4) -> str:
        key = 'get_formated_data'
        if key in self._cache:
            return self._cache[key]
        attribs = self._get_data_items()
        str_lst = base.Util.get_formated_dict_list_str(obj=attribs, indent=indent)
        self._cache[key] = str_lst
        return self._cache[key]

    def get_dict_data(self) -> dict:
        info = self.get_info()
        items = self._get_data_items()
        info['items'] = items
        return info

    def get_info(self) -> Dict[str, object]:
        """
        Gets info

        Returns:
            Dict[str, object]: {
                "name": "str, class name",
                "imports": "List[str], imports",
                "typing_imports": "List[str], imports that require typing",
                "namespace": "str, Namespace",
                "extends": "List[str], class extends",
                "desc": "List[str], class description",
                "url": "str, api url"
            }
        """
        key = 'get_info'
        if key in self._cache:
            return self._cache[key]
        ns = base.UrlObj(self._url)
        ni = self._sdk_data.name_info
        ex = self._sdk_data.extends
        desc = ApiDesc(self._api_data)
        # must be called here to make sure imports are included.
        # method is cached so no big dea.
        self._get_data_items()
        result = {
            'name': ni.name,
            'namespace': ns.namespace_str,
            'imports': [],
            'typing_imports': list(self._api_data.api_properties.imports),
            'extends': ex.ex_lst,
            'desc': desc.get_obj(),
            "url": ns.url
        }
        # if ni.name == 'Exception':
        #     # make special exception for root exception:
        #     result['extends'] = ['XInterface']

        logger.debug('ParserEx.get_info() name: %s', ni.name)
        logger.debug('ParserEx.get_info() namespace: %s',
                     ns.namespace_str)
        self._cache[key] = result
        return self._cache[key]

    def _get_data_items(self) -> dict:
        key = '_get_data_items'
        if key in self._cache:
            return self._cache[key]
        attribs = {}
        prop = self._get_properties_data()
        attribs['properties'] = prop

        self._cache[key] = attribs
        return self._cache[key]

    def _get_properties_data(self) -> List[dict]:
        attribs = []
        props = self._api_data.api_properties
        if props.requires_typing:
            self._requires_typing = True
        properties: List[Property] = props.properties
        for p in properties:
            if not p.name:
                continue
            d = {
                "name": p.name,
                "type": p.type,
                "desc": p.desc
            }
            attribs.append(d)
        return attribs

    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        key = '_get_data_items'
        try:
            if not key in self._cache:
                msg = "ParserEx._get_data_items() method must be called before accessing imports"
                raise Exception(msg)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._imports

    @property
    def requires_typing(self) -> bool:
        """Gets requires typing value"""
        key = '_get_data_items'
        try:
            if not key in self._cache:
                msg = "ParserEx._get_data_items() method must be called before accessing requires_typing"
                raise Exception(msg)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._requires_typing

class WriterEx(base.WriteBase):
    # region Constructor
    @TypeCheckKw(arg_info={
        "write_file": 0, "write_json": 0,
        "copy_clipboard": 0, "print_template": 0,
        "print_json": 0, "clear_on_print": 0,
        "write_template_long": 0,
        "include_desc": 0
        },
        types=[bool],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser: ParserEx, **kwargs):
        super().__init__(**kwargs)
        self._parser: ParserEx = parser
        self._copy_clipboard: bool = kwargs.get('copy_clipboard', False)
        self._print_template: bool = kwargs.get('print_template', False)
        self._write_file: bool = kwargs.get('write_template', False)
        self._print_json: bool = kwargs.get('print_json', True)
        self._write_json: bool = kwargs.get('write_json', False)
        self._clear_on_print: bool = kwargs.get('clear_on_print', True)
        # include_desc determines if templete outputs desc
        self._include_desc: bool = kwargs.get('include_desc', True)
        self._write_template_long: bool = kwargs.get(
            'write_template_long', False)
        self._indent_amt = 4
        self._json_str = None
        self._p_name: str = None
        self._p_imports: Set[str] = set()
        self._p_imports_typing: Set[str] = set()
        self._p_namespace: str = None
        self._p_extends: List[str] = None
        self._p_desc: List[str] = None
        self._p_data: str = None
        self._p_url: str = None
        self._p_requires_typing = False
        self._path_dir = Path(__file__).parent
        self._cache: Dict[str, object] = {}

        t_file = 'exception'
        if not self._write_template_long:
            t_file += '_stub'
        t_file += '.tmpl'
        _path = Path(self._path_dir, 'template', t_file)
        try:
            if not _path.exists():
                raise FileNotFoundError(
                    f"unable to find templae file '{_path}'")
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        self._template_file = _path
        self._template: str = self._get_template()
    # endregion Constructor

    def write(self):
        self._set_info()
        self._set_template_data()
        logger.info("Processing %s.%s", self._p_namespace, self._p_name)
        try:
            if self._clear_on_print and (self._print_template or self._print_json):
                logger.debug('Printing to terminal')
                os.system('cls' if os.name == 'nt' else 'clear')
            if self._copy_clipboard:
                xerox.copy(self._template)
                logger.debug('copied to clipbord')
            if self._print_template:
                print(self._template)
            if self._print_json:
                print(self._get_json())
            if self._write_file:
                self._write_to_file()
            if self._write_json:
                self._write_to_json()
        except Exception as e:
            logger.exception(e)

    def _get_json(self) -> str:
        if not self._json_str is None:
            return self._json_str
        p_dict = {}
        p_dict['from_imports'] = self._get_from_imports()
        p_dict['from_imports_typing'] = self._get_from_imports_typing()
        p_dict.update(self._parser.get_dict_data())
        if 'typing_imports' in p_dict:
            del p_dict['typing_imports']

        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "name": p_dict['name'],
            "type": "exception",
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {
                "include_desc": self._include_desc},
            "data": p_dict
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._json_str = str_jsn
        return self._json_str

    # region Template
    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def _set_template_data(self):
        if self._write_template_long is False:
            return
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{ns}', str(self._p_namespace))
        self._template = self._template.replace('{link}', self._p_url)
        self._template = self._template.replace(
            '{requires_typing}', str(self._p_requires_typing))
        self._template = self._template.replace(
            '{include_desc}', str(self._include_desc))
        self._template = self._template.replace(
            '{inherits}', base.Util.get_string_list(lines=self._p_extends))
        self._template = self._template.replace(
            '{imports}', "[]")
        self._template = self._template.replace(
            '{from_imports}',
            base.Util.get_formated_dict_list_str(self._get_from_imports())
        )
        self._template = self._template.replace(
            '{from_imports_typing}',
            base.Util.get_formated_dict_list_str(
                self._get_from_imports_typing())
        )
        if len(self._p_desc) > 0:
            desc = base.Util.get_formated_dict_list_str(self._p_desc, indent=4)
        else:
            desc = "[]"
        self._template = self._template.replace('{desc}', desc)
        if self._indent_amt > 0:
            indent = ' ' * self._indent_amt
            indented = textwrap.indent(self._p_data, indent).lstrip()
        else:
            indented = self._p_data.lstrip()
        self._template = self._template.replace('{data}', indented)
    # endregion Template

    # region get Imports
    def _get_from_imports(self) -> List[List[str]]:
        key = '_get_from_imports'
        if key in self._cache:
            return self._cache[key]
        lst = []
        for ns in self._p_imports:
            f, n = base.Util.get_rel_import(
                i_str=ns, ns=self._p_namespace
            )
            lst.append([f, n])
        self._cache[key] = lst
        return self._cache[key]

    def _get_from_imports_typing(self) -> List[List[str]]:
        key = '_get_from_imports_typing'
        if key in self._cache:
            return self._cache[key]
        lst = []
        for ns in self._p_imports_typing:
            f, n = base.Util.get_rel_import(
                i_str=ns, ns=self._p_namespace
            )
            lst.append([f, n])
        self._cache[key] = lst
        return self._cache[key]
     
     # endregion get Imports

    # region set data
    def _set_info(self):
        def get_extends(lst:List[str]) -> List[str]:
            return [base.Util.get_last_part(s) for s in lst]
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_namespace = data['namespace']
        self._p_extends = get_extends(data['extends'])
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_data = self._parser.get_formated_data()
        self._validate_p_info()
        typing_imports = data['typing_imports']
        self._p_imports_typing.update(typing_imports)
        self._p_imports.update(data['extends'])
        if len(self._p_imports_typing) > 0:
            self._p_requires_typing = True
        if not self._p_requires_typing:
            self._p_requires_typing = self._parser.requires_typing
        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()
    # end region set data

    # region validation
    def _validate_p_info(self):
        try:
            if not self._p_name:
                raise Exception(
                    "InterfaceWriter: validation fail: name is an empty string.")
            if not self._p_url:
                raise Exception(
                    "InterfaceWriter: validation fail: url is an empty string.")
            if not self._p_namespace:
                raise Exception(
                    "InterfaceWriter: validation fail: namespace is an empty string.")
        except Exception as e:
            logger.error(e)
            raise e
    # endregion validation

    def _get_uno_obj_path(self) -> Path:
        if not self._p_name:
            try:
                raise Exception(
                    "InterfaceWriter._get_uno_obj_path() Parser provided a name that is an empty string.")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e

        uno_obj_path = Path(self._path_dir.parent, 'uno_obj')
        name_parts: List[str] = self._p_namespace.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append(self._p_name + '.tppi')
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        return obj_path

    def _write_to_file(self):
        with open(self._file_full_path, 'w') as f:
            f.write(self._template)
        logger.info("Created file: %s", self._file_full_path)

    def _write_to_json(self):
        p = self._file_full_path.parent
        jsn_p = p / (str(self._file_full_path.stem) + '.json')
        jsn_str = self._get_json()
        with open(jsn_p, 'w') as f:
            f.write(jsn_str)
        logger.info("Created file: %s", jsn_p)

def _main():
    # url = 'https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1configuration_1_1CannotLoadConfigurationException.html'
    url = 'https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1uno_1_1Exception.html'
    sys.argv.extend(['-d', '-n', '-j', '-t', '-v', '-L', 'debug.log', '-u', url])
    main()
    
def main():
    global logger
    
    # region Parser
    parser = argparse.ArgumentParser(description='interface')
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=True)
    parser.add_argument(
        '-s', '--no-sort',
        help='No sorting of results',
        action='store_false',
        dest='sort',
        default=True)
    parser.add_argument(
        '-x', '--no-cache',
        help='No caching',
        action='store_false',
        dest='cache',
        default=True)
    parser.add_argument(
        '-d', '--no-desc',
        help='No description will be outputed in template',
        action='store_false',
        dest='desc',
        default=True)
    parser.add_argument(
        '-p', '--no-print-clear',
        help='No clearing of terminal when output to terminal.',
        action='store_false',
        dest='no_print_clear',
        default=True)
    parser.add_argument(
        '-g', '--long-template',
        help='Writes a long format template. Requires --write-template is set. No Autoload',
        action='store_true',
        dest='long_format',
        default=False)
    parser.add_argument(
        '-c', '--clipboard',
        help='Copy to clipboard',
        action='store_true',
        dest='clipboard',
        default=False)
    parser.add_argument(
        '-n', '--print-json',
        help='Print json to terminal',
        action='store_true',
        dest='print_json',
        default=False)
    parser.add_argument(
        '-m', '--print-template',
        help='Print template to terminal',
        action='store_true',
        dest='print_template',
        default=False)
    parser.add_argument(
        '-t', '--write-template',
        help='Write template file into obj_uno subfolder',
        action='store_true',
        dest='write_template',
        default=False)
    parser.add_argument(
        '-j', '--write-json',
        help='Write json file into obj_uno subfolder',
        action='store_true',
        dest='write_json',
        default=False)
    # region Dummy Args for Logging
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use',
        type=str,
        required=False)
    # endregion Dummy Args for Logging
    args = parser.parse_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    # endregion Parser
    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)

    p = ParserEx(
        url=args.url,
        sort=args.sort,
        cache=args.cache
    )
    w = WriterEx(
        parser=p,
        print_template=args.print_template,
        print_json=args.print_json,
        copy_clipboard=args.clipboard,
        write_template=args.write_template,
        write_json=args.write_json,
        clear_on_print=(not args.no_print_clear),
        write_template_long=args.long_format,
        include_desc=args.desc
    )
    if args.print_template is False and args.print_json is False:
        print('')
    w.write()

if __name__ == '__main__':
    main()

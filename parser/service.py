#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains a service
"""
# region imports
from abc import abstractmethod
import os
import sys
import argparse
import logging
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
from typing import Dict, List, NamedTuple, Set, Tuple, Union
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, SubClass, TypeCheck, TypeCheckKw
from pathlib import Path
try:
    import base
except ModuleNotFoundError:
    import parser.base as base
from logger.log_handle import get_logger
from parser.enm import main
from parser import __version__, JSON_ID
# endregion imports

# region Logger
logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger
    logger = l
    base._set_loggers(l)

_set_loggers(None)
# endregion Logger

# Works both for python 2 and 3
# from scratch.uno_obj.awt.x_font import XFont


# region API Classes
class ApiTables(base.BlockObj):
    @TypeCheck(base.SoupObj, ftype=DecFuncEnum.METHOD)
    def __init__(self, soup: base.SoupObj):
        self._soup = soup
        super().__init__(soup)
        self._data = None
    
    def get_obj(self) -> ResultSet:
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        self._data = soup.find_all('table', class_='memberdecls')
        return self._data


class ApiTableFindBase(base.BlockObj):
    """Abstract Class for finding tables"""
    @TypeCheck(ApiTables, ftype=DecFuncEnum.METHOD)
    def __init__(self, tables: ApiTables):
        self._tables = tables
        super().__init__(self._tables.soup)
        self._data = None
        self._has_data = None
    
    def get_obj(self) -> Union[Tag, None]:
        """
        Gets Table as Tag if match if found

        Returns:
            Union[Tag, None]: Table if found; Otherwise,  ``None``
        """
        if not self._data is None:
            return self._data
        if self._has_data is False:
            return None
        tables = self._tables.get_obj()
        for tbl in tables:
            if self._find_table(tbl):
                self._data = tbl
                self._has_data = True
                logger.debug("ApiTableFindBase.get_obj() Found table: %s", self._get_a_name())
                break
        if self._has_data is None:
            logger.debug(
                "ApiTableFindBase.get_obj() Did not find table: %s", self._get_a_name())
            self._has_data = False
        return self._data

    @abstractmethod
    def _get_a_name(self) -> str:
        """Gets name such as service"""
    
    def _find_table(self, t: Tag) -> bool:
        t_heading = t.find('tr', class_='heading')
        if not t_heading:
            return False
        t_a = t_heading.find('a',  attrs={"name": self._get_a_name()})
        if t_a:
            return True
        return False


class ApiIncludedServicesBlock(ApiTableFindBase):

    def _get_a_name(self) -> str:
        return 'services'


class ApiExportedInterfacesBlock(ApiTableFindBase):

    def _get_a_name(self) -> str:
        return 'interfaces'


class ApiInheritedBlock(ApiTableFindBase):

    def _get_a_name(self) -> str:
        return 'inherited'


class ApiComponentExtends:
    @SubClass(ApiTableFindBase, ftype=DecFuncEnum.METHOD)
    def __init__(self, table: ApiTableFindBase):
        self._table = table
        self._data = None
    
    def _get_rows(self) -> List[Tag]:
        results = []
        tag = self._table.get_obj()
        if not tag:
            return results
        rs = tag.select('tr')
        for r in rs:
            class_ : List[str] = r.get('class', None)
            if not class_:
                continue
            if 'inherit_header' in class_:
                # Exported interfaces are alos included in the same table
                # to filter out these stop when row with class including
                # inherit_header is found.
                break
            if class_[0].startswith('memitem:'):
                results.append(r)
        return results
    
    def get_obj(self) -> List[str]:
        if not self._data is None:
            return self._data
        results = []
        rows = self._get_rows()
        for row in rows:
            tag = row.find('td', class_='memItemRight')
            if not tag:
                continue
            try:
                s: str = tag.text
                s = s.replace("::", ".")
                results.append(base.Util.get_clean_ns(input=s, ltrim=True))
            except Exception as e:
                logger.debug('ApiComponentExtends.get_obj() parsing error. continuing...')
                continue
        self._data = results
        return self._data


class ApiDescBlock(base.BlockObj):
    """Gets block that contains description for service"""
    @TypeCheck(base.SoupObj, ftype=DecFuncEnum.METHOD)
    def __init__(self, soup: base.SoupObj):
        self._soup = soup
        super().__init__(soup)
        self._data = None
        self._has_data = None

    def get_obj(self) -> Union[Tag, None]:
        """
        Get the descripton block

        Returns:
            Union[Tag, None]: Description block if found; Otherwise, ``None``
        """
        if not self._data is None:
            return self._data
        if self._has_data == False:
            return None
        soup = self.soup.soup
        self._data = soup.select_one('body > div.contents > div.textblock')
        self._has_data = not self._data is None
        return self._data


class ApiSince:
    """Gets Component Since information"""
    @TypeCheck(ApiDescBlock, ftype=DecFuncEnum.METHOD)
    def __init__(self, block: ApiDescBlock):
        self._block = block
        self._data = None

    def get_obj(self) -> List[str]:
        """
        Gets component since info

        Returns:
            List[str]: List of since infor or empyt list if since data is not found.
        """
        if not self._data is None:
            return self._data
        tag = self._block.get_obj()
        self._data = []
        if not tag:
            return self._data
        t_since = tag.find('dl', class_='since')
        if not t_since:
            return self._data
        dd = t_since.select_one('dd')
        if not dd:
            return self._data
        self._data.append('**Since**')
        self._data.append('')
        self._data.append('    ' + dd.text.strip())
        return self._data

class ApiDesc:
    """Gets Component description"""
    @TypeCheck(ApiDescBlock, ftype=DecFuncEnum.METHOD)
    def __init__(self, block: ApiDescBlock):
        self._block = block
        self._data = None

    def _get_since(self) -> List[str]:
        since = ApiSince(self._block)
        return since.get_obj()

    def get_obj(self) -> List[str]:
        """
        Gets description of the component. Includes Since data if available.

        Returns:
            List[str]: Description a a list of str.
        """
        if not self._data is None:
            return self._data
        tag = self._block.get_obj()
        self._data = []
        if not tag:
            return self._data
        lines_found = tag.select('p')
        p_obj = base.TagsStrObj(tags=lines_found)
        self._data.extend(p_obj.get_data())
        since = self._get_since()
        if since:
            self._data.append('')
            self._data.extend(since)
        return self._data

class ApiNs(base.ApiNamespace):
    """Get the Name object for the interface"""

    def __init__(self, soup: base.SoupObj):
        super().__init__(soup)
        self._namespace_str = None
        self._namespace = None

    @property
    def namespace(self) -> List[str]:
        """Gets namespace value"""
        if self._namespace is None:
            self._namespace = self.get_obj()[:-1]
        return self._namespace

    @property
    def namespace_str(self) -> str:
        if self._namespace_str is None:
            self._namespace_str = '.'.join(self.namespace)
        return self._namespace_str

class ApiData(base.APIData):
    @TypeCheck((str, base.SoupObj), bool, ftype=DecFuncEnum.METHOD)
    def __init__(self, url_soup: Union[str, base.SoupObj], allow_cache: bool):
        super().__init__(url_soup=url_soup, allow_cache=allow_cache)
        self._ns: ApiNs = None
        self._api_tables: ApiTables = None
        self._api_included_services_block: ApiIncludedServicesBlock = None
        self._api_exported_interfaces_block: ApiExportedInterfacesBlock = None
        self._api_inherited_block: ApiInheritedBlock = None
        self._api_desc_block: ApiDescBlock = None
        self._api_desc: ApiDesc = None
        self._api_since: ApiSince = None
        self._inherited: base.ApiInherited = None

    # region Properties
    @property
    def ns(self) -> ApiNs:
        """Gets the service Description object"""
        if self._ns is None:
            self._ns = ApiNs(
                self.soup_obj)
        return self._ns


    @property
    def api_tables(self) -> ApiTables:
        """Gets api_tables value"""
        if self._api_tables is None:
            self._api_tables = ApiTables(self._soup_obj)
        return self._api_tables
    
    @property
    def api_included_services_block(self) -> ApiIncludedServicesBlock:
        """Gets api_tables value"""
        if self._api_included_services_block is None:
            self._api_included_services_block = ApiIncludedServicesBlock(self.api_tables)
        return self._api_included_services_block

    @property
    def api_exported_interfaces_block(self) -> ApiExportedInterfacesBlock:
        """Gets api_tables value"""
        if self._api_exported_interfaces_block is None:
            self._api_exported_interfaces_block = ApiExportedInterfacesBlock(
                self.api_tables)
        return self._api_exported_interfaces_block

    @property
    def api_inherited_block(self) -> ApiInheritedBlock:
        if self._api_inherited_block is None:
            self._api_inherited_block = ApiInheritedBlock(self.api_tables)
        return self._api_inherited_block
    
    @property
    def api_desc_block(self) -> ApiDescBlock:
        if self._api_desc_block is None:
            self._api_desc_block = ApiDescBlock(self.soup_obj)
        return self._api_desc_block
    
    @property
    def api_desc(self) -> ApiDesc:
        if self._api_desc is None:
            self._api_desc = ApiDesc(self.api_desc_block)
        return self._api_desc
    
    @property
    def api_since(self) -> ApiSince:
        if self._api_since is None:
            self._api_since = ApiSince(self.api_desc_block)
        return self._api_since
    
    @property
    def inherited(self) -> base.ApiInherited:
        """Gets class that get all inherited value"""
        if self._inherited is None:
            self._inherited = base.ApiInherited(self.soup_obj)
        return self._inherited

    # endregion Properties

# endregion API Classes

# region Parser
class ParserService(base.ParserBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._api_data = ApiData(
            url_soup=self.url,
            allow_cache=self.allow_cache
            )
        self._cache = {}

    def get_parser_args(self) -> dict:
        args = {
            "sort": self.sort
        }
        return args

    def get_dict_data(self) -> dict:
        info = self.get_info()
        return info
    
    def _get_extends(self) -> List[str]:
        extends = set()
        for el in self._api_data.inherited.get_obj():
            extends.add(el.fullns)
        return list(extends)

    def get_formated_data(self, indent=4) -> str:
        key = 'get_formated_data'
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = "{}"
        return self._cache[key]

    def get_info(self) -> Dict[str, object]:
        key = 'get_info'
        if key in self._cache:
            return self._cache[key]
        desc = self._api_data.api_desc.get_obj()
        # prime data
        self._api_data.ns.get_obj()
        result = {
            'name': self._api_data.name.get_obj(),
            'namespace': self._api_data.ns.namespace_str,
            'extends': self._get_extends(),
            'url': self._api_data.url_obj.url,
            'desc': desc
        }
        self._cache[key] = result
        return self._cache[key]

    @property
    def api_data(self) -> ApiData:
        return self._api_data
# endregion Parser


# region Writer
class WriterService(base.WriteBase):
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
    def __init__(self, parser: ParserService, **kwargs):
        super().__init__(**kwargs)
        self._parser: ParserService = parser
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
        self._indent_amt = 0
        self._p_name: str = None
        self._p_namespace: str = None
        self._p_extends: List[str] = None
        self._p_imports: Set[str] = set()
        self._p_desc: List[str] = None
        self._p_url: str = None
        self._path_dir = Path(__file__).parent
        self._cache: Dict[str, object] = {}
        t_file = 'service'
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

    # region Json
    def _get_json(self) -> str:
        key = '_get_json'
        if key in self._cache:
            return self._cache[key]
        p_dict = {}
        p_dict['from_imports'] = self._get_from_imports()
        p_dict['quote'] = []
        p_dict['typings'] = []
        p_dict['requires_typing'] = False
        p_dict.update(self._parser.get_dict_data())
   
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "timestamp": str(base.Util.get_timestamp_utc()),
            "name": p_dict['name'],
            "type": "service",
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {
                "include_desc": self._include_desc},
            "data": p_dict
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._cache[key] = str_jsn
        return self._cache[key]
    # endregion Json

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
    # endregion get Imports

    # region set data
    def _set_info(self):
        def get_extends(lst: List[str]) -> List[str]:
            return [base.Util.get_last_part(s) for s in lst]
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_namespace = data['namespace']
        self._p_extends = get_extends(data['extends'])
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_data = self._parser.get_formated_data()
        self._validate_p_info()
        self._p_imports.update(data['extends'])
        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()
    # endregion set data
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

    # region Path
    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        if not self._p_name:
            try:
                raise Exception(
                    "InterfaceWriter._get_uno_obj_path() Parser provided a name that is an empty string.")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e
        uno_obj_path = Path(self._path_dir.parent,
                            base.APP_CONFIG.uno_base_dir)
        name_parts: List[str] = self._p_namespace.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append(self._p_name + '.tppi')
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._cache[key] = obj_path
        return self._cache[key]
    # endregion Path
    # region write files
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
    # endregion write files

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
            '{requires_typing}', 'False')
        self._template = self._template.replace('{quote}', 'set()')
        self._template = self._template.replace('{typings}', 'set()')
        self._template = self._template.replace(
            '{include_desc}', str(self._include_desc))
        self._template = self._template.replace(
            '{inherits}', base.Util.get_string_list(lines=self._p_extends))
        self._template = self._template.replace(
            '{from_imports}',
            base.Util.get_formated_dict_list_str(self._get_from_imports())
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
    
    # region Write
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
    # endregion Write
# endregion Writer

# region Parse method


def _get_parsed_kwargs(**kwargs) -> Dict[str, str]:
    required = ("url",)
    lookups = {
        "u": "url",
        "url": "url",
        "L": "log_file",
        "log_file": "log_file"
    }
    result = {}
    for k, v in kwargs.items():
        if not isinstance(k, str):
            continue
        if k in lookups:
            key = lookups[k]
            result[key] = v
    for k in required:
        if not k in result:
            # k is missing from kwargs
            raise base.RequiredError(f"Missing required arg {k}.")
    return result


def _get_parsed_args(*args) -> Dict[str, bool]:
    # key, value and value is a key into defaults
    defaults = {
        'no_sort': True,
        "no_cache": True,
        "no_desc": True,
        "no_print_clear": True,
        "long_template": False,
        "clipboard": False,
        "print_json": False,
        "print_template": False,
        "write_template": False,
        "write_json": False,
        "verbose": False
    }
    found = {
        'no_sort': False,
        "no_cache": False,
        "no_desc": False,
        "no_print_clear": False,
        "long_template": True,
        "clipboard": True,
        "print_json": True,
        "print_template": True,
        "write_template": True,
        "write_json": True,
        "verbose": True,
    }
    lookups = {
        "s": "no_sort",
        "no_sort": "no_sort",
        "x": "no_cache",
        "no_cache": "no_cache",
        "p": "no_print_clear",
        "d": "no_desc",
        "no_desc": "no_desc",
        "no_print_clear": "no_print_clear",
        "g": "long_template",
        "long_template": "long_template",
        "c": "clipboard",
        "clipboard": "clipboard",
        "n": "print_json",
        "print_json": "print_json",
        "m": "print_template",
        "print_template": "print_template",
        "t": "write_template",
        "write_template": "write_template",
        "j": "write_json",
        "write_json": "write_json",
        "v": "verbose",
        "verbose": "verbose"
    }
    result = {k: v for k, v in defaults.items()}
    for arg in args:
        if not isinstance(arg, str):
            continue
        if arg in lookups:
            key = lookups[arg]
            result[key] = found[key]
    return result


def parse(*args, **kwargs):
    """
    Parses data, alternative to running on command line.

    Other Arguments:
        'no_sort' (str, optional): Short form ``'s'``. No sorting of results. Default ``False``
        'no_cache' (str, optional): Short form ``'x'``. No caching. Default ``False``
        'no_desc' (str, optional): Short form ``'d'``. No description will be outputed in template, Defalut ``False``
        'no_print_clear (str, optional): Short form ``'p'``. No clearing of terminal
            when otuput to terminal. Default ``False``
        'print_json' (str, optional): Short form ``'n'``. Print json to termainl. Default ``False``
        'print_template' (str, optional): Short form ``'m'``. Print template to terminal. Default ``False``
        'write_template' (str, optional): Short form ``'t'``. Write template file into obj_uno subfolder. Default ``False``
        'long_template' (str, optional): Short form ``'g'``. Writes a long format template.
            Requires write_template is set. Default ``False``
        'clipboard' (str, optional): Short form ``'c'``. Copy to clipboard. Default ``False``
        'write_json' (str, optional): Short form ``'j'``. Write json file into obj_uno subfolder. Default ``False``
        'verbose' (str, optional): Short form ``'v'``. Verobose output.

    Keyword Arguments:
        url (str): Short form ``u``. url to parse
        log_file (str, optional): Short form ``L``. Log File
    """
    global logger
    pkwargs = _get_parsed_kwargs(**kwargs)
    pargs = _get_parsed_args(*args)
    if logger is None:
        log_args = {}
        if 'log_file' in pkwargs:
            log_args['log_file'] = pkwargs['log_file']
        else:
            log_args['log_file'] = 'service.log'
        if pargs['verbose']:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    p = ParserService(
        url=pkwargs['url'],
        sort=pargs['no_sort'],
        cache=pargs['no_cache']
    )
    w = WriterService(
        parser=p,
        print_template=pargs['print_template'],
        print_json=pargs['print_json'],
        copy_clipboard=pargs['clipboard'],
        write_template=pargs['write_template'],
        write_json=pargs['write_json'],
        clear_on_print=(not pargs['no_print_clear']),
        write_template_long=pargs['long_template'],
        include_desc=pargs['no_desc']
    )
    w.write()
# endregion Parse method


# region Main
def _main():
    # ic = ImportCheck()
    # ic.test()
    # return
    # url = "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1AccessibleIconChoiceControl.html"
    # url = "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1AnimatedImagesControlModel.html"
    # url = "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1SpinningProgressControlModel.html"
    # url = "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1AccessibleCheckBox.html"
    url = "https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1report_1_1Shape.html"
    # sys.argv.extend(['-n', '-v', '-L', 'service.log', '-u', url])
    # main()
    args = ('v', 'n' )
    kwargs = {
        "u": url,
        "log_file": "debug.log"
    }
    parse(*args, **kwargs)

def get_cmd_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='service')
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=True)
    parser.add_argument(
        '-d', '--no-desc',
        help='No description will be outputed in template',
        action='store_false',
        dest='desc',
        default=True)
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
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use. Defaults to service.log',
        type=str,
        required=False)
    args = parser.parse_args()
    return args


def main():
    global logger

    args = get_cmd_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'service.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)

    p = ParserService(
        url=args.url,
        sort=args.sort,
        cache=args.cache
    )
    w = WriterService(
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
# endregion Main

if __name__ == '__main__':
   main()

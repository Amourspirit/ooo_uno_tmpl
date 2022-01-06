#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains a structure
"""
# region Imports
import os
import sys
import logging
import argparse
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple, Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, TypeCheck, TypeCheckKw
from kwhelp import rules
from pathlib import Path
import textwrap
import xerox # requires xclip - sudo apt-get install xclip
try:
    import base
except ModuleNotFoundError:
    import parser.base as base
try:
    from mod_type import PythonType
except ModuleNotFoundError:
    from parser.mod_type import PythonType
from logger.log_handle import get_logger
from parser import __version__, JSON_ID
# endregion Imports

# region Logger

logger = None

def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l

_set_loggers(None)
# endregion Logger

# region Data Class
@dataclass
class DataItem:
    name: str
    is_py_type: bool
    datatype: str
    orig_type: str
    lines: List[str] = field(default_factory=list)

    def __lt__(self, other: 'DataItem'):
        return self.name < other.name

# endregion Data Class

# region API


class ApiPropertiesBlock(base.ApiSummaryBlock):
    def _get_match_name(self) -> str:
        return 'pub-attribs'


class ApiTypesBlock(base.ApiSummaryBlock):
    def _get_match_name(self) -> str:
        return 'pub-types'

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
    # region constructor
    @TypeCheck((str, base.SoupObj), bool, ftype=DecFuncEnum.METHOD)
    def __init__(self, url_soup: Union[str, base.SoupObj], allow_cache: bool):
        super().__init__(url_soup=url_soup, allow_cache=allow_cache)

        self._ns: ApiNs = None
        self._desc: base.ApiDesc = None
        self._properties_block: ApiPropertiesBlock = None
        self._property_summaries: base.ApiSummaries = None
        self._property_summary_rows: base.ApiSummaryRows = None
        
        self._types_block: ApiTypesBlock = None
        self._type_summaries: base.ApiSummaries = None
        self._type_summary_rows: base.ApiSummaryRows = None
        self._name_rules_engine = base.RulesName()
        self._set_name_rules()
    # endregion constructor

    # region Name Rules
    def _set_name_rules(self) -> None:
        self._name_rules_engine.register_rule(base.RuleNameNoGenerics)
    
    def _get_name_rules_engine(self) -> Union[base.IRulesName, None]:
        """
        Gets Name Rules Engine. Overrides parent class

        Returns:
            base.IRulesName: base.RulesName() instance
        """
        return self._name_rules_engine
    # endregion Name Rules

    # region Properties
    @property
    def ns(self) -> ApiNs:
        """Gets the interface Description object"""
        if self._ns is None:
            self._ns = ApiNs(
                self.soup_obj)
        return self._ns

    @property
    def desc(self) -> base.ApiDesc:
        """Gets the interface Description object"""
        if self._desc is None:
            self._desc = base.ApiDesc(self.soup_obj)
        return self._desc

    @property
    def properties_block(self) -> ApiPropertiesBlock:
        """Gets Summary Properties block"""
        if self._properties_block is None:
            self._properties_block = ApiPropertiesBlock(
                self.public_members)
        return self._properties_block

    @property
    def property_summary_rows(self) -> base.ApiSummaryRows:
        """Get Summary rows for Properties"""
        if self._property_summary_rows is None:
            self._property_summary_rows = base.ApiSummaryRows(
                self.properties_block)
        return self._property_summary_rows

    @property
    def property_summaries(self) -> base.ApiSummaries:
        """Get Summary info list for Properties"""
        if self._property_summaries is None:
            self._property_summaries = base.ApiSummaries(
                self.property_summary_rows)
        return self._property_summaries

    @property
    def types_block(self) -> ApiTypesBlock:
        """Gets Summary Properties block"""
        if self._types_block is None:
            self._types_block = ApiTypesBlock(
                self.public_members)
        return self._types_block

    @property
    def types_summary_rows(self) -> base.ApiSummaryRows:
        """Get Summary rows for Properties"""
        if self._type_summary_rows is None:
            self._type_summary_rows = base.ApiSummaryRows(
                self.types_block)
        return self._type_summary_rows

    @property
    def types_summaries(self) -> base.ApiSummaries:
        """Get Summary info list for Properties"""
        if self._type_summaries is None:
            self._type_summaries = base.ApiSummaries(
                self.types_summary_rows)
        return self._type_summaries
    # endregion Properties
# endregion API

# region Parser

class Parser(base.ParserBase):
    # region Constructor
    @RuleCheckAllKw(arg_info={"url": 0, "sort": 1, "replace_dual_colon": 1},
                    rules=[rules.RuleStrNotNullEmptyWs, rules.RuleBool],
                    ftype=DecFuncEnum.METHOD)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._allow_caching = kwargs.get('allow_cache', True)
        self._api_data: ApiData = ApiData(
            url_soup=self.url, allow_cache=self._allow_cache)
        self._data = None
        self._imports: Set[str] = set()
        self._requires_typing = False
        self._cache: Dict[str, object] = {
            "python_types": []
        }

    # endregion Constructor

    # region Data
    def get_dict_data(self) -> dict:
        info = self.get_info()
        items = self._get_data_items()
        info['items'] = items
        return info
    # endregion Data
    # region Info
    def get_info(self) -> Dict[str, str]:
        """
        Gets info

        Returns:
            Dict[str, str]: {
                "name": "name of constant",
                "fullname": "full name such as com.sun.star.awt.Command"
                "desc": "(List[str]), description of constant",
                "url": "Url to LibreOffice of constant",
                "namespace": "namespace",
                "imports": "List[str], imports",
                "extends": "(List[str]), inherits"
            }
        """
        key = 'get_info'
        if key in self._cache:
            return self._cache[key]
        try:
            ex = []
            for el in self._api_data.inherited.get_obj():
                ex.append(el.fullns)
            ni = self._api_data.name.get_obj()
            ns = self._api_data.ns.namespace_str
            full_name = ns + '.' + ni.name
            info = {
                "name": ni.name,
                "fullname": full_name,
                "desc": self._api_data.desc.get_obj(),
                "url": self.url,
                "namespace": ns,
                'imports': [],
                "extends": ex
            }
            self._cache[key] = info
            return self._cache[key]
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e

    def get_parser_args(self) -> dict:
        args = {
            "sort": self._sort
        }
        return args

    # endregion Info

    # region Data

    def get_formated_data(self, indent=4) -> str:
        key = 'get_formated_data'
        if key in self._cache:
            return self._cache[key]
        items = self._get_data_items()
        str_lst = base.Util.get_formated_dict_list_str(
            obj=items, indent=indent)
        self._cache[key] = str_lst
        return self._cache[key]
    
    def _get_data_items(self) -> List[dict]:
        key = '_get_data_items'
        if key in self._cache:
            return self._cache[key]
        p_data = self._get_properties_data()
        self._cache[key] = []
        if 'properties' in p_data:
            self._cache[key].extend(p_data['properties'])
        t_data = self._get_types_data()
        if 'types' in t_data:
            self._cache[key].extend(t_data['types'])
        return self._cache[key]

    def _get_summary_data(self, si_lst: List[base.SummaryInfo], key: str) -> dict:
        attribs = {}
        for i, si in enumerate(si_lst):
            if logger.level <= logging.DEBUG:
                logger.debug(
                    "%s._get_summary_data() Processing: %s, %s",
                    self.__class__.__name__, si.name, si.id)
            if i == 0:
                attribs[key] = []
            if not si.name:
                continue
            attrib = {
                "name": si.name,
                "type": si.p_type.type,
                "lines": self._api_data.get_desc_detail(si.id).get_obj()
            }
            attribs[key].append(attrib)
            if si.p_type.requires_typing:
                logger.debug(
                    "%s._get_summary_data() Return '%s' type require typing for: %s, %s",
                    self.__class__.__name__, si.p_type.type, si.name, si.id)
                self._requires_typing = True

        if self.sort:
            if key in attribs:
                newlist = sorted(attribs[key],
                                 key=lambda d: d['name'])
                attribs[key] = newlist
        return attribs

    def _get_properties_data(self):
        import_info = self._api_data.get_import_info_property()
        if import_info.requires_typing:
            self._requires_typing = True
        self._imports.update(import_info.imports)

        si_lst = self._api_data.property_summaries.get_obj()
        key = 'properties'
        return self._get_summary_data(si_lst=si_lst, key=key)
    
    def _get_types_data(self):
        import_info = self._api_data.get_import_info_type()
        if import_info.requires_typing:
            self._requires_typing = True
        self._imports.update(import_info.imports)

        si_lst = self._api_data.types_summaries.get_obj()
        key = 'types'
        return self._get_summary_data(si_lst=si_lst, key=key)

    # endregion Data

    # region Properties
    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        key = 'get_formated_data'
        if not key in self._cache:
            self.get_formated_data()

        key = 'imports_clean'
        if not key in self._cache:
            if len(self._imports) > 0:
                info = self.get_info()
                ns = info['namespace']
                self._imports = base.Util.get_clean_imports(
                    ns=ns, imports=self._imports)
            self._cache[key] = True
        return self._imports

    @property
    def requires_typing(self) -> set:
        """Gets if import if typing is required"""
        return self._requires_typing

    @property
    def api_data(self) -> ApiData:
        return self._api_data
    # endregion Properties

# endregion Parser

# region Writer
class StructWriter(base.WriteBase):

    # region Constructor
    @TypeCheckKw(arg_info={
        "sort": 0,
        "copy_clipboard": 0,
        "print_template": 0,
        "print_json": 0,
        "write_file": 0,
        "write_json": 0,
        "auto_import": 0,
        "write_template_long": 0,
        "_dynamic_struct": 0
        },
        types=[bool],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser:Parser, **kwargs):
        super().__init__(**kwargs)
        self._parser = parser
        self._sort = kwargs.get('sort', True)
        self._copy_clipboard = kwargs.get('copy_clipboard', False)
        self._print_template = kwargs.get('print_template', False)
        self._auto_import = kwargs.get('auto_import', True)
        self._write_file = kwargs.get('write_template', False)
        self._print_json = kwargs.get('print_json', True)
        self._write_json = kwargs.get('write_json', False)
        self._dynamic_struct = kwargs.get('dynamic_struct', False)
        self._include_desc: bool = kwargs.get('include_desc', True)
        self._write_template_long: bool = kwargs.get(
            'write_template_long', False)
        self._indent_amt = 4
        self._cache: Dict[str, object] = {}
        self._json_str = None
        self._file_full_path = None
        self._p_name = None
        self._p_namespace = None
        self._p_fullname = None
        self._p_url = None
        self._p_desc = None
        self._p_extends: List[str] = None
        self._p_imports: Set[str] = set()
        self._p_imports_typing: Set[str] = set()
        self._p_requires_typing = False
        
        self._path_dir = Path(os.path.dirname(__file__))
        t_file = 'struct'
        if not self._write_template_long:
            t_file += '_stub'
        t_file += '.tmpl'
        _path = Path(self._path_dir, 'template', t_file)
        try:
            if not _path.exists():
                raise FileNotFoundError(f"unable to find templae file '{_path}'")
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        self._template_file = _path
        self._template: str = self._get_template()
    # endregion Constructor


    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def write(self):
        self._set_info()
        self._set_template_data()
        logger.info("Processing %s", self._p_fullname)
        try:
            if self._copy_clipboard:
                xerox.copy(self._template)
                logger.debug('copied to clipbord')
            if self._print_template or self._print_json:
                logger.debug('Printing to terminal')
                os.system('cls' if os.name == 'nt' else 'clear')
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
        p_dict = {
            "name": 'place holder',
            "namespace": 'place holder',
            "url": 'place holder'
        }
        p_dict['from_imports'] = self._get_from_imports()
        p_dict['from_imports_typing'] = self._get_from_imports_typing()
        p_dict['quote'] = self._get_quote_flat()
        p_dict['typings'] = self._get_typings()
        p_dict['requires_typing'] = self._p_requires_typing
        p_dict.update(self._parser.get_dict_data())
        if 'typing_imports' in p_dict:
            del p_dict['typing_imports']

        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            # "timestamp": str(base.Util.get_timestamp_utc()),
            "libre_office_ver": base.APP_CONFIG.libre_office_ver,
            "type": "struct",
            "name": p_dict['name'],
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {
                "sort": self._sort,
                "dynamic_struct": self._dynamic_struct,
                "include_desc": self._include_desc
            },
            "data": p_dict
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._json_str = str_jsn
        return self._json_str

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

    # region quote/typings
    def _get_quote_flat(self) -> List[str]:
        key = '_get_quote_flat'
        if key in self._cache:
            return self._cache[key]

        t_set: Set[str] = set()
        # grab all the properties that need quotes
        si_lst = self._parser.api_data.property_summaries.get_obj()
        for si in si_lst:
            t = si.p_type
            if t.requires_typing or t.is_py_type is False:
                t_set.add(t.type)
        si_lst = self._parser.api_data.types_summaries.get_obj()
        for si in si_lst:
            t = si.p_type
            if t.requires_typing or t.is_py_type is False:
                t_set.add(t.type)
        self._cache[key] = list(t_set)
        return self._cache[key]

    def _get_typings(self) -> List[str]:
        key = '_get_typings'
        if key in self._cache:
            return self._cache[key]
        t_set: Set[str] = set()
        si_lst = self._parser.api_data.property_summaries.get_obj()
        for si in si_lst:
            t = si.p_type
            if t.requires_typing:
                t_set.add(t.type)
        si_lst = self._parser.api_data.types_summaries.get_obj()
        for si in si_lst:
            t = si.p_type
            if t.requires_typing:
                t_set.add(t.type)
        self._cache[key] = list(t_set)
        return self._cache[key]

    # endregion quote/typing

    def _set_template_data(self):
        if self._write_template_long is False:
            return
        self._template = self._template.replace(
            '{libre_office_ver}', base.APP_CONFIG.libre_office_ver)
        self._template = self._template.replace(
            '{dynamic_struct}', str(self._dynamic_struct))
        self._template = self._template.replace('{sort}', str(self._sort))


        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{ns}', str(self._p_namespace))
        self._template = self._template.replace('{link}', self._p_url)
        self._template = self._template.replace(
            '{quote}',
            str(set(self._get_quote_flat())))
        self._template = self._template.replace(
            '{typings}',
            str(set(self._get_typings())))
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

    def _set_info(self):
        def get_extends(lst: List[str]) -> List[str]:
            return [base.Util.get_last_part(s) for s in lst]
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_fullname = data['fullname']
        self._p_data = self._parser.get_formated_data()
        self._p_namespace = data['namespace']
        self._p_extends = get_extends(data['extends'])
        self._validate_p_info()
        self._p_imports.update(data['imports'])
        self._p_imports.update(data['extends'])
        self._p_imports_typing.update(self._parser.imports)

        self._p_imports_typing = self._p_imports_typing - self._p_imports
        if len(self._p_imports_typing) > 0:
            self._p_requires_typing = True
        if not self._p_requires_typing:
            self._p_requires_typing = self._parser.requires_typing

        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()

        # prime cache and set other params such as self._p_requires_typing
        self._get_quote_flat()
        self._get_typings()

    # region validation
    def _validate_p_info(self):
        try:
            if not self._p_name:
                raise Exception(
                    "StructWriter: validation fail: name is an empty string.")
            if not self._p_url:
                raise Exception(
                    "StructWriter: validation fail: url is an empty string.")
            if not self._p_namespace:
                raise Exception(
                    "StructWriter: validation fail: namespace is an empty string.")
        except Exception as e:
            logger.error(e)
            raise e
    # endregion validation

    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        uno_obj_path = Path(self._path_dir.parent,
                            base.APP_CONFIG.uno_base_dir)
        name_parts = self._p_fullname.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        index = len(path_parts) -1
        if not path_parts[index]:
            try:
                raise Exception(
                    "StructWriter._get_uno_obj_path() parsing path yielded an empty string")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e
        path_parts[index] = base.Util.get_clean_filename(path_parts[index]) + '.tmpl'
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._cache[key] = obj_path
        return self._cache[key]

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
        "verbose": False,
        "dynamic_struct": False,
        "no_auto_import": True
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
        "dynamic_struct": True,
        "no_auto_import": False
    }
    lookups = {
        "s": "no_sort",
        "no_sort": "no_sort",
        "x": "no_cache",
        "no_cache": "no_cache",
        "d": "do_desc",
        "no_desc": "no_desc",
        "p": "no_print_clear",
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
        "verbose": "verbose",
        "y": "dynamic_struct",
        "dynamic_struct": "dynamic_struct",
        "a": "no_auto_import",
        "no_auto_import": "no_auto_import"
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
        'no_print_clear (str, optional): Short form ``'p'``. No clearing of terminal
            when otuput to terminal. Default ``False``
        'no_desc' (str, optional): Short from ``'d'``. No description will be outputed in template. Default ``False``
        'dynamic_struct' (str, optional): Short form ``'d'``. Template will generate dynameic struct conten. Default ``False``
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
            log_args['log_file'] = 'struct.log'
        if pargs['verbose']:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    p = Parser(
        url=pkwargs['url'],
        sort=pargs['no_sort'],
        cache=pargs['no_cache']
    )
    w = StructWriter(
        parser=p,
        copy_clipboard=pargs['clipboard'],
        print_template=pargs['print_template'],
        print_json=pargs['print_json'],
        write_template=pargs['write_template'],
        write_json=pargs['write_json'],
        write_template_long=pargs['long_template'],
        clear_on_print=(not pargs['no_print_clear']),
        dynamic_struct=pargs['dynamic_struct']
    )
    w.write()
# endregion Parse method

# region Main
def _main():
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Ambiguous_3_01T_01_4.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1GetPropertyTolerantResult.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1TextMarkupDescriptor.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Pair_3_01T_00_01U_01_4.html' # generics
    url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1accessibility_1_1AccessibleRelation.html'
    args = ('v', 'n')
    kwargs = {
        "u": url,
        "log_file": "debug.log"
    }
    parse(*args, **kwargs)
    # sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    # main()

def main():
    global logger

    # http://pymotw.com/2/argparse/
    parser = argparse.ArgumentParser(description='const')
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=True)
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
        '-s', '--no-sort',
        help='No sorting of results',
        action='store_false',
        dest='sort',
        default=True)
    parser.add_argument(
        '-y', '--dynamic-struct',
        help='Template will generate dynamic struct content',
        action='store_true',
        dest='dynamic_struct',
        default=False)
    parser.add_argument(
        '-d', '--no-desc',
        help='No description will be outputed in template',
        action='store_false',
        dest='desc',
        default=True)
    parser.add_argument(
        '-c', '--clipboard',
        help='Copy to clipboard',
        action='store_true',
        dest='clipboard',
        default=False)
    parser.add_argument(
        '-g', '--long-template',
        help='Writes a long format template. Requires --write-template is set. No Autoload',
        action='store_true',
        dest='long_format',
        default=False)
    parser.add_argument(
        '-t', '--write-template',
        help='Write template file into obj_uno subfolder',
        action='store_true',
        dest='write_template',
        default=False)
    parser.add_argument(
        '-m', '--print-template',
        help='Print template to terminal',
        action='store_true',
        dest='print_template',
        default=False)
    parser.add_argument(
        '-n', '--print-json',
        help='Print json to terminal',
        action='store_true',
        dest='print_json',
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
        help='Log file to use. Default to struct.log',
        type=str,
        required=False)

    args = parser.parse_args()

    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'struct.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')

    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)
    p = Parser(
        url=args.url,
        sort=args.sort,
        cache=args.cache
        )
    if args.print_template is False and args.print_json is False:
        print('')
    w = StructWriter(
        parser=p,
        copy_clipboard=args.clipboard,
        print_template=args.print_template,
        print_json=args.print_json,
        write_template=args.write_template,
        write_json=args.write_json,
        write_template_long=args.long_format,
        dynamic_struct=args.dynamic_struct
        )
    w.write()
    
if __name__ == '__main__':
    main()
# endregion Main
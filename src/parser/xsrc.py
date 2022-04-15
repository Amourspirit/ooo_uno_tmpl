#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains an interface
"""

# region Imports
from kwhelp.decorator import AcceptedTypes, DecFuncEnum, RequireArgs, TypeCheck, TypeCheckKw
import os
import sys
import argparse
import logging
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
import re
from typing import Dict, List, Set, Union
from dataclasses import asdict
from pathlib import Path
from . import base, __version__, JSON_ID
from .api.api_data import APIData
from .api.api_detail_block import ApiDetailBlock
from .api.api_desc_detail import ApiDescDetail
from .api.api_proto_block import ApiProtoBlock
from .api.api_namespace import ApiNamespace
from .common.config import APP_CONFIG
from .common import log_load
from .common import known
from .common.util import Util
from .dataclass.summary_info import SummaryInfo
from .dataclass.import_info import ImportInfo
from .web.soup_obj import SoupObj
from ..logger.log_handle import get_logger
from ..utilities import util as mutil
from ..model.shared.data.methods.method_arg import MethodArg, ArgDirection
# endregion Imports

# region Logger
logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger
    log = log_load.Log()
    log.logger = l
    logger = log.logger


_set_loggers(None)
# endregion Logger

# region Regex
re_component_start = re.compile(r"(interface.*){", re.DOTALL)
re_name_info_start = re.compile(r"(interface)\s*[a-zA-Z0-9]+[ :]+")
re_name_info_name = re.compile(r"interface\s*(?P<NAME>[a-zA-Z0-9_]+)")
# endregion Regex

# region SDK API Reference
re_ln_pattern = re.compile(r"\A\s*(:?[0-9]*)\s*")
# https://regex101.com/r/xAqRAU/1/
re_args_pattern = re.compile(r"\s*(?:\[(\S{2,3})\])?\s*(\S*)\s(\S*)")
# https://regex101.com/r/HU09ZZ/1
re_method_pattern = re.compile(
    r"(\S*)\s*(?:(\S*)\()(?:\s(.*)\))|(\S*)\s*([0-9A-Z-a-z]*)")
# https://regex101.com/r/BdDT4u/1
re_raises_pattern = re.compile(r"\s*(raises\s*\(.*\))")

re_interface_pattern = re.compile(r"interface\s*([a-zA-Z0-9.]*)\s*;")
re_property_pattern = re.compile(
    r"(?:\[attribute[ ,a-z]*\])(?:[ ]+)([a-zA-Z0-9. {}()]*);")
re_comment_start_pattern = re.compile(r"(?:(\/\*)|(?:\*)\s)")
# endregion SDK API Reference

# region API Interface classes


class ApiNs(ApiNamespace):
    """Get the Name object for the interface"""

    def __init__(self, soup: SoupObj):
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


class ApiInterfaceData(APIData):
    # region Constructor
    @TypeCheck((str, SoupObj), bool, bool, bool, ftype=DecFuncEnum.METHOD)
    def __init__(self, url_soup: Union[str, SoupObj], allow_cache: bool, long_names: bool = False, remove_parent_inherited=True):
        super().__init__(url_soup=url_soup, allow_cache=allow_cache,
                         long_names=long_names, remove_parent_inherited=remove_parent_inherited)
        self._si_key = 'summeries'
        self._detail_block_key = 'detail_block'
        self._ns: ApiNs = None
        self._cache = {
            self._si_key: {},
            self._detail_block_key: {}
        }
    # endregion Constructor

    # region Methods
    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_detail_block(self, a_id: str) -> ApiDetailBlock:
        """
        Gets detail block of a function.
        Gets the 

        Args:
            a_id (str): id of block such as ``aa1d747451151fbd244196e6305348dbc``

        Returns:
            ApiDetailBlock: object
        """
        key = f"get_detail_block_{a_id}"
        if key in self._cache:
            return self._cache[key]
        result = super().get_detail_block(a_id=a_id)
        self._cache[key] = result
        return result

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_proto_block(self, a_id: str) -> ApiProtoBlock:
        """Gets the block for a method information"""
        key = f"get_proto_block_{a_id}"
        if key in self._cache:
            return self._cache[key]
        result = super().get_proto_block(a_id=a_id)
        self._cache[key] = result
        return self._cache[key]

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_desc_detail(self, a_id: str) -> ApiDescDetail:
        """Gets Description obj for method or property"""
        key = f"get_desc_detail_{a_id}"
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = super().get_desc_detail(a_id=a_id)
        return self._cache[key]

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_import_info_method(self, a_id: str) -> ImportInfo:
        """
        Gets imports for method params and return type

        Args:
            si_id (str): Function summary Info

        Returns:
            ImportInfo: Import info
        """
        key = 'get_import_info_method_' + a_id
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = super().get_import_info_method(a_id=a_id)
        return self._cache[key]

    # endregion Methods

    # region Properties

    @property
    def ns(self) -> ApiNamespace:
        """Gets the interface Description object"""
        if self._ns is None:
            self._ns = ApiNs(
                self.soup_obj)
        return self._ns

    # endregion Properties
# endregion API Interface classes

# region Parse


class Parser(base.ParserBase):

    # region Constructor
    @TypeCheckKw(
        arg_info={
            "long_names": 0,
            "remove_parent_inherited": 0
        },
        types=[bool],
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._long_names: bool = kwargs.get('long_names', False)
        self._remove_parent_inherited: bool = kwargs.get(
            'remove_parent_inherited', True)
        self._api_data = ApiInterfaceData(
            url_soup=self.url,
            allow_cache=self.allow_cache,
            long_names=self._long_names,
            remove_parent_inherited=self._remove_parent_inherited
        )
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._cache = {}
    # endregion Constructor

    def get_dict_data(self) -> dict:
        info = self.get_info()
        items = self._get_data_items()
        info['items'] = items
        return info

    def get_parser_args(self) -> dict:
        args = {
            "sort": self.sort,
            "long_names": self.long_names,
            "remove_parent_inherited": self._remove_parent_inherited
        }
        return args

    def get_full_name(self) -> str:
        ni = self._api_data.name.get_obj()
        return self._api_data.ns.namespace_str + '.' + ni.name

    def get_info(self) -> Dict[str, object]:
        """
        Gets info

        Returns:
            Dict[str, object]: {
                "name": "str, class name",
                "imports": "List[str], imports",
                "namespace": "str, Namespace",
                "extends": "List[str], class extends",
                "desc": "List[str], class description",
                "url": "str, api url"
            }
        """
        key = 'get_info'
        if key in self._cache:
            return self._cache[key]
        ex = []
        for el in self._api_data.inherited.get_obj():
            ex.append(el.fullns)
        # ex_s = Util.get_clean_imports(ns=ns.namespace_str, imports=ex)
        ni = self._api_data.name.get_obj()
        result = {
            # 'name': ni.name,
            'name': ni.name,
            'imports': [],
            'namespace': self._api_data.ns.namespace_str,
            'extends': ex,
            'desc': self._api_data.desc.get_obj(),
            "url": self._api_data.url_obj.url,
        }
        logger.debug('Parser.get_info() name: %s', result['name'])
        logger.debug('Parser.get_info() namespace: %s',
                     result['namespace'])
        self._cache[key] = result
        return self._cache[key]

    # region get data

    def get_formated_data(self) -> str:
        key = 'get_formated_data'
        if key in self._cache:
            return self._cache[key]
        attribs = self._get_data_items()
        str_lst = Util.get_formated_dict_list_str(obj=attribs, indent=4)
        self._cache[key] = str_lst
        return self._cache[key]

    def _get_data_items(self) -> dict:
        key = '_get_data_items'
        if key in self._cache:
            return self._cache[key]
        attribs = {}
        methods = self._get_methods_data()
        prop = self._get_properties_data()
        types = self._get_types_data()
        if 'methods' in methods:
            attribs.update(methods)
        if 'types' in types:
            attribs.update(types)
        if 'properties' in prop:
            attribs.update(prop)
        self._cache[key] = attribs
        return self._cache[key]

    def _get_methods_data(self) -> dict:
        attribs = {}
        si_lst = self._api_data.func_summaries.get_obj()
        for i, si in enumerate(si_lst):
            if logger.level <= logging.DEBUG:
                logger.debug(
                    "%s._get_methods_data() Processing: %s, %s",
                    self.__class__.__name__, si.name, si.id)
            import_info = self._api_data.get_import_info_method(si.id)
            params_info = self._api_data.get_prams_info(si.id)
            lst_info = params_info.get_obj()
            if i == 0:
                attribs['methods'] = []
            if import_info.requires_typing:
                logger.debug(
                    "%s._get_methods_data() Imports require typing for: %s, %s",
                    self.__class__.__name__, si.name, si.id)
                self._requires_typing = True
            self._imports.update(import_info.imports)
            if params_info.requires_typing:
                logger.debug(
                    "%s._get_methods_data() Params require typing for: %s, %s",
                    self.__class__.__name__, si.name, si.id)
                self._requires_typing = True
            self._imports.update(params_info.imports)
            if si.p_type.requires_typing:
                logger.debug(
                    "%s._get_methods_data() Return '%s' type require typing for: %s, %s",
                    self.__class__.__name__, si.p_type.type, si.name, si.id)
                self._requires_typing = True
            args = []
            attrib = {
                "name": si.name,
                "returns": si.p_type.type,
                "returns_origin": si.p_type.origin,
                "desc": self._api_data.get_desc_detail(si.id).get_obj(),
                "raises": self._api_data.get_method_ex(si.id).get_obj() or []
            }
            for pi in lst_info:
                if logger.level <= logging.DEBUG:
                    logger.debug(
                        f"{self.__class__.__name__}._get_methods_data() {si.name} param, Name: {pi.name}, Type: {pi.type}, Direction: {pi.direction}")
                meth = MethodArg(
                    name=pi.name,
                    type=pi.type,
                    direction=ArgDirection(pi.direction),
                    origin=pi.p_type.origin
                )
                args.append(asdict(meth))
            attrib['args'] = args
            attribs['methods'].append(attrib)

        if self.sort:
            if 'methods' in attribs:
                newlist = sorted(attribs['methods'], key=lambda d: d['name'])
                attribs['methods'] = newlist
        return attribs

    def _get_summary_data(self, si_lst: List[SummaryInfo], key: str) -> dict:
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
                "returns": si.p_type.type,
                "origtype": si.p_type.origtype,
                "origin": si.p_type.origin,
                "desc": self._api_data.get_desc_detail(si.id).get_obj(),
                "raises_get": '',
                "raises_set": ''
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
        si_lst = self._api_data.property_summaries.get_obj()
        key = 'properties'
        import_info = self._api_data.get_import_info_property()
        if len(import_info.imports) > 0:
            # return {}
            if import_info.requires_typing:
                self._requires_typing = True
            self._imports.update(import_info.imports)
        return self._get_summary_data(si_lst=si_lst, key=key)

    def _get_types_data(self):
        # treat typedef as property
        si_lst = self._api_data.types_summaries.get_obj()
        key = 'types'
        import_info = self._api_data.get_import_info_type()
        if len(import_info.imports) > 0:
            # return {}
            if import_info.requires_typing:
                self._requires_typing = True
            self._imports.update(import_info.imports)
        return self._get_summary_data(si_lst=si_lst, key=key)

    # endregion get data

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
                self._imports = Util.get_clean_imports(
                    ns=ns, imports=self._imports)
            self._cache[key] = True
        return self._imports

    @property
    def requires_typing(self) -> bool:
        """Gets requires typing value"""
        try:
            key = 'get_formated_data'
            if not key in self._cache:
                msg = "Parser.get_formated_data() method must be called before accessing requires_typing"
                raise Exception(msg)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._requires_typing

    @property
    def api_data(self) -> ApiInterfaceData:
        return self._api_data

    @property
    def long_names(self) -> bool:
        """Gets long_names value"""
        return self._long_names

    @property
    def remove_parent_inherited(self) -> bool:
        """Gets remove_parent_inherited value"""
        return self._remove_parent_inherited
    # endregion Properties
# endregion Parse

# region Writer


class Writer(base.WriteBase):
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
    def __init__(self, parser: Parser, **kwargs):
        super().__init__(**kwargs)
        self._parser: Parser = parser
        self._copy_clipboard: bool = kwargs.get('copy_clipboard', False)
        self._print_template: bool = kwargs.get('print_template', False)
        self._write_file: bool = kwargs.get('write_template', False)
        self._print_json: bool = kwargs.get('print_json', True)
        self._write_json: bool = kwargs.get('write_json', False)
        self._clear_on_print: bool = kwargs.get('clear_on_print', True)
        self._include_desc: bool = kwargs.get('include_desc', True)
        self._json_out: bool = kwargs.get('json_out', True)
        self._allow_db = kwargs.get('allow_db', True)
        self._write_template_long: bool = kwargs.get(
            'write_template_long', False)
        self._allow_known_json: bool = bool(
            kwargs.get('allow_known_json', True))
        self._write_path: Union[str, None] = kwargs.get('write_path', None)
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

        t_file = self._get_template_name()
        if not self._write_template_long:
            t_file += '_stub'
        t_file += '.tmpl'
        self._template_dir = Path(self._path_dir, 'template')
        _path = Path(self._template_dir, t_file)
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

    def _get_template_name(self) -> str:
        """
        Gets the template name without extension or appended __stub

        Returns:
            str: interface
        """
        return 'interface'

    def _get_template_dyn(self) -> Union[str, None]:
        return 'interface_dyn.tmpl'
    
    def _get_template_pyi(self) -> Union[str, None]:
        return 'interface_pyi.tmpl'

    def write(self) -> Union[str, None]:
        """
        Writes files/templates according to parameters

        Returns:
            Union[str, None]: Returns json string if ``json_out`` is ``True``
        """
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
                self._write_to_file_dyn()
                self._write_to_file_pyi()
            if self._write_json:
                self._write_to_json()
            if self._json_out:
                return self._get_json()
        except Exception as e:
            logger.exception(e)

    def _get_json_type(sefl) -> str:
        return "interface"

    def _get_json(self) -> str:
        if not self._json_str is None:
            return self._json_str
        if self._allow_known_json:
            full_ns = self._parser.get_full_name()
            known_json = known.get_known_json(full_ns=full_ns)
            if known_json:
                self._json_str = known_json
                return self._json_str
        p_dict = {}
        p_dict['allow_db'] = self._allow_db
        p_dict['from_imports'] = self._get_from_imports()
        p_dict['from_imports_typing'] = self._get_from_imports_typing()
        p_dict['extends_map'] = self._get_imports_map()
        p_dict['quote'] = self._get_quote_flat()
        p_dict['typings'] = self._get_typings()
        p_dict['requires_typing'] = self._p_requires_typing
        p_dict['full_imports'] = self._get_full_imports()
        p_dict.update(self._parser.get_dict_data())

        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            # "timestamp": str(Util.get_timestamp_utc()),
            "libre_office_ver": APP_CONFIG.libre_office_ver,
            "name": p_dict['name'],
            "type": self._get_json_type(),
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {
                "include_desc": self._include_desc
            },
            "data": p_dict
        }
        str_jsn = Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._json_str = str_jsn
        return self._json_str

    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    # region get Imports
    def _get_full_imports(self) -> Dict[str, List[str]]:
        key = '_get_full_imports'
        if key in self._cache:
            return self._cache[key]

        def get_imports() -> List[str]:
            ims = []
            lst_im = list(self._p_imports)
            # sort for consistency in json
            lst_im.sort()
            for ns in lst_im:
                ims.append(Util.get_full_import(
                    ns=self._p_namespace, name=ns))
            return ims

        def get_imports_typing() -> List[str]:
            ims = []
            lst_im = list(self._p_imports_typing)
            # sort for consistency in json
            lst_im.sort()
            for ns in lst_im:
                ims.append(Util.get_full_import(
                    ns=self._p_namespace, name=ns))
            return ims
        result = {
            "general": get_imports(),
            "typing": get_imports_typing()
        }
        self._cache[key] = result
        return self._cache[key]

    def _get_from_imports(self) -> List[List[str]]:
        key = '_get_from_imports'
        if key in self._cache:
            return self._cache[key]
        lst = []
        if self._parser.long_names:
            rel_fn = Util.get_rel_import_long
        else:
            rel_fn = Util.get_rel_import
        lst_im = list(self._p_imports)
        # sort for consistency in json
        lst_im.sort()
        for ns in lst_im:
            # f, n = rel_fn(ns, self._p_namespace)
            # lst.append([f, n])
            lst.append([*rel_fn(ns, self._p_namespace)])
        self._cache[key] = lst
        return self._cache[key]

    def _get_from_imports_typing(self) -> List[List[str]]:
        key = '_get_from_imports_typing'
        if key in self._cache:
            return self._cache[key]
        lst = []
        if self._parser.long_names:
            rel_fn = Util.get_rel_import_long
        else:
            rel_fn = Util.get_rel_import
        lst_im = list(self._p_imports_typing)
        # sort for consistency in json
        lst_im.sort()
        for ns in lst_im:
            # f, n = rel_fn(ns, self._p_namespace)
            # lst.append([f, n])
            lst.append([*rel_fn(ns, self._p_namespace)])
        self._cache[key] = lst
        return self._cache[key]

    def _get_imports_map(self) -> Dict[str, str]:
        key = '_get_imports_map'
        if key in self._cache:
            return self._cache[key]
        results = {}
        if self._parser.long_names is False:
            return results
        # sort for consistency in json
        lst = list(self._p_imports)
        lst.sort()
        for im in lst:
            results[im] = Util.get_rel_import_long_name(
                im, ns=self._p_namespace)
        self._cache[key] = results
        return self._cache[key]

    def _get_quote_flat(self) -> List[str]:
        key = '_get_quote_flat'
        if key in self._cache:
            return self._cache[key]

        t_set: Set[str] = set()
        # grab all the methods that need quotes
        si_lst = self._parser.api_data.func_summaries.get_obj()
        for si in si_lst:
            t = si.p_type
            if t.requires_typing or t.is_py_type is False:
                t_set.add(t.type)
            # process method params
            params_info = self._parser.api_data.get_prams_info(si.id)
            p_lst = params_info.get_obj()
            for pinfo in p_lst:
                if pinfo.p_type:
                    if pinfo.p_type.requires_typing or pinfo.p_type.is_py_type is False:
                        t_set.add(pinfo.p_type.type)

        # grab all the properties that need quotes
        si_lst = self._parser.api_data.property_summaries.get_obj()
        for si in si_lst:
            t = si.p_type
            if t.requires_typing or t.is_py_type is False:
                t_set.add(t.type)

        # grab all types summaries
        si_lst = self._parser.api_data.types_summaries.get_obj()
        for si in si_lst:
            t = si.p_type
            if t.requires_typing or t.is_py_type is False:
                t_set.add(t.type)

        # grab all export summaries
        si_lst = self._parser.api_data.exported_summaries.get_obj()
        for si in si_lst:
            t = si.p_type
            if t.requires_typing or t.is_py_type is False:
                t_set.add(t.type)

        lst = list(t_set)
        # sort for consistency in json
        lst.sort()
        self._cache[key] = lst
        return self._cache[key]

    def _get_typings(self) -> List[str]:
        key = '_get_typings'
        if key in self._cache:
            return self._cache[key]
        t_set: Set[str] = set()
        si_lst = self._parser.api_data.func_summaries.get_obj()
        for si in si_lst:
            t = si.p_type
            if t.requires_typing:
                t_set.add(t.type)
            # process method params
            params_info = self._parser.api_data.get_prams_info(si.id)
            p_lst = params_info.get_obj()
            for pinfo in p_lst:
                if pinfo.p_type:
                    if pinfo.p_type.requires_typing:
                        t_set.add(pinfo.p_type.type)
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
        si_lst = self._parser.api_data.exported_summaries.get_obj()
        for si in si_lst:
            t = si.p_type
            if t.requires_typing:
                t_set.add(t.type)
        lst = list(t_set)
        # sort for consistency in json
        lst.sort()
        self._cache[key] = lst
        return self._cache[key]
    # endregion get Imports

    def _set_template_data(self):
        if self._write_template_long is False:
            return
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{ns}', str(self._p_namespace))
        self._template = self._template.replace('{link}', self._p_url)
        self._template = self._template.replace(
            '{allow_db}', str(self._allow_db))
        self._template = self._template.replace(
            '{extends_map}', Util.get_formated_dict_list_str(self._get_imports_map()))
        self._template = self._template.replace(
            '{libre_office_ver}', APP_CONFIG.libre_office_ver)
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
            '{inherits}', Util.get_string_list(lines=self._p_extends))
        self._template = self._template.replace(
            '{imports}', "[]")
        self._template = self._template.replace(
            '{from_imports}',
            Util.get_formated_dict_list_str(self._get_from_imports())
        )
        self._template = self._template.replace(
            '{from_imports_typing}',
            Util.get_formated_dict_list_str(
                self._get_from_imports_typing())
        )
        if len(self._p_desc) > 0:
            desc = Util.get_formated_dict_list_str(self._p_desc, indent=4)
        else:
            desc = "[]"
        self._template = self._template.replace('{desc}', desc)
        if self._indent_amt > 0:
            indent = ' ' * self._indent_amt
            indented = textwrap.indent(self._p_data, indent).lstrip()
        else:
            indented = self._p_data.lstrip()
        self._template = self._template.replace('{data}', indented)

    def _set_info(self):
        key = '_set_info'
        if key in self._cache:
            return

        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_namespace = data['namespace']
        self._p_extends = data['extends']
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_data = self._parser.get_formated_data()
        self._p_requires_typing = False
        self._validate_p_info()
        _imports = data['imports']
        self._p_imports.update(_imports)
        for el in self._parser.api_data.inherited.get_obj():
            if el.python_import:
                continue
            self._p_imports.add(el.fullns)
        self._p_imports_typing.update(self._parser.imports)
        self._p_imports = Util.get_clean_imports(
            ns=self._p_namespace,
            imports=self._p_imports
        )
        self._p_imports_typing = Util.get_clean_imports(
            ns=self._p_namespace,
            imports=self._p_imports_typing
        )
        # in some cases such as XIntrospectionAccess
        # https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XIntrospectionAccess.html
        # class is a subclass of XInterface and has a method the has return type XInterface.
        # remove any overlap in _p_imports_typing
        self._p_imports_typing = self._p_imports_typing - self._p_imports
        if len(self._p_imports_typing) > 0:
            self._p_requires_typing = True
        if not self._p_requires_typing:
            self._p_requires_typing = self._parser.requires_typing
        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()
        self._cache[key] = True

    def _validate_p_info(self):
        try:
            if not self._p_name:
                raise Exception(
                    "Writer: validation fail: name is an empty string.")
            if not self._p_url:
                raise Exception(
                    "Writer: validation fail: url is an empty string.")
            if not self._p_namespace:
                raise Exception(
                    "Writer: validation fail: namespace is an empty string.")
        except Exception as e:
            logger.error(e)
            raise e

    def _get_template_ext(self) -> str:
        """Gets Template extension. Can be overriden"""
        return APP_CONFIG.template_interface_ext

    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        if not self._p_name:
            try:
                raise Exception(
                    "Writer._get_uno_obj_path() Parser provided a name that is an empty string.")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e
        if self._write_path:
            write_path = self._write_path
        else:
            write_path = APP_CONFIG.uno_base_dir
        uno_obj_path = Path(mutil.get_root(), write_path)
        name_parts: List[str] = self._p_namespace.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append(self._p_name + self._get_template_ext())
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._cache[key] = obj_path
        return self._cache[key]

    def _write_to_file(self):
        with open(self._file_full_path, 'w') as f:
            f.write(self._template)
        logger.info("Created file: %s", self._file_full_path)

    def _write_to_file_dyn(self):
        name = self._get_template_dyn()
        if name is None:
            return
        p = self._template_dir / name
        with open(p, 'r') as t_file:
            contents = t_file.read()

        out_file = self._file_full_path.stem + APP_CONFIG.template_dyn_ext
        write_path = self._file_full_path.parent / out_file
        with open(write_path, 'w') as out_file:
            out_file.write(contents)
        logger.info('create file: %s', write_path)

    def _write_to_file_pyi(self):
        name = self._get_template_pyi()
        if name is None:
            return
        p = self._template_dir / name
        with open(p, 'r') as t_file:
            contents = t_file.read()

        out_file = self._file_full_path.stem + APP_CONFIG.template_pyi_ext
        write_path = self._file_full_path.parent / out_file
        with open(write_path, 'w') as out_file:
            out_file.write(contents)
        logger.info('create file: %s', write_path)

    def _write_to_json(self):
        p = self._file_full_path.parent
        jsn_p = p / (str(self._file_full_path.stem) + '.json')
        jsn_str = self._get_json()
        with open(jsn_p, 'w') as f:
            f.write(jsn_str)
        logger.info("Created file: %s", jsn_p)
# endregion Writer

# region Parse method


class Processer:
    """Processes parsing and writing"""
    @RequireArgs('url', ftype=DecFuncEnum.METHOD)
    def __init__(self, p: type[Parser], w: type[Writer], **kwargs):
        """
        Constructor

        Args:
            p (type[Parser]): Parser class
            w (type[Writer]): Writer class

        Keyword Arguments:
            url (str): url to parse
            sort (str, optional): Sorting of results. Default ``True``
            cache (str, optional): Caching. Default ``False``
            clear_on_print (str, optional): Clearing of terminal when otuput to terminal. Default ``False``
            include_desc (str, optional): Description will be outputed in template. Default ``True``
            json_out (bool, optional): returns json to caller if ``True``. Default ``False``
            long_names (str, optional): Long names. Default set in config ``use_long_import_names`` property.
                Toggles values set in config.
            write_template_long (str, optional): Writes a long format template.
                Requires write_template is set. Default ``False``
            copy_clipboard (str, optional): Copy to clipboard. Default ``False``
            print_json (str, optional): Print json to termainl. Default ``False``
            print_template (str, optional): Print template to terminal. Default ``False``
            write_template (str, optional): Write template file into obj_uno subfolder. Default ``False``
            write_json (str, optional): Write json file into obj_uno subfolder. Default ``False``
            write_path (str, optional): The root path to write data files (json, tmpl) into. Defaut set in config ``uno_base_dir``
            allow_known_json (bool, optional): Allow Known Json to be used. Default ``True``
            verbose (str, optional): Verobose output.
            log_file (str, optional): Log File
            remove_parent_inherited (bool, optional): Determins if parsers remove classes from inhertiance if an inherited class
                is already inherited by a parent class.
        """
        self._parser = p
        self._writer = w
        self._url = str(kwargs['url'])
        self._sort = bool(kwargs.get('sort', True))
        self._cache = bool(kwargs.get('cache', False))
        self._json_out = bool(kwargs.get('json_out', False))
        self._print_clear = bool(kwargs.get('clear_on_print', False))
        self._long_template = bool(kwargs.get('write_template_long', False))
        self._clipboard = bool(kwargs.get('copy_clipboard', False))
        self._print_json = bool(kwargs.get('print_json', False))
        self._print_template = bool(kwargs.get('print_template', False))
        self._write_template = bool(kwargs.get('write_template', False))
        self._write_json = bool(kwargs.get('write_json', False))
        self._verbose = bool(kwargs.get('verbose', False))
        self._include_desc = bool(kwargs.get('include_desc', True))
        self._long_names = bool(kwargs.get(
            'long_names', APP_CONFIG.use_long_import_names))
        self._remove_parent_inherited = bool(
            kwargs.get('remove_parent_inherited', APP_CONFIG.remove_parent_inherited))
        self._allow_know_json = bool(kwargs.get('allow_known_json', True))
        self._write_path: Union[str, None] = kwargs.get('write_path', None)

    def process(self) -> Union[str, None]:
        parser = self._parser(
            url=self._url,
            sort=self._sort,
            cache=self._cache,
            long_names=self._long_names,
            remove_parent_inherited=self._remove_parent_inherited
        )
        w = self._writer(
            parser=parser,
            print_template=self._print_template,
            print_json=self._print_json,
            copy_clipboard=self._clipboard,
            write_template=self._write_template,
            write_json=self._write_json,
            clear_on_print=self._print_clear,
            write_template_long=self._long_template,
            include_desc=self._include_desc,
            json_out=self._json_out,
            allow_known_json=self._allow_know_json,
            write_path=self._write_path
        )
        return w.write()


def get_kwargs_from_args(args: argparse.ArgumentParser) -> dict:
    """
    Converts argparse args into dictionary that can be passed to ``parse()``

    Args:
        args (argparse.ArgumentParser): args

    Returns:
        dict: dictionary that contain key values matching ``parser()`` args.
    """
    d = {
        "url": args.url,
        "sort": args.sort,
        "cache": args.cache,
        "clear_on_print": args.print_clear,
        "copy_clipboard": args.clipboard,
        "print_template": args.print_template,
        "write_template": args.write_template,
        "write_template_long": args.long_format,
        "print_json": args.print_json,
        "write_json": args.write_json,
        "include_desc": args.desc,
        "long_names": args.long_names,
        "allow_known_json": args.allow_know_json,
        "log_file": args.log_file,
        "verbose": args.verbose
    }
    if args.write_path:
        d['write_path'] = args.write_path
    return d


def parse(**kwargs) -> Union[str, None]:
    """
    Parses data, alternative to running on command line.

    Keyword Arguments:
        url (str): url to parse
        sort (str, optional): Sorting of results. Default ``True``
        cache (str, optional): Caching. Default ``False``
        clear_on_print (str, optional): Clearing of terminal when otuput to terminal. Default ``False``
        include_desc (str, optional): Description will be outputed in template. Default ``True``
        json_out (bool, optional): returns json to caller if ``True``. Default ``False``
        long_names (str, optional): Long names. Default set in config ``use_long_import_names`` property.
            Toggles values set in config.
        write_template_long (str, optional): Writes a long format template.
            Requires write_template is set. Default ``False``
        copy_clipboard (str, optional): Copy to clipboard. Default ``False``
        print_json (str, optional): Print json to termainl. Default ``False``
        print_template (str, optional): Print template to terminal. Default ``False``
        write_template (str, optional): Write template file into obj_uno subfolder. Default ``False``
        write_json (str, optional): Write json file into obj_uno subfolder. Default ``False``
        write_path (str, optional): The root path to write data files (json, tmpl) into. Defaut set in config ``uno_base_dir``
        allow_known_json (bool, optional): Allow Known Json to be used. Default ``True``
        verbose (str, optional): Verobose output.
        log_file (str, optional): Log File
    
    Returns:
        Union[str, None]: Returns json string if json_out is ``True``
    """
    global logger
    _url = str(kwargs['url'])
    _sort = bool(kwargs.get('sort', True))
    _cache = bool(kwargs.get('cache', True))
    _json_out = bool(kwargs.get('json_out', False))
    _print_clear = bool(kwargs.get('clear_on_print', False))
    _clipboard = bool(kwargs.get('copy_clipboard', False))
    _print_template = bool(kwargs.get('print_template', False))
    _write_template = bool(kwargs.get('write_template', False))
    _long_template = bool(kwargs.get('write_template_long', False))
    _print_json = bool(kwargs.get('print_json', False))
    _write_json = bool(kwargs.get('write_json', bool))
    _include_desc = bool(kwargs.get('include_desc', True))
    _long_names = bool(kwargs.get(
        'long_names', APP_CONFIG.use_long_import_names))
    _allow_know_json = bool(kwargs.get('allow_known_json', True))
    _log_file = kwargs.get('log_file', None)
    _verbose = bool(kwargs.get('verbose', False))
    _write_path = kwargs.get('write_path', None)

    if logger is None:
        log_args = {}
        if _log_file:
            log_args['log_file'] = _log_file
        else:
            log_args['log_file'] = 'interface.log'
        if _verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    parser: Parser = kwargs.get('class_parser', Parser)
    writer: Writer = kwargs.get('class_writer', Writer)
    proc = Processer(
        p=parser,
        w=writer,
        url=_url,
        sort=_sort,
        cache=_cache,
        print_template=_print_template,
        print_json=_print_json,
        copy_clipboard=_clipboard,
        write_template=_write_template,
        write_json=_write_json,
        clear_on_print=_print_clear,
        write_template_long=_long_template,
        include_desc=_include_desc,
        long_names=_long_names,
        json_out=_json_out,
        allow_known_json=_allow_know_json,
        write_path=_write_path
    )
    return proc.process()

# endregion Parse method

# region Main


def _main():
    os.system('cls' if os.name == 'nt' else 'clear')
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XIntrospectionAccess.html' # has a sequence
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XPropertyControl.html'  # no import
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XGridColumnModel.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1deployment_1_1XPackage.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tree_1_1XMutableTreeNode.html'
    url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XDevice.html'
    kwargs = {
        "url": url,
        "log_file": "debug.log",
        'verbose': True,
        "write_json": True,
        "write_path": 'scratch/uno_obj'
    }
    # sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    # main()
    parse(**kwargs)


# region Parser
def set_cmd_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=True)
    parser.add_argument(
        '-o', '--out',
        help=f"Out path of templates and json data. Default: '{APP_CONFIG.uno_base_dir}'",
        type=str,
        dest='write_path',
        default=None,
        required=False)
    parser.add_argument(
        '-d', '--no-desc',
        help='No description will be outputed in template',
        action='store_false',
        dest='desc',
        default=True)
    parser.add_argument(
        '-l', '--long-names',
        help='Toggels default value of config. Short Names such as XInterface will be generated instead of XInterface_8f010a43 or vice versa',
        action='store_false' if APP_CONFIG.use_long_import_names else 'store_true',
        dest='long_names',
        default=APP_CONFIG.use_long_import_names)
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
        dest='print_clear',
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
        '-k', '--no-allow-known-json',
        help='Do not allow Known Json',
        action='store_false',
        dest='allow_know_json',
        default=True)


def set_cmd_args_local(parser) -> None:
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use. Defaults to interface.log',
        type=str,
        required=False)

# endregion Parser


def main():
    global logger
    parser = argparse.ArgumentParser(description='interface')
    set_cmd_args(parser)
    set_cmd_args_local(parser)
    args = parser.parse_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'interface.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    if args.print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)
    args_dict = get_kwargs_from_args(args)

    if args.print_template is False and args.print_json is False:
        print('')
    parse(**args_dict)

# endregion Main

#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains an interface
"""

# region Imports
import os
import sys
import argparse
import logging
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
import re
from typing import Dict, List, Set, Union
from kwhelp.decorator import AcceptedTypes, DecFuncEnum, RequireArgs, TypeCheckKw
from pathlib import Path
try:
    import base
except ModuleNotFoundError:
    import parser.base as base
from logger.log_handle import get_logger
from parser.base import SummaryInfo
from parser import __version__, JSON_ID
# endregion Imports

# region Logger
logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger
    logger = l
    base._set_loggers(l)


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


class ApiInterfaceData(base.APIData):
    # region Constructor
    def __init__(self, url_soup: Union[str, base.SoupObj], allow_cache: bool):
        super().__init__(url_soup=url_soup, allow_cache=allow_cache)
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
    def get_detail_block(self, a_id: str) -> base.ApiDetailBlock:
        """
        Gets detail block of a function.
        Gets the 

        Args:
            si (SummaryInfo): Function summary Info to get the details block for.

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
    def get_proto_block(self, a_id: str) -> base.ApiProtoBlock:
        """Gets the block for a method information"""
        key = f"get_proto_block_{a_id}"
        if key in self._cache:
            return self._cache[key]
        result = super().get_proto_block(a_id=a_id)
        self._cache[key] = result
        return self._cache[key]


    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_desc_detail(self, a_id: str) -> base.ApiDescDetail:
        """Gets Description obj for method or property"""
        key = f"get_desc_detail_{a_id}"
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = super().get_desc_detail(a_id=a_id)
        return self._cache[key]

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def get_import_info_method(self, a_id: str) -> base.ImportInfo:
        """
        Gets imports for method params and return type

        Args:
            si_id (str): Function summary Info

        Returns:
            base.ImportInfo: Import info
        """
        key = 'get_import_info_method_' + a_id
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = super().get_import_info_method(a_id=a_id)
        return self._cache[key]

    
    # endregion Methods

    # region Properties

    @property
    def ns(self) -> ApiNs:
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
        arg_info={"allow_cache": bool},
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._allow_caching = kwargs.get('allow_cache', True)
        self._api_data = ApiInterfaceData(
            url_soup=self.url, allow_cache=self._allow_cache)
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
            "sort": self.sort
        }
        return args

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
        ni = self._api_data.name.get_obj()
        result = {
            # 'name': ni.name,
            'name': ni.name,
            # convert set to list for json
            # 'imports': list(im.get_obj()),
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
        str_lst = base.Util.get_formated_dict_list_str(obj=attribs, indent=4)
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

    def _get_methods_data(self):
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
                "desc": self._api_data.get_desc_detail(si.id).get_obj(),
                "raises": self._api_data.get_method_ex(si.id).get_obj() or []
            }
            for pi in lst_info:
                if logger.level <= logging.DEBUG:
                    logger.debug(
                        f"{self.__class__.__name__}._get_methods_data() {si.name} param, Name: {pi.name}, Type: {pi.type}, Direction: {pi.direction}")
                args.append((pi.name, pi.type, pi.direction))
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
        import_info = self._api_data.get_import_info_property()
        if import_info.requires_typing:
            self._requires_typing = True
        self._imports.update(import_info.imports)

        if self.sort:
            if key in attribs:
                newlist = sorted(attribs[key],
                                 key=lambda d: d['name'])
                attribs[key] = newlist
        return attribs


    def _get_properties_data(self):
        si_lst = self._api_data.property_summaries.get_obj()
        key = 'properties'
        return self._get_summary_data(si_lst=si_lst, key=key)

    def _get_types_data(self):
        # treat typedef as property
        si_lst = self._api_data.types_summaries.get_obj()
        key = 'types'
        return self._get_summary_data(si_lst=si_lst, key=key)

    # endregion get data

    # region Properties
    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        try:
            key = 'get_formated_data'
            if not key in self._cache:
                msg = "Parser.get_formated_data() method must be called before accessing imports"
                raise Exception(msg)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
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

        t_file = self._get_template_name()
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

    def _get_template_name(self) -> str:
        """
        Gets the template name without extension or appended __stub

        Returns:
            str: interface
        """
        return 'interface'

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

    def _get_json_type(sefl) -> str:
        return "interface"

    def _get_json(self) -> str:
        if not self._json_str is None:
            return self._json_str
        p_dict = {}
        p_dict['from_imports'] = self._get_from_imports()
        p_dict['from_imports_typing'] = self._get_from_imports_typing()
        p_dict['quote'] = self._get_quote_flat()
        p_dict['typings'] = self._get_typings()
        p_dict['requires_typing'] = self._p_requires_typing
        p_dict.update(self._parser.get_dict_data())

        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "timestamp": str(base.Util.get_timestamp_utc()),
            "name": p_dict['name'],
            "type": self._get_json_type(),
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {
                "include_desc": self._include_desc
            },
            "data": p_dict
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._json_str = str_jsn
        return self._json_str

    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

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
            # lst.append(f)
            # lst.append(n)
            lst.append([f, n])
        self._cache[key] = lst
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

        self._cache[key] = list(t_set)
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
        self._cache[key] = list(t_set)
        return self._cache[key]
    # endregion get Imports

    def _set_template_data(self):
        if self._write_template_long is False:
            return
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

    def _set_info(self):
        key = '_set_info'
        if key in self._cache:
            return

        def get_extends(lst: List[str]) -> List[str]:
            return [base.Util.get_last_part(s) for s in lst]
            # return [s.rsplit('.', 1)[1] for s in lst]
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_namespace = data['namespace']
        self._p_extends = get_extends(data['extends'])
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_data = self._parser.get_formated_data()
        self._p_requires_typing = False
        self._validate_p_info()
        _imports = data['imports']
        self._p_imports.update(_imports)
        self._p_imports.update(data['extends'])
        self._p_imports_typing.update(self._parser.imports)
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
        return base.APP_CONFIG.template_interface_ext

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

        uno_obj_path = Path(self._path_dir.parent,
                            base.APP_CONFIG.uno_base_dir)
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

    def _write_to_json(self):
        p = self._file_full_path.parent
        jsn_p = p / (str(self._file_full_path.stem) + '.json')
        jsn_str = self._get_json()
        with open(jsn_p, 'w') as f:
            f.write(jsn_str)
        logger.info("Created file: %s", jsn_p)
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
        "verbose": True
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


class Processer:
    """Processes parsing and writing"""
    @RequireArgs('url', ftype=DecFuncEnum.METHOD)
    def __init__(self, p: type[Parser], w: type[Writer], **kwargs):
        """
        Constructor

        Args:
            p (type[Parser]): Parser class
            w (type[Writer]): Writer class

        Other Arguments:
            url (str): url to parse
            sort (bool, optional): No sorting of results. Default ``True``
            cache (bool, optional): caching. Default ``False``
            clear_on_print (bool, optional): No clearing of terminal when otuput to terminal. Default ``False``
            write_template_long (bool, optional): Writes a long format template. Requires write_template is set. Default ``False``
            copy_clipboard (bool, optional): Copy to clipboard. Default ``False``
            print_json (bool, optional):Print json to termainl. Default ``False``
            print_template (bool, optional): Print template to terminal. Default ``False``
            write_template (bool, optional): Write template file into obj_uno subfolder. Default ``False``
            write_json (bool, optional): Write json file into obj_uno subfolder. Default ``False``
            verbose (bool, optional): Verobose output. Default ``False``
        """
        self._parser = p
        self._writer = w
        self._url = str(kwargs['url'])
        self._sort = bool(kwargs.get('sort', True))
        self._cache = bool(kwargs.get('cache', False))
        self._print_clear = bool(kwargs.get('clear_on_print', False))
        self._long_template = bool(kwargs.get('write_template_long', False))
        self._clipboard = bool(kwargs.get('copy_clipboard', False))
        self._print_json = bool(kwargs.get('print_json', False))
        self._print_template = bool(kwargs.get('print_template', False))
        self._write_template = bool(kwargs.get('write_template', False))
        self._write_json = bool(kwargs.get('write_json', bool))
        self._verbose = bool(kwargs.get('verbose', False))
        self._include_desc = bool(kwargs.get('include_desc', True))

    def process(self) -> None:
        parser = self._parser(
            url=self._url,
            sort=self._sort,
            cache=self._cache
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
            include_desc=self._include_desc
        )
        w.write()


def parse(*args, **kwargs):
    """
    Parses data, alternative to running on command line.

    Other Arguments:
        'no_sort' (str, optional): Short form ``'s'``. No sorting of results. Default ``False``
        'no_cache' (str, optional): Short form ``'x'``. No caching. Default ``False``
        'no_print_clear (str, optional): Short form ``'p'``. No clearing of terminal
            when otuput to terminal. Default ``False``
        'no_desc' (str, optional): Short from ``'d'``. No description will be outputed in template. Default ``False``
        'long_template' (str, optional): Short form ``'g'``. Writes a long format template.
            Requires write_template is set. Default ``False``
        'clipboard' (str, optional): Short form ``'c'``. Copy to clipboard. Default ``False``
        'print_json' (str, optional): Short form ``'n'``. Print json to termainl. Default ``False``
        'print_template' (str, optional): Short form ``'m'``. Print template to terminal. Default ``False``
        'write_template' (str, optional): Short form ``'t'``. Write template file into obj_uno subfolder. Default ``False``
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
            log_args['log_file'] = 'interface.log'
        if pargs['verbose']:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    parser: Parser = kwargs.get('class_parser', Parser)
    writer: Writer = kwargs.get('class_writer', Writer)
    proc = Processer(
        p=parser,
        w=writer,
        url=pkwargs['url'],
        sort=pargs['no_sort'],
        cache=pargs['no_cache'],
        print_template=pargs['print_template'],
        print_json=pargs['print_json'],
        copy_clipboard=pargs['clipboard'],
        write_template=pargs['write_template'],
        write_json=pargs['write_json'],
        clear_on_print=(not pargs['no_print_clear']),
        write_template_long=pargs['long_template'],
        include_desc=pargs['no_desc']
    )
    proc.process()

# endregion Parse method

# region Main
def _main():
    os.system('cls' if os.name == 'nt' else 'clear')
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XIntrospectionAccess.html' # has a sequence
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleTextSelection.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XStyleSettings.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XPropertyControl.html'  # no import
    url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XMessageBoxFactory.html'
    args = ('v', 'n')
    kwargs = {
        "u": url,
        "log_file": "debug.log"
    }
    # sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    # main()
    parse(*args, **kwargs)


def get_cmd_args() -> argparse.Namespace:
    # region Parser
    parser = argparse.ArgumentParser(description='interface')
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
        help='Log file to use. Defaults to interface.log',
        type=str,
        required=False)
    # endregion Parser
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
            log_args['log_file'] = 'interface.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)

    proc = Processer(
        p=Parser,
        w=Writer,
        url=args.url,
        sort=args.sort,
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
    proc.process()


if __name__ == '__main__':
    main()
# endregion Main
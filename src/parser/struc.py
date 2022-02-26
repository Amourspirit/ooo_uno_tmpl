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
from typing import Dict, List, Set, Union
from kwhelp.decorator import DecFuncEnum, TypeCheck, TypeCheckKw
from pathlib import Path
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
from . import base, __version__, JSON_ID
from .api.api_namespace import ApiNamespace
from .api.api_data import APIData
from .common.config import APP_CONFIG
from .common import log_load
from .common.util import Util
from .dataclass.summary_info import SummaryInfo
from .rules.name.i_rules_name import IRulesName
from .rules.name.rules_name import RulesName
from .rules.name.rule_name_no_generics import RuleNameNoGenerics
from .web.soup_obj import SoupObj
from ..logger.log_handle import get_logger
from ..utilities import util
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

# region Data Class


@dataclass
class DataItem:
    name: str
    is_py_type: bool
    datatype: str
    orig_type: str
    lines: List[str] = field(default_factory=list)

    def __lt__(self, other: object):
        if not isinstance(other, DataItem):
            return NotImplemented
        return self.name < other.name

# endregion Data Class

# region API


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


class ApiData(APIData):
    # region constructor
    @TypeCheck((str, SoupObj), bool, bool, bool, ftype=DecFuncEnum.METHOD)
    def __init__(self, url_soup: Union[str, SoupObj], allow_cache: bool, long_names: bool = False, remove_parent_inherited: bool = True):
        super().__init__(
            url_soup=url_soup,
            allow_cache=allow_cache,
            long_names=long_names,
            remove_parent_inherited=remove_parent_inherited
        )

        self._ns: ApiNs = None

        self._name_rules_engine = RulesName()
        self._set_name_rules()
    # endregion constructor

    # region Name Rules
    def _set_name_rules(self) -> None:
        self._name_rules_engine.register_rule(RuleNameNoGenerics)

    def _get_name_rules_engine(self) -> Union[IRulesName, None]:
        """
        Gets Name Rules Engine. Overrides parent class

        Returns:
            IRulesName: RulesName() instance
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

    # endregion Properties
# endregion API

# region Parser


class Parser(base.ParserBase):
    # region Constructor
    @TypeCheckKw(
        arg_info={"allow_cache": bool, "long_names": bool},
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._allow_caching: bool = kwargs.get('allow_cache', True)
        self._long_names: bool = kwargs.get('long_names', False)
        self._remove_parent_inherited: bool = kwargs.get(
            'remove_parent_inherited', True)
        self._api_data: ApiData = ApiData(
            url_soup=self.url,
            allow_cache=self._allow_cache,
            long_names=self._long_names,
            remove_parent_inherited=self._remove_parent_inherited
        )
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
            "sort": self._sort,
            "long_names": self.long_names,
            "remove_parent_inherited": self._remove_parent_inherited
        }
        return args

    # endregion Info

    # region Data

    def get_formated_data(self, indent=4) -> str:
        key = 'get_formated_data'
        if key in self._cache:
            return self._cache[key]
        items = self._get_data_items()
        str_lst = Util.get_formated_dict_list_str(
            obj=items, indent=indent)
        self._cache[key] = str_lst
        return self._cache[key]

    def _get_data_items(self) -> List[dict]:
        key = '_get_data_items'
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = []
        t_data = self._get_types_data()
        if 'types' in t_data:
            self._cache[key].extend(t_data['types'])
        p_data = self._get_properties_data()
        if 'properties' in p_data:
            self._cache[key].extend(p_data['properties'])
        return self._cache[key]

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
                self._imports = Util.get_clean_imports(
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

    @property
    def long_names(self) -> bool:
        """Gets long_names value"""
        return self._long_names
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
    def __init__(self, parser: Parser, **kwargs):
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
        self._json_out: bool = kwargs.get('json_out', True)
        self._include_desc: bool = kwargs.get('include_desc', True)
        self._write_template_long: bool = kwargs.get(
            'write_template_long', False)
        self._write_path: Union[str, None] = kwargs.get('write_path', None)
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

    def _get_template_dyn(self) -> Union[str, None]:
        return 'struct_dyn.tmpl'

    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def write(self) -> Union[str, None]:
        """
        Writes files/templates according to parameters

        Returns:
            Union[str, None]: Returns json string if ``json_out`` is ``True``
        """
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
                self._write_to_file_dyn()
            if self._write_json:
                self._write_to_json()
            if self._json_out:
                return self._get_json()
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
        p_dict['extends_map'] = self._get_imports_map()
        p_dict['quote'] = self._get_quote_flat()
        p_dict['typings'] = self._get_typings()
        p_dict['requires_typing'] = self._p_requires_typing
        p_dict.update(self._parser.get_dict_data())
        if 'typing_imports' in p_dict:
            del p_dict['typing_imports']

        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            # "timestamp": str(Util.get_timestamp_utc()),
            "libre_office_ver": APP_CONFIG.libre_office_ver,
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
        str_jsn = Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._json_str = str_jsn
        return self._json_str

    # region get Imports
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
        lst = list(t_set)
        # sort for consistency in json
        lst.sort()
        self._cache[key] = lst
        return self._cache[key]

    # endregion quote/typing

    def _set_template_data(self):
        if self._write_template_long is False:
            return
        self._template = self._template.replace(
            '{libre_office_ver}', APP_CONFIG.libre_office_ver)
        self._template = self._template.replace(
            '{dynamic_struct}', str(self._dynamic_struct))
        self._template = self._template.replace('{sort}', str(self._sort))
        self._template = self._template.replace(
            '{extends_map}', Util.get_formated_dict_list_str(self._get_imports_map()))

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

    def _write_to_file(self):
        with open(self._file_full_path, 'w') as f:
            f.write(self._template)
        logger.info("Created file: %s", self._file_full_path)

    def _write_to_file_dyn(self):
        dyn_name = self._get_template_dyn()
        if dyn_name is None:
            return
        dyn_path = self._template_dir / dyn_name
        with open(dyn_path, 'r') as t_file:
            dyn_contents = t_file.read()

        dyn_out_file = self._file_full_path.stem + APP_CONFIG.template_dyn_ext
        write_path = self._file_full_path.parent / dyn_out_file
        with open(write_path, 'w') as out_file:
            out_file.write(dyn_contents)
        logger.info('create file: %s', write_path)

    def _write_to_json(self):
        p = self._file_full_path.parent
        jsn_p = p / (str(self._file_full_path.stem) + '.json')
        jsn_str = self._get_json()
        with open(jsn_p, 'w') as f:
            f.write(jsn_str)
        logger.info("Created file: %s", jsn_p)

    def _set_info(self):
        def get_extends(lst: List[str]) -> List[str]:
            return [Util.get_last_part(s) for s in lst]
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
        self._p_imports = Util.get_clean_imports(
            ns=self._p_namespace,
            imports=self._p_imports
        )
        self._p_imports_typing = Util.get_clean_imports(
            ns=self._p_namespace,
            imports=self._p_imports_typing
        )
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
        if self._write_path:
            write_path = self._write_path
        else:
            write_path = APP_CONFIG.uno_base_dir
        uno_obj_path = Path(util.get_root(), write_path)
        name_parts = self._p_fullname.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        index = len(path_parts) - 1
        if not path_parts[index]:
            try:
                raise Exception(
                    "StructWriter._get_uno_obj_path() parsing path yielded an empty string")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e

        path_parts[index] = Util.get_clean_filename(
            path_parts[index]) + APP_CONFIG.template_struct_ext
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._cache[key] = obj_path
        return self._cache[key]

# endregion Writer

# region Parse method


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
        "log_file": args.log_file,
        "verbose": args.verbose,
        "dynamic_struct": args.dynamic_struct
    }
    if args.write_path:
        d['write_path'] = args.write_path
    return d


def parse(**kwargs) -> Union[str, None]:
    """
    Parses data, alternative to running on command line.

    Keyword Arguments:
        url (str): url to parse
        sort (str, optional): Sorting of results. Default ``False``
        cache (str, optional): Caching. Default ``False``
        clear_on_print (str, optional): Clearing of terminal when otuput to terminal. Default ``False``
        dynamic_struct (str, optional): Template will generate dynameic struct content. Default ``True``
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
        verbose (str, optional): Verobose output.
        log_file (str, optional): Log File

    Returns:
        Union[str, None]: Returns json string if ``json_out`` is ``True``
    """
    global logger
    _url = str(kwargs['url'])
    _sort = bool(kwargs.get('sort', False))
    _cache = bool(kwargs.get('cache', True))
    _print_clear = bool(kwargs.get('clear_on_print', False))
    _clipboard = bool(kwargs.get('copy_clipboard', False))
    _print_template = bool(kwargs.get('print_template', False))
    _write_template = bool(kwargs.get('write_template', False))
    _long_template = bool(kwargs.get('write_template_long', False))
    _print_json = bool(kwargs.get('print_json', False))
    _write_json = bool(kwargs.get('write_json', bool))
    _long_names = bool(kwargs.get(
        'long_names', APP_CONFIG.use_long_import_names))
    _json_out = bool(kwargs.get('json_out', False))
    _log_file = kwargs.get('log_file', None)
    _verbose = bool(kwargs.get('verbose', False))
    _include_desc = bool(kwargs.get('include_desc', True))
    _dynamic_struct = bool(kwargs.get('dynamic_struct', True))
    _write_path = kwargs.get('write_path', None)

    if logger is None:
        log_args = {}
        if _log_file:
            log_args['log_file'] = _log_file
        else:
            log_args['log_file'] = 'struct.log'
        if _verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    p = Parser(
        url=_url,
        sort=_sort,
        cache=_cache,
        long_names=_long_names,
        remove_parent_inherited=APP_CONFIG.remove_parent_inherited
    )
    w = StructWriter(
        parser=p,
        copy_clipboard=_clipboard,
        print_template=_print_template,
        print_json=_print_json,
        write_template=_write_template,
        write_json=_write_json,
        write_template_long=_long_template,
        clear_on_print=_print_clear,
        dynamic_struct=_dynamic_struct,
        include_desc=_include_desc,
        json_out=_json_out,
        write_path=_write_path
    )
    return w.write()
# endregion Parse method

# region Main


def _main():
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Ambiguous_3_01T_01_4.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1GetPropertyTolerantResult.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1TextMarkupDescriptor.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Pair_3_01T_00_01U_01_4.html' # generics
    # url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1accessibility_1_1AccessibleRelation.html'
    url = 'https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1SubIncrement.html'
    kwargs = {
        "url": url,
        "log_file": "debug.log",
        "verbose": True,
        "print_json": True,
        "print_template": False,
        "write_template_long": False
    }
    parse(**kwargs)
    # sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    # main()

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
        '-s', '--sort',
        help='sorting of results',
        action='store_true',
        dest='sort',
        default=False)
    parser.add_argument(
        '-y', '--no-dynamic-struct',
        help='Template will generate dynamic struct content',
        action='store_false',
        dest='dynamic_struct',
        default=True)
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


def set_cmd_args_local(parser) -> None:
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
 # endregion Parser


def main():
    global logger

    # http://pymotw.com/2/argparse/
    parser = argparse.ArgumentParser(description='const')
    set_cmd_args(parser)
    set_cmd_args_local(parser)
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

    if not args.print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')

    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)
    args_dict = get_kwargs_from_args(args)
    if args.print_template is False and args.print_json is False:
        print('')
    parse(**args_dict)

# endregion Main

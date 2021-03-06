# coding: utf-8
"""
Process a link to a page that contains an typeDef
Each Type Defination is exported as a seperate file

For instance:
https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1util.html
will ouptut three classes
changes_set.py => ChangesSet
color.py => Color
language.py => Language

"""
# region Imports
import os
import sys
import argparse
import logging
from typing import Dict, List, Set, Union
from kwhelp.decorator import DecFuncEnum, TypeCheckKw
from pathlib import Path
from dataclasses import dataclass, field
from . import base, __version__, JSON_ID
from .api.api_namespace import ApiNamespace
from .api.api_data import APIData
from .api.api_desc_detail import ApiDescDetail
from .api.api_summary_block import ApiSummaryBlock
from .api.api_summary_rows import ApiSummaryRows
from .common.config import APP_CONFIG
from .common import log_load
from .common.util import Util
from .dataclass.name_info import NameInfo
from .web.block_obj import BlockObj
from .web.soup_obj import SoupObj
from ..logger.log_handle import get_logger
from .mod_type import PythonType
from ..utilities import util as mutil

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

# region Data Classes


@dataclass
class SummaryInfo:
    id: str
    name: str
    type: str
    requires_typing: bool
    from_imports: Set[str] = field(default_factory=set)
    imports: Set[str] = field(default_factory=set)
    p_type: PythonType = None

    def __lt__(self, other: 'SummaryInfo'):
        return self.name < other.name


@dataclass
class TypeDef(SummaryInfo):
    desc: List[str] = field(default_factory=list)


class ApiTypeDefBlock(ApiSummaryBlock):
    """TypeDef Summary Block. Inherits ApiSummaryBlock"""

    def _get_match_name(self) -> str:
        return 'typedef-members'


class ApiSummaries(BlockObj):
    """Gets summary information for a public member block"""

    def __init__(self, block: ApiSummaryRows, name_info: NameInfo, ns: str) -> None:
        self._block: ApiSummaryRows = block
        self._name_info = name_info
        super().__init__(self._block.soup)
        self._data = None
        self._ns = ns

    def get_obj(self) -> List[SummaryInfo]:
        if not self._data is None:
            return self._data
        self._data = []
        rows = self._block.get_obj()
        for row in rows:
            _from_imports: Set[str] = set()
            _imports: Set[str] = set()
            _req_typing = False
            cls_name = row.get('class')[0]
            id_str = cls_name.rsplit(sep=':', maxsplit=1)[1]
            itm_lft = row.find('td', class_='memItemLeft')
            _type = None
            name = ''
            if itm_lft:
                _type: str = itm_lft.text.strip().replace('::', '.')
                if _type.lower().startswith('typedef'):
                    _type = _type.split(maxsplit=1)[1]
            itm_rgt = row.find('td', class_='memItemRight')
            if itm_rgt:
                itm_name = itm_rgt.select_one('a')
                if itm_name:
                    name = itm_name.text.strip()
                    name = Util.get_clean_method_name(name)
            if not name:
                msg = f"{self.__class__.__name__}.get_obj(). Missing name. Url: {self.url_obj.url_only}"
                logger.error(msg)
                raise Exception(msg)
            if _type:
                p_type = Util.get_python_type(
                    in_type=_type, name_info=self._name_info, ns=self._ns
                )
                s_type = p_type.type
                if p_type.requires_typing:
                    _req_typing = True
                _from_imports.update(p_type.get_all_from_imports())
                _imports.update(p_type.get_all_imports())
            else:
                p_type = PythonType(
                    name=name,
                    type=s_type,
                    realtype=s_type,
                    requires_typing=_req_typing,
                    ns=self._ns
                )
                msg = f"{self.__class__.__name__}.get_obj(). Missing return type for {name}. Url: {self.url_obj.url_only}"
                logger.error(msg)
                raise Exception(msg)

            si = SummaryInfo(
                id=id_str,
                name=name,
                type=s_type,
                requires_typing=_req_typing,
                from_imports=_from_imports,
                imports=_imports,
                p_type=p_type
            )

            self._data.append(si)
        return self._data


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
            self._namespace = self.get_obj()
        return self._namespace

    @property
    def namespace_str(self) -> str:
        if self._namespace_str is None:
            self._namespace_str = '.'.join(self.namespace)
        return self._namespace_str


class ApiData(APIData):
    # region Constructor
    def __init__(self, url_soup: Union[str, SoupObj], allow_cache: bool):
        super().__init__(url_soup=url_soup, allow_cache=allow_cache)
        self._si_key = 'summeries'
        self._detail_block_key = 'detail_block'
        self._type_def_block: ApiTypeDefBlock = None  # ApiSummaryBlock
        self._type_def_summary_rows: ApiSummaryRows = None
        self._type_def_summaries: ApiSummaries = None
        self._ns: ApiNs = None
        self._cache = {}
    # endregion Constructor

    # region Methods
    def get_desc_detail(self, a_id: str) -> ApiDescDetail:
        """Gets Description obj for method or property"""

        key = f"get_desc_detail_{a_id}"
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = super().get_desc_detail(a_id=a_id)
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

    @property
    def type_def_block(self) -> ApiTypeDefBlock:
        """Gets type defination smmary block. Inherits ApiSummaryBlock"""
        if self._type_def_block is None:
            self._type_def_block = ApiTypeDefBlock(
                self.public_members)
        return self._type_def_block

    @property
    def type_def_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for Properties"""
        if self._type_def_summary_rows is None:
            self._type_def_summary_rows = ApiSummaryRows(
                self.type_def_block)
        return self._type_def_summary_rows

    @property
    def type_def_summaries(self) -> ApiSummaries:
        """Get Summary info list for functions"""
        if self._type_def_summaries is None:
            self._type_def_summaries = ApiSummaries(
                block=self.type_def_summary_rows,
                name_info=self.name.get_obj(),
                ns=self.ns.namespace_str
            )
        return self._type_def_summaries

    # endregion Properties

# endregion Data Classes

# region Parse


class ParserTypeDef(base.ParserBase):

    # region Constructor
    @TypeCheckKw(
        arg_info={"allow_cache": bool},
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._allow_caching = kwargs.get('allow_cache', True)
        self._api_data = ApiData(
            url_soup=self.url, allow_cache=self._allow_cache)
        self._cache = {}
    # endregion Constructor

    def get_dict_data(self) -> dict:
        """
        Gets Dictionary of information

        Returns:
            Dict[str, object]: {
                "namespace": "str, Namespace",
                "url": "str, api url",
                "items": "(List[TypeDef]): Type definations"
            }
        """
        key = 'get_dict_data'
        if key in self._cache:
            return self._cache[key]
        info = self.get_info()
        items = self._get_data_items()
        info['items'] = items
        self._cache[key] = info
        return self._cache[key]

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
                "namespace": "str, Namespace",
                "url": "str, api url"
            }
        """
        key = 'get_info'
        if key in self._cache:
            return self._cache[key]

        # im = self._sdk_data.imports
        result = {
            'namespace': self._api_data.ns.namespace_str,
            "url": self._api_data.url_obj.url
        }
        logger.debug('ParserTypeDef.get_info() namespace: %s',
                     result['namespace'])
        self._cache[key] = result
        return self._cache[key]

    def _get_data_items(self) -> List[TypeDef]:
        attribs: List[TypeDef] = []
        si_lst = self._api_data.type_def_summaries.get_obj()
        if self.sort:
            si_lst.sort()
        for si in si_lst:
            desc: List[str] = self._api_data.get_desc_detail(si.id).get_obj()
            t_def = TypeDef(
                id=si.id,
                name=si.name,
                type=si.type,
                requires_typing=si.requires_typing,
                from_imports=si.from_imports,
                imports=si.imports
            )
            t_def.desc.extend(desc)
            attribs.append(t_def)
        return attribs

    def get_formated_data(self) -> str:
        key = 'get_formated_data'
        if key in self._cache:
            return self._cache[key]
        attribs = self._get_data_items()
        str_lst = Util.get_formated_dict_list_str(obj=attribs, indent=4)
        self._cache[key] = str_lst
        return self._cache[key]

    @property
    def api_data(self) -> ApiData:
        return self._api_data
# endregion Parse

# region Writer


class WriterTypeDef(base.WriteBase):
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
    def __init__(self, parser: ParserTypeDef, **kwargs):
        super().__init__(**kwargs)
        self._parser: ParserTypeDef = parser
        self._copy_clipboard: bool = kwargs.get('copy_clipboard', False)
        self._print_template: bool = kwargs.get('print_template', False)
        self._write_file: bool = kwargs.get('write_template', False)
        self._print_json: bool = kwargs.get('print_json', True)
        self._write_json: bool = kwargs.get('write_json', False)
        self._allow_db = kwargs.get('allow_db', True)
        self._clear_on_print: bool = kwargs.get('clear_on_print', True)
        self._write_template_long: bool = kwargs.get(
            'write_template_long', False)
        self._write_path: Union[str, None] = kwargs.get('write_path', None)
        self._include_desc: bool = kwargs.get('include_desc', True)
        self._indent_amt = 4
        self._p_namespace: str = None
        self._p_url: str = None
        self._path_dir = Path(__file__).parent
        self._cache: Dict[str, object] = {}

        t_file = 'typedef'
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

    def write(self):
        self._set_info()
        logger.info("Processing %s", self._p_namespace)
        try:
            if self._clear_on_print and (self._print_template or self._print_json):
                logger.debug('Printing to terminal')
                os.system('cls' if os.name == 'nt' else 'clear')
            if self._print_template:
                self._print_to_terminal()
            if self._print_json:
                self._print_json_to_terminal()
            if self._write_file:
                self._write_to_file()
                self._write_to_file_dyn()
                self._write_to_file_pyi()
            if self._write_json:
                self._write_to_json()
        except Exception as e:
            logger.exception(e)
            raise e

    def _get_json(self, t_def: TypeDef) -> str:
        d_data = self._parser.get_dict_data()
        p_dict = {
            "name": t_def.name,
            "namespace": d_data['namespace'],
            "url": d_data['url'],
            "allow_db": self._allow_db,
            "type": t_def.type,
            "requires_typing": t_def.requires_typing
        }

        p_dict['from_imports'] = self._get_from_imports(t_def)
        p_dict['imports'] = self._get_imports(t_def)
        p_dict['quote'] = self._get_quote_flat(t_def.id)
        p_dict['typings'] = self._get_typings(t_def.id)
        p_dict['desc'] = t_def.desc

        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            # "timestamp": str(Util.get_timestamp_utc()),
            "libre_office_ver": APP_CONFIG.libre_office_ver,
            "name": t_def.name,
            "type": "typedef",
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

    def _get_template_dyn(self) -> Union[str, None]:
        return 'typedef_dyn.tmpl'

    def _get_template_pyi(self) -> Union[str, None]:
        return 'typedef_pyi.tmpl'

    # region get Imports
    def _get_from_imports(self, t_def: TypeDef) -> List[List[str]]:
        key = '_get_from_imports_' + t_def.id
        if key in self._cache:
            return self._cache[key]
        lst = []
        lst_im = list(t_def.from_imports)
        # sort for consistency in json
        lst_im.sort()
        for ns in lst_im:
            f, n = Util.get_rel_import(
                i_str=ns, ns=self._p_namespace
            )
            lst.append([f, n])
        self._cache[key] = lst
        return self._cache[key]

    def _get_imports(self, t_def: TypeDef) -> List[List[str]]:
        key = '_get_imports_' + t_def.id
        if key in self._cache:
            return self._cache[key]
        lst_im = list(t_def.imports)
        # sort for consistency in json
        lst_im.sort()
        self._cache[key] = lst_im
        return self._cache[key]
    # endregion get Imports

    def _get_quote_flat(self, si_id: str) -> List[str]:
        # si_id will limit this to one item max
        si_lst = self._parser.api_data.type_def_summaries.get_obj()
        # sort for consistency in json
        si_lst.sort()
        t_lst = []
        for si in si_lst:
            if si.id == si_id:
                t = si.p_type
                if t.requires_typing or t.is_py_type is False:
                    t_lst.append(t.type)
                break
        return t_lst

    def _get_typings(self, si_id: str) -> List[str]:
        si_lst = self._parser.api_data.type_def_summaries.get_obj()
        # sort for consistency in json
        si_lst.sort()
        t_lst = []
        for si in si_lst:
            if si.id == si_id:
                t = si.p_type
                if t.requires_typing:
                    t_lst.append(t.type)
                break
        return t_lst

    def _get_template_data(self, t_def: TypeDef) -> str:
        if self._write_template_long is False:
            return self._template
        t = self._template
        t = t.replace('{allow_db}', str(self._allow_db))
        t = t.replace('{libre_office_ver}', APP_CONFIG.libre_office_ver)
        t = t.replace('{name}', t_def.name)
        t = t.replace('{ns}', str(self._p_namespace))
        t = t.replace('{link}', self._p_url)
        t = t.replace('{type}', t_def.type)
        t = t.replace(
            '{quote}',
            str(set(self._get_quote_flat(t_def.id))))
        t = t.replace(
            '{typings}',
            str(set(self._get_typings(t_def.id))))
        t = t.replace(
            '{requires_typing}', str(t_def.requires_typing))
        t = t.replace(
            '{include_desc}', str(self._include_desc))
        t = t.replace(
            '{from_imports}',
            Util.get_formated_dict_list_str(self._get_from_imports(t_def))
        )
        t = t.replace(
            '{imports}',
            Util.get_formated_dict_list_str(self._get_imports(t_def))
        )
        if len(t_def.desc) > 0:
            desc = Util.get_formated_dict_list_str(t_def.desc, indent=4)
        else:
            desc = "[]"
        t = t.replace('{desc}', desc)
        return t

    def _set_info(self):
        # all imports for typeDef require typing
        data = self._parser.get_info()
        self._p_namespace = data['namespace']
        self._p_url = data['url']
        self._validate_p_info()
        # if self._write_file or self._write_json:
        #     self._file_full_path = self._get_uno_obj_path()

    def _validate_p_info(self):
        try:
            if not self._p_url:
                raise Exception(
                    "WriterTypeDef: validation fail: url is an empty string.")
            if not self._p_namespace:
                raise Exception(
                    "WriterTypeDef: validation fail: namespace is an empty string.")
        except Exception as e:
            logger.error(e)
            raise e

    def _get_uno_obj_path(self, t_def: TypeDef) -> Path:
        key = '_get_uno_obj_path_' + t_def.id
        if key in self._cache:
            return self._cache[key]
        # _p_name = Util.camel_to_snake(t_def.name)
        _p_name = t_def.name
        if self._write_path:
            write_path = self._write_path
        else:
            write_path = APP_CONFIG.uno_base_dir
        uno_obj_path = Path(mutil.get_root(), write_path)
        name_parts: List[str] = self._p_namespace.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append(_p_name + APP_CONFIG.template_typedef_ext)
        obj_path = uno_obj_path.joinpath(*path_parts)
        # because all typedef are written to the same dir
        # only need ot call mkdirp once.
        mk = self._cache.get('_get_uno_obj_path_mk', False)
        if not mk:
            self._mkdirp(obj_path.parent)
            mk = True
            self._cache['_get_uno_obj_path_mk'] = mk
        self._cache[key] = obj_path
        return self._cache[key]

    def _get_t_def_lst(self) -> List[TypeDef]:
        """Gets a list of TypeDef from praser or cache"""
        key = '_get_t_def_lst'
        if key in self._cache:
            return self._cache[key]
        info = self._parser.get_dict_data()
        self._cache[key] = info['items']
        return self._cache[key]

    def _print_to_terminal(self):
        t_defs = self._get_t_def_lst()
        for t_def in t_defs:
            print('')
            t_str = self._get_template_data(t_def)
            print(t_str)

    def _write_to_file(self):
        t_defs = self._get_t_def_lst()
        for t_def in t_defs:
            file_path = self._get_uno_obj_path(t_def)
            t_str = self._get_template_data(t_def)
            with open(file_path, 'w') as f:
                f.write(t_str)
            logger.info("Created file: %s", file_path)

    def _write_to_file_dyn(self):
        name = self._get_template_dyn()
        if name is None:
            return
        p = self._template_dir / name
        with open(p, 'r') as t_file:
            contents = t_file.read()

        t_defs = self._get_t_def_lst()
        for t_def in t_defs:
            tmpl_file_path = self._get_uno_obj_path(t_def)
            file_path = tmpl_file_path.parent
            file_path = file_path.joinpath(
                tmpl_file_path.stem + APP_CONFIG.template_dyn_ext)
            with open(file_path, 'w') as f:
                f.write(contents)
            logger.info("Created file: %s", file_path)

    def _write_to_file_pyi(self):
        name = self._get_template_pyi()
        if name is None:
            return
        p = self._template_dir / name
        with open(p, 'r') as t_file:
            contents = t_file.read()

        t_defs = self._get_t_def_lst()
        for t_def in t_defs:
            tmpl_file_path = self._get_uno_obj_path(t_def)
            file_path = tmpl_file_path.parent
            file_path = file_path.joinpath(
                tmpl_file_path.stem + APP_CONFIG.template_pyi_ext)
            with open(file_path, 'w') as f:
                f.write(contents)
            logger.info("Created file: %s", file_path)

    def _print_json_to_terminal(self):
        t_defs = self._get_t_def_lst()
        for t_def in t_defs:
            print('')
            jsn_str = self._get_json(t_def)
            print(jsn_str)

    def _write_to_json(self):
        t_defs = self._get_t_def_lst()
        for t_def in t_defs:
            file_path = self._get_uno_obj_path(t_def)
            p = file_path.parent
            jsn_p = p / (str(file_path.stem) + '.json')
            jsn_str = self._get_json(t_def)
            with open(jsn_p, 'w') as f:
                f.write(jsn_str)
            logger.info("Created file: %s", jsn_p)
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
        "print_template": args.print_template,
        "write_template": args.write_template,
        "write_template_long": args.long_format,
        "print_json": args.print_json,
        "write_json": args.write_json,
        "include_desc": args.desc,
        "log_file": args.log_file,
        "verbose": args.verbose
    }
    if args.write_path:
        d['write_path'] = args.write_path
    return d


def parse(**kwargs):
    """
    Parses data, alternative to running on command line.

    Keyword Arguments:
        url (str): url to parse
        sort (str, optional): Sorting of results. Default ``True``
        cache (str, optional): Caching. Default ``False``
        clear_on_print (str, optional): Clearing of terminal when otuput to terminal. Default ``False``
        include_desc (str, optional): Description will be outputed in template. Default ``True``
        long_names (str, optional): Long names. Default set in config ``use_long_import_names`` property.
            Toggles values set in config.
        write_template_long (str, optional): Writes a long format template.
            Requires write_template is set. Default ``False``
        print_json (str, optional): Print json to termainl. Default ``False``
        print_template (str, optional): Print template to terminal. Default ``False``
        write_template (str, optional): Write template file into obj_uno subfolder. Default ``False``
        write_json (str, optional): Write json file into obj_uno subfolder. Default ``False``
        write_path (str, optional): The root path to write data files (json, tmpl) into. Defaut set in config ``uno_base_dir``
        verbose (str, optional): Verobose output.
        log_file (str, optional): Log File
    """
    global logger
    _url = str(kwargs['url'])
    _sort = bool(kwargs.get('sort', True))
    _cache = bool(kwargs.get('cache', True))
    _print_clear = bool(kwargs.get('clear_on_print', False))
    _print_template = bool(kwargs.get('print_template', False))
    _write_template = bool(kwargs.get('write_template', False))
    _long_template = bool(kwargs.get('write_template_long', False))
    _print_json = bool(kwargs.get('print_json', False))
    _write_json = bool(kwargs.get('write_json', bool))
    _include_desc = bool(kwargs.get('include_desc', True))
    _log_file = kwargs.get('log_file', None)
    _verbose = bool(kwargs.get('verbose', False))
    _write_path = kwargs.get('write_path', None)

    if logger is None:
        log_args = {}
        if _log_file:
            log_args['log_file'] = _log_file
        else:
            log_args['log_file'] = 'typedef.log'
        if _verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    p = ParserTypeDef(
        url=_url,
        sort=_sort,
        cache=_cache
    )
    w = WriterTypeDef(
        parser=p,
        print_template=_print_template,
        print_json=_print_json,
        write_template=_write_template,
        write_json=_write_json,
        clear_on_print=_print_clear,
        write_template_long=_long_template,
        include_desc=_include_desc,
        write_path=_write_path
    )
    w.write()

# endregion Parse method

# region Main


def _main():
    global logger

    if logger is None:
        log_args = {
            "log_file": "typedef.log",
            "level": logging.DEBUG
        }
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1util.html'
    kwargs = {
        "url": url,
        "log_file": "debug.log",
        "verbose": True,
        "print_json": True
    }
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
        dest='print_clear',
        default=True)
    parser.add_argument(
        '-g', '--long-template',
        help='Writes a long format template. Requires --write-template is set. No Autoload',
        action='store_true',
        dest='long_format',
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


def set_cmd_args_local(parser) -> None:
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
# endregion Parser

# region main


def main():
    global logger

    # region Parser
    parser = argparse.ArgumentParser(description='typedef')
    set_cmd_args(parser)
    set_cmd_args_local(parser)
    args = parser.parse_args()

    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'typedef.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    # endregion Parser
    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)

    args_dict = get_kwargs_from_args(args)
    if args.print_template is False and args.print_json is False:
        print('')
    parse(**args_dict)
# endregion Main

# endregion Main

# coding: utf-8
import os
import sys
import re
import importlib
import logging
import time
import calendar
from datetime import datetime
from rel import mod_rel as RelInfo
import sqlite3 as sql
from pathlib import Path
from datetime import datetime, timezone
from types import ModuleType
from typing import Iterable, Tuple, List, Union, Optional
from Cheetah.Template import Template
from dataclasses import dataclass
from src.logger.log_handle import get_logger
from enum import Enum
from src.data_manage.db_class.base_sql import BaseSql as DbBaseSql
from src.data_manage.db_class.qry_component import QryComponent
from src.data_manage.data_class.component import Component
from src.data_manage.data_class.component_kind import ComponentKind


# set up path for importing modules from main app
_project_root = os.environ.get("project_root", None)
if _project_root:
    if _project_root not in sys.path:
        sys.path.insert(0, _project_root)

py_name_pattern = re.compile("[\W_]+")

_REG_TO_SNAKE = re.compile(r"(?<!^)(?=[A-Z])|(?<=[A-zA-Z])(?=[0-9])")  # re.compile(r"(?<!^)(?=[A-Z])")
_REG_LETTER_AFTER_NUMBER = re.compile(r"(?<=\d)(?=[a-zA-Z])")

RESERVER_WORDS = {
    "and",
    "as",
    "assert",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "False",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "None",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "True",
    "try",
    "while",
    "with",
    "yield",
}

# region Resource DB Related


@dataclass
class ExtendsInfo:
    parent: str
    namespace: str
    sort: int
    map_name: Union[str, None]

    def __lt__(self, other: object):
        if not isinstance(other, ExtendsInfo):
            return NotImplemented
        return self.sort < other.sort


class DbConnect:
    def __init__(self) -> None:
        root_dir: Union[str, None] = os.environ.get("project_root", None)
        resource_dir: Union[str, None] = os.environ.get("config_resource_dir", None)
        db_name: Union[str, None] = os.environ.get("config_db_mod_info", None)

        if root_dir is None:
            raise ValueError("DbConnect: Resource project_root environment value is not set")
        if resource_dir is None:
            raise ValueError("DbConnect: Resource config_resource_dir environment value is not set")
        if db_name is None:
            raise ValueError("DbConnect: Resource config_db_mod_info environment value is not set")
        self._db_name = db_name
        self._root_dir = Path(root_dir)
        self._resource_dir = resource_dir
        self._conn = str(self._root_dir / self._resource_dir / self._db_name)

    @property
    def connection_str(self) -> str:
        """Gets connection_str value"""
        return self._conn

    @property
    def root_dir(self) -> Path:
        """Gets root_dir value"""
        return self._root_dir


class SqlCtx:
    # Using a context manager: https://tinyurl.com/y8dplak5
    def __init__(self, connect_str: str) -> None:
        self._cstr = connect_str

    def __enter__(self):
        # DateTime for sqlite:
        #   See: https://stackoverflow.com/a/37222799/1171746
        #   See: https://stackoverflow.com/a/1830499/1171746
        self.connection: sql.Connection = sql.connect(self._cstr, detect_types=sql.PARSE_DECLTYPES)
        self.connection.row_factory = sql.Row
        self.cursor: sql.Cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def get_connection(self) -> sql.Connection:
        return self._conn


class BaseSql(DbBaseSql):
    def __init__(self) -> None:
        self._db_connect = DbConnect()
        super().__init__(connect_str=self.conn_str)

    @property
    def conn_str(self) -> str:
        """Gets connect_str value"""
        return self._db_connect.connection_str


class SqlExtends(BaseSql):
    def __init__(self) -> None:
        super().__init__()

    def get_extends(self, namespace: str) -> List[ExtendsInfo]:
        results: List[ExtendsInfo] = []
        query = """SELECT extend.namespace as ns, extend.map_name as map_name FROM extend
        LEFT JOIN component on component.id_component = extend.fk_component_id
        WHERE component.id_component = :namespace"""

        qry_sort = """SELECT module_detail.sort as sort FROM module_detail
        WHERE module_detail.id_namespace = :namespace LIMIT 1"""
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(query, {"namespace": namespace})
            for row in db.cursor:
                results.append(ExtendsInfo(namespace=row["ns"], sort=-1, map_name=row["map_name"], parent=namespace))
            for ei in results:
                db.cursor.execute(qry_sort, {"namespace": ei.namespace})
                for row in db.cursor:
                    ei.sort = int(row["sort"])
        return results


class SqlComponent(BaseSql):
    def __init__(self) -> None:
        super().__init__()
        self.qry_component = QryComponent(connect_str=self.conn_str)

    def get_component(self, full_ns: str, tipe: str | ComponentKind = "") -> Union[Component, None]:
        """
        Gets component instance for a given namespace.

        If the namespace does not start with ``com.sun.star.`` then ``None`` is returned without checking the database.

        Args:
            full_ns (str): full namespace used for match.
            tipe (str, ComponentTypeKind, optional): Type to check for match.

        Returns:
            Union[Component, None]: Component instance if ``full_ns`` is a match; Otherwise, ``None``
        """
        return self.qry_component.get_component(full_ns, tipe=tipe)

    def get_component_by_map_name(self, map_name: str) -> Union[Component, None]:
        """
        Gets component instance for a given map_name

        Args:
            map_name (str): map_name used for match.

        Returns:
            Union[Component, None]: Component instance if ``map_name`` is a match; Otherwise, ``None``
        """
        return self.qry_component.get_component_by_map_name(map_name)

    def is_type(self, namespace: str, tipe: str | ComponentKind = "typedef") -> bool:
        """
        Gets if the namespace is a type of the given type.

        If the namespace does not start with ``com.sun.star.`` then ``False`` is returned without checking the database.

        Args:
            namespace (str): Namespace to check such as ``com.sun.star.xsd.Year``.
            tipe (str, ComponentTypeKind, optional): Type to check for match. Defaults to "typedef".

        Returns:
            bool: If the namespace is a type of the given type.
        """
        return self.qry_component.is_type(namespace, tipe)

    def is_type_from_map_name(self, map_name: str, tipe: str | ComponentKind = "typedef") -> bool:
        """
        Gets if the map_name is a type of the given type.

        Args:
            map_name (str): Map name to check such as ``Year_578a07e8``.
            tipe (str, ComponentTypeKind, optional): Type to check for match. Defaults to "typedef".

        Returns:
            bool: If the map_name is a type of the given type.
        """
        return self.qry_component.is_type_from_map_name(map_name, tipe)


# endregion Resource DB Related


@dataclass
class TmplConfig:
    project_root: str
    resource_dir: str
    uno_obj_dir: str
    dyn_dir: str
    helper_ns: str
    helper_mod: str
    enum_mod: str
    env: str


class BaseTpml(Template):
    def __init__(self, *args, **kwargs):
        self.using_future_annotations = False
        self._post_lines: set[str] = set()
        super().__init__(*args, **kwargs)
        self._is_class_init = True
        self._is_class_data = False
        self._logger = None
        self.__cache = {}
        if not hasattr(self, "extends_map"):
            setattr(self, "extends_map", {})

        self._logger: logging.Logger = get_logger(
            logger_name="Template — " + self.__class__.__name__, add_handler_console=False
        )
        self._config = self._get_config()
        self._app_root = self._config.project_root

    def _get_config(self) -> TmplConfig:
        project_root = os.environ["project_root"]
        resource_dir = os.environ["config_resource_dir"]
        uno_obj_dir = os.environ["config_uno_obj_dir"]
        dyn_dir = os.environ["config_dyn_dir"]
        helper_ns = os.environ["config_helper_ns"]
        helper_mod = os.environ["config_helper_mod"]
        enum_mod = os.environ["config_enum_mod"]
        env = os.environ["config_oenv_ns"]

        return TmplConfig(
            project_root=project_root,
            resource_dir=resource_dir,
            uno_obj_dir=uno_obj_dir,
            dyn_dir=dyn_dir,
            helper_ns=helper_ns,
            helper_mod=helper_mod,
            enum_mod=enum_mod,
            env=env,
        )

    def init_data(self):
        self._is_class_init = True

    def load_data(self):
        self._is_class_data = True

    # region Logger
    def _log_to_logger(self, level: int, msg: object, *args, **kwargs):
        if not self._logger:
            return
        self._logger.log(level, msg, *args, **kwargs)

    def _ldebug(self, msg: object, *args, **kwargs):
        self._log_to_logger(logging.debug, msg, *args, **kwargs)

    def _linfo(self, msg: object, *args, **kwargs):
        self._log_to_logger(logging.INFO, msg, *args, **kwargs)

    def _lwarn(self, msg: object, *args, **kwargs):
        self._log_to_logger(logging.WARN, msg, *args, **kwargs)

    def _lerr(self, msg: object, *args, **kwargs):
        self._log_to_logger(logging.ERROR, msg, *args, **kwargs)

    # endregion Logger

    def camel_to_snake(self, input: str) -> str:
        """
        Converts Camel case to snake clase

        Args:
            name (str): Camel name

        Returns:
            str: snake case
        """
        return RelInfo.camel_to_snake(input)

    def get_clean_name(self, input: str) -> str:
        """
        Removes all char from a string except for ``a-zA-Z0-9_``

        Args:
            input (str): string to clean

        Returns:
            str: input with any other chars removed
        """
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        return py_name_pattern.sub("", input)

    def line_gen(self, input) -> str:
        """
        Generates lines from str or list like

        Args:
            input (str, list, tuple, set): input str or iterable str

        Yields:
            [str]: line by line
        """
        if isinstance(input, str):
            yield input
            return
        for s in input:
            yield s

    def dict_keys_to_str(self, input: dict, sep: str = ", ") -> str:
        """
        Converts a dictionary's keys into a string separated by ``sep``

        Args:
            input (dict): input dictionary
            sep (str, optional): separator. Defaults to ``', '``

        Returns:
            str: keys a string.
        """
        keys = list(input.keys())
        if len(keys) == 0:
            return ""
        return sep.join(keys)

    def lst_to_str(self, input, sep: str = ", ") -> str:
        """
        Writes list items into a str separated by ``sep``.
        If input is ``str`` then it is returned verbatim

        Args:
            input (str, Iterable[str]): input to parse
            sep (str, optional): Separate usd when joining list. Defaults to ', '.

        Returns:
            str: value
        """
        if isinstance(input, str):
            return input
        if len(input) == 0:
            return ""
        return sep.join(input)

    def is_out_arg(self, input: str) -> bool:
        """Gets if input is ``out`"""
        if not input:
            return False
        return input == "out"

    def get_last_part(self, input: str, sep=".") -> str:
        """
        Splits a string and returns the last part

        Args:
            input (str): string to get last part of.
            sep (str, optional): string used to split. Defaults to ``.``

        Returns:
            str: last part of input
        """
        if not input:
            return ""
        _parts = input.rsplit(sep=sep, maxsplit=1)
        return _parts.pop()

    def convert_lst_last(self, lst: List[str], sep=".") -> List[str]:
        """
        Converts a list of Long names such as ["com.sun.star.uno.XInterface"]
        into list of last part such as ["XInterface"]

        Args:
            lst (List[str]): Input list
            sep (str, optional): string used to split. Defaults to ``.``

        Returns:
            List[str]: result list
        """
        result = []
        for itm in lst:
            result.append(self.get_last_part(input=itm, sep=sep))
        return result

    # region sorting
    def _sort_dict(self, d: dict, reverse: bool = False) -> dict:
        """
        Sorts a dictionary by its keys

        Args:
            d (dict): input dictionary
            reverse (bool, optional): If ``True`` result are reversed. Defaults to ``False``.

        Returns:
            dict: new sorted dict.
        """
        if not d:
            return {}
        keys = list(d.keys())
        keys.sort(reverse=reverse)
        result = {}
        for key in keys:
            result[key] = d[key]
        return result

    def _sort_dicts(self, lst: List[dict], sort_key: str) -> List[dict]:
        """
        Sort a list of Dictionaries

        Args:
            lst (List[dict]): List of dictionaries to sort
            sort_key (str): Key of dictionary used for sorting

        Returns:
            List[dict]: Sorted list of dictionaries.
        """
        if len(lst) == 0:
            return lst
        keys: List[str] = []
        _result: List[dict] = []
        for i, itm in enumerate(lst):
            keys.append((itm[sort_key], i))
        keys.sort()
        for k in keys:
            _result.append(lst[k[1]])
        return _result

    # endregion sorting

    def dynamic_imp(self, package: str, mod_name: str, class_name: str) -> Tuple[ModuleType, object]:
        try:
            module = importlib.import_module(f"{package}.{mod_name}")
            my_class = getattr(module, class_name)
            return module, my_class
        except Exception as e:
            # print(e)
            raise e

    def get_safe_word(self, in_str: object) -> object:
        """
        Get safe word. If a word is a reserved python word then _ is appended.

        Args:
            in_str (object): input

        Returns:
            object: if ``in_str`` is not str then it is returned verbatim. Otherwise returns str.
        """
        if not isinstance(in_str, str):
            return in_str
        if in_str in RESERVER_WORDS:
            return in_str + "_"
        return in_str

    def get_q_wrapped(self, in_str: str, quote: Optional[str] = "'") -> str:
        """
        Wraps a string in quotes

        Args:
            in_str (str): string to wrap
            quote (Optional[str], optional): string prepend and append. Defaults to "'".

        Returns:
            str: in_str with quote prepended and appended.
        """
        return f"{quote}{in_str}{quote}"

    def is_q_type(self, in_type: object) -> bool:
        """Gets if in_type is in quote"""
        if not isinstance(in_type, str):
            return False
        if in_type in self.quote:
            return True
        return False

    def get_q_type(self, in_type: object) -> object:
        """
        If in_type is in quote then it is quoted.
        Unless ``using_future_annotations`` property is ``True`` then it is returned verbatim.
        """
        
        if not self.using_future_annotations and self.is_q_type(in_type=in_type):
            return self.get_q_wrapped(in_str=in_type)
        return in_type

    def get_timestamp_utc(self) -> str:
        """
        Gets utc timestamp in format of ``2021-12-16 11:37:50+00:00``

        Returns:
            datetime: utc timestamp
        """
        current_GMT = time.gmtime()
        ts = calendar.timegm(current_GMT)
        return str(datetime.fromtimestamp(ts, tz=timezone.utc))

    # region Class inherits and From Imports

    def get_from_import(self, class_name: str, im_data: Iterable[str]) -> str:
        """
        Get a from string such as 'from ..sdbcx.table_descriptor import DataSettings`

        Args:
            class_name (str): Name if the class then is using the import or is extended by import
            im_data (List[str]): List of str expected to be a length of two or three.

        Returns:
            str: string formatted for a from statement
        """

        def is_self_import(path: str, name: str) -> bool:
            # in theory this should not happened as parser check for this condition and remove self imports.
            if name != class_name:
                return False
            p_parts = path.rsplit(sep=".", maxsplit=1)
            if len(p_parts) != 2:
                raise Exception("get_from_import() Expected im_parts param to have a length of two!")
            # in the cases where there is a single . such as .x_package then
            # im_parts will be ['', 'x_package']
            # This indicates that class it trying to import itself
            return p_parts[0] == ""

        im_len = len(im_data)
        if im_len < 2:
            raise Exception(
                f"{self.__class__.__name__}.get_from_import() Expected im_data param to have a min length of two!"
            )
        im = im_data[0]  # .sdbcx.table_descriptor
        name = im_data[1]  # DataSettings
        if is_self_import(im, name):
            return ""
        if im_len == 3:
            s_as = im_data[2]
            return f"from {im} import {name} as {s_as}"
        if name == class_name:
            # can not extend a class with the same name.
            # Change the from import and elsewhere change the extends name to match
            im_parts = im.rsplit(sep=".", maxsplit=1)
            # because there is a standard through all templates for snake case name and name,
            # such table_descriptor, TableDescriptor
            # it means we can rely on this standard to adjust import
            im_last = im_parts.pop()
            im = ".".join(im_parts)
            return f"from {im} import {im_last}"
        return f"from {im} import {name}"

    def get_class_inherits(self, class_name: str, imports: Union[str, List[str]]) -> str:
        """
        Gets class inherits taking into account if an inherit is the same name as the class.

        Args:
            class_name (str): Name of the class inheriting
            imports (Union[str, List[str]]): string or list of strings of class inherits

        Returns:
            str: comma sep string of inherits.
        """

        def get_import(name: str) -> str:
            def is_mapped(name: str) -> bool:
                return name in self.extends_map

            def get_mapped(name: str) -> bool:
                return self.extends_map[name]

            if is_mapped(name):
                return get_mapped(name)
            _name = self.get_last_part(input=name)
            if class_name == _name:
                return f"{self.camel_to_snake(_name)}.{_name}"
            else:
                return _name

        if isinstance(imports, str):
            return get_import(imports)
        im_lst: List[str] = []

        for s in imports:
            im_lst.append(get_import(s))
        s = "object"
        for i, im in enumerate(im_lst):
            if i == 0:
                s = ""
            if i > 0:
                s += ", "
            s += im
        return s

    def get_class_inherits_from_db(self, default: str = "object") -> str:
        """
        Gets class inherits taking into account if an inherit is the same name as the class.

        Args:
            class_name (str): Name of the class inheriting
            imports (Union[str, List[str]]): string or list of strings of class inherits

        Returns:
            str: comma sep string of inherits.
        """
        key = "get_class_inherits_from_db_" + default
        if key in self.__cache:
            return self.__cache[key]

        def get_import(extend: ExtendsInfo) -> str:
            def is_mapped() -> bool:
                return not extend.map_name is None

            def get_mapped() -> bool:
                return extend.map_name

            if is_mapped():
                return get_mapped()
            _name = self.get_last_part(extend.namespace)
            return _name

        ns = f"{self.namespace}.{self.name}"
        sql_entends = SqlExtends()
        extends = sql_entends.get_extends(namespace=ns)
        len_ent = len(extends)
        if len_ent == 0:
            self.__cache[key] = default
            return self.__cache[key]
        if len_ent == 1:
            self.__cache[key] = get_import(extends[0])
            return self.__cache[key]
        extends.sort()  # sort, gets it sort order from database

        im_lst: List[str] = []

        for ex in extends:
            im_lst.append(get_import(ex))
        s = "object"
        for i, im in enumerate(im_lst):
            if i == 0:
                s = ""
            if i > 0:
                s += ", "
            s += im
        self.__cache[key] = s
        return self.__cache[key]

    # endregion Class inherits and From Imports

    def get_abstract_imports(self, abm: List[bool], abp: List[bool]) -> List[str]:
        """
        Gets a list with abstractmethod/abstractproperty appended as needed

        Args:
            abm (List[bool]): List of booleans to test for abstractmethod
            abp (List[bool]): List of booleans to test for abstractproperty

        Returns:
            List[str]: [description]
        """
        a_method = True in abm
        a_prop = True in abp
        results = []
        if a_method:
            results.append("abstractmethod")
        if a_prop:
            results.append("abstractproperty")
        return results

    def get_rel_import(self, in_str: str, ns: str, sep: str = ".") -> str:
        ri = RelInfo.get_rel_import(in_str=in_str, ns=ns, sep=sep)
        return f"from {ri.frm} import {ri.imp}"

    def get_rel_import_long(self, in_str: str, ns: str, sep: str = ".") -> str:
        ri = RelInfo.get_rel_import_long(in_str=in_str, ns=ns, sep=sep)
        return f"from {ri.frm} import {ri.imp} as {ri.as_}"

    # region Camel and Snake Case
    def to_camel_case(self, s: str) -> str:
        """
        Converts string to ``CamelCase``

        Args:
            s (str): string to convert such as ``snake_case_word`` or ``pascalCaseWord``

        Returns:
            str: string converted to ``CamelCaseWord``
        """
        s = s.strip()
        if not s:
            return ""
        result = s
        if "_" in s:
            result = "".join(word.title() for word in s.split("_"))
            return result
        # convert to CamelCase if pascalCase was passed in.
        result = result[:1].upper() + result[1:]
        return result

    def to_pascal_case(self, s: str) -> str:
        """
        Converts string to ``pascalCase``

        Args:
            s (str): string to convert such as ``snake_case_word`` or  ``CamelCaseWord``

        Returns:
            str: string converted to ``pascalCaseWord``
        """
        result = self.to_camel_case(s)
        if result:
            result = result[:1].lower() + result[1:]
        return result

    def to_snake_case(self, s: str) -> str:
        """
        Convert string to ``snake_case``

        Args:
            s (str): string to convert such as ``pascalCaseWord`` or  ``CamelCaseWord``

        Returns:
            str: string converted to ``snake_case_word``
        """
        s = s.strip()
        if not s:
            return ""
        result = _REG_TO_SNAKE.sub("_", s)
        result = _REG_LETTER_AFTER_NUMBER.sub("_", result)
        return result.lower()

    def to_snake_case_upper(self, s: str) -> str:
        """
        Convert string to ``SNAKE_CASE``

        Args:
            s (str): string to convert such as ``snake_case_word`` or ``pascalCaseWord`` or  ``CamelCaseWord``

        Returns:
            str: string converted to ``SNAKE_CASE_WORD``
        """
        result = self.to_snake_case(s)
        if not s:
            return ""
        return result.upper()

    # endregion Camel and Snake Case

    # region post process
    def _set_post_process_str(self, s: str) -> None:
        """
        Adds a post process line to the post process lines.
        The prefix ``# post_process: rule_name: `` is added to the line.

        Args:
            s (str): _description_
        """
        # see also src.post namespace
        post_str = f"# post_process: rule_name: {s.lstrip()}"
        self._post_lines.add(post_str)
    
    def get_post_process(self) -> str:
        """
        Gets the post process lines as a string.
        This is use in a template to add post process lines to the generated code.
        The post processing takes place after the code is generated by ``app make``.

        Returns:
            str: post process lines as a string
        """
        # see also src.post namespace
        if not self._post_lines:
            return ""
        return "\n".join(self._post_lines)
    
    # endregion post process

    # region Properties
    @property
    def config(self) -> TmplConfig:
        return self._config

    # endregion Properties

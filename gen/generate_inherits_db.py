# coding: utf-8
"""
Reads module_links.json file and writes all naespaces and clases in to a database.
"""
from dataclasses import dataclass, asdict
import os
import glob
import json
import verr
import sqlite3 as sql
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, Set, List
from config import AppConfig
from parser import __version__, JSON_ID
# region Dataclass


@dataclass(frozen=True, eq=True)
class Ns:
    ns: str
    sort: int
# endregion Dataclass

# region Database


class SqlCtx:
    # https://stackoverflow.com/questions/26793753/using-a-context-manager-for-connecting-to-a-sqlite3-database
    def __init__(self, connect_str: str) -> None:
        self._cstr = connect_str

    def __enter__(self):
        # DateTime for sqlite:
        #   See: https://stackoverflow.com/a/37222799/1171746
        #   See: https://stackoverflow.com/a/1830499/1171746
        self.connection: sql.Connection = sql.connect(
            self._cstr, detect_types=sql.PARSE_DECLTYPES)
        self.connection.row_factory = sql.Row
        self.cursor: sql.Cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def get_connection(self) -> sql.Connection:
        return self._conn


class SqlNs:
    def __init__(self, connect_str: str) -> None:
        self._conn_str = connect_str
        self._is_init = False
        self._is_init_update = False
        if self._is_init is False:
            self._init()

    def _init(self) -> None:
        self._create_table_if_not_exist()
        self._is_init = True

    # region Table Create / Drop

    def _create_table_if_not_exist(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS namespace (
            ns TEXT PRIMARY KEY,
            sort INTEGER
            )"""
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)

    def _drop_table_if_exist(self) -> None:
        query = 'DROP TABLE IF EXISTS namespace'
        with SqlCtx(self._conn_str) as db:
            with db.connection:
                db.cursor.execute(query)
    # endregion Table Create / Drop

    def get_row_count(self) -> int:
        if self.has_data is False:
            return 0
        query = 'SELECT count() FROM namespace'
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)
            num_of_rows = db.cursor.fetchone()[0]
        return num_of_rows

    def insert_namespaces(self, ns_lst: List[Ns]) -> None:
        values = [asdict(ns) for ns in ns_lst]

        with SqlCtx(self._conn_str) as db:
            with db.connection:
                db.cursor.executemany(
                    "INSERT INTO namespace VALUES (:ns, :sort)", values)

    def remove_all(self) -> None:
        self._drop_table_if_exist()
        self._create_table_if_not_exist()

    def update_namespace(self, ns_lst: List[Ns]) -> None:
        self.remove_all()
        self.insert_namespaces(ns_lst=ns_lst)

    def has_data(self) -> bool:
        query = 'SELECT ns FROM namespace limit 1'
        has_data = False
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)
            for _ in db.cursor:
                has_data = True
        return has_data



# endregion Database


class ParseModuleLinks:

    def __init__(self, config: AppConfig) -> None:
        self._app_config = config
        root_dir = os.environ.get('project_root', None)
        if root_dir:
            self._root_dir = Path(root_dir)
        else:
            self._root_dir = Path(__file__).parent.parent
        self._imports: List[str] = []
        self._min_ver = verr.Version.parse(config.min_module_links_ver)
        self._db_cnn = str(self._root_dir / config.resource_dir / config.db_mod_info)
        self._ns_db = SqlNs(connect_str=self._db_cnn)

    def get_module_link_files(self) -> Set[str]:
        dirname = str(self._root_dir / self._app_config.uno_base_dir)
        # https://stackoverflow.com/questions/20638040/glob-exclude-pattern
        # root module_links.json needs to be remove from listing.
        # it will not need any processing here.
        # using sets and deduct seem the simplist way.
        pattern = dirname + f'/**/{self._app_config.module_links_file}'
        root_json = Path(dirname, self._app_config.module_links_file)
        files = set(glob.glob(pattern, recursive=True))
        ex_files = set()
        ex_files.add(str(root_json))
        # deduct sets:
        return files - ex_files
    
    def get_count(self) -> int:
        return self._ns_db.get_row_count()

    def write_all_ns(self) -> None:
        # this can be done multi thread
        self._imports.clear()
        if self._ns_db.has_data():
            msg = f"{self.__class__.__name__}.write_all_ns() Can not write because there is already data in the database for namespace"
            raise Exception(msg)

        m_files = self.get_module_link_files()
        for j_file in m_files:
            with open(j_file, 'r') as file:
                j_data = json.load(file)
            self._validite_json(file=file, data=j_data)
            self._read(json_data=j_data)

        sorted_lst = self._get_ns_lst()
        self._ns_db.insert_namespaces(ns_lst=sorted_lst)

    def update_all_ns(self) -> None:
        self._ns_db.remove_all()
        self.write_all_ns()
        
    def _get_ns_lst(self) -> List[Ns]:
        self._imports.sort()
        ns_lst = []
        for i, ns in enumerate(self._imports):
            ns_lst.append(Ns(ns=ns, sort=i ))
        return ns_lst

    # region Read Json into Imports
    def _read(self, json_data: dict) -> None:
        ns: str = json_data['namespace']
        self._read_classes_ex(ns, json_data)
        self._read_classes_interface(ns, json_data)
        self._read_classes_service(ns, json_data)
        self._read_classes_singleton(ns, json_data)
        self._read_classes_struct(ns, json_data)
        self._read_const(ns, json_data)
        self._read_enums(ns, json_data)
        self._read_typedef(ns, json_data)
        

    def _read_enums(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data'].get('enums', [])
        for itm in lst:
            self._imports.append(f"{ns}.{itm['name']}")

    def _read_const(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data'].get('constants', [])
        for itm in lst:
            self._imports.append(f"{ns}.{itm['name']}")

    def _read_typedef(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data'].get('typedef', [])
        for itm in lst:
            self._imports.append(f"{ns}.{itm['name']}")

    def _read_classes_service(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'service', [])
        for itm in lst:
            self._imports.append(f"{ns}.{itm['name']}")

    def _read_classes_struct(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'struct', [])
        for itm in lst:
            self._imports.append(f"{ns}.{itm['name']}")

    def _read_classes_ex(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'exception', [])
        for itm in lst:
            self._imports.append(f"{ns}.{itm['name']}")
    
    def _read_classes_interface(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'interface', [])
        for itm in lst:
            self._imports.append(f"{ns}.{itm['name']}")

    def _read_classes_singleton(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'singleton', [])
        for itm in lst:
            self._imports.append(f"{ns}.{itm['name']}")

    # endregion Read Json into Imports
    
    # region Validation
    def _validite_json(self, file: str, data: dict):
        msg = f"{self.__class__.__name__}._validite_json() "

        key = 'id'
        if not key in data:
            _msg = f"{msg} Json missing id field. File: {file}"
            raise Exception(_msg)
        if data[key] != JSON_ID:
            _msg = f"{msg} Json data bad id field. Expected: {JSON_ID}, Got: {data[key]}. File: {file}"
            raise Exception(_msg)
        key = 'type'
        if not key in data:
            _msg = f"{msg} Json missing type field. File: {file}"
            raise Exception(_msg)
        if data[key] != 'module_links':
            _msg = f"{msg} Json data bad id field. Expected: module_links, Got: {data[key]}. File: {file}"
            raise Exception(_msg)
        key = 'url_base'
        if not key in data:
            _msg = f"{msg} Json missing url_base field. File: {file}"
            raise Exception(_msg)
        key = 'version'
        if not key in data:
            _msg = f"{msg} Json missing version field. File: {file}"
            raise Exception(_msg)
        json_ver = verr.Version.parse(data[key])
        if json_ver < self._min_ver:
            _msg = f"{msg} Version fail Expect a min version of '{self._min_ver}', got '{json_ver}'. File: {file}"
            raise Exception(_msg)
        key = 'data'
        if not key in data:
            _msg = f"{msg} Json missing data field. File: {file}"
            raise Exception(_msg)
        if not isinstance(data[key], dict):
            _msg = f"{msg} Json data field is not a dictionary. File: {file}"
            raise Exception(_msg)
    # endregion Validation

class ModuleLinksControler:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        self._parser = ParseModuleLinks(config=config)
        self._write_all = bool(kwargs.get('write_all', False))
        self._update_all = bool(kwargs.get('update_all', False))
        self._count = bool(kwargs.get('count_all', False))

    def results(self) -> Any:
        if self._count:
            return self._parser.get_count()
        elif self._write_all:
            self._parser.write_all_ns()
        elif self._update_all:
            self._parser.update_all_ns()
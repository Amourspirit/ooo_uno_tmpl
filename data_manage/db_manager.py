# coding: utf-8
"""
Creates a datbase if not existing. Database must be init. See DatabaseControler
Reads module_links.json file and writes info in a database.
Reads Component json files and writes info in a database.
"""
# region Imports
from abc import abstractmethod
from dataclasses import dataclass, asdict
import os
import glob
import json
import verr
import sqlite3 as sql
from pathlib import Path
from typing import Any, Dict, Set, List, Union
from config import AppConfig
from parser import __version__, JSON_ID
# endregion Imports

# region Dataclass


@dataclass(frozen=True, eq=True)
class Extends:
    namespace: str
    map_name: Union[str, None]
    fk_component_id: str
    id_extends: Union[int, None] = None


@dataclass(frozen=True, eq=True)
class ExtendsMap:
    name: str
    fk_extends_id: int
    id_extends_map: Union[int, None] = None
@dataclass(frozen=True, eq=True)
class ComponentType:
    id_component_type: str


@dataclass(frozen=True, eq=True)
class Component:
    id_component: str
    name: str
    namespace: str
    type: str
    version: str
    lo_ver: str
    file: str


@dataclass(frozen=True, eq=True)
class ModuleInfo:
    id_module_info: str
    url_base: str
    file: str


@dataclass(frozen=True, eq=True)
class ModuleDetail:
    id_namespace: str
    name: str
    namespace: str
    href: str
    component_type: str
    sort: int = -1

    def __lt__(self, other: object):
        if not isinstance(other, ModuleDetail):
            return NotImplemented
        return self.sort < other.sort
# endregion Dataclass

# region Database


class SqlCtx:
    # Using a context manager: https://tinyurl.com/y8dplak5
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


class BaseSql:
    def __init__(self, connect_str: str) -> None:
        self._conn_str = connect_str

    @abstractmethod
    def _create_table_if_not_exist(self) -> None:
        """Create Table if it does not exsit"""

    @abstractmethod
    def get_table_name(self) -> str:
        """Table Name"""

    def _drop_table_if_exist(self) -> None:
        query = 'DROP TABLE IF EXISTS ' + self.get_table_name()
        with SqlCtx(self._conn_str) as db:
            with db.connection:
                db.cursor.execute(query)

    def get_row_count(self) -> int:
        if self.has_data is False:
            return 0
        query = 'SELECT count() FROM ' + self.get_table_name()
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)
            num_of_rows = db.cursor.fetchone()[0]
        return num_of_rows

    def remove_all(self) -> None:
        self._drop_table_if_exist()
        self._create_table_if_not_exist()

    def has_data(self) -> bool:
        query = f"SELECT * FROM {self.get_table_name()} limit 1"
        has_data = False
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)
            for _ in db.cursor:
                has_data = True
        return has_data

    @property
    def conn_str(self) -> str:
        """Gets connect_str value"""
        return self._conn_str


class SqlInitDb:
    def __init__(self, connect_str: str) -> None:
        self._conn_str = connect_str
        self._is_init = False

    def init_db(self) -> None:
        if self._is_init:
            return
        self._create_module_info()
        self._create_module_details()
        self._create_component_type()
        self._create_component()
        self._create_extends()
        self._is_init = True

    def _create_extends(self) -> None:
        # auto primary key: https://stackoverflow.com/a/26652736/1171746
        query = """CREATE TABLE IF NOT EXISTS extends (
            id_extends INTEGER PRIMARY KEY AUTOINCREMENT,
            namespace VARCHAR(255) NOT NULL,
            map_name VARCHAR(255),
            fk_component_id VARCHAR(255) NOT NULL
            )"""
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)
    

    def _create_module_info(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS module_info (
            id_module_info VARCHAR(255) PRIMARY KEY,
            url_base TEXT NOT NULL,
            file VARCHAR(255) NOT NULL
            )"""
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)

    def _create_module_details(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS module_detail (
            id_namespace VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            namespace VARCHAR(255) NOT NULL,
            href TEXT,
            component_type VARCHAR(20) NOT NULL,
            sort INTEGER NOT NULL
            )"""
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)

    def _create_component_type(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS component_type (
            id_component_type VARCHAR(20) PRIMARY KEY
            )"""
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)
        if not self.has_data(table='component_type'):
            values = [
                ('const',),
                ('enum',),
                ('exception',),
                ('interface',),
                ('singleton',),
                ('service',),
                ('struct',),
                ('typedef',)
            ]
            with SqlCtx(self._conn_str) as db:
                with db.connection:
                    db.cursor.executemany(
                        "INSERT INTO component_type VALUES (?)", values)

    def _create_component(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS component (
            id_component VARCHAR(50) PRIMARY KEY,
            type VARCHAR(20) NOT NULL,
            version VARCHAR(20) NOT NULL,
            name VARCHAR(50) NOT NULL,
            namespace VARCHAR(255) NOT NULL,
            lo_ver VARCHAR(50) NOT NULL,
            file VARCHAR(255) NOT NULL
            )"""
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)

    def has_data(self, table: str) -> bool:
        query = f"SELECT * FROM {table} limit 1"
        has_data = False
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)
            for _ in db.cursor:
                has_data = True
        return has_data

# region    Table Classes
# region        SQL Component


class SqlComponent(BaseSql):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    def get_table_name(self) -> str:
        """Gets the current table name"""
        return 'component'

    def insert(self, data: List[Component]) -> None:
        """
        Inserts/updates data. Handles inserting and updating

        Args:
            data (List[Component]): data to update
        """
        # SQLite UPSERT / UPDATE OR INSERT
        # https://stackoverflow.com/questions/15277373/sqlite-upsert-update-or-insert
        values = [asdict(itm) for itm in data]
        query = """INSERT INTO component
        VALUES (:id_component, :type, :version, :name, :namespace, :lo_ver, :file)
        ON CONFLICT(id_component) 
        DO UPDATE SET type=excluded.type, version=excluded.version,
        name=excluded.name, namespace=excluded.namespace, lo_ver=excluded.lo_ver, file=excluded.file;
        """
        with SqlCtx(self.conn_str) as db:
            with db.connection:
                db.cursor.executemany(query, values)

    def update(self, data: List[Component]) -> None:
        """
        Updates data. Handles updating

        Args:
            data (List[Component]): data to update
        """
        # self.remove_all()
        self.insert(data)
# endregion     SQL Component

# region        SQL ComponentExtends


class SqlComponentExtends(BaseSql):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    def get_table_name(self) -> str:
        """Gets the current table name"""
        return 'component'

    def insert(self, data: List[Extends]) -> None:
        """
        Inserts/updates data. Handles inserting and updating

        Args:
            data (List[Extends]): data to update
        """
        values = [asdict(itm) for itm in data]

        with SqlCtx(self.conn_str) as db:
            query = """INSERT INTO extends
            VALUES (:id_extends, :namespace, :map_name, :fk_component_id)
            ON CONFLICT(id_extends) 
            DO UPDATE SET namespace=excluded.namespace, map_name=excluded.map_name,
            fk_component_id=excluded.fk_component_id;
            """
            with db.connection:
                db.cursor.executemany(query, values)

    def update(self, data: List[Extends]) -> None:
        """
        Updates data. Handles updating

        Args:
            data (List[Extends]): data to update
        """
        self.insert(data=data)
# endregion     SQL ComponentExtends


# region        SQL Module Detail


class SqlModuleDetail(BaseSql):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    def get_table_name(self) -> str:
        """Gets the current table name"""
        return 'module_detail'

    def insert(self, data: List[ModuleDetail]) -> None:
        """
        Inserts/updates data. Handles inserting and updating

        Args:
            data (List[ModuleDetail]): data to update
        """
        # SQLite UPSERT / UPDATE OR INSERT
        # https://stackoverflow.com/questions/15277373/sqlite-upsert-update-or-insert
        values = [asdict(itm) for itm in data]
        with SqlCtx(self.conn_str) as db:
            query = """INSERT INTO module_detail
            VALUES (:id_namespace, :name, :namespace, :href, :component_type, :sort)
            ON CONFLICT(id_namespace) 
            DO UPDATE SET name=excluded.name, namespace=excluded.namespace,
            href=excluded.href, component_type=excluded.component_type, sort=excluded.sort;
            """
            # query = "INSERT INTO module_details VALUES (:id_namespace, :name, :namespace, :href, :component_type, :sort)"
            with db.connection:
                db.cursor.executemany(query, values)

    def update(self, data: List[ModuleDetail]) -> None:
        """
        Updates data. Handles updating

        Args:
            data (List[ModuleDetail]): data to update
        """
        # self.remove_all()
        self.insert(data)

# endregion     SQL Module Detail

# region        SQL Module Info


class SqlModuleInfo(BaseSql):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    def get_table_name(self) -> str:
        """Gets the current table name"""
        return 'module_info'

    def insert(self, data: List[ModuleInfo]) -> None:
        """
        Inserts/updates data. Handles inserting and updating

        Args:
            data (List[ModuleInfo]): data to update
        """
        values = [asdict(itm) for itm in data]
        with SqlCtx(self.conn_str) as db:
            query = """INSERT INTO module_info
            VALUES (:id_module_info, :url_base, :file)
            ON CONFLICT(id_module_info) 
            DO UPDATE SET url_base=excluded.url_base, file=excluded.file;
            """
            with db.connection:
                db.cursor.executemany(query, values)

    def update(self, data: List[ModuleInfo]) -> None:
        """
        Updates data. Handles updating

        Args:
            data (List[ModuleInfo]): data to update
        """
        self.insert(data)
# endregion         SQL Module Info

# endregion Table Classes


class DbConnect:
    def __init__(self, config: AppConfig) -> None:
        self._app_config = config
        root_dir = os.environ.get('project_root', None)
        if root_dir:
            self._root_dir = Path(root_dir)
        else:
            self._root_dir = Path(__file__).parent.parent
        self._conn = str(self._root_dir /
                         config.resource_dir / config.db_mod_info)

    @property
    def connection_str(self) -> str:
        """Gets connection_str value"""
        return self._conn

    @property
    def root_dir(self) -> Path:
        """Gets root_dir value"""
        return self._root_dir
# endregion Database

# region Parse


class ParseModuleJson:
    def __init__(self, config: AppConfig) -> None:
        self._app_config = config
        self._components: List[Component] = []
        self._extends: List[Extends] = []
        self._min_ver = verr.Version.parse(config.min_json_data_ver)
        self._valid_types = tuple(self._app_config.component_types)
        conn = DbConnect(self._app_config)
        self._db_cnn = conn.connection_str
        self._root_dir = conn.root_dir
        self._component_tbl = SqlComponent(connect_str=self._db_cnn)
        self._extends_tbl = SqlComponentExtends(connect_str=self._db_cnn)

    def get_module_json_files(self) -> List[str]:
        def filter_fn(name) -> bool:
            p_name = Path(name).name
            if p_name == self._app_config.module_links_file:
                return False
            return True
        dirname = str(self._root_dir / self._app_config.uno_base_dir)
        pattern = dirname + '/**/*.json'
        all_files = glob.glob(pattern, recursive=True)
        files = filter(filter_fn, all_files)
        return files

    def _write_all(self) -> None:
        self._components.clear()
        m_files = self.get_module_json_files()
        for j_file in m_files:
            with open(j_file, 'r') as file:
                j_data = json.load(file)
            self._validite_json(file=file, data=j_data)
            self._read(json_data=j_data, file=j_file)

        self._component_tbl.insert(data=self._components)
        self._extends_tbl.insert(data=self._extends)

    def update_all_details(self) -> None:
        self._write_all()

    def _read(self, json_data: dict, file: str) -> None:
        self._read_main(json_data=json_data, file=file)

    def _read_main(self, json_data: dict, file: str) -> None:
        rel = Path(file).relative_to(self._root_dir)
        ns = json_data['namespace']
        name = json_data['name']
        c = Component(
            id_component=f"{ns}.{name}",
            name=name,
            namespace=ns,
            type=json_data['type'],
            version=json_data['version'],
            lo_ver=json_data['libre_office_ver'],
            file=str(rel)
        )
        self._read_extends(json_data=json_data, comp=c)
        self._components.append(c)

    def _read_extends(self, json_data: dict, comp: Component) -> None:
        j_extends: List[str] = json_data['data'].get('extends', [])
        j_extends_map: Dict[str, str] = json_data['data'].get('extends_map', {})
        for ext in j_extends:
            map_name = j_extends_map.get(ext, None)
            self._extends.append(
                Extends(namespace=ext, map_name=map_name, fk_component_id=comp.id_component))

    # region Validation
    def _validite_json(self, file: str, data: dict):
        msg = f"{self.__class__.__name__}._validite_json() "

        key = 'id'
        if not key in data:
            _msg = f"{msg} Json missing id field. File: {file}"
            raise Exception(_msg)
        if data[key] != 'uno-ooo-parser':
            _msg = f"{msg} Json data bad id field. Expected: uno-ooo-parser, got: {data[key]}. File: {file}"
            raise Exception(_msg)
        key = 'type'
        if not key in data:
            _msg = f"{msg} Json missing type field. File: {file}"
            raise Exception(_msg)
        if not data[key] in self._valid_types:
            _msg = f"{msg} Json data bad id field. Expected: one of {self._valid_types}, got: {data[key]}. File: {file}"
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


class ParseModuleLinks:

    def __init__(self, config: AppConfig) -> None:
        self._app_config = config
        self._module_details: List[ModuleDetail] = []
        self._module_infos: List[ModuleInfo] = []
        self._min_ver = verr.Version.parse(config.min_module_links_ver)
        conn = DbConnect(self._app_config)
        self._db_cnn = conn.connection_str
        self._root_dir = conn.root_dir
        self._module_detail_tbl = SqlModuleDetail(connect_str=self._db_cnn)
        self._module_info_tbl = SqlModuleInfo(connect_str=self._db_cnn)

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

    def get_count_details(self) -> int:
        return self._module_detail_tbl.get_row_count()

    def _write_all(self) -> None:
        self._module_details.clear()
        self._module_infos.clear()
        m_files = self.get_module_link_files()
        for j_file in m_files:
            with open(j_file, 'r') as file:
                j_data = json.load(file)
            self._validite_json(file=file, data=j_data)
            self._read(json_data=j_data, file=j_file)

        sorted_lst = self._get_detail_lst()

        self._module_detail_tbl.insert(data=sorted_lst)
        self._module_info_tbl.insert(data=self._module_infos)

    def write_all_details(self) -> None:
        if self._module_detail_tbl.has_data():
            msg = f"{self.__class__.__name__}.write_all_details() Can not write because there is already data in the database for {self._module_detail_tbl.get_table_name()}"
            raise Exception(msg)
        if self._module_info_tbl.has_data():
            msg = f"{self.__class__.__name__}.write_all_details() Can not write because there is already data in the database for {self._module_detail_tbl.get_table_name()}"
            raise Exception(msg)
        self._write_all()

    def update_all_details(self) -> None:
        self._write_all()

    def _get_detail_lst(self) -> List[ModuleDetail]:
        self._module_details
        _sorted = sorted(self._module_details, key=lambda im: im.id_namespace)
        lst = []
        for i, el in enumerate(_sorted):
            lst.append(ModuleDetail(
                id_namespace=el.id_namespace,
                name=el.name,
                namespace=el.namespace,
                href=el.href,
                component_type=el.component_type,
                sort=i
            ))
        return lst

    # region Read Json into Imports
    def _read(self, json_data: dict, file: str) -> None:
        rel = Path(file).relative_to(self._root_dir)
        ns: str = json_data['namespace']
        self._read_classes_ex(ns, json_data)
        self._read_classes_interface(ns, json_data)
        self._read_classes_service(ns, json_data)
        self._read_classes_singleton(ns, json_data)
        self._read_classes_struct(ns, json_data)
        self._read_const(ns, json_data)
        self._read_enums(ns, json_data)
        self._read_typedef(ns, json_data)
        self._module_infos.append(ModuleInfo(
            id_module_info=ns,
            url_base=json_data['url_base'],
            file=str(rel)
        ))

    def _read_enums(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data'].get('enums', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='enum'
            ))

    def _read_const(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data'].get('constants', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='const'
            ))

    def _read_typedef(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data'].get('typedef', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='typedef'
            ))

    def _read_classes_service(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'service', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='service'
            ))

    def _read_classes_struct(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'struct', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='struct'
            ))

    def _read_classes_ex(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'exception', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='exception'
            ))

    def _read_classes_interface(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'interface', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='interface'
            ))

    def _read_classes_singleton(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'singleton', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='singleton'
            ))

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

# endregion Parse

# region Controller


class ModuleLinksControler:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        self._parser = ParseModuleLinks(config=config)
        self._write_all = bool(kwargs.get('write_all', False))
        self._update_all = bool(kwargs.get('update_all', False))
        self._count = bool(kwargs.get('count_all', False))

    def results(self) -> Any:
        if self._count:
            return self._parser.get_count_details()
        elif self._write_all:
            self._parser.write_all_details()
        elif self._update_all:
            self._parser.update_all_details()
        return None

    def _init_database(self) -> None:
        db = SqlInitDb(self._conn.connection_str)
        db.init_db()


class DatabaseControler:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        self._parser = ParseModuleLinks(config=config)
        self._init_db = bool(kwargs.get('init_db', False))
        self._conn = DbConnect(config)

    def results(self) -> None:
        if self._init_db:
            self._init_database()

    def _init_database(self) -> None:
        db = SqlInitDb(self._conn.connection_str)
        db.init_db()


class ComponentControler:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        self._parser = ParseModuleJson(config=config)
        self._write_all = bool(kwargs.get('write_all', False))
        self._update_all = bool(kwargs.get('update_all', False))

    def results(self) -> Any:
        if self._update_all or self._write_all:
            self._parser.update_all_details()
        return None

# endregion Controller

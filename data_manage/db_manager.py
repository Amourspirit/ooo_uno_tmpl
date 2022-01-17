# coding: utf-8
"""
Creates a datbase if not existing. Database must be init. See DatabaseControler
Reads module_links.json file and writes info in a database.
Reads Component json files and writes info in a database.
"""
# region Imports
from abc import abstractmethod
from dataclasses import dataclass, asdict, field
from enum import unique
from optparse import Option
import os
import glob
import json
import verr
import sqlite3 as sql
import textwrap
import queue
from pathlib import Path
from typing import Any, Dict, Optional, Set, List, Union, Tuple
from config import AppConfig
from parser import __version__, JSON_ID, mod_rel as RelInfo
# endregion Imports


# region Dataclass


@dataclass(frozen=True, eq=True)
class Extend:
    namespace: str
    map_name: Union[str, None]
    fk_component_id: str
    id_extend: Union[int, None] = None

@dataclass(frozen=True, eq=True)
class NamespaceChild:
    namespace: str
    parent: str
    sort: int = -1

    def __lt__(self, other: object):
        if not isinstance(other, NamespaceChild):
            return NotImplemented
        return self.sort < other.sort
@dataclass(frozen=True, eq=True)
class FullImport:
    namespace: str
    requires_typing: bool
    fk_component_id: str
    id_full_import: Union[int, None] = None
    sort: int = -1

    def __lt__(self, other: object):
        if not isinstance(other, FullImport):
            return NotImplemented
        return self.sort < other.sort
@dataclass
class NamespaceTree:
    namespace: str
    sort: int = -1
    children: 'List[NamespaceTree]' = field(default_factory=list)

    def __lt__(self, other: object):
        if not isinstance(other, NamespaceTree):
            return NotImplemented
        return self.sort < other.sort

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

    @property
    def conn_str(self) -> str:
        """Gets connect_str value"""
        return self._conn_str


class BaseSqlTable(BaseSql):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

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
        self._create_extend()
        self._create_full_import()
        self._is_init = True

    def _create_extend(self) -> None:
        # auto primary key: https://stackoverflow.com/a/26652736/1171746
        query = """CREATE TABLE IF NOT EXISTS extend (
            id_extend INTEGER PRIMARY KEY AUTOINCREMENT,
            namespace VARCHAR(255) NOT NULL,
            map_name VARCHAR(255),
            fk_component_id VARCHAR(255) NOT NULL
            )"""
        with SqlCtx(self._conn_str) as db:
            db.cursor.execute(query)
    
    def _create_full_import(self) -> None:
        # bool : https://tinyurl.com/y9yocjx5
        query = """CREATE TABLE IF NOT EXISTS full_import (
            id_full_import INTEGER PRIMARY KEY AUTOINCREMENT,
            namespace VARCHAR(255) NOT NULL,
            requires_typing BOOLEAN NOT NULL CHECK (requires_typing IN (0, 1)),
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


class SqlComponent(BaseSqlTable):
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
        if len(data) == 0:
            return
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


class SqlComponentExtend(BaseSqlTable):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    def get_table_name(self) -> str:
        """Gets the current table name"""
        return 'extend'

    def insert(self, data: List[Extend]) -> None:
        """
        Inserts/updates data. Handles inserting and updating

        Args:
            data (List[Extend]): data to update
        """
        if len(data) == 0:
            return
        values = [asdict(itm) for itm in data]

        with SqlCtx(self.conn_str) as db:
            query = """INSERT INTO extend
            VALUES (:id_extend, :namespace, :map_name, :fk_component_id)
            ON CONFLICT(id_extend) 
            DO UPDATE SET namespace=excluded.namespace, map_name=excluded.map_name,
            fk_component_id=excluded.fk_component_id;
            """
            with db.connection:
                db.cursor.executemany(query, values)

    def update(self, data: List[Extend]) -> None:
        """
        Updates data. Handles updating

        Args:
            data (List[Extend]): data to update
        """
        self.insert(data=data)
# endregion     SQL ComponentExtends

# region        SQL SqlComponentFullImports


class SqlComponentFullImport(BaseSqlTable):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    def get_table_name(self) -> str:
        """Gets the current table name"""
        return 'full_import'

    def insert(self, data: List[FullImport]) -> None:
        """
        Inserts/updates data. Handles inserting and updating

        Args:
            data (List[FullImport]): data to update
        """
        if len(data) == 0:
            return
        values = [asdict(itm) for itm in data]

        with SqlCtx(self.conn_str) as db:
            query = """INSERT INTO full_import
            VALUES (:id_full_import, :namespace, :requires_typing, :fk_component_id)
            ON CONFLICT(id_full_import) 
            DO UPDATE SET namespace=excluded.namespace, requires_typing=excluded.requires_typing,
            fk_component_id=excluded.fk_component_id;
            """
            with db.connection:
                db.cursor.executemany(query, values)

    def update(self, data: List[FullImport]) -> None:
        """
        Updates data. Handles updating

        Args:
            data (List[FullImport]): data to update
        """
        self.insert(data=data)
# endregion     SQL SqlComponentFullImports

# region        SQL Module Detail


class SqlModuleDetail(BaseSqlTable):
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
        if len(data) == 0:
            return
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


class SqlModuleInfo(BaseSqlTable):
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
        if len(data) == 0:
            return
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

# region    Query

class NsImports(BaseSql):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    # region    Flat/ Flat Related
    
    # region        Query
    def _get_qry_ns(self) -> str:
        query = """SELECT extend.namespace as ns, module_detail.sort as sort FROM extend
        LEFT JOIN module_detail on module_detail.id_namespace = extend.namespace
        WHERE extend.fk_component_id like :namespace"""
        return query
    # endregion     Queries
    
    # region        Tree
    def get_ns_tree(self, namespace: str) -> NamespaceTree:
        """
        Gets a tree of namesapce

        Args:
            namespace (str): Input namesapce

        Returns:
            NamespaceTree: Tree Object that contains children.
        
        Example:
            com.sun.star.registry.NestedRegistry
                com.sun.star.lang.XInitialization
                    com.sun.star.uno.XInterface
                com.sun.star.registry.XSimpleRegistry
                    com.sun.star.uno.XInterface
        """
        query = self._get_qry_ns()
        ns_dict = {}

        def is_cache(ns: str) -> bool:
            return ns in ns_dict

        def get_cache(ns: str) -> List[NamespaceTree]:
            return ns_dict[ns]

        def set_cache(ns: str, lst: List[NamespaceTree]) -> None:
            ns_dict[ns] = lst

        def set_tree_children(db: SqlCtx, ns_tree: NamespaceTree):
            """
            Sets children for ``ns_tree``. Children are automatically appended to ``ns_tree``
            
            As children are found they are cached. On subsequent calls if namespace is in cached it is returned.

            Args:
                db (SqlCtx): Database connection
                ns_tree (NamespaceTree): namespace info

            """
            if is_cache(ns_tree.namespace):
                ns_tree.children = [
                    ns_obj for ns_obj in get_cache(ns_tree.namespace)]
                return ns_tree.children
            db.cursor.execute(query, {"namespace": ns_tree.namespace})
            results = []
            for row in db.cursor:
                results.append(NamespaceTree(
                    namespace=row['ns'],
                    sort=row['sort']
                ))
            ns_tree.children = results
            set_cache(ns=ns_tree.namespace, lst=ns_tree.children)
            return ns_tree.children

        def build_tree(db: SqlCtx, tree_obj: NamespaceTree) -> None:
            """
            Recursivly finds all children for ``tree_obj`` and appends them to children.

            Args:
                db (SqlCtx): database connection
                tree_obj (NamespaceTree): namespace info
            """
            que = queue.Queue()

            def recurse(q: queue.Queue) -> None:
                # q contain siblings that have been aded to a parent already
                # now each sibling need to find it children
                sibling_que = queue.Queue()
                while not q.empty():
                    # sibling is not a parent
                    parent: NamespaceTree = q.get()
                    set_tree_children(db=db, ns_tree=parent)
                    for child in parent.children:
                        sibling_que.put(child)
                if not sibling_que.empty():
                    recurse(q=sibling_que)
            set_tree_children(db=db, ns_tree=tree_obj)
            for child in tree_obj.children:
                que.put(child)
            recurse(q=que)

        with SqlCtx(self.conn_str) as db:
            qry_sort = """SELECT module_detail.sort FROM module_detail
            WHERE module_detail.id_namespace like :namespace LIMIT 1;"""
            db.cursor.execute(qry_sort, {"namespace": namespace})
            for row in db.cursor:
                tree = NamespaceTree(
                    namespace=namespace,
                    sort=row['sort'])
                build_tree(db=db, tree_obj=tree)
                result = tree
        return result
    # endregion     Tree


    def get_flat_ns(self, namespace: str, full:bool) -> List[NamespaceChild]:
        """
        Gets direct extends of an object or the extends of 2nd level children.

        Args:
            namespace (str): Names of geit extends of.
            full (bool): If ``True`` gets extends for 1st level inherits;
                Otherwise, Gets extends for 2nd level children.

        Returns:
            List[Tuple[int, str]]: List of tuple containing entries for sort and then namesapce
        
        Notes:
            On second level (``full=False``) results, there is a filter applied that removes duplicate inherits.
            Only a pure list of inherits are returned. For instance XInterface would not be imported more thant onece.
            This is on purpose to remove any potential pythpon MRO issues.
        
            Importing com.sun.star.form.component.RichTextControl as ``full=True`` returns the following namespaces:
                com.sun.star.awt.UnoControlEditModel,
                com.sun.star.form.FormControlModel,
                com.sun.star.text.TextRange
            Importing as ``full=False``:
                com.sun.star.awt.UnoControlModel,
                com.sun.star.beans.XFastPropertySet,
                com.sun.star.beans.XPropertyState,
                com.sun.star.container.XContentEnumerationAccess,
                com.sun.star.form.FormComponent,
                com.sun.star.style.CharacterProperties,
                com.sun.star.style.CharacterPropertiesAsian,
                com.sun.star.style.CharacterPropertiesComplex,
                com.sun.star.style.ParagraphProperties,
                com.sun.star.style.ParagraphPropertiesAsian,
                com.sun.star.style.ParagraphPropertiesComplex,
                com.sun.star.text.XTextRange
            
            Notice that in the model there are a total of 15 child imports. This method returns 12 becuase duplicates
            are merged and/or removed.
            
            See Model `here <https://tinyurl.com/yb3eu5ng>`_
        """
        query = self._get_qry_ns()
        ns_dict = {}
        
        def is_cache(ns: str) -> bool:
            return ns in ns_dict
        
        def get_cache(ns: str) -> List[NamespaceChild]:
            return ns_dict[ns]
        
        def set_cache(ns: str, lst: List[NamespaceChild]) -> None:
            ns_dict[ns] = lst

        def get_ns_children(db: SqlCtx, ns: str) -> List[NamespaceChild]:
            if is_cache(ns):
                return [itm for itm in get_cache(ns)]
            db.cursor.execute(query, {"namespace": ns})
            children = []
            for row in db.cursor:
                children.append(NamespaceChild(
                    namespace=row['ns'],
                    parent=ns,
                    sort=row['sort']
                ))
            set_cache(ns=ns, lst=children)
            return children

        def process_flat(db: SqlCtx, flats: Set[NamespaceChild]) -> List[NamespaceChild]:
            # Lookup each namespaces children, perferably as unique only.
            # remove any child match from main list that is in namespace children.
            #
            # Loop through the list again, ignoring any namespace already processed.
            #
            # Keep in mind that a processed namespace could be removed by a match later down the list.
            # This means the list of done items needs to be checked and if match, removed.
            processed: Set[NamespaceChild] = set()
            flats_set: Set[NamespaceChild] = set(list(flats))
            
            for flat in flats:
                children = get_ns_children(db=db, ns=flat.namespace)
                for child in children:
                    if child in processed:
                        continue
                    if child in flats_set:
                        flats_set.remove(child)
                    flat_children = get_unique(db=db, ns=child.namespace)
                    for flat_child in flat_children:
                        if flat_child in processed:
                            continue
                        if flat_child in flat_children:
                            if flat_child in flats_set:
                                flats_set.remove(flat_child)
                        processed.add(flat_child)
                    processed.add(child)
            lst = list(flats_set)
            lst.sort()
            return lst
                
        def get_unique(db: SqlCtx, ns: str) -> Set[NamespaceChild]:
            que = queue.Queue()
            flat_set: Set[NamespaceChild] = set()
            def recurse(q: queue.Queue) -> None:
                # q contain siblings that have been aded to a parent already
                # now each sibling need to find it children
                sibling_que = queue.Queue()
                while not q.empty():
                    # sibling is not a parent
                    parent: NamespaceChild = q.get()
                    children = get_ns_children(db=db, ns=parent.namespace)
                    for child in children:
                        if child in flat_set:
                            continue
                        flat_set.add(child)
                        sibling_que.put(child)
                if not sibling_que.empty():
                    recurse(q=sibling_que)
            
            root_children = get_ns_children(db=db, ns=ns)
            for root_child in root_children:
                que.put(root_child)
                flat_set.add(root_child)
            recurse(q=que)

            # results = list(flat_set)
            # results.sort()
            return flat_set

        def build_flat(db: SqlCtx, ns: str) -> List[NamespaceChild]:
            flats: Set[NamespaceChild] = set()
            children: List[str] = []
            # getting child namespaces first leaves the direct
            # children out of results. This is perfered.
            db.cursor.execute(query, {"namespace": ns})
            for row in db.cursor:
                children.append(row['ns'])
            for child in children:
                c_flat = get_unique(db=db, ns=child)
                flats.update(c_flat)
            return process_flat(db=db, flats=flats)

        def build_flat_full(db: SqlCtx, ns: str) -> List[NamespaceChild]:
            flats: Set[NamespaceChild] = get_unique(db=db, ns=ns)
            return process_flat(db=db, flats=flats)


        with SqlCtx(self.conn_str) as db:
            if full:
                result = build_flat_full(db=db, ns=namespace)
            else:
                result = build_flat(db=db, ns=namespace)
        return result

    def get_ns_from_full(self, full_ns: str) -> str:
        """
        Gets full namespace from a full namespace

        Args:
            full_ns (str): Full namespace such as ``com.sun.star.uno.XInterface``

        Returns:
            str: namespace such as ``com.sun.star.uno``
        """
        qry = """SELECT module_detail.namespace as ns FROM module_detail
            WHERE module_detail.id_namespace like :namespace LIMIT 1;"""
        result = ''
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry, {"namespace": full_ns})
            for row in db.cursor:
                result = row['ns']
        return result
    
    def get_ns_link(self, full_ns: str) -> str:
        """
        Gets URL for a namespace

        Args:
            full_ns (str): Full Namespace such as ``com.sun.star.uno.XInterface``

        Returns:
            str: Url link
        """
        qry = """SELECT module_info.url_base || '/' || module_detail.href as link
            FROM module_detail
            JOIN module_info on module_detail.namespace = module_info.id_module_info
            WHERE module_detail.id_namespace like :namespace LIMIT 1;"""
        result = ''
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry, {"namespace": full_ns})
            for row in db.cursor:
                result = row['link']
        return result
    
    def get_flat_imports(self, namespace: str, full: bool) -> Tuple[str, str, str]:
        # if importing from children. The children imports need to be relative this namespace
        flats: List[NamespaceChild] = self.get_flat_ns(
            namespace=namespace, full=full)
        ns = self.get_ns_from_full(full_ns = namespace)
        results = []
        for flat in flats:
            from_, cls_, lng = RelInfo.get_rel_import_long(in_str=flat.namespace, ns=ns)
            results.append((from_, cls_, lng))
        return results

    def get_extends_long(self, namespace: str, full: bool) -> List[str]:
        flats = self.get_flat_ns(namespace=namespace, full=full)
        
        ns = self.get_ns_from_full(full_ns = namespace)
        results = []
        for flat in flats:
            lng = RelInfo.get_rel_import_long_name(
                in_str=flat.namespace, ns=ns)
            results.append(lng)
        return results

    def get_extends_short(self, namespace: str, full: bool) -> List[str]:
        flats = self.get_flat_ns(namespace=namespace, full=full)
        
        ns = self.get_ns_from_full(full_ns = namespace)
        results = []
        for flat in flats:
            lng = RelInfo.get_rel_import_short_name(
                in_str=flat.namespace, ns=ns)
            results.append(lng)
        return results
    # endregion Flat/ Flat Related

    # region IMPORTS
    # region    Query
    def _get_imports_qry(self, typing:bool) -> str:
        """
        Gets Query string for querying full_import Table

        Args:
            typing (bool): If True then requires_typing parameter is included in query string

        Returns:
            str: query string
        """
        qry = """SELECT full_import.id_full_import, full_import.namespace as ns, full_import.requires_typing as requires_typing, module_detail.sort as sort
            FROM full_import
            LEFT JOIN module_detail on module_detail.id_namespace = full_import.namespace
            WHERE full_import.fk_component_id like :namespace"""
        if typing is True:
            qry += ' AND full_import.requires_typing = :requires_typing'
        qry += ';'
        return qry
    
    def _get_imports_children_qry(self, typing:bool) -> str:
        """
        Gets Query string for querying full_import Table for all 2nd level import from given namesapce

        Args:
            typing (bool): If True then requires_typing parameter is included in query string

        Returns:
            str: query string
        """
        qry = """SELECT DISTINCT full_import.namespace as ns, full_import.requires_typing as requires_typing, module_detail.sort as sort
            FROM full_import
            LEFT JOIN module_detail on module_detail.id_namespace = full_import.namespace
            WHERE full_import.fk_component_id in (SELECT full_import.namespace FROM full_import
                WHERE full_import.fk_component_id like :namespace)"""
        if typing is True:
            qry += ' AND full_import.requires_typing = :requires_typing'
        qry += ' ORDER by sort;'
        return qry
    # endregion Query

    def _get_imports(self, full_ns: str, children:bool, typing: Optional[bool] = None) -> List[FullImport]:
        """
        Gets imports for a given namespace.

        Args:
            full_ns (str): Namespace to get imports for
            children (bool): If True then 2nd level childre are imported; Otherwise 1st level.
            typing (Optional[bool], optional): If ``True`` only imports that requre typing are returned.
                If ``False`` only imports that do not requrine typing are retruned.
                If None all imports for ``full_ns`` are returned. Defaults to ``None``.

        Returns:
            List[FullImport]: Import Information
        """
        args = {"namespace": full_ns}
        if typing is None:
            if children:
                qry_str = self._get_imports_children_qry(False)
            else:
                qry_str = self._get_imports_qry(False)
        else:
            if children:
                qry_str = self._get_imports_children_qry(True)
            else:
                qry_str = self._get_imports_qry(True)
            args['requires_typing'] = 1 if typing is True else 0
        results = []
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry_str, args)
            for row in db.cursor:
                namesapce: str = row['ns']
                id_full_import: int = -1 if children else row.get['id_full_import']
                requires_typing: bool = bool(row['requires_typing'])
                sort_ = int(row['sort'])
                results.append(FullImport(
                    namespace=namesapce,
                    requires_typing=requires_typing,
                    fk_component_id=full_ns,
                    sort=sort_,
                    id_full_import=id_full_import
                ))
        results.sort()
        return results
    def get_imports(self, full_ns: str, typing: Optional[bool] = None) -> List[FullImport]:
        """
        Gets imports for a given namespace.

        Args:
            full_ns (str): Namespace to get imports for
            typing (Optional[bool], optional): If ``True`` only imports that requre typing are returned.
                If ``False`` only imports that do not requrine typing are retruned.
                If None all imports for ``full_ns`` are returned. Defaults to ``None``.

        Returns:
            List[FullImport]: Import Information
        """
        return self._get_imports(full_ns=full_ns, children=False, typing=typing)
    
    def get_imports_child(self, full_ns: str) -> List[FullImport]:
        # get all extends imports
        # if Typing get all typing import
        # ignore any typing import that are imported with extends imports
        qry_fi = """SELECT full_import.id_full_import, full_import.namespace as ns, full_import.requires_typing, full_import.fk_component_id, module_detail.sort as sort
            FROM full_import
            LEFT JOIN module_detail on module_detail.id_namespace = full_import.namespace
            WHERE full_import.namespace like :child_ns
            and full_import.fk_component_id = :parent_ns
            LIMIT 1;"""
        def get_full_import(db:SqlCtx, ns_child: NamespaceChild) -> FullImport:

            args = {"parent_ns": ns_child.parent, "child_ns": ns_child.namespace}
            fi = None
            db.cursor.execute(qry_fi, args)
            for row in db.cursor:
                fi = FullImport(
                    namespace=row['ns'],
                    requires_typing=bool(row['requires_typing']),
                    fk_component_id=row['fk_component_id'],
                    sort=int(row['sort']),
                    id_full_import=int(row['id_full_import'])
                )
            if fi is None:
                msg = f"{self.__class__.__name__}.get_imports_child().get_full_import() Failed to get Full Inport data from database"
                raise Exception(msg)
            return fi

        flats = self.get_flat_ns(namespace=full_ns, full=False)
        ims = []
        with SqlCtx(self.conn_str) as db:
            for flat in flats:
                ims.append(get_full_import(
                    db=db, ns_child=flat
                ))
        ims.sort()
        return ims
    
    # endregion IMPORTS
# endregion Query

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
        self._extends: List[Extend] = []
        self._full_imports: List[FullImport] = []
        self._min_ver = verr.Version.parse(config.min_json_data_ver)
        self._valid_types = tuple(self._app_config.component_types)
        conn = DbConnect(self._app_config)
        self._db_cnn = conn.connection_str
        self._root_dir = conn.root_dir
        self._component_tbl = SqlComponent(connect_str=self._db_cnn)
        self._extend_tbl = SqlComponentExtend(connect_str=self._db_cnn)
        self._full_import_tbl = SqlComponentFullImport(connect_str=self._db_cnn)

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
        self._extend_tbl.insert(data=self._extends)
        self._full_import_tbl.insert(data=self._full_imports)

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
        self._read_full_imports(json_data=json_data, comp=c)
        self._components.append(c)

    def _read_extends(self, json_data: dict, comp: Component) -> None:
        j_extends: List[str] = json_data['data'].get('extends', [])
        j_extends_map: Dict[str, str] = json_data['data'].get('extends_map', {})
        for ext in j_extends:
            map_name = j_extends_map.get(ext, None)
            self._extends.append(
                Extend(namespace=ext, map_name=map_name, fk_component_id=comp.id_component))

    def _read_full_imports(self, json_data: dict, comp: Component) -> None:
        j_imports: Dict[List[str]] = json_data['data'].get('full_imports', {})
        gen_lst: List[str] = j_imports.get('general', [])
        type_lst: List[str] = j_imports.get('typing', [])
        for ns in gen_lst:
            self._full_imports.append(FullImport(
                namespace=ns,
                requires_typing=False,
                fk_component_id=comp.id_component
            ))
        for ns in type_lst:
            self._full_imports.append(FullImport(
                namespace=ns,
                requires_typing=True,
                fk_component_id=comp.id_component
            ))
        
        
    

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

class NamespaceControler:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        self._conn = DbConnect(config)
        self._ns_name: Union[str, None] = kwargs.get('ns_name', None)
        self._ns_flat: Union[str, None] = kwargs.get('ns_flat', None)
        self._ns_child_only: Union[str, None] = bool(kwargs.get('ns_child_only', True))
        self._ns_flat_frm: Union[str, None] = kwargs.get('ns_flat_frm', None)
        self._ns_extends_lng: Union[str, None] = kwargs.get(
            'extends_long', None)
        self._ns_extends_short: Union[str, None] = kwargs.get(
            'extends_short', None)
        self._link: Union[str, None] = kwargs.get('ns_link', None)
        self._ns_full_import: Union[str, None] = kwargs.get('ns_full_import', None)
        self._ns_full_import_typing: Union[bool, None] = kwargs.get(
            'ns_full_import_typing', None)
        self._ns_full_import_child: bool = bool(
            kwargs.get('ns_full_import_child', False))
        self._ns_full_import_from: bool = bool(
            kwargs.get('ns_full_import_from', False))
        self._ns_full_import_from_long: bool = bool(
            kwargs.get('ns_full_import_from_long', False))

    def results(self):
        if self._ns_name:
            return self._process_ns_tree()
        elif self._ns_flat:
            return self._get_flat_unique_ns()
        elif self._ns_flat_frm:
            return self._get_flat_frm()
        elif self._ns_extends_lng:
            return self._get_extends(long=True)
        elif self._ns_extends_short:
            return self._get_extends(long=False)
        elif self._link:
            return self._get_link()
        elif self._ns_full_import:
            return self._get_imports()

    def _process_ns_tree(self) -> str:
        """
        Gets Namespace Tree as str

        Returns:
            str: See Example
        
        Examle:
            com.sun.star.registry.NestedRegistry
                com.sun.star.lang.XInitialization
                    com.sun.star.uno.XInterface
                com.sun.star.registry.XSimpleRegistry
                    com.sun.star.uno.XInterface
        """
        indent_amt = 4
        qry = NsImports(self._conn.connection_str)

        def get_str(nt: NamespaceTree, in_str: str, indent: int) -> str:
            ns_str = in_str
            nt.children.sort()
            for ns_itm in nt.children:
                s = ns_itm.namespace
                s = textwrap.indent(s, ' ' * indent)
                s = '\n' + s
                ns_str += s
                ns_str = get_str(nt=ns_itm, in_str=ns_str,
                                 indent=indent + indent_amt)
            return ns_str

        n_tree = qry.get_ns_tree(namespace=self._ns_name)
        # return None
        # return str(n_tree)
        s_result = get_str(
            nt=n_tree, in_str=n_tree.namespace, indent=indent_amt)
        return s_result

    def _get_flat_unique_ns(self) -> str:
        qry = NsImports(self._conn.connection_str)
        flat_full = not self._ns_child_only
        n_flat = qry.get_flat_ns(namespace=self._ns_flat, full=flat_full)
        s = ''
        for i, itm in enumerate(n_flat):
            if i > 0:
                s += ', '
            s += itm.namespace
        return s
    
    def _get_flat_frm(self) -> str:
        qry = NsImports(self._conn.connection_str)
        full = not self._ns_child_only
        froms = qry.get_flat_imports(namespace=self._ns_flat_frm, full=full)
        s = ''
        for i, frm in enumerate(froms):
            if i > 0:
                s += '\n'
            s += f"from {frm[0]} import {frm[1]} as {frm[2]}"
        return s
    
    def _get_extends(self, long: bool) -> str:
        qry = NsImports(self._conn.connection_str)
        full = not self._ns_child_only
        if long:
            extends = qry.get_extends_long(namespace=self._ns_extends_lng, full=full)
        else:
            extends = qry.get_extends_short(namespace=self._ns_extends_short, full=full)
        s = ''
        for i, ex in enumerate(extends):
            if i > 0:
                s += ', '
            s += ex
        return s
    
    def _get_link(self) -> str:
        qry = NsImports(self._conn.connection_str)
        return qry.get_ns_link(full_ns=self._link)

    def _get_imports(self) -> str:
        qry = NsImports(self._conn.connection_str)
        def get_full_imports_str(imports: List[FullImport]) -> str:
            s = ''
            for i, im in enumerate(imports):
                if i > 0:
                    s += '\n'
                s += im.namespace
            return s
        def get_from_imports_short(imports: List[FullImport]) -> str:
            ns = self._ns_full_import.rsplit(sep='.', maxsplit=1)[0]
            s = ''
            for i, im in enumerate(imports):
                if i > 0:
                    s += '\n'
                rel = RelInfo.get_rel_import(
                    in_str=im.namespace, ns=ns)
                    
                s += f"from {rel[0]} import {rel[1]}"
            return s

        def get_from_imports_long(imports: List[FullImport]) -> str:
            ns = self._ns_full_import.rsplit(sep='.', maxsplit=1)[0]
            s = ''
            for i, im in enumerate(imports):
                if i > 0:
                    s += '\n'
                rel = RelInfo.get_rel_import_long(
                    in_str=im.namespace, ns=ns)

                s += f"from {rel[0]} import {rel[1]} as {rel[2]}"
            return s
        if self._ns_full_import_child:
            ims = qry.get_imports_child(
                full_ns=self._ns_full_import)
        else:
            ims = qry.get_imports(
                full_ns=self._ns_full_import, typing=self._ns_full_import_typing)
        if len(ims) == 0:
            return ''
        if self._ns_full_import_from:
            if self._ns_full_import_from_long:
                return get_from_imports_long(imports=ims)
            return get_from_imports_short(imports=ims)
        return get_full_imports_str(imports=ims)

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

# coding: utf-8
from .sql_ctx import SqlCtx
class InitDb:
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

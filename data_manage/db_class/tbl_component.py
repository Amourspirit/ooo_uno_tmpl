# coding: utf-8
from .base_sql_table import BaseSqlTable
from dataclasses import asdict
from typing import List
from .sql_ctx import SqlCtx
from ..data_class.component import Component

class TblComponent(BaseSqlTable):
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
        VALUES (:id_component, :type, :version, :name, :namespace, :lo_ver, :file, :c_name, :map_name)
        ON CONFLICT(id_component) 
        DO UPDATE SET type=excluded.type, version=excluded.version,
        name=excluded.name, namespace=excluded.namespace, lo_ver=excluded.lo_ver, file=excluded.file,
        c_name=excluded.c_name, map_name=excluded.map_name;
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

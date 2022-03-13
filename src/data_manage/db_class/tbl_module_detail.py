# coding: utf-8
from typing import List
from dataclasses import asdict
from .sql_ctx import SqlCtx
from .base_sql_table import BaseSqlTable
from ..data_class.module_detail import ModuleDetail


class TblModuleDetail(BaseSqlTable):
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

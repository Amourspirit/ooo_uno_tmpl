# coding: utf-8
from typing import List
from dataclasses import asdict
from .sql_ctx import SqlCtx
from .base_sql_table import BaseSqlTable
from ..data_class.module_info import ModuleInfo


class TblModuleInfo(BaseSqlTable):
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

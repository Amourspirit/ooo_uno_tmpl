# coding: utf-8
from typing import List
from dataclasses import asdict
from .sql_ctx import SqlCtx
from ..data_class.full_import import FullImport
from .base_sql_table import BaseSqlTable


class TblComponentFullImport(BaseSqlTable):
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

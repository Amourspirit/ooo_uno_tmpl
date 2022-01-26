# coding: utf-8
from typing import List
from dataclasses import asdict
from .sql_ctx import SqlCtx
from ..data_class.extend import Extend
from .base_sql_table import BaseSqlTable

class TblComponentExtend(BaseSqlTable):
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

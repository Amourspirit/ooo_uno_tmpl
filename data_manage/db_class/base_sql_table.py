# coding: utf-8
from abc import abstractmethod
from .base_sql import BaseSql
from .sql_ctx import SqlCtx

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

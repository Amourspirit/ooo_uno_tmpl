# coding: utf-8
from .base_sql import BaseSql
from .sql_ctx import SqlCtx


class QryFile(BaseSql):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    def get_file_path(self, full_ns: str) -> str:
        """
        Gets a file path from database for a given component namespace

        Args:
            full_ns (str): namespace such as ``com.sun.star.util.MeasureUnit``

        Returns:
            str: File path
        """
        qry = "SELECT component.file FROM component WHERE component.id_component like :namespace LIMIT 1"
        path = ''
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry, {"namespace": full_ns})
            for row in db.cursor:
                path = row['file']
        return path

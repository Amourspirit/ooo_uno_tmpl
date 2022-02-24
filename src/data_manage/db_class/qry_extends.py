# coding: utf-8
from typing import List
from .base_sql import BaseSql
from .sql_ctx import SqlCtx
from ..data_class.extend import Extend


class QryExtends(BaseSql):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    def get_extends(self, full_ns: str) -> List[Extend]:
        qry_str = """SELECT extend.id_extend, extend.namespace as ns, extend.map_name, extend.fk_component_id, module_detail.sort as sort FROM extend
            LEFT JOIN module_detail on extend.namespace = module_detail.id_namespace
            WHERE extend.fk_component_id like :namespace
            ORDER by module_detail.sort;"""
        args = {"namespace": full_ns}
        results = []
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry_str, args)
            for row in db.cursor:
                results.append(Extend(
                    namespace=row['ns'],
                    map_name=row['map_name'],
                    fk_component_id=row['fk_component_id'],
                    id_extend=row['id_extend'],
                    sort=row['sort']
                ))
        return results

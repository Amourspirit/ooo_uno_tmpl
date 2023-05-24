# coding: utf-8
from typing import Dict, List, Optional, Union
from .base_sql import BaseSql
from .sql_ctx import SqlCtx
from ..data_class.component import Component
from ..data_class.component_kind import ComponentKind


class QryComponent(BaseSql):
    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    def get_component(self, full_ns: str, tipe: str | ComponentKind = "") -> Union[Component, None]:
        """
        Gets component instance for a given namespace.

        If the namespace does not start with ``com.sun.star.`` then ``None`` is returned without checking the database.

        Args:
            full_ns (str): full namespace used for match.
            tipe (str, ComponentTypeKind, optional): Type to check for match.

        Returns:
            Union[Component, None]: Component instance if ``full_ns`` is a match; Otherwise, ``None``
        """
        if not full_ns or not full_ns.startswith("com.sun.star."):
            return None

        args = {"namespace": full_ns}
        qry_str = """SELECT component.id_component, component.name, component.namespace as ns,
            component.type, component.version, component.lo_ver, component.file, component.url, component.c_name,
            component.map_name, module_detail.sort as sort
            FROM component
            LEFT JOIN module_detail ON module_detail.id_namespace = component.id_component
            Where component.id_component like :namespace"""
        if tipe:
            qry_str += " and component.type like :type"
            args["type"] = str(tipe)
        qry_str += " Limit 1;"

        result: Component = None
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry_str, args)
            for row in db.cursor:
                result = Component(
                    id_component=row["id_component"],
                    name=row["name"],
                    namespace=row["ns"],
                    type=row["type"],
                    version=row["version"],
                    lo_ver=row["lo_ver"],
                    file=row["file"],
                    url=row["url"],
                    c_name=row["c_name"],
                    map_name=row["map_name"],
                    sort=row["sort"],
                )

        return result

    def get_component_by_map_name(self, map_name: str) -> Union[Component, None]:
        """
        Gets component instance for a given map_name

        Args:
            map_name (str): map_name used for match.

        Returns:
            Union[Component, None]: Component instance if ``map_name`` is a match; Otherwise, ``None``
        """
        qry_str = """SELECT component.id_component, component.name, component.namespace as ns,
            component.type, component.version, component.lo_ver, component.file, component.url, component.c_name,
            component.map_name, module_detail.sort as sort
            FROM component
            LEFT JOIN module_detail ON module_detail.id_namespace = component.id_component
            WHERE component.map_name like :mapped_name
            Limit 1;"""
        args = {"mapped_name": map_name}
        result: Component = None
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry_str, args)
            for row in db.cursor:
                result = Component(
                    id_component=row["id_component"],
                    name=row["name"],
                    namespace=row["ns"],
                    type=row["type"],
                    version=row["version"],
                    lo_ver=row["lo_ver"],
                    file=row["file"],
                    url=row["url"],
                    c_name=row["c_name"],
                    map_name=row["map_name"],
                    sort=row["sort"],
                )

        return result

    def get_components(self, search_str: str) -> List[Component]:
        """
        Gets component instances for a given namespace

        Args:
            search_str (str): search string that can be used with % and _

        Returns:
            List[Component]: Component instances.
        """
        qry_str = """SELECT component.id_component, component.name, component.namespace as ns,
            component.type, component.version, component.lo_ver, component.file, component.url, component.c_name,
            component.map_name, module_detail.sort as sort
            FROM component
            LEFT JOIN module_detail ON module_detail.id_namespace = component.id_component
            Where component.id_component like :namespace
            ORDER By module_detail.sort;"""
        args = {"namespace": search_str}
        results: List[Component] = []
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry_str, args)
            for row in db.cursor:
                results.append(
                    Component(
                        id_component=row["id_component"],
                        name=row["name"],
                        namespace=row["ns"],
                        type=row["type"],
                        version=row["version"],
                        lo_ver=row["lo_ver"],
                        file=row["file"],
                        url=row["url"],
                        c_name=row["c_name"],
                        map_name=row["map_name"],
                        sort=row["sort"],
                    )
                )

        return results

    def get_components_group_by_ns(self, search_str: Optional[str] = None) -> Dict[str, Component]:
        """
        Gets component instances for a given namespace

        Args:
            search_str (str, optional): search string that can be used with % and _

        Returns:
            Dict[str, Component]: Component instances grouped by namespace.
        """
        qry_str = """SELECT component.id_component, component.name, component.namespace as ns,
            component.type, component.version, component.lo_ver, component.file, component.url, component.c_name,
            component.map_name, module_detail.sort as sort
            FROM component
            LEFT JOIN module_detail ON module_detail.id_namespace = component.id_component"""
        if search_str:
            qry_str += " Where component.id_component like :namespace"
        qry_str += " ORDER By component.id_component;"
        args = {"namespace": search_str}
        results: Dict[str, Component] = {}
        with SqlCtx(self.conn_str) as db:
            if search_str:
                db.cursor.execute(qry_str, args)
            else:
                db.cursor.execute(qry_str)
            for row in db.cursor:
                component = Component(
                    id_component=row["id_component"],
                    name=row["name"],
                    namespace=row["ns"],
                    type=row["type"],
                    version=row["version"],
                    lo_ver=row["lo_ver"],
                    file=row["file"],
                    url=row["url"],
                    c_name=row["c_name"],
                    map_name=row["map_name"],
                    sort=row["sort"],
                )
                if not component.namespace in results:
                    results[component.namespace] = []
                results[component.namespace].append(component)
        return results

    def is_type(self, full_ns: str, tipe: str | ComponentKind = "typedef") -> bool:
        """
        Gets if the namespace is a type of the given type.

        If the namespace does not start with ``com.sun.star.`` then ``False`` is returned without checking the database.

        Args:
            namespace (str): Namespace to check such as ``com.sun.star.xsd.Year``.
            tipe (str, ComponentTypeKind, optional): Type to check for match. Defaults to "typedef".

        Returns:
            bool: If the namespace is a type of the given type.
        """
        if not full_ns or not full_ns.startswith("com.sun.star."):
            return False

        query = """SELECT * FROM component
            WHERE component.id_component like :namespace
            and component.type like :type
            LIMIT 1;"""
        result = False
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(query, {"namespace": full_ns, "type": str(tipe)})
            row = db.cursor.fetchone()
            if not row is None:
                result = True
        return result

    def is_type_from_map_name(self, map_name: str, tipe: str | ComponentKind = "typedef") -> bool:
        """
        Gets if the map_name is a type of the given type.

        Args:
            map_name (str): Map name to check such as ``Year_578a07e8``.
            tipe (str, ComponentTypeKind, optional): Type to check for match. Defaults to "typedef".

        Returns:
            bool: If the map_name is a type of the given type.
        """
        query = """SELECT * FROM component
            WHERE component.map_name like :map_name
            and component.type like :type
            LIMIT 1;"""
        result = False
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(query, {"map_name": map_name, "type": str(tipe)})
            row = db.cursor.fetchone()
            if not row is None:
                result = True
        return result

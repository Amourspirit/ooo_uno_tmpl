# coding: utf-8
from typing import List, Tuple, Union
from config import AppConfig
import textwrap
from ..db_class.db_connect import DbConnect
from ..db_class.qry_ns_imports import QryNsImports
from ..data_class.namespace_tree import NamespaceTree
from ..data_class.namespace_child import NamespaceChild
from ..data_class.full_import import FullImport
from ..data_class.component import Component
from ..util import Util
from parser import mod_rel as RelInfo
from tabulate import tabulate
from dataclasses import astuple, asdict, fields

class NamespaceControler:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        """
        Constructor

        Args:
            config (AppConfig): App Config

        Keyword Arguments:
            ns_name (str, optional): Namesapce, get tree data for namesapce.
            ns_flat (str, optional): Namesapce, get flat unique inherits. Other Opt - b_child, b_json
            ns_flat_frm (str, optional): Namesapce, get flat unique inherits in from format. Other Opt - b_child, b_json
            extends_long (str, optional): Namesapce, gets extends in long format. Other Opt - b_child, b_json
            extends_short (str, optional): Namesapce, gets extends in short format. Other Opt - b_child, b_json
            ns_commponent (str, optional): Namespace, get Components that match passed in namesapce.
            ns_import (str, optional): Namespace, get imports.  Other Opt - b_child, b_typing, b_from, b_from_long, b_json
            ns_import_typing_child (str, optional): Namespace, get child imports.  Other Opt - b_from, b_from_long, b_json
            ns_link (str, optional): Namesapce, get url for a given namespace.
            b_child (bool, optional): Determins if returns chiild namespaces. Default True
            b_json (bool, optional): Determsin if result is json str.

        """
        self._conn = DbConnect(config)
        self._ns_name: Union[str, None] = kwargs.get('ns_name', None)
        self._ns_flat: Union[str, None] = kwargs.get('ns_flat', None)
        self._ns_flat_frm: Union[str, None] = kwargs.get('ns_flat_frm', None)
        self._ns_component: Union[str, None] = kwargs.get('ns_commponent', None)

        self._ns_extends_lng: Union[str, None] = kwargs.get(
            'extends_long', None)
        self._ns_extends_short: Union[str, None] = kwargs.get(
            'extends_short', None)
        self._link: Union[str, None] = kwargs.get('ns_link', None)

        self._ns_import: Union[str, None] = kwargs.get('ns_import', None)
        self._ns_import_typing_child: Union[str, None] = kwargs.get(
            'ns_import_typing_child', None)

        self._b_typing: Union[bool, None] = kwargs.get('b_typing', None)
        self._b_child: bool = bool(kwargs.get('b_child', False))
        self._b_from: bool = bool(kwargs.get('b_from', False))
        self._b_from_long: bool = bool(kwargs.get('b_from_long', False))
        self._b_json: bool = bool(kwargs.get('b_json', False))

    def results(self):
        if self._ns_name:
            return self._process_ns_tree()
        elif self._ns_flat:
            return self._get_flat_unique_ns()
        elif self._ns_flat_frm:
            return self._get_flat_frm()
        elif self._ns_extends_lng:
            return self._get_extends(long=True)
        elif self._ns_extends_short:
            return self._get_extends(long=False)
        elif self._link:
            return self._get_link()
        elif self._ns_import:
            if self._b_child:
                return self._get_imports_child()
            return self._get_imports()
        elif self._ns_import_typing_child:
            return self._get_imports_typing_child()
        elif self._ns_component:
            return self._get_componets()

    def _get_componets(self) -> str:
        qry = QryNsImports(self._conn.connection_str)
        lst = qry.get_components(full_ns=self._ns_component)
        def get_format_str() -> str:
            # id_width = max(len(itm.id_component) for itm in lst)
            # headers = ['id_component', 'name', 'namespace',
            #            'type', 'version', 'lo_ver', 'file', 'sort']
            headers = [field.name for field in fields(Component)]
            data = [astuple(itm) for itm in lst]
            
            return tabulate(data, headers=headers, tablefmt='simple')

        def get_format_json() -> str:
            data = [asdict(itm) for itm in lst]
            return Util.get_formated_dict_list_str(data)
        if self._b_json:
            return get_format_json()
        return get_format_str()

    def _process_ns_tree(self) -> str:
        """
        Gets Namespace Tree as str

        Returns:
            str: See Example

        Examle:
            com.sun.star.registry.NestedRegistry
                com.sun.star.lang.XInitialization
                    com.sun.star.uno.XInterface
                com.sun.star.registry.XSimpleRegistry
                    com.sun.star.uno.XInterface
        """
        indent_amt = 4
        qry = QryNsImports(self._conn.connection_str)

        def get_str(nt: NamespaceTree, in_str: str, indent: int) -> str:
            ns_str = in_str
            nt.children.sort()
            for ns_itm in nt.children:
                s = ns_itm.namespace
                s = textwrap.indent(s, ' ' * indent)
                s = '\n' + s
                ns_str += s
                ns_str = get_str(nt=ns_itm, in_str=ns_str,
                                 indent=indent + indent_amt)
            return ns_str

        n_tree = qry.get_ns_tree(namespace=self._ns_name)
        # return None
        # return str(n_tree)
        s_result = get_str(
            nt=n_tree, in_str=n_tree.namespace, indent=indent_amt)
        return s_result

    def _get_flat_unique_ns(self) -> str:
        def get_lines(lst: List[NamespaceChild]) -> List[str]:
            lines_lst = []
            for itm in lst:
                lines_lst.append(itm.namespace)
            return lines_lst
        qry = QryNsImports(self._conn.connection_str)
        flat_full = not self._b_child
        n_flat = qry.get_flat_ns(namespace=self._ns_flat, full=flat_full)
        lines = get_lines(n_flat)
        if self._b_json:
            return Util.get_formated_dict_list_str(lines)
        else:
            return ", ".join(lines)

    def _get_flat_frm(self) -> str:
        def get_lines(lst: List[tuple]) -> List[str]:
            lines_lst = []
            for frm in lst:
                lines_lst.append(f"from {frm[0]} import {frm[1]} as {frm[2]}")
            return lines_lst
        qry = QryNsImports(self._conn.connection_str)
        full = not self._b_child
        froms = qry.get_flat_imports(namespace=self._ns_flat_frm, full=full)
        if self._b_json:
            return Util.get_formated_dict_list_str(froms)
        else:
            lines = get_lines(froms)
            return "\n".join(lines)

    def _get_extends(self, long: bool) -> str:
        qry = QryNsImports(self._conn.connection_str)
        full = not self._b_child
        if long:
            extends = qry.get_extends_long(
                namespace=self._ns_extends_lng, full=full)
        else:
            extends = qry.get_extends_short(
                namespace=self._ns_extends_short, full=full)
        if self._b_json:
            return Util.get_formated_dict_list_str(extends)
        else:
            return ", ".join(extends)

    def _get_link(self) -> str:
        qry = QryNsImports(self._conn.connection_str)
        return qry.get_ns_link(full_ns=self._link)

    def _ns_child_lst_to_lines(self, lst: List[NamespaceChild]) -> str:
        def get_lines() -> List[str]:
            lines_lst = []
            for im in lst:
                lines_lst.append(im.namespace)
            return lines_lst
        lines = get_lines()
        if self._b_json:
            return Util.get_formated_dict_list_str(lines)
        else:
            return "\n".join(lines)

    def _ns_child_lst_to_from(self, lst: List[NamespaceChild], namespace: str) -> str:
        def get_lines() -> List[str]:
            ns = namespace.rsplit(sep='.', maxsplit=1)[0]
            lines_lst = []
            for im in lst:
                rel = RelInfo.get_rel_import(
                    in_str=im.namespace, ns=ns)
                lines_lst.append(f"from {rel[0]} import {rel[1]}")
            return lines_lst

        def get_json() -> str:
            ns = namespace.rsplit(sep='.', maxsplit=1)[0]
            lines_lst = []
            for im in lst:
                rel = RelInfo.get_rel_import(
                    in_str=im.namespace, ns=ns)
                lines_lst.append((rel[0], rel[1]))
            return Util.get_formated_dict_list_str(lines_lst)

        if self._b_json:
            return get_json()
        else:
            lines = get_lines()
            return "\n".join(lines)

    def _ns_child_lst_to_from_long(self, lst: List[NamespaceChild], namespace: str) -> str:
        def get_lines() -> List[str]:
            ns = namespace.rsplit(sep='.', maxsplit=1)[0]
            lines_lst = []
            for im in lst:
                rel = RelInfo.get_rel_import_long(
                    in_str=im.namespace, ns=ns)
                lines_lst.append(f"from {rel[0]} import {rel[1]} as {rel[2]}")
            return lines_lst

        def get_json() -> str:
            ns = namespace.rsplit(sep='.', maxsplit=1)[0]
            lines_lst = []
            for im in lst:
                rel = RelInfo.get_rel_import_long(
                    in_str=im.namespace, ns=ns)
                lines_lst.append((rel[0], rel[1], rel[2]))
            return Util.get_formated_dict_list_str(lines_lst)

        if self._b_json:
            return get_json()
        else:
            lines = get_lines()
            return "\n".join(lines)

    def _get_imports_child(self) -> str:
        qry = QryNsImports(self._conn.connection_str)
        ims = qry.get_imports_child(
            full_ns=self._ns_import)
        if len(ims) == 0:
            if self._b_json:
                return '[]'
            return ''
        if self._b_from:
            if self._b_from_long:
                return self._ns_child_lst_to_from_long(ims, self._ns_import)
            return self._ns_child_lst_to_from(ims, self._ns_import)
        return self._ns_child_lst_to_lines(ims)

    def _get_imports_typing_child(self) -> str:
        qry = QryNsImports(self._conn.connection_str)
        ims = qry.get_imports_child_typing(
            full_ns=self._ns_import_typing_child)
        if len(ims) == 0:
            if self._b_json:
                return '[]'
            return ''
        if self._b_from:
            if self._b_from_long:
                return self._ns_child_lst_to_from_long(ims, self._ns_import_typing_child)
            return self._ns_child_lst_to_from(ims, self._ns_import_typing_child)
        return self._ns_child_lst_to_lines(ims)

    def _get_imports(self) -> str:
        qry = QryNsImports(self._conn.connection_str)

        def get_lines(imports: List[FullImport]) -> List[str]:
            lines_lst = []
            for im in imports:
                lines_lst.append(im.namespace)
            return lines_lst

        def get_full_imports_str(imports: List[FullImport]) -> str:
            lines = get_lines(imports)
            if self._b_json:
                return Util.get_formated_dict_list_str(lines)
            return "\n".join(lines)

        def get_from_imports_short(imports: List[FullImport]) -> str:
            ns = self._ns_import.rsplit(sep='.', maxsplit=1)[0]

            def get_rel_lst() -> List[Tuple[str, str]]:
                rel_lst = []
                for im in imports:
                    rel_lst.append(RelInfo.get_rel_import(
                        in_str=im.namespace, ns=ns))
                return rel_lst
            rels = get_rel_lst()
            if self._b_json:
                return Util.get_formated_dict_list_str(rels)
            frm_lst = []
            for rel in rels:
                frm_lst.append(f"from {rel[0]} import {rel[1]}")
            return "\n".join(frm_lst)

        def get_from_imports_long(imports: List[FullImport]) -> str:
            ns = self._ns_import.rsplit(sep='.', maxsplit=1)[0]

            def get_rel_lst() -> List[Tuple[str, str, str]]:
                rel_lst = []
                for im in imports:
                    rel_lst.append(RelInfo.get_rel_import_long(
                        in_str=im.namespace, ns=ns))
                return rel_lst
            rels = get_rel_lst()
            if self._b_json:
                return Util.get_formated_dict_list_str(rels)
            frm_lst = []
            for rel in rels:
                frm_lst.append(f"from {rel[0]} import {rel[1]} as {rel[2]}")
            return "\n".join(frm_lst)

        ims = qry.get_imports(
            full_ns=self._ns_import, typing=self._b_typing)
        if len(ims) == 0:
            if self._b_json:
                return '[]'
            return ''
        if self._b_from:
            if self._b_from_long:
                return get_from_imports_long(imports=ims)
            return get_from_imports_short(imports=ims)
        return get_full_imports_str(imports=ims)

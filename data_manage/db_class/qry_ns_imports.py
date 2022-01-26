# coding: utf-8
import queue
from typing import List, Set, Tuple, Optional
from .base_sql import BaseSql
from .sql_ctx import SqlCtx
from ..data_class.namespace_tree import NamespaceTree
from ..data_class.namespace_child import NamespaceChild
from ..data_class.full_import import FullImport
from parser import mod_rel as RelInfo

class QryNsImports(BaseSql):
    """Namespace related Query"""

    def __init__(self, connect_str: str) -> None:
        super().__init__(connect_str=connect_str)

    # region    LINK
    def get_ns_link(self, full_ns: str) -> str:
        """
        Gets URL for a namespace

        Args:
            full_ns (str): Full Namespace such as ``com.sun.star.uno.XInterface``

        Returns:
            str: Url link
        """
        qry = """SELECT module_info.url_base || '/' || module_detail.href as link
            FROM module_detail
            JOIN module_info on module_detail.namespace = module_info.id_module_info
            WHERE module_detail.id_namespace like :namespace LIMIT 1;"""
        result = ''
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry, {"namespace": full_ns})
            for row in db.cursor:
                result = row['link']
        return result
    # endregion LINK
    
    # region    Flat/ Flat Related

    # region        Query
    def _get_qry_ns(self) -> str:
        query = """SELECT extend.namespace as ns, module_detail.sort as sort FROM extend
        LEFT JOIN module_detail on module_detail.id_namespace = extend.namespace
        WHERE extend.fk_component_id like :namespace
        ORDER by sort"""
        return query
    # endregion     Queries

    # region        Tree
    def get_ns_tree(self, namespace: str) -> NamespaceTree:
        """
        Gets a tree of namesapce

        Args:
            namespace (str): Input namesapce

        Returns:
            NamespaceTree: Tree Object that contains children.
        
        Example:
            com.sun.star.registry.NestedRegistry
                com.sun.star.lang.XInitialization
                    com.sun.star.uno.XInterface
                com.sun.star.registry.XSimpleRegistry
                    com.sun.star.uno.XInterface
        """
        query = self._get_qry_ns()
        ns_dict = {}

        def is_cache(ns: str) -> bool:
            return ns in ns_dict

        def get_cache(ns: str) -> List[NamespaceTree]:
            return ns_dict[ns]

        def set_cache(ns: str, lst: List[NamespaceTree]) -> None:
            ns_dict[ns] = lst

        def set_tree_children(db: SqlCtx, ns_tree: NamespaceTree):
            """
            Sets children for ``ns_tree``. Children are automatically appended to ``ns_tree``
            
            As children are found they are cached. On subsequent calls if namespace is in cached it is returned.

            Args:
                db (SqlCtx): Database connection
                ns_tree (NamespaceTree): namespace info

            """
            if is_cache(ns_tree.namespace):
                ns_tree.children = [
                    ns_obj for ns_obj in get_cache(ns_tree.namespace)]
                return ns_tree.children
            db.cursor.execute(query, {"namespace": ns_tree.namespace})
            results = []
            for row in db.cursor:
                results.append(NamespaceTree(
                    namespace=row['ns'],
                    sort=row['sort']
                ))
            ns_tree.children = results
            set_cache(ns=ns_tree.namespace, lst=ns_tree.children)
            return ns_tree.children

        def build_tree(db: SqlCtx, tree_obj: NamespaceTree) -> None:
            """
            Recursivly finds all children for ``tree_obj`` and appends them to children.

            Args:
                db (SqlCtx): database connection
                tree_obj (NamespaceTree): namespace info
            """
            que = queue.Queue()

            def recurse(q: queue.Queue) -> None:
                # q contain siblings that have been aded to a parent already
                # now each sibling need to find it children
                sibling_que = queue.Queue()
                while not q.empty():
                    # sibling is not a parent
                    parent: NamespaceTree = q.get()
                    set_tree_children(db=db, ns_tree=parent)
                    for child in parent.children:
                        sibling_que.put(child)
                if not sibling_que.empty():
                    recurse(q=sibling_que)
            set_tree_children(db=db, ns_tree=tree_obj)
            for child in tree_obj.children:
                que.put(child)
            recurse(q=que)

        with SqlCtx(self.conn_str) as db:
            qry_sort = """SELECT module_detail.sort FROM module_detail
            WHERE module_detail.id_namespace like :namespace LIMIT 1;"""
            db.cursor.execute(qry_sort, {"namespace": namespace})
            for row in db.cursor:
                tree = NamespaceTree(
                    namespace=namespace,
                    sort=row['sort'])
                build_tree(db=db, tree_obj=tree)
                result = tree
        return result
    # endregion     Tree

    def get_flat_ns(self, namespace: str, full: bool) -> List[NamespaceChild]:
        """
        Gets direct extends of an object or the extends of 2nd level children.

        Args:
            namespace (str): Names of geit extends of.
            full (bool): If ``True`` gets extends for 1st level inherits;
                Otherwise, Gets extends for 2nd level children.

        Returns:
            List[Tuple[int, str]]: List of tuple containing entries for sort and then namesapce
        
        Notes:
            On second level (``full=False``) results, there is a filter applied that removes duplicate inherits.
            Only a pure list of inherits are returned. For instance XInterface would not be imported more thant onece.
            This is on purpose to remove any potential pythpon MRO issues.
        
            Importing com.sun.star.form.component.RichTextControl as ``full=True`` returns the following namespaces:
                com.sun.star.awt.UnoControlEditModel,
                com.sun.star.form.FormControlModel,
                com.sun.star.text.TextRange
            Importing as ``full=False``:
                com.sun.star.awt.UnoControlModel,
                com.sun.star.beans.XFastPropertySet,
                com.sun.star.beans.XPropertyState,
                com.sun.star.container.XContentEnumerationAccess,
                com.sun.star.form.FormComponent,
                com.sun.star.style.CharacterProperties,
                com.sun.star.style.CharacterPropertiesAsian,
                com.sun.star.style.CharacterPropertiesComplex,
                com.sun.star.style.ParagraphProperties,
                com.sun.star.style.ParagraphPropertiesAsian,
                com.sun.star.style.ParagraphPropertiesComplex,
                com.sun.star.text.XTextRange
            
            Notice that in the model there are a total of 15 child imports. This method returns 12 becuase duplicates
            are merged and/or removed.
            
            See Model `here <https://tinyurl.com/yb3eu5ng>`_
        """
        query = self._get_qry_ns()
        ns_dict = {}

        def is_cache(ns: str) -> bool:
            return ns in ns_dict

        def get_cache(ns: str) -> List[NamespaceChild]:
            return ns_dict[ns]

        def set_cache(ns: str, lst: List[NamespaceChild]) -> None:
            ns_dict[ns] = lst

        def get_ns_children(db: SqlCtx, ns: str) -> List[NamespaceChild]:
            if is_cache(ns):
                return [itm for itm in get_cache(ns)]
            db.cursor.execute(query, {"namespace": ns})
            children = []
            for row in db.cursor:
                children.append(NamespaceChild(
                    namespace=row['ns'],
                    sort=row['sort']
                ))
            set_cache(ns=ns, lst=children)
            return children

        def process_flat(db: SqlCtx, flats: Set[NamespaceChild]) -> List[NamespaceChild]:
            # Lookup each namespaces children, perferably as unique only.
            # remove any child match from main list that is in namespace children.
            #
            # Loop through the list again, ignoring any namespace already processed.
            #
            # Keep in mind that a processed namespace could be removed by a match later down the list.
            # This means the list of done items needs to be checked and if match, removed.
            processed: Set[NamespaceChild] = set()
            flats_set: Set[NamespaceChild] = set(list(flats))

            for flat in flats:
                children = get_ns_children(db=db, ns=flat.namespace)
                for child in children:
                    if child in processed:
                        continue
                    if child in flats_set:
                        flats_set.remove(child)
                    flat_children = get_unique(db=db, ns=child.namespace)
                    for flat_child in flat_children:
                        if flat_child in processed:
                            continue
                        if flat_child in flat_children:
                            if flat_child in flats_set:
                                flats_set.remove(flat_child)
                        processed.add(flat_child)
                    processed.add(child)
            lst = list(flats_set)
            lst.sort()
            return lst

        def get_unique(db: SqlCtx, ns: str) -> Set[NamespaceChild]:
            que = queue.Queue()
            flat_set: Set[NamespaceChild] = set()

            def recurse(q: queue.Queue) -> None:
                # q contain siblings that have been aded to a parent already
                # now each sibling need to find it children
                sibling_que = queue.Queue()
                while not q.empty():
                    # sibling is not a parent
                    parent: NamespaceChild = q.get()
                    children = get_ns_children(db=db, ns=parent.namespace)
                    for child in children:
                        if child in flat_set:
                            continue
                        flat_set.add(child)
                        sibling_que.put(child)
                if not sibling_que.empty():
                    recurse(q=sibling_que)

            root_children = get_ns_children(db=db, ns=ns)
            for root_child in root_children:
                que.put(root_child)
                flat_set.add(root_child)
            recurse(q=que)

            # results = list(flat_set)
            # results.sort()
            return flat_set

        def build_flat(db: SqlCtx, ns: str) -> List[NamespaceChild]:
            flats: Set[NamespaceChild] = set()
            children: List[str] = []
            # getting child namespaces first leaves the direct
            # children out of results. This is perfered.
            db.cursor.execute(query, {"namespace": ns})
            for row in db.cursor:
                children.append(row['ns'])
            for child in children:
                c_flat = get_unique(db=db, ns=child)
                flats.update(c_flat)
            return process_flat(db=db, flats=flats)

        def build_flat_full(db: SqlCtx, ns: str) -> List[NamespaceChild]:
            flats: Set[NamespaceChild] = get_unique(db=db, ns=ns)
            return process_flat(db=db, flats=flats)

        with SqlCtx(self.conn_str) as db:
            if full:
                result = build_flat_full(db=db, ns=namespace)
            else:
                result = build_flat(db=db, ns=namespace)
        return result

    def get_ns_from_full(self, full_ns: str) -> str:
        """
        Gets full namespace from a full namespace

        Args:
            full_ns (str): Full namespace such as ``com.sun.star.uno.XInterface``

        Returns:
            str: namespace such as ``com.sun.star.uno``
        """
        qry = """SELECT module_detail.namespace as ns FROM module_detail
            WHERE module_detail.id_namespace like :namespace LIMIT 1;"""
        result = ''
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry, {"namespace": full_ns})
            for row in db.cursor:
                result = row['ns']
        return result

    

    def get_flat_imports(self, namespace: str, full: bool) -> List[Tuple[str, str, str]]:
        # if importing from children. The children imports need to be relative this namespace
        flats: List[NamespaceChild] = self.get_flat_ns(
            namespace=namespace, full=full)
        ns = self.get_ns_from_full(full_ns=namespace)
        results = []
        for flat in flats:
            from_, cls_, lng = RelInfo.get_rel_import_long(
                in_str=flat.namespace, ns=ns)
            results.append((from_, cls_, lng))
        return results

    def get_extends_long(self, namespace: str, full: bool) -> List[str]:
        flats = self.get_flat_ns(namespace=namespace, full=full)

        ns = self.get_ns_from_full(full_ns=namespace)
        results = []
        for flat in flats:
            lng = RelInfo.get_rel_import_long_name(
                in_str=flat.namespace, ns=ns)
            results.append(lng)
        return results

    def get_extends_short(self, namespace: str, full: bool) -> List[str]:
        flats = self.get_flat_ns(namespace=namespace, full=full)

        ns = self.get_ns_from_full(full_ns=namespace)
        results = []
        for flat in flats:
            lng = RelInfo.get_rel_import_short_name(
                in_str=flat.namespace, ns=ns)
            results.append(lng)
        return results
    # endregion Flat/ Flat Related

    # region IMPORTS
    # region    Query
    def _get_imports_qry(self, typing: bool) -> str:
        """
        Gets Query string for querying full_import Table

        Args:
            typing (bool): If True then requires_typing parameter is included in query string

        Returns:
            str: query string
        """
        qry = """SELECT full_import.id_full_import, full_import.namespace as ns, full_import.requires_typing as requires_typing, module_detail.sort as sort
            FROM full_import
            LEFT JOIN module_detail on module_detail.id_namespace = full_import.namespace
            WHERE full_import.fk_component_id like :namespace"""
        if typing is True:
            qry += ' AND full_import.requires_typing = :requires_typing'
        qry += ';'
        return qry

    def _get_imports_children_qry(self, typing: bool) -> str:
        """
        Gets Query string for querying full_import Table for all 2nd level import from given namesapce

        Args:
            typing (bool): If True then requires_typing parameter is included in query string

        Returns:
            str: query string
        """
        qry = """SELECT DISTINCT full_import.namespace as ns, full_import.requires_typing as requires_typing, module_detail.sort as sort
            FROM full_import
            LEFT JOIN module_detail on module_detail.id_namespace = full_import.namespace
            WHERE full_import.fk_component_id in (SELECT full_import.namespace FROM full_import
                WHERE full_import.fk_component_id like :namespace)"""
        if typing is True:
            qry += ' AND full_import.requires_typing = :requires_typing'
        qry += ' ORDER by sort;'
        return qry
    # endregion Query

    def _get_imports(self, full_ns: str, children: bool, typing: Optional[bool] = None) -> List[FullImport]:
        """
        Gets imports for a given namespace.

        Args:
            full_ns (str): Namespace to get imports for
            children (bool): If True then 2nd level childre are imported; Otherwise 1st level.
            typing (Optional[bool], optional): If ``True`` only imports that requre typing are returned.
                If ``False`` only imports that do not requrine typing are retruned.
                If None all imports for ``full_ns`` are returned. Defaults to ``None``.

        Returns:
            List[FullImport]: Import Information
        """
        args = {"namespace": full_ns}
        if typing is None:
            if children:
                qry_str = self._get_imports_children_qry(False)
            else:
                qry_str = self._get_imports_qry(False)
        else:
            if children:
                qry_str = self._get_imports_children_qry(True)
            else:
                qry_str = self._get_imports_qry(True)
            args['requires_typing'] = 1 if typing is True else 0
        results = []
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry_str, args)
            for row in db.cursor:
                namesapce: str = row['ns']
                id_full_import: int = -1 if children else row['id_full_import']
                requires_typing: bool = bool(row['requires_typing'])
                sort_ = int(row['sort'])
                results.append(FullImport(
                    namespace=namesapce,
                    requires_typing=requires_typing,
                    fk_component_id=full_ns,
                    sort=sort_,
                    id_full_import=id_full_import
                ))
        results.sort()
        return results

    def get_imports(self, full_ns: str, typing: Optional[bool] = None) -> List[FullImport]:
        """
        Gets imports for a given namespace.

        Args:
            full_ns (str): Namespace to get imports for
            typing (Optional[bool], optional): If ``True`` only imports that requre typing are returned.
                If ``False`` only imports that do not requrine typing are retruned.
                If None all imports for ``full_ns`` are returned. Defaults to ``None``.

        Returns:
            List[FullImport]: Import Information
        """
        return self._get_imports(full_ns=full_ns, children=False, typing=typing)

    def get_imports_child(self, full_ns: str) -> List[NamespaceChild]:
        flats = self.get_flat_ns(namespace=full_ns, full=False)
        flats.sort()
        return flats

    def get_imports_child_typing(self, full_ns: str) -> List[NamespaceChild]:
        qry_str = """SELECT DISTINCT full_import.namespace as ns, module_detail.sort
            FROM full_import
            left JOIN module_detail on full_import.namespace = module_detail.id_namespace
            WHERE full_import.requires_typing
            AND full_import.fk_component_id in (SELECT DISTINCT full_import.namespace FROM full_import
            WHERE full_import.fk_component_id like :namespace)
            ORDER by sort"""
        results = []
        with SqlCtx(self.conn_str) as db:
            db.cursor.execute(qry_str, {"namespace": full_ns})
            for row in db.cursor:
                namesapce: str = row['ns']
                sort_ = int(row['sort'])
                results.append(NamespaceChild(
                    namespace=namesapce,
                    sort=sort_,
                ))
        return results
    # endregion IMPORTS

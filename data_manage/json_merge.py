# coding: utf-8
"""
Manages merging of component json files
"""
import os
import json
from pathlib import Path
from typing import List, Set
from config import AppConfig
from parser import mod_rel as RelInfo
from . import db_manager as db

# NOTE:
#   When origin json data has been overwritten this class will not work properly becuase
#   it will read json data from a modifiled json file. Therefore data is not valid to run
#   this class on.
#
# class purpose:
#
#   merge data that is dropped when a components inherits is flattened
# * read current inherits
# * read flattened child inherits.
# * drop any 1st level inherits that are in 2nd level inherits
# * from 1st level get all from_typing imports that are not in 2nd level
# * drop all 1st level import are for extends


class JsonMerge:
    def __init__(self, config: AppConfig, full_ns: str) -> None:
        self._config = config
        self._namespace = full_ns
        project_root = os.environ.get('project_root', None)
        if project_root is None:
            raise Exception("project_root environment variable not set")
        self._project_root = Path(project_root)
        ns_parts = full_ns.rsplit(sep='.', maxsplit=1)
        self._namespace = ns_parts[0]
        self._c_name = ns_parts[1]
        self._origin_extends: Set[str] = self._get_original_extends()
        self._files: List[str] = self._get_files()

    def _get_original_extends(self) -> Set[str]:
        qry_ext = db.QryExtends(self._conn.connection_str)
        exts = qry_ext.get_extends(self._namespace)
        return set([e.namespace for e in exts])

    def _get_child_extends(self) -> Set[str]:
        qry = db.QryNsImports(self._conn.connection_str)
        n_flat = qry.get_flat_ns(namespace=self._namespace, full=False)
        ext = set()
        for ns in n_flat:
            ext.add(ns.namespace)
        return ext

    def _get_file_json(self, file: str) -> dict:
        file_path = self._project_root / self._config.uno_obj_dir / file

        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def _get_files(self) -> List[str]:
        qry_f = db.QryFile(self._conn.connection_str)
        files = []
        for ns in self._origin_extends:
            files.append(qry_f.get_file_path(ns))
        return files

    def _get_orig_json(self) -> dict:
        qry_f = db.QryFile(self._conn.connection_str)
        file_name = qry_f.get_file_path(self._namespace)
        return self._get_file_json(file_name)

    def _process_extends(self, j_orig: dict) -> None:
        namespace = j_orig['namesapce']
        extends = list(self._get_child_extends())
        extends_map = {}
        for ex in extends:
            ln = RelInfo.get_rel_import_long_name(
                in_str=ex, ns=namespace
            )
            extends_map[ex] = ln
        j_orig['data']['extends'] = extends
        j_orig['data']['extends_map'] = extends_map

    def _process_from_imports(self, j_data: dict, j_orig: dict) -> None:
        namespace = j_orig['namesapce']
        imp_gen: List[str] = j_data['full_imports']['general']
        full_imports = []
        for im in imp_gen:
            full_imports.append(RelInfo.get_rel_import_long(
                in_str=im, ns=namespace
            ))
        j_orig['data']['from_imports'] = full_imports

    def _process_from_imports_typing(self, j_data: dict, j_orig: dict) -> None:
        namespace = j_orig['namesapce']
        imp_gen: List[str] = j_data['full_imports']['typing']
        full_imports = []
        for im in imp_gen:
            full_imports.append(RelInfo.get_rel_import_long(
                in_str=im, ns=namespace
            ))
        j_orig['data']['from_imports_typing'] = full_imports

    def get_merged(self) -> dict:
        j_orig = self._get_orig_json()
        j_data = self._get_merged_data()
        j_orig['data']['allow_db'] = j_data['allow_db']
        j_orig['data']['requires_typing'] = j_data['requires_typing']
        j_orig['data']['quote'] = j_data['quote']
        j_orig['data']['typings'] = j_data['typings']
        j_orig['data']['imports'] = j_data['imports']
        j_orig['data']['items'] = j_data['items']
        self._process_extends(j_orig=j_orig)
        self._process_from_imports(j_data=j_data, j_orig=j_orig)
        self._process_from_imports_typing(j_data=j_data, j_orig=j_orig)
        return j_orig

    def _get_merged_data(self) -> dict:
        requires_typing = False

        result_data = {
            "allow_db": False,
            "quote": [],
            "typings": [],
            "requires_typing": False,
            "full_imports": {
                "general": [],
                "typing": []
            },
            "imports": [],
            "items": {},
            "component_namespace": []
        }

        # region SETS
        quotes = set()
        typings = set()
        from_imports_typing = set()
        full_imp_general = set()
        full_imp_typing = set()
        itm_methods = set()
        itm_types = set()
        itm_properties = set()
        component_namesapces = set()
        # endregion SETS

        # region process Methods
        def process_quote_data(data: dict) -> None:
            lst = data.get('quote', [])
            quotes.update(lst)

        def process_typings_data(data: dict) -> None:
            lst = data.get('typings', [])
            typings.update(lst)

        def process_full_imp_gen_data(data: dict) -> None:
            lst = data['full_imports'].get('general', [])
            full_imp_general.update(lst)

        def process_full_imp_typing_data(data: dict) -> None:
            lst = data['full_imports'].get('typing', [])
            full_imp_typing.update(lst)

        def process_itm_methods(data: dict) -> None:
            lst = data['items'].get('methods', [])
            is_init = False
            for d in lst:
                name = d['name']
                if name in itm_methods:
                    continue
                itm_methods.add(name)

                if not is_init:
                    is_init = True
                    if not 'methods' in result_data['items']:
                        result_data['items']['methods'] = []
                result_data['items']['methods'].append(d)

        def process_itm_types(data: dict) -> None:
            lst = data['items'].get('types', [])
            is_init = False
            for d in lst:
                name = d['name']
                if name in itm_types:
                    continue
                itm_types.add(name)

                if not is_init:
                    is_init = True
                    if not 'types' in result_data['items']:
                        result_data['items']['types'] = []
                result_data['items']['types'].append(d)

        def process_itm_properties(data: dict) -> None:
            lst = data['items'].get('types', [])
            is_init = False
            for d in lst:
                name = d['name']
                if name in itm_properties:
                    continue
                itm_properties.add(name)

                if not is_init:
                    is_init = True
                    if not 'properties' in result_data['items']:
                        result_data['items']['properties'] = []
                result_data['items']['properties'].append(d)

        def process_requires_typing(data: dict) -> None:
            nonlocal requires_typing
            req = bool(data.get('requires_typing', False))
            if req:
                requires_typing = True

        # endregion process Methods

        for file in self._files:
            j_data_dict = self._get_file_json(file)
            namespace = j_data_dict['namespace']
            name = j_data_dict['name']
            full_ns = namespace + '.' + name

            # ignore any child imports that are also an original extend
            # if full_ns in self._origin_extends:
            #     continue
            component_namesapces.add(full_ns)
            j_data: dict = j_data_dict['data']
            process_quote_data(j_data)
            process_typings_data(j_data)
            process_full_imp_gen_data(j_data)
            process_full_imp_typing_data(j_data)
            process_itm_methods(j_data)
            process_requires_typing(j_data)
            process_itm_types(j_data)
            process_itm_properties(j_data)

        if len(component_namesapces) > 0:
            result_data['component_namespace'].extends(component_namesapces)

        if len(quotes) > 0:
            result_data['quote'].extend(quotes)

        if len(typings) > 0:
            result_data['typings'].extend(quotes)

        if len(full_imp_general) > 0:
            result_data['full_imports']['general'].extend(full_imp_general)

        if len(full_imp_typing) > 0:
            result_data['full_imports']['typing'].extend(full_imp_typing)

        if len(from_imports_typing) > 0:
            for ns in from_imports_typing:
                # from_imports_typing
                result_data['from_imports_typing'].append(
                    RelInfo.get_rel_import_long(
                        in_str=ns,
                        ns=self._namespace
                    ))
        result_data['requires_typing'] = requires_typing

        return result_data

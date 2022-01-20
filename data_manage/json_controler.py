# coding: utf-8
import os
import json
from pathlib import Path
from typing import Any, Dict, List, Union
from config import AppConfig
from . import db_manager as db
from .json_merge import JsonMerge
# from ..parser import xsrc
# from ..parser import service
from parser import mod_rel as RelInfo

class JsonController:
    def __init__(self, config: AppConfig, **kwargs) -> None:
        self._config = config
        self._namespace: Union[str, None] = kwargs.get('namespace', None)
        project_root = os.environ.get('project_root', None)
        if project_root is None:
            raise Exception("project_root environment variable not set")
        self._project_root = Path(project_root)
        self._conn = db.DbConnect(config)
        self._db_qry_file = db.QryFile(self._conn.connection_str)
        self._root_file = self._db_qry_file.get_file_path(full_ns=self._namespace)

    def results(self) -> Any:
        if self._namespace:
            return db.Util.get_formated_dict_list_str(self._get_data())

    def _get_file_json(self, file: str) -> dict:
        file_path = self._project_root.joinpath(file)

        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def _get_ns_data(self) -> dict:
        return self._get_file_json(self._root_file)


    def _get_files(self) -> List[str]:
        qry_ns = db.QryNsImports(self._conn.connection_str)
        ns_lst = qry_ns.get_flat_ns(self._namespace, False)
        files = []
        for ns in ns_lst:
            files.append(self._db_qry_file.get_file_path(ns.namespace))
        return files

    def _get_data(self) -> dict:
        files = self._get_files()
        j_merge = JsonMerge(config=self._config,
                            files=files, full_ns=self._namespace)
        merged_data = j_merge.get_merged_data()
        data = self._get_ns_data()
        data['data']['name'] = merged_data['name']
        data['data']['namespace'] = merged_data['namespace']
        data['data']['allow_db'] = merged_data['allow_db']
        data['data']['quote'] = merged_data['quote']
        data['data']['typings'] = merged_data['typings']
        data['data']['requires_typing'] = merged_data['requires_typing']
        data['data']['full_imports'] = merged_data['full_imports']
        data['data']['from_imports_typing'] = merged_data['from_imports_typing']
        data['data']['from_imports'] = merged_data['from_imports']
        data['data']['imports'] = merged_data['imports']
        data['data']['items'] = merged_data['items']
        data['data']['extends'] = self._get_extends()
        data['data']['extends_map'] = self._get_extends_map(data['data']['extends'])
        data['data']['from_imports'] = self._get_from_imports()
        return data

    def _get_from_imports(self) -> List[List[str]]:
        nc = db.NamespaceControler(
            config=self._config,
            ns_flat_frm=self._namespace,
            b_json=True,
            b_child=False,
        )
        return json.loads(nc.results())

    def _get_extends(self) -> List[str]:
        nc = db.NamespaceControler(
            config=self._config,
            ns_flat=self._namespace,
            b_json=True,
            b_child=False
        )
        return json.loads(nc.results())

    def _get_extends_map(self, extends: List[str]) -> Dict[str, str]:
        e_map = {}
        for ex in extends:
            name = RelInfo.get_rel_import_long_name(
                in_str=ex,
                ns=self._namespace
            )
            e_map[ex] = name
        return e_map

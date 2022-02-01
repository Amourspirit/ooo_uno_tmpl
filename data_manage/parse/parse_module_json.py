# coding: utf-8
import verr
import json
import glob
from pathlib import Path
from typing import List, Dict
from config import AppConfig
from ..data_class.extend import Extend
from ..data_class.component import Component
from ..data_class.full_import import FullImport
from ..db_class.tbl_component import TblComponent
from ..db_class.tbl_component_extend import TblComponentExtend
from ..db_class.tbl_component_full_import import TblComponentFullImport
from ..db_class.db_connect import DbConnect
from rel import mod_rel as RelInfo

class ParseModuleJson:
    def __init__(self, config: AppConfig) -> None:
        self._app_config = config
        self._components: List[Component] = []
        self._extends: List[Extend] = []
        self._full_imports: List[FullImport] = []
        self._min_ver = verr.Version.parse(config.min_json_data_ver)
        self._valid_types = tuple(self._app_config.component_types)
        conn = DbConnect(self._app_config)
        self._db_cnn = conn.connection_str
        self._root_dir = conn.root_dir
        self._component_tbl = TblComponent(connect_str=self._db_cnn)
        self._extend_tbl = TblComponentExtend(connect_str=self._db_cnn)
        self._full_import_tbl = TblComponentFullImport(
            connect_str=self._db_cnn)
        self._json_data_dir: Path = self._root_dir.joinpath(
            self._app_config.data_dir)

    def get_module_json_files(self) -> List[str]:
        def filter_fn(name) -> bool:
            p_name = Path(name).name
            if p_name == self._app_config.module_links_file:
                return False
            return True
        dirname = str(self._json_data_dir)
        pattern = dirname + '/**/*.json'
        all_files = glob.glob(pattern, recursive=True)
        files = filter(filter_fn, all_files)
        return files

    def _write_all(self) -> None:
        self._components.clear()
        m_files = self.get_module_json_files()
        for j_file in m_files:
            with open(j_file, 'r') as file:
                j_data = json.load(file)
            self._validite_json(file=file, data=j_data)
            self._read(json_data=j_data, file=j_file)

        self._component_tbl.insert(data=self._components)
        self._extend_tbl.insert(data=self._extends)
        self._full_import_tbl.insert(data=self._full_imports)

    def update_all_details(self) -> None:
        self._write_all()

    def _read(self, json_data: dict, file: str) -> None:
        self._read_main(json_data=json_data, file=file)

    def _read_main(self, json_data: dict, file: str) -> None:
        rel = Path(file).relative_to(self._json_data_dir)
        ns = json_data['namespace']
        name = json_data['name']
        c = Component(
            id_component=f"{ns}.{name}",
            name=name,
            namespace=ns,
            type=json_data['type'],
            version=json_data['version'],
            lo_ver=json_data['libre_office_ver'],
            file=str(rel),
            c_name=RelInfo.camel_to_snake(name)
        )
        self._read_extends(json_data=json_data, comp=c)
        self._read_full_imports(json_data=json_data, comp=c)
        self._components.append(c)

    def _read_extends(self, json_data: dict, comp: Component) -> None:
        j_extends: List[str] = json_data['data'].get('extends', [])
        j_extends_map: Dict[str, str] = json_data['data'].get(
            'extends_map', {})
        for ext in j_extends:
            map_name = j_extends_map.get(ext, None)
            self._extends.append(
                Extend(namespace=ext, map_name=map_name, fk_component_id=comp.id_component))

    def _read_full_imports(self, json_data: dict, comp: Component) -> None:
        j_imports: Dict[List[str]] = json_data['data'].get('full_imports', {})
        gen_lst: List[str] = j_imports.get('general', [])
        type_lst: List[str] = j_imports.get('typing', [])
        for ns in gen_lst:
            self._full_imports.append(FullImport(
                namespace=ns,
                requires_typing=False,
                fk_component_id=comp.id_component
            ))
        for ns in type_lst:
            self._full_imports.append(FullImport(
                namespace=ns,
                requires_typing=True,
                fk_component_id=comp.id_component
            ))

    # region Validation

    def _validite_json(self, file: str, data: dict):
        msg = f"{self.__class__.__name__}._validite_json() "

        key = 'id'
        if not key in data:
            _msg = f"{msg} Json missing id field. File: {file}"
            raise Exception(_msg)
        if data[key] != 'uno-ooo-parser':
            _msg = f"{msg} Json data bad id field. Expected: uno-ooo-parser, got: {data[key]}. File: {file}"
            raise Exception(_msg)
        key = 'type'
        if not key in data:
            _msg = f"{msg} Json missing type field. File: {file}"
            raise Exception(_msg)
        if not data[key] in self._valid_types:
            _msg = f"{msg} Json data bad id field. Expected: one of {self._valid_types}, got: {data[key]}. File: {file}"
            raise Exception(_msg)
        key = 'version'
        if not key in data:
            _msg = f"{msg} Json missing version field. File: {file}"
            raise Exception(_msg)
        json_ver = verr.Version.parse(data[key])
        if json_ver < self._min_ver:
            _msg = f"{msg} Version fail Expect a min version of '{self._min_ver}', got '{json_ver}'. File: {file}"
            raise Exception(_msg)
        key = 'data'
        if not key in data:
            _msg = f"{msg} Json missing data field. File: {file}"
            raise Exception(_msg)
        if not isinstance(data[key], dict):
            _msg = f"{msg} Json data field is not a dictionary. File: {file}"
            raise Exception(_msg)
    # endregion Validation

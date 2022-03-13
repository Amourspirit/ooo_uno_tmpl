# coding: utf-8
from typing import List
from ...cfg.config import AppConfig
from ..data_class.extend import Extend
from ..data_class.component import Component
from ..data_class.full_import import FullImport
from ..db_class.tbl_component import TblComponent
from ..db_class.tbl_component_extend import TblComponentExtend
from ..db_class.tbl_component_full_import import TblComponentFullImport
from ..db_class.db_connect import DbConnect


class DbModuleJson:
    def __init__(self, config: AppConfig) -> None:
        self._app_config = config
        self._components: List[Component] = []
        self._extends: List[Extend] = []
        self._full_imports: List[FullImport] = []
        conn = DbConnect(self._app_config)
        self._db_cnn = conn.connection_str
        self._component_tbl = TblComponent(connect_str=self._db_cnn)
        self._extend_tbl = TblComponentExtend(connect_str=self._db_cnn)
        self._full_import_tbl = TblComponentFullImport(
            connect_str=self._db_cnn)


    def update_all(self) -> None:
        self._write_all()

    def _write_all(self) -> None:
        self._component_tbl.insert(data=self._components)
        self._extend_tbl.insert(data=self._extends)
        self._full_import_tbl.insert(data=self._full_imports)

    # region Properties
    @property
    def components(self) -> List[Component]:
        return self._components
    
    @property
    def extends(self) -> List[Extend]:
        return self._extends
    
    @property
    def full_imports(self) -> List[FullImport]:
        return self._full_imports
    # endregion Properties
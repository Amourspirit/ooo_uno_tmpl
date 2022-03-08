# coding: utf-8
import hashlib
from .parser_base import ParserBase
from .db_module_json import DbModuleJson
from ..data_class.full_import import FullImport
from ..data_class.component import Component
from ..data_class.extend import Extend
from ...model.service.model_service import ModelService

class ParseService(ParserBase):

    def __init__(self, db: DbModuleJson, json_data: dict, component: Component) -> None:
        super().__init__(db=db, component=component)
        self._model = ModelService(**json_data)
    
    def _read_full_imports(self) -> None:
        for ns in self._model.data.full_imports.general:
            id_ = self.get_id(ns)
            self.db.full_imports.append(FullImport(
                id_full_import=id_,
                namespace=ns,
                requires_typing=False,
                fk_component_id=self.component.id_component
            ))
        for ns in self._model.data.full_imports.typing:
            id_ = self.get_id(ns)
            self.db.full_imports.append(FullImport(
                id_full_import=id_,
                namespace=ns,
                requires_typing=False,
                fk_component_id=self.component.id_component
            ))

    def _read_extends(self) -> None:
        for ext in self._model.data.extends:
            map_name = self._model.data.extends_map.get(ext, None)
            key = self.component.id_component + ext
            id_ = hashlib.md5(key.encode('utf-8')).hexdigest()
            self.db.extends.append(
                Extend(id_extend=id_, namespace=ext, map_name=map_name, fk_component_id=self.component.id_component))
            
    def update(self) -> None:
        self._read_full_imports()
        self._read_extends()
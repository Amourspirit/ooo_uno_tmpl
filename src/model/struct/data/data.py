# coding: utf-8
from typing import List, Dict
from ...shared.data.shared_data import BaseData
from ...shared.data.from_import import FromImport
from .data_item import DataItem

class Data(BaseData):
    quote: List[str]
    typings: List[str]
    from_imports: List[FromImport]
    from_imports_typing: List[FromImport]
    extends_map: Dict[str, str]
    extends: List[str]
    quote: List[str]
    imports: List[str]
    desc: List[str]
    typings: List[str]
    requires_typing: bool
    items: List[DataItem]
    
    @property
    def fullname(self) -> str:
        return self.namespace + "." + self.name

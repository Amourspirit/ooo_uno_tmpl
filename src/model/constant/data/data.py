# coding: utf-8
from typing import List
from ...shared.data.shared_data import BaseData
from ...shared.data.from_import import FromImport
from .items.data_item import DataItem


class Data(BaseData):
    flags: bool
    allow_db: bool
    quote: List[str]
    typings: List[str]
    requires_typing: bool
    from_imports: List[FromImport]
    from_imports_typing: List[FromImport]
    items: List[DataItem]

    @property
    def fullname(self) -> str:
        return self.namespace + "." + self.name

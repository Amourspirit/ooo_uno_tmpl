# coding: utf-8
from typing import List
from .items.data_items import DataItems
from ...shared.data.shared_data import BaseData
from ...shared.data.full_imports import FullImports
from ...shared.data.from_import import FromImport


class Data(BaseData):
    from_imports: List[FromImport]
    from_imports_typing: List[FromImport]
    extends_map: dict
    quote: List[str]
    typings: List[str]
    requires_typing: bool
    full_imports: FullImports
    imports: List[str]
    extends: List[str]
    items: DataItems

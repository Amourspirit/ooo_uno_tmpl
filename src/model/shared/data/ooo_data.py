# coding: utf-8
from typing import List, Dict
from .items.data_items import DataItems
from .shared_data import BaseData
from .full_imports import FullImports
from .from_import import FromImport


class Data(BaseData):
    from_imports: List[FromImport]
    from_imports_typing: List[FromImport]
    extends_map: Dict[str, str]
    quote: List[str]
    typings: List[str]
    requires_typing: bool
    full_imports: FullImports
    imports: List[str]
    extends: List[str]
    items: DataItems

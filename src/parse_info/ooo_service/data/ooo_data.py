# coding: utf-8
from typing import Tuple
from .items.data_items import DataItems
from ...shared.data.shared_data import DataBase
from ...shared.data.from_imports import FromImports
from ...shared.data.full_imports import FullImports

class Data(DataBase):
    from_imports: FromImports
    from_imports_typing: FromImports
    extends_map: dict
    quote: Tuple[str]
    requires_typing: bool
    full_imports: FullImports
    imports: Tuple[str]
    extends: Tuple[str]
    items: DataItems

# coding: utf-8
from typing import List
from ..shared.data.shared_data import BaseData
from ..shared.data.from_import import FromImport

class Data(BaseData):
    allow_db: bool
    type: str
    requires_typing: bool
    from_imports: List[FromImport]
    imports: List[str]
    quote: List[str]
    typings: List[str]

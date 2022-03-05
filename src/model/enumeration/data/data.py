# coding: utf-8
from typing import List, Union
from ...shared.data.shared_data import BaseData, validator
from .items.data_item import DataItem
from ...shared.data import validators

class Data(BaseData):
    allow_db: bool
    quote: List[str]
    typings: List[str]
    desc: Union[List[str], str]
    url: str
    items: List[DataItem]
    _str_null_empty = validator('url', allow_reuse=True)(validators.str_null_empty)
    
    @property
    def fullname(self) -> str:
        return self.namespace + "." + self.name

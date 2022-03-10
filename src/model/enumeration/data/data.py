# coding: utf-8
from typing import List, Union
from ...shared.data.shared_data import BaseData
from .items.data_item import DataItem

class Data(BaseData):
    allow_db: bool
    quote: List[str]
    typings: List[str]
    desc: Union[List[str], str]
    items: List[DataItem]
    
    @property
    def fullname(self) -> str:
        return self.namespace + "." + self.name

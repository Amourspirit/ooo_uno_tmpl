# coding: utf-8
from typing import List
from pydantic import BaseModel
from .link_item import LinkItem
from .link_data_class import LinkDataClass


class LinkData(BaseModel):
    modules: List[LinkItem]
    enums: List[LinkItem]
    constants: List[LinkItem]
    typedef: List[LinkItem]
    classes: LinkDataClass

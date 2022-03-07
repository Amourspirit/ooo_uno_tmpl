# coding: utf-8
from typing import List, Optional
from .link_item import LinkItem
from pydantic import BaseModel


class LinkDataClass(BaseModel):
    service: Optional[List[LinkItem]]
    struct: Optional[List[LinkItem]]
    exception: Optional[List[LinkItem]]
    interface: Optional[List[LinkItem]]

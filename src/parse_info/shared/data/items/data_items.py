# coding: utf-8
from typing import List, Optional
from pydantic import BaseModel
from ..methods.method import Method
from ..properties.prop import Prop

class DataItems(BaseModel):
    methods: Optional[List[Method]]
    properties: Optional[List[Prop]]

# coding: utf-8
from typing import List, Optional
from pydantic import BaseModel
from ..methods.method import Method
from ..properties.prop import Prop
from ..types.types import Tipe

class DataItems(BaseModel):
    methods: Optional[List[Method]]
    properties: Optional[List[Prop]]
    types: Optional[List[Tipe]]

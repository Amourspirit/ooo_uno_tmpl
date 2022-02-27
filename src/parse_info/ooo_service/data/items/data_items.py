# coding: utf-8
from typing import List, Optional
from pydantic import BaseModel
from ....shared.data.methods.method import Method
from ....shared.data.properties.prop import Prop

class DataItems(BaseModel):
    methods: Optional[List[Method]]
    properties: Optional[List[Prop]]

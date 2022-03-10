# coding: utf-8
from typing import List
from pydantic import BaseModel, validator
from ....shared.data import validators

class DataItem(BaseModel):
    # fields are populated in the order they're defined in the class
    name: str
    value: str
    desc: List[str]
    _str_null_empty = validator('name','value', allow_reuse=True)(validators.str_null_empty)
# coding: utf-8
from typing import List
from pydantic import BaseModel, validator
from ..shared.data import validators
from ..shared.ooo_class import OooClass

class BaseData(BaseModel):
    name: str
    namespace: str
    url: str

    _str_null_empty = validator('name','url', allow_reuse=True)(validators.str_null_empty)
    _namespace_validate = validator('namespace', allow_reuse=True)(
        validators.namespace)
    
    @property
    def full_name(self) -> str:
        return self.namespace + '.' + self.name

class OooDataClass(OooClass):
    data: BaseData

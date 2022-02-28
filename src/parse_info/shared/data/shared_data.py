# coding: utf-8
from typing import List
from pydantic import BaseModel, validator
from . import validators


class BaseData(BaseModel):
    name: str
    namespace: str
    allow_db: bool
    url: str
    desc: List[str]
    _str_null_empty = validator('name','url', allow_reuse=True)(validators.str_null_empty)
    _namespace_validate = validator('namespace', allow_reuse=True)(
        validators.namespace)

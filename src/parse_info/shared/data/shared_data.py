# coding: utf-8
from typing import List
import pydantic
from pydantic import BaseModel

class DataBase(BaseModel):
    name: str
    namespace: str
    allow_db: bool
    url: str
    desc: List[str]

    @pydantic.validator('name')
    def validate_name(cls, value: str) -> str:
        s = value.strip()
        if len(s) > 0:
            return s
        raise ValueError(
            f"root/data/name must not be null or empty string")

    @pydantic.validator('namespace')
    def validate_namespace(cls, value: str) -> str:
        if value.startswith('com.sun.star.'):
            return value
        raise ValueError(
            f"root/data/namespace must start with 'com.sun.star.'. Current value: {value}")

# coding: utf-8
from typing import List, Optional
import pydantic
from pydantic import BaseModel

class Tipe(BaseModel):
    name: str
    returns: str
    origtype: Optional[str]
    desc: List[str]
    raises_get: Optional[str]
    raises_set: Optional[str]

    @pydantic.validator('name', 'returns')
    def validate_str_len(cls, value: str) -> str:
        s = value.strip()
        if len(s) > 0:
            return s
        raise ValueError("must not be null or empty string")


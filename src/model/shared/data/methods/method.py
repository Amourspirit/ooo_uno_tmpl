# coding: utf-8
from pydantic import BaseModel
import pydantic
from typing import List, Optional
# from .raises import MethodRaises
from .method_arg import MethodArg


class Method(BaseModel):
    name: str
    returns: str
    returns_origin: Optional[str]
    desc: List[str]
    args: List[MethodArg]
    # raises: List[MethodRaises]
    raises: List[str]

    @pydantic.validator('name')
    def validate_method_name(cls, value: str) -> str:
        s = value.strip()
        if len(s) > 0:
            return s
        raise ValueError(
            f"root/data/item/method/name must not be null or empty string")

    @pydantic.validator('returns')
    def validate_returns(cls, value: str) -> str:
        s = value.strip()
        if len(s) > 0:
            return s
        raise ValueError(
            f"root/data/item/method/returns must not be null or empty string")

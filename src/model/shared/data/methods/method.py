# coding: utf-8
from typing import List
import pydantic
from pydantic import BaseModel
from enum import Enum
from .raises import MethodRaises
from pydantic.fields import Field, PrivateAttr
from dataclasses import dataclass
# from dataclasses import dataclass


class ArgDirection(str, Enum):
    IN = "in"
    OUT = "out"

    def __str__(self) -> str:
        return self.value

@dataclass
class MethodArg:
    name: str
    type: str
    direction: ArgDirection


class Method(BaseModel):
    name: str
    returns: str
    desc: List[str]
    args: List[MethodArg]
    raises: List[MethodRaises]
   
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

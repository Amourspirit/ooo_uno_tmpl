# coding: utf-8
from typing import List
import pydantic
from pydantic import BaseModel

class Prop(BaseModel):
    name: str
    returns: str
    desc: List[str]

    # @pydantic.validator('name')
    # def validate_namespace(cls, value: str) -> str:
    #     s = value.strip()
    #     if len(s) > 0:
    #         return s
    #     raise ValueError(
    #         f"root/data/item/method/name must not be null or empty string")

    # @pydantic.validator('returns')
    # def validate_namespace(cls, value: str) -> str:
    #     s = value.strip()
    #     if len(s) > 0:
    #         return s
    #     raise ValueError(
    #         f"root/data/item/method/returns must not be null or empty string")

# coding: utf-8
from typing import Union, List
from pydantic import BaseModel, Field, validator
from .....parser.enumerations.value_type import ValTypeEnum


class DataItem(BaseModel):
    # fields are populated in the order they're defined in the class
    name: str
    type: str
    value_type: Union[str, ValTypeEnum]
    value: Union[str, int, float]
    desc: List[str] = Field(alias='lines')
    
    @validator('value_type')
    def validate_id(cls, v: str) -> ValTypeEnum:
        try:
            v_t = ValTypeEnum(v)
            return v_t
        except:
            raise
# values, **kwargs

    @validator('value')
    def validate_value(cls, v: str, values, **kwargs):
        e: ValTypeEnum = values['value_type']
        if e == ValTypeEnum.INTEGER:
            return int(v)
        if e == ValTypeEnum.FLOAT:
            return float(v)
        return v

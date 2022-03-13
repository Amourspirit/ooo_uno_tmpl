# coding: utf-8
import verr
from pydantic import BaseModel, validator
from .ooo_type import OooType
from .data import validators

class OooClass(BaseModel):
    id: str
    version: str
    libre_office_ver: str
    name: str
    namespace: str
    type: OooType
    _str_null_empty = validator('name', allow_reuse=True)(
        validators.str_null_empty)
    _namespace_valid = validator('namespace', allow_reuse=True)(
        validators.namespace)

    @validator('id')
    def validate_id(cls, value: str) -> str:
        if value == 'uno-ooo-parser':
            return value
        raise ValueError(
            f"root/id/ must be 'uno-ooo-parser'. Current value: {value}")


    @validator('version')
    def validate_version(cls, value: str) -> str:
        v_result = verr.Version.try_parse(value)
        if v_result[0] == False:
            raise ValueError(f"root/version has a bad format: {value}")
        else:
            cls.ver = v_result[1]
        return value

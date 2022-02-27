# coding: utf-8
import verr
import pydantic
from pydantic import BaseModel
from .ooo_type import OooType

class OooClass(BaseModel):
    id: str
    version: str
    libre_office_ver: str
    name: str
    namespace: str
    type: OooType

    @pydantic.validator('id')
    def validate_id(cls, value: str) -> str:
        if value == 'uno-ooo-parser':
            return value
        raise ValueError(
            f"root/id/ must be 'uno-ooo-parser'. Current value: {value}")

    @pydantic.validator('name')
    def validate_name(cls, value: str) -> str:
        s = value.strip()
        if len(s) > 0:
            return s
        raise ValueError(
            f"root/name must not be null or empty string")

    @pydantic.validator('namespace')
    def validate_namespace(cls, value: str) -> str:
        if value.startswith('com.sun.star.'):
            return value
        raise ValueError(
            f"root/namespace must start with 'com.sun.star.'. Current value: {value}")

    @pydantic.validator('version')
    def validate_version(cls, value: str) -> str:
        v_result = verr.Version.try_parse(value)
        if v_result[0] == False:
            raise ValueError(f"root/version has a bad format: {value}")
        else:
            cls.ver = v_result[1]
        return value

# coding: utf-8
import verr
from pydantic import BaseModel, validator
from .link_data import LinkData
from ..shared.ooo_type import OooType

class ModelModuleLinks(BaseModel):
    id: str
    name: str
    namespace: str
    version: str
    libre_office_ver: str
    type: OooType
    url_base: str
    data: LinkData
    
    @validator('id')
    def validate_id(cls, value: str) -> str:
        if value == 'uno-ooo-parser':
            return value
        raise ValueError(
            f"root/id/ must be 'uno-ooo-parser'. Current value: {value}")
    
    @validator('type')
    def validate_type(cls, value: str) -> str:
        if value == 'module_links':
            return value
        raise ValueError(
            f"root/module_links/ must be 'module_links'. Current value: {value}")

    @validator('version')
    def validate_version(cls, value: str) -> str:
        v_result = verr.Version.try_parse(value)
        if v_result[0] == False:
            raise ValueError(f"root/version has a bad format: {value}")
        else:
            cls.ver = v_result[1]
        return value

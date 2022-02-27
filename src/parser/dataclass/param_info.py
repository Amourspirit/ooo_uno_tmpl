# coding: utf-8
from dataclasses import dataclass
from ..mod_type import PythonType
from typing import Optional


@dataclass
class ParamInfo:
    direction: str = ''
    name: str = ''
    type: str = ''
    p_type: Optional[PythonType] = None

    def __lt__(self, other: object):
        if not isinstance(other, ParamInfo):
            return NotImplemented
        return self.name < other.name

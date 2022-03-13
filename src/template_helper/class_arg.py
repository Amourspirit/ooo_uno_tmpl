# coding: utf-8
from dataclasses import dataclass
from typing import Union
from ..parser.mod_type import PythonType

@dataclass
class ClassArg:
    name: str
    type: str
    default: str
    p_type: Union[PythonType, None]

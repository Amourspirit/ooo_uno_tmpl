# coding: utf-8
from dataclasses import dataclass
from typing import Union
from ..data_manage.data_class.component import Component

@dataclass
class ClassArg:
    name: str
    type: str
    default: str
    component: Union[Component, None]
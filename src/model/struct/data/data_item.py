# coding: utf-8
from dataclasses import dataclass
from typing import Union, List

@dataclass
class DataItem:
    name: str
    type: str
    desc: List[str]
    origtype: Union[str, None]

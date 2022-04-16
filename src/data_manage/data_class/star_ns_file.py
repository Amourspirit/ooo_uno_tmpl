# coding: utf-8
from dataclasses import dataclass
from typing import List
from .component import Component


@dataclass
class StarNsFile:
    file_name: str
    component: Component
    lines: List[str]
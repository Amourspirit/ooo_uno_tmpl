# coding: utf-8
from dataclasses import dataclass
from typing import Optional


@dataclass
class NameInfo:
    name: str
    "Name to use in code gen"
    orig_name: str
    """Origin name found from html"""
    # extra_data: Optional[object] = None
    # """Extra data that can be set in rules or otherwise"""

    def __lt__(self, other: object):
        if not isinstance(other, NameInfo):
            return NotImplemented
        return self.name < other.name
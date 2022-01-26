# coding: utf-8
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Component:
    id_component: str
    name: str
    namespace: str
    type: str
    version: str
    lo_ver: str
    file: str
    sort: int = -1

    def __lt__(self, other: object):
        if not isinstance(other, Component):
            return NotImplemented
        return self.sort < other.sort

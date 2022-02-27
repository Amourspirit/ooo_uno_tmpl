# coding: utf-8
from dataclasses import dataclass
from .ns import Ns


@dataclass(frozen=True)
class Area:
    name: str
    ns: Ns
    href: str
    x1: int
    y1: int
    x2: int
    y2: int
    title: str = ''

    def __lt__(self, other: object):
        if not isinstance(other, Area):
            return NotImplemented
        return self.name < other.name

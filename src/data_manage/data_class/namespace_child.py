# coding: utf-8
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class NamespaceChild:
    namespace: str
    sort: int = -1

    def __lt__(self, other: object):
        if not isinstance(other, NamespaceChild):
            return NotImplemented
        return self.sort < other.sort

# coding: utf-8
from dataclasses import dataclass, field
from typing import List

@dataclass
class NamespaceTree:
    namespace: str
    sort: int = -1
    children: 'List[NamespaceTree]' = field(default_factory=list)

    def __lt__(self, other: object):
        if not isinstance(other, NamespaceTree):
            return NotImplemented
        return self.sort < other.sort
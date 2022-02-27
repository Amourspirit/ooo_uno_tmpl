# coding: utf-8
from dataclasses import dataclass


@dataclass(frozen=True)
class Ns:
    name: str
    namespace: str
    python_import: bool = False

    @property
    def fullns(self):
        if self.python_import:
            return self.name
        return self.namespace + '.' + self.name

    def __lt__(self, other: object):
        if not isinstance(other, Ns):
            return NotImplemented
        return self.fullns < other.fullns

# coding: utf-8
from dataclasses import dataclass
from typing import Union

@dataclass(frozen=True, eq=True)
class FullImport:
    namespace: str
    requires_typing: bool
    fk_component_id: str
    id_full_import: Union[int, None] = None
    sort: int = -1

    def __lt__(self, other: object):
        if not isinstance(other, FullImport):
            return NotImplemented
        return self.sort < other.sort

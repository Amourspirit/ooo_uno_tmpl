# coding: utf-8
from dataclasses import dataclass
from typing import Union

@dataclass(frozen=True, eq=True)
class Extend:
    namespace: str
    map_name: Union[str, None]
    fk_component_id: str
    id_extend: Union[str, None] = None
    sort: int = -1

    def __lt__(self, other: object):
        if not isinstance(other, Extend):
            return NotImplemented
        return self.sort < other.sort

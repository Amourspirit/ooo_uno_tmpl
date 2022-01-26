# coding: utf-8
from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True, eq=True)
class ExtendsMap:
    name: str
    fk_extends_id: int
    id_extends_map: Union[int, None] = None

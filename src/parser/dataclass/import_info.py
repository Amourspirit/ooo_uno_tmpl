# coding: utf-8
from dataclasses import dataclass, field
from typing import Set


@dataclass
class ImportInfo:
    requires_typing: bool = False
    imports: Set[str] = field(default_factory=set)

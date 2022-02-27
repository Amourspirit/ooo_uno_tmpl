# coding: utf-8
from dataclasses import dataclass
from typing import Optional
from .shape import Shape

@dataclass
class AreaInfo:
    is_inherited: bool
    shape: Optional[Shape] = None

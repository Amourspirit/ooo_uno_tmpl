# coding: utf-8
from typing import Tuple
from pydantic.dataclasses import dataclass


@dataclass
class FullImports:
    general: Tuple[str]
    typing: Tuple[str]

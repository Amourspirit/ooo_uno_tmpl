# coding: utf-8
from typing import List
from dataclasses import dataclass


@dataclass
class FullImports:
    general: List[str]
    typing: List[str]

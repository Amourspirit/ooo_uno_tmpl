# coding: utf-8
from dataclasses import dataclass


@dataclass
class ClassArg:
    name: str
    type: str
    default: str
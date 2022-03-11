# coding: utf-8
from dataclasses import dataclass
from enum import Enum


class ArgDirection(str, Enum):
    IN = "in"
    OUT = "out"

    def __str__(self) -> str:
        return self.value


@dataclass
class MethodArg:
    name: str
    type: str
    direction: ArgDirection
    origin: str

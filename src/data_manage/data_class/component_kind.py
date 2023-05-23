from __future__ import annotations
from enum import Enum


class ComponentKind(str, Enum):
    CONST = "const"
    ENUM = "enum"
    EXCEPTION = "exception"
    INTERFACE = "interface"
    SINGLETON = "singleton"
    SERVICE = "service"
    STRUCT = "struct"
    TYPEDEF = "typedef"

    def __str__(self) -> str:
        return self.value

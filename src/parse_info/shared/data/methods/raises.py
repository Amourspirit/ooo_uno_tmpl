# coding: utf-8
from dataclasses import dataclass


@dataclass
class MethodRaises:
    """
    Represents an import statment in the form of:
    {long}: ``{short}``
    """
    long: str
    """from portion"""
    short: str
    """import portion"""

    def __str__(self) -> str:
        return f"{self.long}: ``{self.short}``"

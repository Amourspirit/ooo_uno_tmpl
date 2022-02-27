# coding: utf-8
from typing import Optional
# from pydantic.dataclasses import dataclass
from dataclasses import dataclass


@dataclass
class MethodRaises:
    """
    Represents an import statment in the form of:
    {long}: ``{short}``
    """
    long: Optional[str] = None
    """from portion"""
    short: Optional[str] = None
    """import portion"""

    def __str__(self) -> str:
        return f"{self.long}: ``{self.short}``"
    
    def is_valid(self):
        if self.long is None:
            return False
        return True

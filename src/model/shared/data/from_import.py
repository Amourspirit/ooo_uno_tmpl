# coding: utf-8
from typing import Union
from dataclasses import dataclass

# see also: https://stackoverflow.com/questions/64026038/convert-to-pydantic-model-from-tuple


@dataclass
class FromImport:
    """
    Represents an import statment in the form of
    from {frm} import {imp} as {az}
    """
    frm: str
    """from portion"""
    imp: str
    """import portion"""
    az: Union[str, None] = None
    """as portion"""

    def __str__(self) -> str:
        if isinstance(self.az, str):
            return f"from {self.frm} import {self.imp} as {self.az}"
        return f"from {self.frm} import {self.imp}"

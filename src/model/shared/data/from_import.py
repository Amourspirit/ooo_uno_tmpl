# coding: utf-8
from typing import Union, Tuple
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

    def as_tuple(self) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        Converts FromImport into tuple

        If az has a value then a tuple of <frm, imp, az> is returned.
        Otherwise a tuple of <frm, imp> is returned.

        Returns:
            tuple: Tuple of two or three string.
        """
        if isinstance(self.az, str):
            return (self.frm, self.imp, self.az)
        return (self.frm, self.imp)
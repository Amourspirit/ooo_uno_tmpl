# coding: utf-8
from enum import IntEnum, auto
from ...utilities.enum_util import enum_class_new_flex


class ValTypeEnum(IntEnum):
    # see: https://tinyurl.com/yc67tywv
    STRING = auto()
    INTEGER = auto()
    FLOAT = auto()
    CONST = auto()
    """Const is a another value in the same constant class"""
    CONST_PLUS_INT = auto()
    """Const is a another value in the same constant class with a + int value"""
    CONST_MINUS_INT = auto()
    """Const is a another value in the same constant class with a - int value"""
    IMPORT = auto()
    """Value is a import"""

    def __str__(self) -> str:
        return self._name_


setattr(ValTypeEnum, '__new__', enum_class_new_flex)

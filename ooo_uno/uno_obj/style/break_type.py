# coding: utf-8
# this is a auto generated file generated by Cheetah
from typing import TYPE_CHECKING
from enum import Enum
from ...oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ...helper.enum_helper import uno_enum_class_new
    from com.sun.star.style.BreakType import (
        NONE, COLUMN_BEFORE, COLUMN_AFTER, COLUMN_BOTH, PAGE_BEFORE, PAGE_AFTER, PAGE_BOTH, )


class BreakType(Enum):
    """
    values specify the horizontal alignment of an object within a container object.

    See Also:
        `API BreakType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925>`_
    """
    NONE = 'NONE'
    """
    No column or page break is applied.
    """
    COLUMN_BEFORE = 'COLUMN_BEFORE'
    """
    A column break is applied before the object to which it belongs.
    """
    COLUMN_AFTER = 'COLUMN_AFTER'
    """
    A column break is applied after the object to which it belongs.
    """
    COLUMN_BOTH = 'COLUMN_BOTH'
    """
    A column break is applied before and after the object to which it belongs.
    """
    PAGE_BEFORE = 'PAGE_BEFORE'
    """
    A page break is applied before the object to which it belongs.
    """
    PAGE_AFTER = 'PAGE_AFTER'
    """
    A page break is applied after the object to which it belongs.
    """
    PAGE_BOTH = 'PAGE_BOTH'
    """
    A page break is applied before and after the object to which it belongs.
    """


def _dynamic_enum():
    # Dynamically create class that actuall contains UNO enum instances

    global BreakType

    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "NONE": NONE,
            "COLUMN_BEFORE": COLUMN_BEFORE,
            "COLUMN_AFTER": COLUMN_AFTER,
            "COLUMN_BOTH": COLUMN_BOTH,
            "PAGE_BEFORE": PAGE_BEFORE,
            "PAGE_AFTER": PAGE_AFTER,
            "PAGE_BOTH": PAGE_BOTH,
        }
        BreakType = type('BreakType', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(BreakType, k, v)


if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['BreakType']
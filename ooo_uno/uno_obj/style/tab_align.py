# coding: utf-8
# this is a auto generated file generated by Cheetah
import os
from typing import TYPE_CHECKING
from enum import Enum
from ...oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ...helper.enum_helper import uno_enum_class_new
    from com.sun.star.style.TabAlign import (LEFT, CENTER, RIGHT, DECIMAL, )


class TabAlign(Enum):
    """
    These enumeration values are used to specify the alignment of the text range delimited by a tabulator.

    See Also:
        `API TabAlign <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#a806c06853615662029f86b19111fe0a2>`_
    """
    LEFT = 'LEFT'
    """
    set the horizontal alignment to the left margin from the container object
    """
    CENTER = 'CENTER'
    """
    set the horizontal alignment to the center between the margins from the container object
    """
    RIGHT = 'RIGHT'
    """
    set the horizontal alignment to the right margin from the container object
    """
    DECIMAL = 'DECIMAL'
    """
    The decimal point of the text range to the left of this tabulator is aligned to the position of this tabulator.
    """


def _dynamic_enum():
    # Dynamically create class that actually contains UNO enum instances

    global TabAlign
    ignore = os.environ.get('ooouno_ignore_runtime', 'False')
    if ignore == 'True':
        return
    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "LEFT": LEFT,
            "CENTER": CENTER,
            "RIGHT": RIGHT,
            "DECIMAL": DECIMAL,
        }
        TabAlign = type('TabAlign', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(TabAlign, k, v)


if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['TabAlign']
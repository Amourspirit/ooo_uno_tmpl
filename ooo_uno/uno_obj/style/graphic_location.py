# coding: utf-8
# this is a auto generated file generated by Cheetah
from typing import TYPE_CHECKING
from enum import Enum
from ...oenv import UNO_ENVIRONMENT
if (not TYPE_CHECKING) and UNO_ENVIRONMENT:
    from ...helper.enum_helper import uno_enum_class_new
    from com.sun.star.style.GraphicLocation import (
        NONE, LEFT_TOP, MIDDLE_TOP, RIGHT_TOP, LEFT_MIDDLE, MIDDLE_MIDDLE, RIGHT_MIDDLE, LEFT_BOTTOM, MIDDLE_BOTTOM, RIGHT_BOTTOM, AREA, TILED, )


class GraphicLocation(Enum):
    """
    These enumeration values are used to specify the location of a graphic object within its surroundings.

    See Also:
        `API GraphicLocation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#ae71ca73feb713866e85597329dfaec2e>`_
    """
    NONE = 'NONE'
    """
    No column or page break is applied. This value specifies that a location is not yet assigned.
    """
    LEFT_TOP = 'LEFT_TOP'
    """
    The graphic is located in the top left corner.
    """
    MIDDLE_TOP = 'MIDDLE_TOP'
    """
    The graphic is located in the middle of the top edge.
    """
    RIGHT_TOP = 'RIGHT_TOP'
    """
    The graphic is located in the top right corner.
    """
    LEFT_MIDDLE = 'LEFT_MIDDLE'
    """
    The graphic is located in the middle of the left edge.
    """
    MIDDLE_MIDDLE = 'MIDDLE_MIDDLE'
    """
    The graphic is located at the center of the surrounding object.
    """
    RIGHT_MIDDLE = 'RIGHT_MIDDLE'
    """
    The graphic is located in the middle of the right edge.
    """
    LEFT_BOTTOM = 'LEFT_BOTTOM'
    """
    The graphic is located in the bottom left corner.
    """
    MIDDLE_BOTTOM = 'MIDDLE_BOTTOM'
    """
    The graphic is located in the middle of the bottom edge.
    """
    RIGHT_BOTTOM = 'RIGHT_BOTTOM'
    """
    The graphic is located in the bottom right corner.
    """
    AREA = 'AREA'
    """
    The graphic is scaled to fill the whole surrounding area.
    """
    TILED = 'TILED'
    """
    The graphic is repeatedly spread over the surrounding object like tiles.
    """


def _dynamic_enum():
    # Dynamically create class that actuall contains UNO enum instances

    global GraphicLocation

    # if statment is to stop VS Code from reporting errors
    if (not TYPE_CHECKING) and UNO_ENVIRONMENT:

        _dict = {
            "NONE": NONE,
            "LEFT_TOP": LEFT_TOP,
            "MIDDLE_TOP": MIDDLE_TOP,
            "RIGHT_TOP": RIGHT_TOP,
            "LEFT_MIDDLE": LEFT_MIDDLE,
            "MIDDLE_MIDDLE": MIDDLE_MIDDLE,
            "RIGHT_MIDDLE": RIGHT_MIDDLE,
            "LEFT_BOTTOM": LEFT_BOTTOM,
            "MIDDLE_BOTTOM": MIDDLE_BOTTOM,
            "RIGHT_BOTTOM": RIGHT_BOTTOM,
            "AREA": AREA,
            "TILED": TILED,
        }
        GraphicLocation = type('GraphicLocation', (object,), {
            '__doc__': 'class created dynamically. Class loosly mimics Enum',
            "__new__": uno_enum_class_new
        })
        for k, v in _dict.items():
            setattr(GraphicLocation, k, v)


if UNO_ENVIRONMENT:
    _dynamic_enum()

__all__ = ['GraphicLocation']

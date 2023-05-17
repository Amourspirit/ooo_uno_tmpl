# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.drawing.BitmapMode import NO_REPEAT as BITMAP_MODE_NO_REPEAT
    from com.sun.star.drawing.BitmapMode import REPEAT as BITMAP_MODE_REPEAT
    from com.sun.star.drawing.BitmapMode import STRETCH as BITMAP_MODE_STRETCH

    class BitmapMode(uno.Enum):
        """
        Enum Class


        See Also:
            `API BitmapMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#ad26489b8cfc631a6aa6a1a59fd2e2356>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.drawing.BitmapMode', value)

        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.BitmapMode'
        __ooo_type_name__: str = 'enum'

        NO_REPEAT = cast("BitmapMode", BITMAP_MODE_NO_REPEAT)
        """
        the bitmap is painted in its original or selected size.
        """
        REPEAT = cast("BitmapMode", BITMAP_MODE_REPEAT)
        """
        the bitmap is repeated over the fill area.
        """
        STRETCH = cast("BitmapMode", BITMAP_MODE_STRETCH)
        """
        the bitmap is stretched to fill the area.
        
        The text is stretched so that the longest line goes from the left to the right edge of the shape.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class BitmapMode(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.BitmapMode", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.BitmapMode`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['BitmapMode']

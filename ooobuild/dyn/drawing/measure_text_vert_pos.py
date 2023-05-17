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
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.drawing.MeasureTextVertPos import AUTO as MEASURE_TEXT_VERT_POS_AUTO
    from com.sun.star.drawing.MeasureTextVertPos import BREAKEDLINE as MEASURE_TEXT_VERT_POS_BREAKEDLINE
    from com.sun.star.drawing.MeasureTextVertPos import CENTERED as MEASURE_TEXT_VERT_POS_CENTERED
    from com.sun.star.drawing.MeasureTextVertPos import EAST as MEASURE_TEXT_VERT_POS_EAST
    from com.sun.star.drawing.MeasureTextVertPos import WEST as MEASURE_TEXT_VERT_POS_WEST

    class MeasureTextVertPos(uno.Enum):
        """
        Enum Class


        See Also:
            `API MeasureTextVertPos <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#afb97f6590316423181878e8f5f79f087>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.drawing.MeasureTextVertPos', value)

        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.MeasureTextVertPos'
        __ooo_type_name__: str = 'enum'

        AUTO: MeasureTextVertPos = MEASURE_TEXT_VERT_POS_AUTO
        """
        the connection point is chosen automatically,
        
        Set this to have the application select the best horizontal position for the text.
        """
        BREAKEDLINE: MeasureTextVertPos = MEASURE_TEXT_VERT_POS_BREAKEDLINE
        """
        """
        CENTERED: MeasureTextVertPos = MEASURE_TEXT_VERT_POS_CENTERED
        """
        The text is positioned at the center.
        
        The text is positioned over the main line.
        """
        EAST: MeasureTextVertPos = MEASURE_TEXT_VERT_POS_EAST
        """
        """
        WEST: MeasureTextVertPos = MEASURE_TEXT_VERT_POS_WEST
        """
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class MeasureTextVertPos(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.MeasureTextVertPos", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.MeasureTextVertPos`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['MeasureTextVertPos']

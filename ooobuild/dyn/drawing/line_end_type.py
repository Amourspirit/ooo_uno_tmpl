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
import uno
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoEnumMeta
    class LineEndType(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.LineEndType", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.LineEndType`` Enum. Class loosly mimics Enum"""
        pass
else:
    from com.sun.star.drawing.LineEndType import ARROW as LINE_END_TYPE_ARROW
    from com.sun.star.drawing.LineEndType import CIRCLE as LINE_END_TYPE_CIRCLE
    from com.sun.star.drawing.LineEndType import NONE as LINE_END_TYPE_NONE
    from com.sun.star.drawing.LineEndType import SPECIAL as LINE_END_TYPE_SPECIAL
    from com.sun.star.drawing.LineEndType import SQUARE as LINE_END_TYPE_SQUARE


    class LineEndType(uno.Enum):
        """
        Enum Class


        See Also:
            `API LineEndType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#aa4142382acc18a0dd48cc4a563e2d168>`_
        """
        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.LineEndType'
        __ooo_type_name__: str = 'enum'

        @property
        def typeName(self) -> str:
            return 'com.sun.star.drawing.LineEndType'

        ARROW = LINE_END_TYPE_ARROW
        """
        the line uses an arrow for the line end.
        """
        CIRCLE = LINE_END_TYPE_CIRCLE
        """
        the line uses a circle for the line end.
        """
        NONE = LINE_END_TYPE_NONE
        """
        the area is not filled.
        
        The text size is only defined by the font properties.
        
        Don't animate this text.
        
        the line is hidden.
        
        the joint between lines will not be connected
        
        the line has no special end.
        """
        SPECIAL = LINE_END_TYPE_SPECIAL
        """
        not implemented, yet.
        
        deprecated
        """
        SQUARE = LINE_END_TYPE_SQUARE
        """
        the line will get a half square as additional cap
        
        the line uses a square for the line end.
        """

__all__ = ['LineEndType']


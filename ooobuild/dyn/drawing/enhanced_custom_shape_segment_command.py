# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class EnhancedCustomShapeSegmentCommand(metaclass=UnoConstMeta, type_name="com.sun.star.drawing.EnhancedCustomShapeSegmentCommand", name_space="com.sun.star.drawing"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.drawing.EnhancedCustomShapeSegmentCommand``"""
        pass

    class EnhancedCustomShapeSegmentCommandEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.drawing.EnhancedCustomShapeSegmentCommand", name_space="com.sun.star.drawing"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.drawing.EnhancedCustomShapeSegmentCommand`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.drawing import EnhancedCustomShapeSegmentCommand as EnhancedCustomShapeSegmentCommand
    else:
        # keep document generators happy
        from ...lo.drawing.enhanced_custom_shape_segment_command import EnhancedCustomShapeSegmentCommand as EnhancedCustomShapeSegmentCommand

    class EnhancedCustomShapeSegmentCommandEnum(IntEnum):
        """
        Enum of Const Class EnhancedCustomShapeSegmentCommand

        """
        UNKNOWN = EnhancedCustomShapeSegmentCommand.UNKNOWN
        MOVETO = EnhancedCustomShapeSegmentCommand.MOVETO
        LINETO = EnhancedCustomShapeSegmentCommand.LINETO
        CURVETO = EnhancedCustomShapeSegmentCommand.CURVETO
        CLOSESUBPATH = EnhancedCustomShapeSegmentCommand.CLOSESUBPATH
        ENDSUBPATH = EnhancedCustomShapeSegmentCommand.ENDSUBPATH
        NOFILL = EnhancedCustomShapeSegmentCommand.NOFILL
        NOSTROKE = EnhancedCustomShapeSegmentCommand.NOSTROKE
        ANGLEELLIPSETO = EnhancedCustomShapeSegmentCommand.ANGLEELLIPSETO
        ANGLEELLIPSE = EnhancedCustomShapeSegmentCommand.ANGLEELLIPSE
        ARCTO = EnhancedCustomShapeSegmentCommand.ARCTO
        ARC = EnhancedCustomShapeSegmentCommand.ARC
        CLOCKWISEARCTO = EnhancedCustomShapeSegmentCommand.CLOCKWISEARCTO
        CLOCKWISEARC = EnhancedCustomShapeSegmentCommand.CLOCKWISEARC
        ELLIPTICALQUADRANTX = EnhancedCustomShapeSegmentCommand.ELLIPTICALQUADRANTX
        ELLIPTICALQUADRANTY = EnhancedCustomShapeSegmentCommand.ELLIPTICALQUADRANTY
        QUADRATICCURVETO = EnhancedCustomShapeSegmentCommand.QUADRATICCURVETO
        ARCANGLETO = EnhancedCustomShapeSegmentCommand.ARCANGLETO
        DARKEN = EnhancedCustomShapeSegmentCommand.DARKEN
        """
        darken fill color
        """
        DARKENLESS = EnhancedCustomShapeSegmentCommand.DARKENLESS
        """
        darken fill color less
        """
        LIGHTEN = EnhancedCustomShapeSegmentCommand.LIGHTEN
        """
        lighten fill color
        """
        LIGHTENLESS = EnhancedCustomShapeSegmentCommand.LIGHTENLESS
        """
        lighten fill color less
        """

__all__ = ['EnhancedCustomShapeSegmentCommand', 'EnhancedCustomShapeSegmentCommandEnum']

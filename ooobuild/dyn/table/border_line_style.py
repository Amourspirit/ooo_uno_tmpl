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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.table
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class BorderLineStyle(metaclass=UnoConstMeta, type_name="com.sun.star.table.BorderLineStyle", name_space="com.sun.star.table"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.table.BorderLineStyle``"""
        pass

    class BorderLineStyleEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.table.BorderLineStyle", name_space="com.sun.star.table"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.table.BorderLineStyle`` as Enum values"""
        pass

else:
    from com.sun.star.table import BorderLineStyle as BorderLineStyle

    class BorderLineStyleEnum(IntEnum):
        """
        Enum of Const Class BorderLineStyle

        """
        NONE = BorderLineStyle.NONE
        """
        No border line.
        """
        SOLID = BorderLineStyle.SOLID
        """
        Solid border line.
        """
        DOTTED = BorderLineStyle.DOTTED
        """
        Dotted border line.
        """
        DASHED = BorderLineStyle.DASHED
        """
        Dashed border line.
        """
        DOUBLE = BorderLineStyle.DOUBLE
        """
        Double border line.
        
        Widths of the lines and the gap are all equal, and vary equally with the total width.
        """
        THINTHICK_SMALLGAP = BorderLineStyle.THINTHICK_SMALLGAP
        """
        Double border line with a thin line outside and a thick line inside separated by a small gap.
        """
        THINTHICK_MEDIUMGAP = BorderLineStyle.THINTHICK_MEDIUMGAP
        """
        Double border line with a thin line outside and a thick line inside separated by a medium gap.
        """
        THINTHICK_LARGEGAP = BorderLineStyle.THINTHICK_LARGEGAP
        """
        Double border line with a thin line outside and a thick line inside separated by a large gap.
        """
        THICKTHIN_SMALLGAP = BorderLineStyle.THICKTHIN_SMALLGAP
        """
        Double border line with a thick line outside and a thin line inside separated by a small gap.
        """
        THICKTHIN_MEDIUMGAP = BorderLineStyle.THICKTHIN_MEDIUMGAP
        """
        Double border line with a thick line outside and a thin line inside separated by a medium gap.
        """
        THICKTHIN_LARGEGAP = BorderLineStyle.THICKTHIN_LARGEGAP
        """
        Double border line with a thick line outside and a thin line inside separated by a large gap.
        """
        EMBOSSED = BorderLineStyle.EMBOSSED
        """
        3D embossed border line.
        """
        ENGRAVED = BorderLineStyle.ENGRAVED
        """
        3D engraved border line.
        """
        OUTSET = BorderLineStyle.OUTSET
        """
        Outset border line.
        """
        INSET = BorderLineStyle.INSET
        """
        Inset border line.
        """
        FINE_DASHED = BorderLineStyle.FINE_DASHED
        """
        Finely dashed border line.
        """
        DOUBLE_THIN = BorderLineStyle.DOUBLE_THIN
        """
        Double border line consisting of two fixed thin lines separated by a variable gap.
        """
        DASH_DOT = BorderLineStyle.DASH_DOT
        """
        Line consisting of a repetition of one dash and one dot.
        """
        DASH_DOT_DOT = BorderLineStyle.DASH_DOT_DOT
        """
        Line consisting of a repetition of one dash and 2 dots.
        """
        BORDER_LINE_STYLE_MAX = BorderLineStyle.BORDER_LINE_STYLE_MAX
        """
        Maximum valid border line style value.
        """

__all__ = ['BorderLineStyle', 'BorderLineStyleEnum']

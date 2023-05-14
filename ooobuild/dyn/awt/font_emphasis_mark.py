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
# Namespace: com.sun.star.awt
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FontEmphasisMark(metaclass=UnoConstMeta, type_name="com.sun.star.awt.FontEmphasisMark", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.FontEmphasisMark``"""
        pass

    class FontEmphasisMarkEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.FontEmphasisMark", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.FontEmphasisMark`` as Enum values"""
        pass

else:
    from ...lo.awt.font_emphasis_mark import FontEmphasisMark as FontEmphasisMark

    class FontEmphasisMarkEnum(IntEnum):
        """
        Enum of Const Class FontEmphasisMark

        These values are used to specify the kind of emphasis mark.
        
        They may be expanded in future versions.
        """
        NONE = FontEmphasisMark.NONE
        """
        specifies no emphasis mark.
        """
        DOT = FontEmphasisMark.DOT
        """
        specifies emphasis mark dot.
        """
        CIRCLE = FontEmphasisMark.CIRCLE
        """
        specifies emphasis mark circle.
        """
        DISC = FontEmphasisMark.DISC
        """
        specifies emphasis mark disc.
        """
        ACCENT = FontEmphasisMark.ACCENT
        """
        specifies emphasis mark accent.
        """
        ABOVE = FontEmphasisMark.ABOVE
        """
        specifies that the emphasis mark should be positioned above the characters.
        """
        BELOW = FontEmphasisMark.BELOW
        """
        specifies that the emphasis mark should be positioned below the characters.
        """

__all__ = ['FontEmphasisMark', 'FontEmphasisMarkEnum']

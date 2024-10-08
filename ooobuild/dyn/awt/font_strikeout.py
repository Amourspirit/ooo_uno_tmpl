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
# Namespace: com.sun.star.awt
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

    class FontStrikeout(metaclass=UnoConstMeta, type_name="com.sun.star.awt.FontStrikeout", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.FontStrikeout``"""
        pass

    class FontStrikeoutEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.FontStrikeout", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.FontStrikeout`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.awt import FontStrikeout as FontStrikeout
    else:
        # keep document generators happy
        from ...lo.awt.font_strikeout import FontStrikeout as FontStrikeout

    class FontStrikeoutEnum(IntEnum):
        """
        Enum of Const Class FontStrikeout

        These values are used to specify the kind of strikeout.
        
        They may be expanded in future versions.
        """
        NONE = FontStrikeout.NONE
        """
        specifies not to strike out the characters.
        """
        SINGLE = FontStrikeout.SINGLE
        """
        specifies to strike out the characters with a single line.
        """
        DOUBLE = FontStrikeout.DOUBLE
        """
        specifies to strike out the characters with a double line.
        """
        DONTKNOW = FontStrikeout.DONTKNOW
        """
        The strikeout mode is not specified.
        """
        BOLD = FontStrikeout.BOLD
        """
        specifies to strike out the characters with a bold line.
        """
        SLASH = FontStrikeout.SLASH
        """
        specifies to strike out the characters with slashes.
        """
        X = FontStrikeout.X
        """
        specifies to strike out the characters with X's.
        """

__all__ = ['FontStrikeout', 'FontStrikeoutEnum']

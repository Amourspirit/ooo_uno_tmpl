# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class FontPitch(metaclass=UnoConstMeta, type_name="com.sun.star.awt.FontPitch", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.FontPitch``"""
        pass

    class FontPitchEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.FontPitch", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.FontPitch`` as Enum values"""
        pass

else:
    from ...lo.awt.font_pitch import FontPitch as FontPitch

    class FontPitchEnum(IntEnum):
        """
        Enum of Const Class FontPitch

        These values are used to specify whether the width of a character is fixed or variable.
        
        They may be expanded in future versions.
        """
        DONTKNOW = FontPitch.DONTKNOW
        """
        specifies that the pitch for this font is unknown.
        """
        FIXED = FontPitch.FIXED
        """
        specifies a font with a fixed character width.
        """
        VARIABLE = FontPitch.VARIABLE
        """
        specifies a font with a variable character width.
        """

__all__ = ['FontPitch', 'FontPitchEnum']

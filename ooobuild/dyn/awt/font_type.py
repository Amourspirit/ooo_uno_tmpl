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
import uno
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FontType(metaclass=UnoConstMeta, type_name="com.sun.star.awt.FontType", name_space="com.sun.star.awt"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.awt.FontType``"""
        pass

    class FontTypeEnum(IntFlag, metaclass=ConstEnumMeta, type_name="com.sun.star.awt.FontType", name_space="com.sun.star.awt"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.awt.FontType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.awt import FontType as FontType
    else:
        # keep document generators happy
        from ...lo.awt.font_type import FontType as FontType

    class FontTypeEnum(IntFlag):
        """
        Enum of Const Class FontType

        These values are used to specify the technology of the font representation.
        
        They may be expanded in future versions.
        """
        DONTKNOW = FontType.DONTKNOW
        """
        The type of the font is not known.
        """
        RASTER = FontType.RASTER
        """
        specifies a raster font.
        """
        DEVICE = FontType.DEVICE
        """
        specifies a device font.
        """
        SCALABLE = FontType.SCALABLE
        """
        specifies a scalable font.
        """

__all__ = ['FontType', 'FontTypeEnum']

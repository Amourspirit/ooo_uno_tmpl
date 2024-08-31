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
# Namespace: com.sun.star.rendering
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

    class ColorSpaceType(metaclass=UnoConstMeta, type_name="com.sun.star.rendering.ColorSpaceType", name_space="com.sun.star.rendering"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.rendering.ColorSpaceType``"""
        pass

    class ColorSpaceTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.rendering.ColorSpaceType", name_space="com.sun.star.rendering"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.rendering.ColorSpaceType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.rendering import ColorSpaceType as ColorSpaceType
    else:
        # keep document generators happy
        from ...lo.rendering.color_space_type import ColorSpaceType as ColorSpaceType

    class ColorSpaceTypeEnum(IntEnum):
        """
        Enum of Const Class ColorSpaceType

        Categories for color spaces.
        """
        DEVICE_COLOR = ColorSpaceType.DEVICE_COLOR
        """
        Unspecified device color space - use conversion functions to convert to standard color spaces.
        """
        GREY = ColorSpaceType.GREY
        """
        Grey-value color space.
        
        Use this for monochrome images.
        """
        RGB = ColorSpaceType.RGB
        """
        RGB color space.
        """
        CMYK = ColorSpaceType.CMYK
        """
        CMYK color space.
        
        See Wikipedia for a thorough explanation.
        """
        CMYKOG = ColorSpaceType.CMYKOG
        """
        CMYKOG color space.
        
        See Wikipedia for a thorough explanation.
        """
        CIEXYZ = ColorSpaceType.CIEXYZ
        """
        Standard CieXYZ color space.
        
        See Wikipedia for a thorough explanation.
        """
        CIELAB = ColorSpaceType.CIELAB
        """
        Standard CieLab color space.
        
        See Wikipedia for a thorough explanation. Preferable over CIEXYZ if perceptual uniformity is an issue.
        """
        SRGB = ColorSpaceType.SRGB
        """
        Standard sRGB color space.
        
        See Wikipedia for a thorough explanation.
        """
        HSV = ColorSpaceType.HSV
        """
        HSV color space.
        
        Hue saturation value. See Wikipedia for a thorough explanation.
        """
        HSL = ColorSpaceType.HSL
        """
        HSL color space.
        
        Hue saturation lightness. See Wikipedia for a thorough explanation
        """
        YCBCR = ColorSpaceType.YCBCR
        """
        YCbCr color space.
        
        See Wikipedia for a thorough explanation. This color space is common for digital video.
        """
        INDEXED = ColorSpaceType.INDEXED
        """
        Indexed color space.
        
        The color components of this color space are in fact indices into a color map.
        """

__all__ = ['ColorSpaceType', 'ColorSpaceTypeEnum']

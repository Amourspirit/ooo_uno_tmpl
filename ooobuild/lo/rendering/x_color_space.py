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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.rendering
from __future__ import annotations
import typing
import uno
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .argb_color import ARGBColor as ARGBColor_c6ee0be1
    from .color_component import ColorComponent as ColorComponent_e4c0e78
    from .rgb_color import RGBColor as RGBColor_bbdf0ba0

class XColorSpace(ABC):
    """
    Information how to interpret certain color data.
    
    This interface encapsulates all information that is necessary to interpret color data, by defining a describing color space, like for example CMYK or sRGB. You can either convert between this and an arbitrary other color space, or into the standard RGB or ARGB formats (because those are so overwhelmingly common in computer graphics).
    
    All canvas interfaces standardize to sequences of IEEE doubles for color representation. As this is overly verbose when used for bitmap data, derived interfaces exist, e.g. XIntegerBitmapColorSpace, which use sequences of integers for color representation.

    See Also:
        `API XColorSpace <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XColorSpace.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XColorSpace'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XColorSpace'

    @abstractmethod
    def convertColorSpace(self, deviceColor: typing.Tuple[ColorComponent_e4c0e78, ...], targetColorSpace: XColorSpace) -> typing.Tuple[ColorComponent_e4c0e78, ...]:
        """
        Convert to color of another color space.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertFromARGB(self, rgbColor: typing.Tuple[ARGBColor_c6ee0be1, ...]) -> typing.Tuple[ColorComponent_e4c0e78, ...]:
        """
        Convert sRGB color with linear alpha into this color space.
        
        If this color space does not convey alpha information, the specified alpha value is silently ignored.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertFromPARGB(self, rgbColor: typing.Tuple[ARGBColor_c6ee0be1, ...]) -> typing.Tuple[ColorComponent_e4c0e78, ...]:
        """
        Convert premultiplied sRGB color with linear alpha into this color space.
        
        If this color space does not convey alpha information, the specified alpha value is silently ignored.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertFromRGB(self, rgbColor: typing.Tuple[RGBColor_bbdf0ba0, ...]) -> typing.Tuple[ColorComponent_e4c0e78, ...]:
        """
        Convert sRGB color to a representation in this color space.
        
        If this color space conveys alpha information, it is assumed be fully opaque for the given RGB color value.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertToARGB(self, deviceColor: typing.Tuple[ColorComponent_e4c0e78, ...]) -> typing.Tuple[ARGBColor_c6ee0be1, ...]:
        """
        Convert color value in this color space to sRGB color values, with linear alpha.
        
        If the given input color does not carry alpha information, an alpha value of 1.0 (fully opaque) is assumed.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertToPARGB(self, deviceColor: typing.Tuple[ColorComponent_e4c0e78, ...]) -> typing.Tuple[ARGBColor_c6ee0be1, ...]:
        """
        Convert color value in this color space to premultiplied sRGB color values, with linear alpha.
        
        If the given input color does not carry alpha information, an alpha value of 1.0 (fully opaque) is assumed. The resulting individual RGB color values are premultiplied by the alpha value (e.g. if alpha is 0.5, each color value has only half of the original intensity).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertToRGB(self, deviceColor: typing.Tuple[ColorComponent_e4c0e78, ...]) -> typing.Tuple[RGBColor_bbdf0ba0, ...]:
        """
        Convert color value in this color space to sRGB color values.
        
        Any information not representable in the RGBColor struct is discarded during the conversion. This includes alpha information.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getComponentTags(self) -> uno.ByteSequence:
        """
        Query the kind for each color component.
        
        Color space components tend to correspond to physical attributes like the amount of one specific colorant contained in the final output color. This method returns a sequence of tags, specifying for each component of a color value, to what color attribute (if any) it corresponds. The values must be one of the ColorComponentTag constants.
        
        At the same time, the number of elements in this sequence corresponds to the number of color channels for this color space.
        """
        ...
    @abstractmethod
    def getProperties(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        Query various optional properties from the color space.
        
        If this color space has an ICC color profile, the sequence contains an element named ICCProfile. Some color spaces also have properties Gamma, Whitepoint and Blackpoint. Background information for these is available here.
        """
        ...
    @abstractmethod
    def getRenderingIntent(self) -> int:
        """
        Query rendering intent of this color space.
        """
        ...
    @abstractmethod
    def getType(self) -> int:
        """
        Query type of this color space.
        """
        ...

__all__ = ['XColorSpace']


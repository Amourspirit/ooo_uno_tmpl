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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering
import typing
import uno
from abc import abstractmethod
from .x_color_space import XColorSpace as XColorSpace_e3940d09
if typing.TYPE_CHECKING:
    from .argb_color import ARGBColor as ARGBColor_c6ee0be1
    from .color_component import ColorComponent as ColorComponent_e4c0e78
    from .rgb_color import RGBColor as RGBColor_bbdf0ba0

class XIntegerBitmapColorSpace(XColorSpace_e3940d09):
    """
    A color space for integer bitmap formats.
    
    This interface encapsulates all information specific to a certain integer bitmap color space, like for example 1555 ARGB. Note that the individual elements of the integer color representation sequence need not correspond to the color space's components - instead, the color components might be packed back-to-back into those bytes, as they appear in the raw bitmap data.

    See Also:
        `API XIntegerBitmapColorSpace <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XIntegerBitmapColorSpace.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XIntegerBitmapColorSpace'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XIntegerBitmapColorSpace'

    @abstractmethod
    def convertFromIntegerColorSpace(self, deviceColor: uno.ByteSequence, targetColorSpace: 'XColorSpace_e3940d09') -> 'typing.Tuple[ColorComponent_e4c0e78, ...]':
        """
        Convert integer bitmap color to generic IEEE double device color of another color space.
        
        Color values are properly rounded and clipped, to be valid in the target color space.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertIntegerFromARGB(self, rgbColor: 'typing.Tuple[ARGBColor_c6ee0be1, ...]') -> uno.ByteSequence:
        """
        Convert sRGB color with linear alpha into this color space.
        
        If this color space does not convey alpha information, the specified alpha value is silently ignored. Color values are properly rounded and clipped, to be valid in the target color space.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertIntegerFromPARGB(self, rgbColor: 'typing.Tuple[ARGBColor_c6ee0be1, ...]') -> uno.ByteSequence:
        """
        Convert premultiplied sRGB color with linear alpha into this color space.
        
        If this color space does not convey alpha information, the specified alpha value is silently ignored. Color values are properly rounded and clipped, to be valid in the target color space.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertIntegerFromRGB(self, rgbColor: 'typing.Tuple[RGBColor_bbdf0ba0, ...]') -> uno.ByteSequence:
        """
        Convert sRGB color to an integer representation in this color space.
        
        If this color space conveys alpha information, it is assumed be fully opaque for the given RGB color value. Color values are properly rounded and clipped, to be valid in the target color space.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertIntegerToARGB(self, deviceColor: uno.ByteSequence) -> 'typing.Tuple[ARGBColor_c6ee0be1, ...]':
        """
        Convert color value in this color space to sRGB color values, with linear alpha.
        
        If the given input color does not carry alpha information, an alpha value of 1.0 (fully opaque) is assumed. Color values are properly rounded and clipped, to be valid in the target color space.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertIntegerToPARGB(self, deviceColor: uno.ByteSequence) -> 'typing.Tuple[ARGBColor_c6ee0be1, ...]':
        """
        Convert color value in this color space to premultiplied sRGB color values, with linear alpha.
        
        If the given input color does not carry alpha information, an alpha value of 1.0 (fully opaque) is assumed. Color values are properly rounded and clipped, to be valid in the target color space. The resulting individual RGB color values are premultiplied by the alpha value (e.g. if alpha is 0.5, each color value has only half of the original intensity).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertIntegerToRGB(self, deviceColor: uno.ByteSequence) -> 'typing.Tuple[RGBColor_bbdf0ba0, ...]':
        """
        Convert color value in this color space to sRGB color values.
        
        Any information not representable in the RGBColor struct is discarded during the conversion. This includes alpha information. Color values are properly rounded and clipped, to be valid in the target color space.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertToIntegerColorSpace(self, deviceColor: uno.ByteSequence, targetColorSpace: 'XIntegerBitmapColorSpace') -> uno.ByteSequence:
        """
        Convert integer bitmap color to integer bitmap color of another integer bitmap color space.
        
        Color values are properly rounded and clipped, to be valid in the target color space.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getBitsPerPixel(self) -> int:
        """
        Query number of bits used per bitmap pixel.
        
        This method yields the total number of bits used for a color value. At the associated XIntegerBitmap, the XIntegerBitmap.setPixel() method will expect a sequence of ceil(BitsPerPixel/8) bytes, and the XIntegerReadOnlyBitmap.getPixel() will return that number of bytes. Similarly, the color conversion expect input data in multiples of ceil(BitsPerPixel/8), and also return converted data in chunks of this.
        """
        ...
    @abstractmethod
    def getComponentBitCounts(self) -> uno.ByteSequence:
        """
        Query the number of bits used for each component.
        
        This method returns a sequence of integers, each denoting the number of bits occupied by the respective component. The sum of all component bits must be less or equal than the value returned from getBitsPerPixel(). If the sum is less, excess bits are always kept in the most significant bits of a pixel. Color components will appear in the byte sequences returned from the XIntegerBitmap methods in the order defined here, with the first element starting from the least significant bits of the pixel, etc.
        """
        ...
    @abstractmethod
    def getEndianness(self) -> int:
        """
        Query whether color data bytes need to be swapped.
        """
        ...

__all__ = ['XIntegerBitmapColorSpace']


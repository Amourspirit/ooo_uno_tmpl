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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.rendering
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .x_color_space import XColorSpace as XColorSpace_e3940d09


class FloatingPointBitmapLayout(object):
    """
    Struct Class

    This structure describes the memory layout of a bitmap having floating point color channels.
    
    This structure collects all necessary information to describe the memory layout of a bitmap having floating point color channels
    
    **since**
    
        OOo 2.0

    See Also:
        `API FloatingPointBitmapLayout <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1FloatingPointBitmapLayout.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.FloatingPointBitmapLayout'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.rendering.FloatingPointBitmapLayout'
    """Literal Constant ``com.sun.star.rendering.FloatingPointBitmapLayout``"""

    def __init__(self, ScanLines: typing.Optional[int] = 0, ScanLineBytes: typing.Optional[int] = 0, ScanLineStride: typing.Optional[int] = 0, PlaneStride: typing.Optional[int] = 0, ColorSpace: typing.Optional[XColorSpace_e3940d09] = None, NumComponents: typing.Optional[int] = 0, Endianness: typing.Optional[int] = 0, Format: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            ScanLines (int, optional): ScanLines value.
            ScanLineBytes (int, optional): ScanLineBytes value.
            ScanLineStride (int, optional): ScanLineStride value.
            PlaneStride (int, optional): PlaneStride value.
            ColorSpace (XColorSpace, optional): ColorSpace value.
            NumComponents (int, optional): NumComponents value.
            Endianness (int, optional): Endianness value.
            Format (int, optional): Format value.
        """
        super().__init__()

        if isinstance(ScanLines, FloatingPointBitmapLayout):
            oth: FloatingPointBitmapLayout = ScanLines
            self.ScanLines = oth.ScanLines
            self.ScanLineBytes = oth.ScanLineBytes
            self.ScanLineStride = oth.ScanLineStride
            self.PlaneStride = oth.PlaneStride
            self.ColorSpace = oth.ColorSpace
            self.NumComponents = oth.NumComponents
            self.Endianness = oth.Endianness
            self.Format = oth.Format
            return

        kargs = {
            "ScanLines": ScanLines,
            "ScanLineBytes": ScanLineBytes,
            "ScanLineStride": ScanLineStride,
            "PlaneStride": PlaneStride,
            "ColorSpace": ColorSpace,
            "NumComponents": NumComponents,
            "Endianness": Endianness,
            "Format": Format,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._scan_lines = kwargs["ScanLines"]
        self._scan_line_bytes = kwargs["ScanLineBytes"]
        self._scan_line_stride = kwargs["ScanLineStride"]
        self._plane_stride = kwargs["PlaneStride"]
        self._color_space = kwargs["ColorSpace"]
        self._num_components = kwargs["NumComponents"]
        self._endianness = kwargs["Endianness"]
        self._format = kwargs["Format"]


    @property
    def ScanLines(self) -> int:
        """
        Number of scanlines for this bitmap.
        
        This value must not be negative
        """
        return self._scan_lines

    @ScanLines.setter
    def ScanLines(self, value: int) -> None:
        self._scan_lines = value

    @property
    def ScanLineBytes(self) -> int:
        """
        Number of data bytes per scanline.
        
        This value must not be negative
        """
        return self._scan_line_bytes

    @ScanLineBytes.setter
    def ScanLineBytes(self, value: int) -> None:
        self._scan_line_bytes = value

    @property
    def ScanLineStride(self) -> int:
        """
        Byte offset between the start of two consecutive scanlines.
        
        This value is permitted to be negative, denoting a bitmap whose content is flipped at the x axis.
        """
        return self._scan_line_stride

    @ScanLineStride.setter
    def ScanLineStride(self, value: int) -> None:
        self._scan_line_stride = value

    @property
    def PlaneStride(self) -> int:
        """
        Byte offset between the start of two consecutive planes.
        
        This value is permitted to be negative. If this value is zero, the bitmap is assumed to be in chunky format, otherwise it is assumed to be planar. The difference between chunky and planar layout lies in the way how color channels are interleaved. For a chunky format, all channel data for a single pixel lies consecutively in memory. For a planar layout, the first channel of all pixel is stored consecutive, followed by the second channel, and so forth.
        """
        return self._plane_stride

    @PlaneStride.setter
    def PlaneStride(self, value: int) -> None:
        self._plane_stride = value

    @property
    def ColorSpace(self) -> XColorSpace_e3940d09:
        """
        Color space the bitmap colors shall be interpreted within.
        """
        return self._color_space

    @ColorSpace.setter
    def ColorSpace(self, value: XColorSpace_e3940d09) -> None:
        self._color_space = value

    @property
    def NumComponents(self) -> int:
        """
        Number of color components per pixel.
        
        This value must not be negative
        """
        return self._num_components

    @NumComponents.setter
    def NumComponents(self, value: int) -> None:
        self._num_components = value

    @property
    def Endianness(self) -> int:
        """
        Endianness of the pixel values.
        
        This value must be one of the Endianness constants
        """
        return self._endianness

    @Endianness.setter
    def Endianness(self, value: int) -> None:
        self._endianness = value

    @property
    def Format(self) -> int:
        """
        Format type of this bitmap.
        
        This value must be one of the FloatingPointBitmapFormat constants.
        """
        return self._format

    @Format.setter
    def Format(self, value: int) -> None:
        self._format = value


__all__ = ['FloatingPointBitmapLayout']

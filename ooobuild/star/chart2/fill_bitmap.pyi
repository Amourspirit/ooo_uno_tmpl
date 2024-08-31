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
# Namespace: com.sun.star.chart2
# Libre Office Version: 2024.2
import typing
from ..awt.point import Point as Point_5fb2085e
from ..awt.size import Size as Size_576707ef
from ..drawing.bitmap_mode import BitmapMode as BitmapMode_bced0bd6
from ..drawing.rectangle_point import RectanglePoint as RectanglePoint_f0ff0d93


class FillBitmap(object):
    """
    Struct Class

    This structure contains all properties of a bitmap when used as FillStyle.

    See Also:
        `API FillBitmap <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1FillBitmap.html>`_
    """
    typeName: str = 'com.sun.star.chart2.FillBitmap'

    def __init__(self, aURL: typing.Optional[str] = ..., aOffset: typing.Optional[Point_5fb2085e] = ..., aPositionOffset: typing.Optional[Point_5fb2085e] = ..., aRectanglePoint: typing.Optional[RectanglePoint_f0ff0d93] = ..., bLogicalSize: typing.Optional[bool] = ..., aSize: typing.Optional[Size_576707ef] = ..., aBitmapMode: typing.Optional[BitmapMode_bced0bd6] = ...) -> None:
        """
        Constructor

        Arguments:
            aURL (str, optional): aURL value.
            aOffset (Point, optional): aOffset value.
            aPositionOffset (Point, optional): aPositionOffset value.
            aRectanglePoint (RectanglePoint, optional): aRectanglePoint value.
            bLogicalSize (bool, optional): bLogicalSize value.
            aSize (Size, optional): aSize value.
            aBitmapMode (BitmapMode, optional): aBitmapMode value.
        """
        ...

    @property
    def aURL(self) -> str:
        """
        a URL to the bitmap used.
        
        This may be an internal URL of the graphics manager.
        """
        ...
    @aURL.setter
    def aURL(self, value: str) -> None:
        ...
    @property
    def aOffset(self) -> Point_5fb2085e:
        """
        This is the horizontal and vertical offset where the tile starts.
        
        It is given in percent in relation to the width of the bitmap.
        """
        ...
    @aOffset.setter
    def aOffset(self, value: Point_5fb2085e) -> None:
        ...
    @property
    def aPositionOffset(self) -> Point_5fb2085e:
        """
        Every second line (X) / row (Y) of tiles is moved the given percent of the width of the bitmap.
        """
        ...
    @aPositionOffset.setter
    def aPositionOffset(self, value: Point_5fb2085e) -> None:
        ...
    @property
    def aRectanglePoint(self) -> RectanglePoint_f0ff0d93:
        """
        The RectanglePoint specifies the position inside of the bitmap to use as the top left position for rendering.
        """
        ...
    @aRectanglePoint.setter
    def aRectanglePoint(self, value: RectanglePoint_f0ff0d93) -> None:
        ...
    @property
    def bLogicalSize(self) -> bool:
        """
        specifies if the size is given in percentage or as an absolute value.
        
        If this is TRUE, the properties SizeX and SizeY contain the size of the tile in percent of the size of the original bitmap. If this is FALSE, the size of the tile is specified with 1/100th mm.
        """
        ...
    @bLogicalSize.setter
    def bLogicalSize(self, value: bool) -> None:
        ...
    @property
    def aSize(self) -> Size_576707ef:
        """
        This is the size of the tile for filling.
        
        Depending on the property LogicalSize, this is either relative or absolute.
        """
        ...
    @aSize.setter
    def aSize(self, value: Size_576707ef) -> None:
        ...
    @property
    def aBitmapMode(self) -> BitmapMode_bced0bd6:
        """
        this enum selects how an area is filled with a single bitmap.
        
        It may be repeated, stretched or displayed with blank space around it.
        """
        ...
    @aBitmapMode.setter
    def aBitmapMode(self, value: BitmapMode_bced0bd6) -> None:
        ...


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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.4
import typing
from ..awt.size import Size as Size_576707ef
from .symbol_style import SymbolStyle as SymbolStyle_baa20bd3
from ..drawing.poly_polygon_bezier_coords import PolyPolygonBezierCoords as PolyPolygonBezierCoords_7ec5114b
from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc


class Symbol(object):
    """
    Struct Class

    properties that are used for DataSeries that display symbols.

    See Also:
        `API Symbol <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1Symbol.html>`_
    """
    typeName: str = 'com.sun.star.chart2.Symbol'

    def __init__(self, Style: typing.Optional[SymbolStyle_baa20bd3] = ..., PolygonCoords: typing.Optional[PolyPolygonBezierCoords_7ec5114b] = ..., StandardSymbol: typing.Optional[int] = ..., Graphic: typing.Optional[XGraphic_a4da0afc] = ..., Size: typing.Optional[Size_576707ef] = ..., BorderColor: typing.Optional[int] = ..., FillColor: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Style (SymbolStyle, optional): Style value.
            PolygonCoords (PolyPolygonBezierCoords, optional): PolygonCoords value.
            StandardSymbol (int, optional): StandardSymbol value.
            Graphic (XGraphic, optional): Graphic value.
            Size (Size, optional): Size value.
            BorderColor (int, optional): BorderColor value.
            FillColor (int, optional): FillColor value.
        """
        ...

    @property
    def Style(self) -> SymbolStyle_baa20bd3:
        """
        determines which of the following members determines the appearance of the symbol.
        """
        ...
    @Style.setter
    def Style(self, value: SymbolStyle_baa20bd3) -> None:
        ...
    @property
    def PolygonCoords(self) -> PolyPolygonBezierCoords_7ec5114b:
        """
        The given polygon is used as symbol.
        """
        ...
    @PolygonCoords.setter
    def PolygonCoords(self, value: PolyPolygonBezierCoords_7ec5114b) -> None:
        ...
    @property
    def StandardSymbol(self) -> int:
        """
        Use the nth standard symbol, if Style is set to SymbolStyle.STANDARD.
        
        If n is the number of standard symbols available in an implementation, the symbol number is StandardSymbol modulo n.
        
        The default implementation for example currently uses 8 different standard symbols that are matched to the numbers 0 to 7.
        """
        ...
    @StandardSymbol.setter
    def StandardSymbol(self, value: int) -> None:
        ...
    @property
    def Graphic(self) -> XGraphic_a4da0afc:
        """
        use this graphic as symbol
        """
        ...
    @Graphic.setter
    def Graphic(self, value: XGraphic_a4da0afc) -> None:
        ...
    @property
    def Size(self) -> Size_576707ef:
        """
        The size of the symbol in 100th of a mm.
        """
        ...
    @Size.setter
    def Size(self, value: Size_576707ef) -> None:
        ...
    @property
    def BorderColor(self) -> int:
        """
        The color used for drawing the border of symbols.
        
        Only effective if Style is SymbolStyle.AUTO, SymbolStyle.STANDARD or SymbolStyle.POLYGON.
        """
        ...
    @BorderColor.setter
    def BorderColor(self, value: int) -> None:
        ...
    @property
    def FillColor(self) -> int:
        """
        The color used for filling symbols that contain closed polygons.
        
        Only effective if Style is SymbolStyle.AUTO, SymbolStyle.STANDARD or SymbolStyle.POLYGON.
        """
        ...
    @FillColor.setter
    def FillColor(self, value: int) -> None:
        ...

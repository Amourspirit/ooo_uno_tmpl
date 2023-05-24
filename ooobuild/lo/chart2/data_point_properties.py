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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing
from abc import abstractproperty
from ..beans.property_set import PropertySet as PropertySet_b0e70ba2
from ..drawing.fill_properties import FillProperties as FillProperties_f1200da8
if typing.TYPE_CHECKING:
    from ..awt.gradient import Gradient as Gradient_7a8a0982
    from ..awt.size import Size as Size_576707ef
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from .data_point_label import DataPointLabel as DataPointLabel_dd530cb0
    from .relative_position import RelativePosition as RelativePosition_fae10ddd
    from .symbol import Symbol as Symbol_83c109c2
    from .x_data_point_custom_label_field import XDataPointCustomLabelField as XDataPointCustomLabelField_94771167
    from ..drawing.hatch import Hatch as Hatch_859b09dc
    from ..drawing.line_dash import LineDash as LineDash_a54e0afc
    from com.sun.star.drawing.LineStyle import LineStyleProto
    from com.sun.star.drawing.BitmapMode import BitmapModeProto
    from com.sun.star.drawing.RectanglePoint import RectanglePointProto
    from com.sun.star.drawing.FillStyle import FillStyleProto

class DataPointProperties(PropertySet_b0e70ba2, FillProperties_f1200da8):
    """
    Service Class

    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API DataPointProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1DataPointProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.DataPointProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CustomLabelFields(self) -> typing.Tuple[XDataPointCustomLabelField_94771167, ...]:
        """
        specifies a text with possible fields that is used as a data point label, if set then Label property is ignored
        
        **since**
        
            LibreOffice 6.1
        """
        ...

    @abstractproperty
    def BorderColor(self) -> int:
        """
        Is used for borders around filled objects.
        
        See LineColor.
        """
        ...

    @abstractproperty
    def BorderDash(self) -> LineDash_a54e0afc:
        """
        Is used for borders around filled objects.
        
        See LineDash.
        """
        ...

    @abstractproperty
    def BorderDashName(self) -> str:
        """
        The name of a dash that can be found in the com.sun.star.container.XNameContainer \"com.sun.star.drawing.LineDashTable\", that can be created via the com.sun.star.uno.XMultiServiceFactory of the ChartDocument.
        """
        ...

    @abstractproperty
    def BorderStyle(self) -> LineStyleProto:
        """
        Is used for borders around filled objects.
        
        See LineStyle.
        """
        ...

    @abstractproperty
    def BorderTransparency(self) -> int:
        """
        Is used for borders around filled objects.
        
        See LineTransparence.
        """
        ...

    @abstractproperty
    def BorderWidth(self) -> int:
        """
        Is used for borders around filled objects.
        
        See LineWidth.
        """
        ...

    @abstractproperty
    def Color(self) -> int:
        """
        points to a style that also supports this service (but not this property) that is used as default, if the PropertyState of a property is DEFAULT_VALUE.
        
        This is the main color of a data point.
        
        For charts with filled areas, like bar-charts, this should map to the FillColor of the objects. For line-charts this should map to the LineColor property.
        """
        ...

    @abstractproperty
    def CustomLabelPosition(self) -> RelativePosition_fae10ddd:
        """
        Custom position on the page associated to the CUSTOM label placement.
        
        **since**
        
            LibreOffice 7.0
        """
        ...

    @abstractproperty
    def ErrorBarX(self) -> XPropertySet_bc180bfa:
        """
        If void, no error bars are shown for the data point in x-direction.
        
        The com.sun.star.beans.XPropertySet must support the service ErrorBar.
        """
        ...

    @abstractproperty
    def ErrorBarY(self) -> XPropertySet_bc180bfa:
        """
        If void, no error bars are shown for the data point in y-direction.
        
        The com.sun.star.beans.XPropertySet must support the service ErrorBar.
        """
        ...

    @abstractproperty
    def FillBackground(self) -> bool:
        """
        If TRUE, fills the background of a hatch with the color given in the Color property.
        """
        ...

    @abstractproperty
    def FillBitmapLogicalSize(self) -> bool:
        """
        specifies if the size is given in percentage or as an absolute value.
        
        If this is TRUE, the properties FillBitmapSizeX and FillBitmapSizeY contain the size of the tile in percent of the size of the original bitmap. If this is FALSE, the size of the tile is specified with 1/100th mm.
        """
        ...

    @abstractproperty
    def FillBitmapMode(self) -> BitmapModeProto:
        """
        this enum selects how an area is filled with a single bitmap.
        """
        ...

    @abstractproperty
    def FillBitmapName(self) -> str:
        """
        """
        ...

    @abstractproperty
    def FillBitmapOffsetX(self) -> int:
        """
        This is the horizontal offset where the tile starts.
        
        It is given in percent in relation to the width of the bitmap.
        """
        ...

    @abstractproperty
    def FillBitmapOffsetY(self) -> int:
        """
        This is the vertical offset where the tile starts.
        
        It is given in percent in relation to the width of the bitmap.
        """
        ...

    @abstractproperty
    def FillBitmapPositionOffsetX(self) -> int:
        """
        Every second line of tiles is moved the given percent of the width of the bitmap.
        """
        ...

    @abstractproperty
    def FillBitmapPositionOffsetY(self) -> int:
        """
        Every second row of tiles is moved the given percent of the width of the bitmap.
        """
        ...

    @abstractproperty
    def FillBitmapRectanglePoint(self) -> RectanglePointProto:
        """
        The RectanglePoint specifies the position inside of the bitmap to use as the top left position for rendering.
        """
        ...

    @abstractproperty
    def FillBitmapSizeX(self) -> int:
        """
        This is the width of the tile for filling.
        
        Depending on the property FillBitmapLogicalSize, this is either relative or absolute.
        """
        ...

    @abstractproperty
    def FillBitmapSizeY(self) -> int:
        """
        This is the height of the tile for filling.
        
        Depending on the property FillBitmapLogicalSize, this is either relative or absolute.
        """
        ...

    @abstractproperty
    def FillStyle(self) -> FillStyleProto:
        """
        This enumeration selects the style with which the area will be filled.
        """
        ...

    @abstractproperty
    def Geometry3D(self) -> int:
        """
        describes the geometry of a 3 dimensional data point.
        
        Number is one of constant group DataPointGeometry3D.
        
        This is especially used for 3D bar-charts.
        
        CUBOID==0 CYLINDER==1 CONE==2 PYRAMID==3 CUBOID==else
        """
        ...

    @abstractproperty
    def Gradient(self) -> Gradient_7a8a0982:
        """
        """
        ...

    @abstractproperty
    def GradientName(self) -> str:
        """
        """
        ...

    @abstractproperty
    def Hatch(self) -> Hatch_859b09dc:
        """
        """
        ...

    @abstractproperty
    def HatchName(self) -> str:
        """
        """
        ...

    @abstractproperty
    def Label(self) -> DataPointLabel_dd530cb0:
        """
        """
        ...

    @abstractproperty
    def LabelPlacement(self) -> int:
        """
        specifies a relative position for the data label
        """
        ...

    @abstractproperty
    def LabelSeparator(self) -> str:
        """
        specifies a string that is used to separate the parts of a data label (caption)
        """
        ...

    @abstractproperty
    def LineDash(self) -> LineDash_a54e0afc:
        """
        Is only used for line-chart types.
        """
        ...

    @abstractproperty
    def LineDashName(self) -> str:
        """
        The name of a dash that can be found in the com.sun.star.container.XNameContainer \"com.sun.star.drawing.LineDashTable\", that can be created via the com.sun.star.uno.XMultiServiceFactory of the ChartDocument.
        """
        ...

    @abstractproperty
    def LineStyle(self) -> LineStyleProto:
        """
        """
        ...

    @abstractproperty
    def LineWidth(self) -> int:
        """
        Is only used for line-chart types.
        """
        ...

    @abstractproperty
    def NumberFormat(self) -> int:
        """
        specifies a number format for the display of the value in the data label
        """
        ...

    @abstractproperty
    def Offset(self) -> float:
        """
        describes a value by which a data point is moved from its default position in percent of the maximum allowed distance.
        
        This is especially useful for the explosion of pie-chart segments.
        """
        ...

    @abstractproperty
    def PercentDiagonal(self) -> int:
        """
        A value between 0 and 100 indicating the percentage how round an edge should be.
        """
        ...

    @abstractproperty
    def PercentageNumberFormat(self) -> int:
        """
        specifies a number format for the display of the percentage value in the data label
        """
        ...

    @abstractproperty
    def ReferencePageSize(self) -> Size_576707ef:
        """
        The size of the page at the moment when the font size for data labels was set.
        
        This size is used to resize text in the view when the size of the page has changed since the font sizes were set (automatic text scaling).
        """
        ...

    @abstractproperty
    def ShowErrorBox(self) -> bool:
        """
        In case ErrorBarX and ErrorBarY both are set, and error bars are shown, a box spanning all error-indicators is rendered.
        """
        ...

    @abstractproperty
    def Symbol(self) -> Symbol_83c109c2:
        """
        """
        ...

    @abstractproperty
    def TextWordWrap(self) -> bool:
        """
        specifies if the text of a data label (caption) must be wrapped
        
        **since**
        
            LibreOffice 5.1
        """
        ...

    @abstractproperty
    def Transparency(self) -> int:
        """
        This is the main transparency value of a data point.
        
        For charts with filled areas, like bar-charts, this should map to the FillTransparence of the objects. For line-charts this should map to the LineTransparence property.
        """
        ...

    @abstractproperty
    def TransparencyGradient(self) -> Gradient_7a8a0982:
        """
        This describes the transparency of the fill area as a gradient.
        """
        ...

    @abstractproperty
    def TransparencyGradientName(self) -> str:
        """
        """
        ...


__all__ = ['DataPointProperties']


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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing
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
    from com.sun.star.drawing.LineStyle import LineStyleProto  # type: ignore
    from com.sun.star.drawing.BitmapMode import BitmapModeProto  # type: ignore
    from com.sun.star.drawing.RectanglePoint import RectanglePointProto  # type: ignore
    from com.sun.star.drawing.FillStyle import FillStyleProto  # type: ignore

class DataPointProperties(PropertySet_b0e70ba2, FillProperties_f1200da8):
    """
    Service Class

    
    **since**
    
        LibreOffice 5.1

    See Also:
        `API DataPointProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1DataPointProperties.html>`_
    """
    @property
    def BorderColor(self) -> int:
        """
        Is used for borders around filled objects.
        
        See LineColor.
        """
        ...
    @BorderColor.setter
    def BorderColor(self, value: int) -> None:
        ...
    @property
    def BorderDash(self) -> LineDash_a54e0afc:
        """
        Is used for borders around filled objects.
        
        See LineDash.
        """
        ...
    @BorderDash.setter
    def BorderDash(self, value: LineDash_a54e0afc) -> None:
        ...
    @property
    def BorderDashName(self) -> str:
        """
        The name of a dash that can be found in the com.sun.star.container.XNameContainer \"com.sun.star.drawing.LineDashTable\", that can be created via the com.sun.star.uno.XMultiServiceFactory of the ChartDocument.
        """
        ...
    @BorderDashName.setter
    def BorderDashName(self, value: str) -> None:
        ...
    @property
    def BorderStyle(self) -> LineStyleProto:
        """
        Is used for borders around filled objects.
        
        See LineStyle.
        """
        ...
    @BorderStyle.setter
    def BorderStyle(self, value: LineStyleProto) -> None:
        ...
    @property
    def BorderTransparency(self) -> int:
        """
        Is used for borders around filled objects.
        
        See LineTransparence.
        """
        ...
    @BorderTransparency.setter
    def BorderTransparency(self, value: int) -> None:
        ...
    @property
    def BorderWidth(self) -> int:
        """
        Is used for borders around filled objects.
        
        See LineWidth.
        """
        ...
    @BorderWidth.setter
    def BorderWidth(self, value: int) -> None:
        ...
    @property
    def Color(self) -> int:
        """
        points to a style that also supports this service (but not this property) that is used as default, if the PropertyState of a property is DEFAULT_VALUE.
        
        This is the main color of a data point.
        
        For charts with filled areas, like bar-charts, this should map to the FillColor of the objects. For line-charts this should map to the LineColor property.
        """
        ...
    @Color.setter
    def Color(self, value: int) -> None:
        ...
    @property
    def CustomLabelFields(self) -> typing.Tuple[XDataPointCustomLabelField_94771167, ...]:
        """
        specifies a text with possible fields that is used as a data point label, if set then Label property is ignored
        
        **since**
        
            LibreOffice 6.1
        """
        ...
    @CustomLabelFields.setter
    def CustomLabelFields(self, value: typing.Tuple[XDataPointCustomLabelField_94771167, ...]) -> None:
        ...
    @property
    def CustomLabelPosition(self) -> RelativePosition_fae10ddd:
        """
        Custom position on the page associated to the CUSTOM label placement.
        
        **since**
        
            LibreOffice 7.0
        """
        ...
    @CustomLabelPosition.setter
    def CustomLabelPosition(self, value: RelativePosition_fae10ddd) -> None:
        ...
    @property
    def ErrorBarX(self) -> XPropertySet_bc180bfa:
        """
        If void, no error bars are shown for the data point in x-direction.
        
        The com.sun.star.beans.XPropertySet must support the service ErrorBar.
        """
        ...
    @ErrorBarX.setter
    def ErrorBarX(self, value: XPropertySet_bc180bfa) -> None:
        ...
    @property
    def ErrorBarY(self) -> XPropertySet_bc180bfa:
        """
        If void, no error bars are shown for the data point in y-direction.
        
        The com.sun.star.beans.XPropertySet must support the service ErrorBar.
        """
        ...
    @ErrorBarY.setter
    def ErrorBarY(self, value: XPropertySet_bc180bfa) -> None:
        ...
    @property
    def FillBackground(self) -> bool:
        """
        If TRUE, fills the background of a hatch with the color given in the Color property.
        """
        ...
    @FillBackground.setter
    def FillBackground(self, value: bool) -> None:
        ...
    @property
    def FillBitmapLogicalSize(self) -> bool:
        """
        specifies if the size is given in percentage or as an absolute value.
        
        If this is TRUE, the properties FillBitmapSizeX and FillBitmapSizeY contain the size of the tile in percent of the size of the original bitmap. If this is FALSE, the size of the tile is specified with 1/100th mm.
        """
        ...
    @FillBitmapLogicalSize.setter
    def FillBitmapLogicalSize(self, value: bool) -> None:
        ...
    @property
    def FillBitmapMode(self) -> BitmapModeProto:
        """
        this enum selects how an area is filled with a single bitmap.
        """
        ...
    @FillBitmapMode.setter
    def FillBitmapMode(self, value: BitmapModeProto) -> None:
        ...
    @property
    def FillBitmapName(self) -> str:
        """
        """
        ...
    @FillBitmapName.setter
    def FillBitmapName(self, value: str) -> None:
        ...
    @property
    def FillBitmapOffsetX(self) -> int:
        """
        This is the horizontal offset where the tile starts.
        
        It is given in percent in relation to the width of the bitmap.
        """
        ...
    @FillBitmapOffsetX.setter
    def FillBitmapOffsetX(self, value: int) -> None:
        ...
    @property
    def FillBitmapOffsetY(self) -> int:
        """
        This is the vertical offset where the tile starts.
        
        It is given in percent in relation to the width of the bitmap.
        """
        ...
    @FillBitmapOffsetY.setter
    def FillBitmapOffsetY(self, value: int) -> None:
        ...
    @property
    def FillBitmapPositionOffsetX(self) -> int:
        """
        Every second line of tiles is moved the given percent of the width of the bitmap.
        """
        ...
    @FillBitmapPositionOffsetX.setter
    def FillBitmapPositionOffsetX(self, value: int) -> None:
        ...
    @property
    def FillBitmapPositionOffsetY(self) -> int:
        """
        Every second row of tiles is moved the given percent of the width of the bitmap.
        """
        ...
    @FillBitmapPositionOffsetY.setter
    def FillBitmapPositionOffsetY(self, value: int) -> None:
        ...
    @property
    def FillBitmapRectanglePoint(self) -> RectanglePointProto:
        """
        The RectanglePoint specifies the position inside of the bitmap to use as the top left position for rendering.
        """
        ...
    @FillBitmapRectanglePoint.setter
    def FillBitmapRectanglePoint(self, value: RectanglePointProto) -> None:
        ...
    @property
    def FillBitmapSizeX(self) -> int:
        """
        This is the width of the tile for filling.
        
        Depending on the property FillBitmapLogicalSize, this is either relative or absolute.
        """
        ...
    @FillBitmapSizeX.setter
    def FillBitmapSizeX(self, value: int) -> None:
        ...
    @property
    def FillBitmapSizeY(self) -> int:
        """
        This is the height of the tile for filling.
        
        Depending on the property FillBitmapLogicalSize, this is either relative or absolute.
        """
        ...
    @FillBitmapSizeY.setter
    def FillBitmapSizeY(self, value: int) -> None:
        ...
    @property
    def FillStyle(self) -> FillStyleProto:
        """
        This enumeration selects the style with which the area will be filled.
        """
        ...
    @FillStyle.setter
    def FillStyle(self, value: FillStyleProto) -> None:
        ...
    @property
    def Geometry3D(self) -> int:
        """
        describes the geometry of a 3 dimensional data point.
        
        Number is one of constant group DataPointGeometry3D.
        
        This is especially used for 3D bar-charts.
        
        CUBOID==0 CYLINDER==1 CONE==2 PYRAMID==3 CUBOID==else
        """
        ...
    @Geometry3D.setter
    def Geometry3D(self, value: int) -> None:
        ...
    @property
    def Gradient(self) -> Gradient_7a8a0982:
        """
        """
        ...
    @Gradient.setter
    def Gradient(self, value: Gradient_7a8a0982) -> None:
        ...
    @property
    def GradientName(self) -> str:
        """
        """
        ...
    @GradientName.setter
    def GradientName(self, value: str) -> None:
        ...
    @property
    def Hatch(self) -> Hatch_859b09dc:
        """
        """
        ...
    @Hatch.setter
    def Hatch(self, value: Hatch_859b09dc) -> None:
        ...
    @property
    def HatchName(self) -> str:
        """
        """
        ...
    @HatchName.setter
    def HatchName(self, value: str) -> None:
        ...
    @property
    def Label(self) -> DataPointLabel_dd530cb0:
        """
        """
        ...
    @Label.setter
    def Label(self, value: DataPointLabel_dd530cb0) -> None:
        ...
    @property
    def LabelPlacement(self) -> int:
        """
        specifies a relative position for the data label
        """
        ...
    @LabelPlacement.setter
    def LabelPlacement(self, value: int) -> None:
        ...
    @property
    def LabelSeparator(self) -> str:
        """
        specifies a string that is used to separate the parts of a data label (caption)
        """
        ...
    @LabelSeparator.setter
    def LabelSeparator(self, value: str) -> None:
        ...
    @property
    def LineDash(self) -> LineDash_a54e0afc:
        """
        Is only used for line-chart types.
        """
        ...
    @LineDash.setter
    def LineDash(self, value: LineDash_a54e0afc) -> None:
        ...
    @property
    def LineDashName(self) -> str:
        """
        The name of a dash that can be found in the com.sun.star.container.XNameContainer \"com.sun.star.drawing.LineDashTable\", that can be created via the com.sun.star.uno.XMultiServiceFactory of the ChartDocument.
        """
        ...
    @LineDashName.setter
    def LineDashName(self, value: str) -> None:
        ...
    @property
    def LineStyle(self) -> LineStyleProto:
        """
        """
        ...
    @LineStyle.setter
    def LineStyle(self, value: LineStyleProto) -> None:
        ...
    @property
    def LineWidth(self) -> int:
        """
        Is only used for line-chart types.
        """
        ...
    @LineWidth.setter
    def LineWidth(self, value: int) -> None:
        ...
    @property
    def NumberFormat(self) -> int:
        """
        specifies a number format for the display of the value in the data label
        """
        ...
    @NumberFormat.setter
    def NumberFormat(self, value: int) -> None:
        ...
    @property
    def Offset(self) -> float:
        """
        describes a value by which a data point is moved from its default position in percent of the maximum allowed distance.
        
        This is especially useful for the explosion of pie-chart segments.
        """
        ...
    @Offset.setter
    def Offset(self, value: float) -> None:
        ...
    @property
    def PercentDiagonal(self) -> int:
        """
        A value between 0 and 100 indicating the percentage how round an edge should be.
        """
        ...
    @PercentDiagonal.setter
    def PercentDiagonal(self, value: int) -> None:
        ...
    @property
    def PercentageNumberFormat(self) -> int:
        """
        specifies a number format for the display of the percentage value in the data label
        """
        ...
    @PercentageNumberFormat.setter
    def PercentageNumberFormat(self, value: int) -> None:
        ...
    @property
    def ReferencePageSize(self) -> Size_576707ef:
        """
        The size of the page at the moment when the font size for data labels was set.
        
        This size is used to resize text in the view when the size of the page has changed since the font sizes were set (automatic text scaling).
        """
        ...
    @ReferencePageSize.setter
    def ReferencePageSize(self, value: Size_576707ef) -> None:
        ...
    @property
    def ShowErrorBox(self) -> bool:
        """
        In case ErrorBarX and ErrorBarY both are set, and error bars are shown, a box spanning all error-indicators is rendered.
        """
        ...
    @ShowErrorBox.setter
    def ShowErrorBox(self, value: bool) -> None:
        ...
    @property
    def Symbol(self) -> Symbol_83c109c2:
        """
        """
        ...
    @Symbol.setter
    def Symbol(self, value: Symbol_83c109c2) -> None:
        ...
    @property
    def TextWordWrap(self) -> bool:
        """
        specifies if the text of a data label (caption) must be wrapped
        
        **since**
        
            LibreOffice 5.1
        """
        ...
    @TextWordWrap.setter
    def TextWordWrap(self, value: bool) -> None:
        ...
    @property
    def Transparency(self) -> int:
        """
        This is the main transparency value of a data point.
        
        For charts with filled areas, like bar-charts, this should map to the FillTransparence of the objects. For line-charts this should map to the LineTransparence property.
        """
        ...
    @Transparency.setter
    def Transparency(self, value: int) -> None:
        ...
    @property
    def TransparencyGradient(self) -> Gradient_7a8a0982:
        """
        This describes the transparency of the fill area as a gradient.
        """
        ...
    @TransparencyGradient.setter
    def TransparencyGradient(self, value: Gradient_7a8a0982) -> None:
        ...
    @property
    def TransparencyGradientName(self) -> str:
        """
        """
        ...
    @TransparencyGradientName.setter
    def TransparencyGradientName(self, value: str) -> None:
        ...
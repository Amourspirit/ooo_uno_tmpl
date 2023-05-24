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
from ..beans.property_set import PropertySet as PropertySet_b0e70ba2
from .x_legend import XLegend as XLegend_8cce09f3
from ..drawing.fill_properties import FillProperties as FillProperties_f1200da8
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from .relative_position import RelativePosition as RelativePosition_fae10ddd
    from com.sun.star.chart2.LegendPosition import LegendPositionProto
    from com.sun.star.chart.ChartLegendExpansion import ChartLegendExpansionProto

class Legend(PropertySet_b0e70ba2, FillProperties_f1200da8, LineProperties_f13f0da9, XLegend_8cce09f3):
    """
    Service Class

    Describes a legend for a Diagram.
    
    **since**
    
        LibreOffice 7.0

    See Also:
        `API Legend <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1Legend.html>`_
    """
    @property
    def AnchorPosition(self) -> LegendPositionProto:
        """
        Provides an automated position.
        """
        ...
    @AnchorPosition.setter
    def AnchorPosition(self, value: LegendPositionProto) -> None:
        ...
    @property
    def Expansion(self) -> ChartLegendExpansionProto:
        """
        Determines how the aspect ratio of the legend should roughly be.
        
        Set the Expansion to com.sun.star.chart.HIGH for a legend that is positioned on the right or left hand side. Use com.sun.star.chart.WIDE for a legend that is positioned on top or the bottom.
        """
        ...
    @Expansion.setter
    def Expansion(self, value: ChartLegendExpansionProto) -> None:
        ...
    @property
    def Overlay(self) -> bool:
        """
        Determines, whether the legend should overlay the chart.
        
        **since**
        
            LibreOffice 7.0
        """
        ...
    @Overlay.setter
    def Overlay(self, value: bool) -> None:
        ...
    @property
    def ReferencePageSize(self) -> Size_576707ef:
        """
        contains the size of the page at the time when properties were set (e.g.
        
        the CharHeight).
        
        This way it is possible to resize objects (like text) in the view without modifying the model.
        """
        ...
    @ReferencePageSize.setter
    def ReferencePageSize(self, value: Size_576707ef) -> None:
        ...
    @property
    def RelativePosition(self) -> RelativePosition_fae10ddd:
        """
        The position is as a relative position on the page.
        
        If a relative position is given the legend is not automatically placed, but instead is placed relative on the page.
        
        If VOID, the legend position is solely determined by the AnchorPosition.
        """
        ...
    @RelativePosition.setter
    def RelativePosition(self, value: RelativePosition_fae10ddd) -> None:
        ...
    @property
    def Show(self) -> bool:
        """
        Determines, whether the legend should be rendered by the view.
        """
        ...
    @Show.setter
    def Show(self, value: bool) -> None:
        ...


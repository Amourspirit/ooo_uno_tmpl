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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.chart
import typing
from ..drawing.shape import Shape as Shape_85cc09e5
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222
if typing.TYPE_CHECKING:
    from .chart_legend_position import ChartLegendPosition as ChartLegendPosition_18bc0eb0

class ChartLegend(Shape_85cc09e5, CharacterProperties_1d4f0ef3, UserDefinedAttributesSupplier_9fbe1222):
    """
    Service Class

    specifies the legend of a chart.
    
    The text/font properties which are specified in the service com.sun.star.drawing.Shape correlate to all text objects inside the legend.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ChartLegend <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartLegend.html>`_
    """
    @property
    def Alignment(self) -> 'ChartLegendPosition_18bc0eb0':
        """
        determines the alignment of the legend relative to the diagram.
        """
        ...
    @property
    def AutomaticPosition(self) -> bool:
        """
        If this property is TRUE the position is calculated by the application automatically.
        
        Setting this property to false will have no effect. Instead use the interface com.sun.star.drawing.XShape to set a concrete position.
        """
        ...



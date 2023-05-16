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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.4
import uno
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoEnumMeta
    class ChartLegendPosition(metaclass=UnoEnumMeta, type_name="com.sun.star.chart.ChartLegendPosition", name_space="com.sun.star.chart"):
        """Dynamically created class that represents ``com.sun.star.chart.ChartLegendPosition`` Enum. Class loosly mimics Enum"""
        pass
else:
    from com.sun.star.chart.ChartLegendPosition import BOTTOM as CHART_LEGEND_POSITION_BOTTOM
    from com.sun.star.chart.ChartLegendPosition import LEFT as CHART_LEGEND_POSITION_LEFT
    from com.sun.star.chart.ChartLegendPosition import NONE as CHART_LEGEND_POSITION_NONE
    from com.sun.star.chart.ChartLegendPosition import RIGHT as CHART_LEGEND_POSITION_RIGHT
    from com.sun.star.chart.ChartLegendPosition import TOP as CHART_LEGEND_POSITION_TOP


    class ChartLegendPosition(uno.Enum):
        """
        Enum Class


        See Also:
            `API ChartLegendPosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a65c2b55fdf73cbbf2fdcfef7d305b6c3>`_
        """
        __ooo_ns__: str = 'com.sun.star.chart'
        __ooo_full_ns__: str = 'com.sun.star.chart.ChartLegendPosition'
        __ooo_type_name__: str = 'enum'

        @property
        def typeName(self) -> str:
            return 'com.sun.star.chart.ChartLegendPosition'

        BOTTOM = CHART_LEGEND_POSITION_BOTTOM
        """
        displays the chart legend beneath the diagram.
        """
        LEFT = CHART_LEGEND_POSITION_LEFT
        """
        displays the chart legend on the left side of the diagram.
        """
        NONE = CHART_LEGEND_POSITION_NONE
        """
        error indicators are not displayed.
        
        displays no regression curve.
        
        no chart legend is displayed.
        
        displays no error indicators.
        """
        RIGHT = CHART_LEGEND_POSITION_RIGHT
        """
        displays the chart legend on the right side of the diagram.
        """
        TOP = CHART_LEGEND_POSITION_TOP
        """
        displays the chart legend above the diagram.
        """

__all__ = ['ChartLegendPosition']


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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.4
from __future__ import annotations
import uno


class ChartLegendExpansion(uno.Enum):
    """
    Enum


    See Also:
        `API ChartLegendExpansion <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#ab1908f844354e32092fdec03c1b9b513>`_
    """
    typeName: str = 'com.sun.star.chart.ChartLegendExpansion'

    BALANCED: PyiChartLegendExpansion = ...
    """
    The legend entries are arranged in a way that the aspect ratio of the resulting legend is as near to 1 as possible.
    """
    CUSTOM: PyiChartLegendExpansion = ...
    """
    The size of the legend is given explicitly.
    """
    HIGH: PyiChartLegendExpansion = ...
    """
    The legend entries are stacked in a single column if possible.
    
    If not enough space is available further columns are added.
    """
    WIDE: PyiChartLegendExpansion = ...
    """
    The legend entries are arranged in a single row if possible.
    
    If not enough space is available further rows are added.
    """


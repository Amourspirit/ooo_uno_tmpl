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
    class ChartErrorIndicatorType(metaclass=UnoEnumMeta, type_name="com.sun.star.chart.ChartErrorIndicatorType", name_space="com.sun.star.chart"):
        """Dynamically created class that represents ``com.sun.star.chart.ChartErrorIndicatorType`` Enum. Class loosly mimics Enum"""
        pass
else:
    from com.sun.star.chart.ChartErrorIndicatorType import LOWER as CHART_ERROR_INDICATOR_TYPE_LOWER
    from com.sun.star.chart.ChartErrorIndicatorType import NONE as CHART_ERROR_INDICATOR_TYPE_NONE
    from com.sun.star.chart.ChartErrorIndicatorType import TOP_AND_BOTTOM as CHART_ERROR_INDICATOR_TYPE_TOP_AND_BOTTOM
    from com.sun.star.chart.ChartErrorIndicatorType import UPPER as CHART_ERROR_INDICATOR_TYPE_UPPER


    class ChartErrorIndicatorType(uno.Enum):
        """
        Enum Class


        See Also:
            `API ChartErrorIndicatorType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a1391f7495aa3a95d4bc29dbf29a809ea>`_
        """
        __ooo_ns__: str = 'com.sun.star.chart'
        __ooo_full_ns__: str = 'com.sun.star.chart.ChartErrorIndicatorType'
        __ooo_type_name__: str = 'enum'

        @property
        def typeName(self) -> str:
            return 'com.sun.star.chart.ChartErrorIndicatorType'

        LOWER = CHART_ERROR_INDICATOR_TYPE_LOWER
        """
        displays only the lower value.
        """
        NONE = CHART_ERROR_INDICATOR_TYPE_NONE
        """
        error indicators are not displayed.
        
        displays no regression curve.
        
        no chart legend is displayed.
        
        displays no error indicators.
        """
        TOP_AND_BOTTOM = CHART_ERROR_INDICATOR_TYPE_TOP_AND_BOTTOM
        """
        displays both the upper and lower values.
        """
        UPPER = CHART_ERROR_INDICATOR_TYPE_UPPER
        """
        displays only the upper value.
        """

__all__ = ['ChartErrorIndicatorType']


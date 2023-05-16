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
from enum import Enum


class ChartAxisArrangeOrderType(Enum):
    """
    Enum Class


    See Also:
        `API ChartAxisArrangeOrderType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a9c06520c0f143b00b5aaafeb4772dc39>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartAxisArrangeOrderType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.chart.ChartAxisArrangeOrderType'

    AUTO = 'AUTO'
    """
    The descriptions are arranged automatically.
    """
    SIDE_BY_SIDE = 'SIDE_BY_SIDE'
    """
    The descriptions are arranged side by side.
    """
    STAGGER_EVEN = 'STAGGER_EVEN'
    """
    The descriptions are alternately put on two lines with the even values out of the normal line.
    """
    STAGGER_ODD = 'STAGGER_ODD'
    """
    The descriptions are alternately put on two lines with the odd values out of the normal line.
    """

__all__ = ['ChartAxisArrangeOrderType']


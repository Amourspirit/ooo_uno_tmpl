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
from typing import cast
from enum import Enum
from com.sun.star.chart.ChartDataRowSource import ChartDataRowSourceProto

class ChartDataRowSource(Enum):
    """
    Enum Class


    See Also:
        `API ChartDataRowSource <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a0fb4f8088715abb6eb51a29c4bd79cce>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartDataRowSource'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.chart.ChartDataRowSource'

    COLUMNS = cast(ChartDataRowSourceProto, 'COLUMNS')
    """
    values displayed as data rows are taken from the columns of the data source.
    """
    ROWS = cast(ChartDataRowSourceProto, 'ROWS')
    """
    values displayed as data rows are taken from the rows of the data source.
    """

__all__ = ['ChartDataRowSource']


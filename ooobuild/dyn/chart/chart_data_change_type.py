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
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class ChartDataChangeType(metaclass=UnoEnumMeta, type_name="com.sun.star.chart.ChartDataChangeType", name_space="com.sun.star.chart"):
        """Dynamically created class that represents ``com.sun.star.chart.ChartDataChangeType`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.chart.ChartDataChangeType import ALL as CHART_DATA_CHANGE_TYPE_ALL
        from com.sun.star.chart.ChartDataChangeType import COLUMN_DELETED as CHART_DATA_CHANGE_TYPE_COLUMN_DELETED
        from com.sun.star.chart.ChartDataChangeType import COLUMN_INSERTED as CHART_DATA_CHANGE_TYPE_COLUMN_INSERTED
        from com.sun.star.chart.ChartDataChangeType import DATA_RANGE as CHART_DATA_CHANGE_TYPE_DATA_RANGE
        from com.sun.star.chart.ChartDataChangeType import ROW_DELETED as CHART_DATA_CHANGE_TYPE_ROW_DELETED
        from com.sun.star.chart.ChartDataChangeType import ROW_INSERTED as CHART_DATA_CHANGE_TYPE_ROW_INSERTED

        class ChartDataChangeType(uno.Enum):
            """
            Enum Class


            See Also:
                `API ChartDataChangeType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a37b4d47e7d1600aa406ad115a39fe1da>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.chart.ChartDataChangeType', value)

            __ooo_ns__: str = 'com.sun.star.chart'
            __ooo_full_ns__: str = 'com.sun.star.chart.ChartDataChangeType'
            __ooo_type_name__: str = 'enum'

            ALL = CHART_DATA_CHANGE_TYPE_ALL
            """
            Major changes were applied to the data.
            """
            COLUMN_DELETED = CHART_DATA_CHANGE_TYPE_COLUMN_DELETED
            """
            The column given in the ChartDataChangeEvent, was deleted.
            """
            COLUMN_INSERTED = CHART_DATA_CHANGE_TYPE_COLUMN_INSERTED
            """
            The column given in the ChartDataChangeEvent, was inserted.
            """
            DATA_RANGE = CHART_DATA_CHANGE_TYPE_DATA_RANGE
            """
            The range of columns and rows, given in the ChartDataChangeEvent, has changed.
            """
            ROW_DELETED = CHART_DATA_CHANGE_TYPE_ROW_DELETED
            """
            The row given in the ChartDataChangeEvent, was deleted.
            """
            ROW_INSERTED = CHART_DATA_CHANGE_TYPE_ROW_INSERTED
            """
            The row given in the ChartDataChangeEvent, was inserted.
            """
    else:
        # keep document generators happy
        from ...lo.chart.chart_data_change_type import ChartDataChangeType as ChartDataChangeType


__all__ = ['ChartDataChangeType']

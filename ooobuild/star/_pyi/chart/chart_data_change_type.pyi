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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API ChartDataChangeType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a37b4d47e7d1600aa406ad115a39fe1da>`_
"""

ALL: 'uno.Enum'
"""
Major changes were applied to the data.
"""
COLUMN_DELETED: 'uno.Enum'
"""
The column given in the ChartDataChangeEvent, was deleted.
"""
COLUMN_INSERTED: 'uno.Enum'
"""
The column given in the ChartDataChangeEvent, was inserted.
"""
DATA_RANGE: 'uno.Enum'
"""
The range of columns and rows, given in the ChartDataChangeEvent, has changed.
"""
ROW_DELETED: 'uno.Enum'
"""
The row given in the ChartDataChangeEvent, was deleted.
"""
ROW_INSERTED: 'uno.Enum'
"""
The row given in the ChartDataChangeEvent, was inserted.
"""


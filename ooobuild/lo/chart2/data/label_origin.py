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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2.data
# Libre Office Version: 2024.2
from __future__ import annotations
from enum import Enum


class LabelOrigin(Enum):
    """
    Enum Class


    See Also:
        `API LabelOrigin <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2_1_1data.html#a2afe9ba95ad4b3631057b40391bed0aa>`_
    """
    __ooo_ns__: str = "com.sun.star.chart2.data"
    __ooo_full_ns__: str = "com.sun.star.chart2.data.LabelOrigin"
    __ooo_type_name__: str = "enum"

    @property
    def typeName(self) -> str:
        return "com.sun.star.chart2.data.LabelOrigin"

    COLUMN = "COLUMN"
    """
    Uses the column name for label generation.
    
    A spreadsheet range A1:A6 could, e.g., result in \"Column A\".
    
    If a range consists of more than one column the result of label generation may be empty. Of course, it could also succeed with a string like \"Columns A to B\".
    """
    LONG_SIDE = "LONG_SIDE"
    """
    This is exactly the opposite of SHORT_SIDE.
    
    I.e., if SHORT_SIDE has the same effect as ROW, LONG_SIDE will have the same effect as COLUMN and the other way round.
    """
    ROW = "ROW"
    """
    Uses the column name for label generation.
    
    A spreadsheet range A2:D2 could, e.g., result in \"Row 2\".
    
    If a range consists of more than one row the result of label generation may be empty. Of course, it could also succeed with a string like \"Rows 1-3\".
    """
    SHORT_SIDE = "SHORT_SIDE"
    """
    If a range spans a single row over more than one column, this parameter has the same effect as ROW.
    
    If the range spans a single column over more than one row, this is the same as COLUMN.
    
    In case of a range spanning more than one column and row, the shorter range of both should be used (e.g. a spreadsheet range A1:B10 should treat columns as short side).
    
    In case of a rectangular range, or a range that is composed of more than one contiguous sub-regions, the short side cannot be determined, thus XDataSequence.generateLabel() will return an empty sequence.
    """

__all__ = ["LabelOrigin"]


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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_sheet_cell_ranges import XSheetCellRanges as XSheetCellRanges_edef0d52
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43


class XCellRangesQuery(XInterface_8f010a43):
    """
    provides methods to query for cell ranges with specific contents.
    
    All methods return a collection of cell ranges.

    See Also:
        `API XCellRangesQuery <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XCellRangesQuery.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XCellRangesQuery'

    def queryColumnDifferences(self, aCompare: CellAddress_ae5f0b56) -> XSheetCellRanges_edef0d52:
        """
        queries all cells with different values in a specified row.
        
        This method takes each column of the current cell range(s) and compares all cells with the cell in the specified row. All cells which are different to this comparison cell will be returned.
        """
        ...
    def queryContentCells(self, nContentFlags: int) -> XSheetCellRanges_edef0d52:
        """
        queries all cells with the specified content type(s).
        
        Attention: Despite the CellFlags flags are long values, this method expects a short parameter.
        
        Attention: Empty cells in the range may be skipped depending on the content flag used. For instance, when querying for STYLES, the returned ranges may not include empty cells even if styles are applied to those cells.
        """
        ...
    def queryEmptyCells(self) -> XSheetCellRanges_edef0d52:
        """
        queries all empty cells.
        """
        ...
    def queryFormulaCells(self, nResultFlags: int) -> XSheetCellRanges_edef0d52:
        """
        queries all formula cells with the specified result type.
        """
        ...
    def queryIntersection(self, aRange: CellRangeAddress_ec450d43) -> XSheetCellRanges_edef0d52:
        """
        intersects the current cell range(s) with the specified cell range.
        """
        ...
    def queryRowDifferences(self, aCompare: CellAddress_ae5f0b56) -> XSheetCellRanges_edef0d52:
        """
        queries all cells with different values in a specified column.
        
        This method takes each row of the current cell range(s) and compares all cells with the cell in the specified column. All cells which are different to this comparison cell will be returned.
        """
        ...
    def queryVisibleCells(self) -> XSheetCellRanges_edef0d52:
        """
        queries all visible cells.
        """
        ...



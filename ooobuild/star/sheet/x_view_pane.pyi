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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43


class XViewPane(XInterface_8f010a43):
    """
    represents a pane in a view of a spreadsheet document.

    See Also:
        `API XViewPane <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XViewPane.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XViewPane'

    def getFirstVisibleColumn(self) -> int:
        """
        returns the first column that is visible in the pane.
        """
        ...
    def getFirstVisibleRow(self) -> int:
        """
        returns the first row that is visible in the pane.
        """
        ...
    def getVisibleRange(self) -> CellRangeAddress_ec450d43:
        """
        returns the address of the cell range that consists of the cells which are visible in the pane.
        """
        ...
    def setFirstVisibleColumn(self, nFirstVisibleColumn: int) -> None:
        """
        sets the first column that is visible in the pane.
        """
        ...
    def setFirstVisibleRow(self, nFirstVisibleRow: int) -> None:
        """
        sets the first row that is visible in the pane.
        """
        ...



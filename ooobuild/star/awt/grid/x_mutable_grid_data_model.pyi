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
# Namespace: com.sun.star.awt.grid
from __future__ import annotations
import typing

import uno
from .x_grid_data_model import XGridDataModel as XGridDataModel_f8b20d71
if typing.TYPE_CHECKING:
    from .x_grid_data_listener import XGridDataListener as XGridDataListener_23f10ec6


class XMutableGridDataModel(XGridDataModel_f8b20d71):
    """
    allows to modify the data represented by a XGridDataModel

    See Also:
        `API XMutableGridDataModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XMutableGridDataModel.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.grid.XMutableGridDataModel'

    def addGridDataListener(self, Listener: XGridDataListener_23f10ec6) -> None:
        """
        registers listener to be notified of data changes in the model
        """
        ...
    def addRow(self, Heading: typing.Any, Data: typing.Tuple[object, ...]) -> None:
        """
        appends a row to the model.
        """
        ...
    def addRows(self, Headings: typing.Tuple[object, ...], Data: typing.Tuple[typing.Tuple[object, ...], ...]) -> None:
        """
        appends multiple rows of data to the model.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def insertRow(self, Index: int, Heading: typing.Any, Data: typing.Tuple[object, ...]) -> None:
        """
        inserts a row into the set of data rows

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def insertRows(self, Index: int, Headings: typing.Tuple[object, ...], Data: typing.Tuple[typing.Tuple[object, ...], ...]) -> None:
        """
        inserts multiple rows of data into the model.

        Raises:
            : ````
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def removeAllRows(self) -> None:
        """
        Removes all rows from the model.
        """
        ...
    def removeGridDataListener(self, Listener: XGridDataListener_23f10ec6) -> None:
        """
        revokes a listener which was previously registered via addGridDataListener()
        """
        ...
    def removeRow(self, RowIndex: int) -> None:
        """
        removes a row of data from the model

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def updateCellData(self, ColumnIndex: int, RowIndex: int, Value: typing.Any) -> None:
        """
        updates the content of the given cell

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def updateCellToolTip(self, ColumnIndex: int, RowIndex: int, Value: typing.Any) -> None:
        """
        updates the tooltip to be displayed for a given cell

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def updateRowData(self, ColumnIndexes: uno.ByteSequence, RowIndex: int, Values: typing.Tuple[object, ...]) -> None:
        """
        updates the content of a given row.
        
        The change in the data model will be notified to registered listeners via XGridDataListener.dataChanged(). The GridDataEvent.FirstColumn and GridDataEvent.LastColumn will denote the smallest respectively largest column index from ColumnIndexes.

        Raises:
            : ````
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def updateRowHeading(self, RowIndex: int, Heading: typing.Any) -> None:
        """
        sets a new title for a given row.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def updateRowToolTip(self, RowIndex: int, Value: typing.Any) -> None:
        """
        updates the tooltip for all cells of a given row
        
        Effectively this method is a shortcut for calling updateCellToolTip() multiple times in a row, for all cells of a given row.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...



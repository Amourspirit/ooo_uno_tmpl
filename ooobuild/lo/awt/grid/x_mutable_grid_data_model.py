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
from abc import abstractmethod
from .x_grid_data_model import XGridDataModel as XGridDataModel_f8b20d71
if typing.TYPE_CHECKING:
    from .x_grid_data_listener import XGridDataListener as XGridDataListener_23f10ec6

class XMutableGridDataModel(XGridDataModel_f8b20d71):
    """
    allows to modify the data represented by a XGridDataModel

    See Also:
        `API XMutableGridDataModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XMutableGridDataModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.XMutableGridDataModel'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.grid.XMutableGridDataModel'

    @abstractmethod
    def addGridDataListener(self, Listener: XGridDataListener_23f10ec6) -> None:
        """
        registers listener to be notified of data changes in the model
        """
        ...
    @abstractmethod
    def addRow(self, Heading: object, Data: typing.Tuple[object, ...]) -> None:
        """
        appends a row to the model.
        """
        ...
    @abstractmethod
    def addRows(self, Headings: typing.Tuple[object, ...], Data: typing.Tuple[typing.Tuple[object, ...], ...]) -> None:
        """
        appends multiple rows of data to the model.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def insertRow(self, Index: int, Heading: object, Data: typing.Tuple[object, ...]) -> None:
        """
        inserts a row into the set of data rows

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def insertRows(self, Index: int, Headings: typing.Tuple[object, ...], Data: typing.Tuple[typing.Tuple[object, ...], ...]) -> None:
        """
        inserts multiple rows of data into the model.

        Raises:
            : ````
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def removeAllRows(self) -> None:
        """
        Removes all rows from the model.
        """
        ...
    @abstractmethod
    def removeGridDataListener(self, Listener: XGridDataListener_23f10ec6) -> None:
        """
        revokes a listener which was previously registered via addGridDataListener()
        """
        ...
    @abstractmethod
    def removeRow(self, RowIndex: int) -> None:
        """
        removes a row of data from the model

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def updateCellData(self, ColumnIndex: int, RowIndex: int, Value: object) -> None:
        """
        updates the content of the given cell

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def updateCellToolTip(self, ColumnIndex: int, RowIndex: int, Value: object) -> None:
        """
        updates the tooltip to be displayed for a given cell

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def updateRowData(self, ColumnIndexes: typing.Tuple[int, ...], RowIndex: int, Values: typing.Tuple[object, ...]) -> None:
        """
        updates the content of a given row.
        
        The change in the data model will be notified to registered listeners via XGridDataListener.dataChanged(). The GridDataEvent.FirstColumn and GridDataEvent.LastColumn will denote the smallest respectively largest column index from ColumnIndexes.

        Raises:
            : ````
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def updateRowHeading(self, RowIndex: int, Heading: object) -> None:
        """
        sets a new title for a given row.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def updateRowToolTip(self, RowIndex: int, Value: object) -> None:
        """
        updates the tooltip for all cells of a given row
        
        Effectively this method is a shortcut for calling updateCellToolTip() multiple times in a row, for all cells of a given row.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...

__all__ = ['XMutableGridDataModel']


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
# Namespace: com.sun.star.awt.grid
from typing_extensions import Literal
import typing
from abc import ABC

class XSortableGridData(ABC):
    """
    allows to sort the data represented by a XGridDataModel

    See Also:
        `API XSortableGridData <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XSortableGridData.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.grid.XSortableGridData']

    def getCurrentSortOrder(self) -> 'typing.Tuple[int, bool]':
        """
        returns the current sort order.
        """
        ...
    def removeColumnSort(self) -> None:
        """
        removes any possibly present sorting of the grid data
        """
        ...
    def sortByColumn(self, ColumnIndex: int, SortAscending: bool) -> None:
        """
        sorts the rows represented by the model by a given column's data.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...



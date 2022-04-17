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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .cell_insert_mode import CellInsertMode as CellInsertMode_d47d0c9b
    from .paste_operation import PasteOperation as PasteOperation_d5de0ccf
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XSheetPastable(XInterface_8f010a43):
    """
    represents a sheet into which contents of the clipboard can be pasted.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XSheetPastable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetPastable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSheetPastable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetPastable'

    @abstractmethod
    def paste(self, aDestination: 'CellAddress_ae5f0b56') -> None:
        """
        pastes the contents of the clipboard at the specified position on the sheet.
        """
    @abstractmethod
    def pasteCellRange(self, aDestination: 'CellRangeAddress_ec450d43', nOperation: 'PasteOperation_d5de0ccf', nContents: int, bSkipEmpty: bool, bTranspose: bool, bAsLink: bool, nInsert: 'CellInsertMode_d47d0c9b') -> None:
        """
        pastes clipboard data from a cell range into another cell range.
        
        The contents of the clipboard must be from a cell range.
        """
    @abstractmethod
    def pasteFormat(self, aDestination: 'CellAddress_ae5f0b56', aFormat: str) -> None:
        """
        pastes the contents of the clipboard at the specified position on the sheet, using the specified format.
        """

__all__ = ['XSheetPastable']


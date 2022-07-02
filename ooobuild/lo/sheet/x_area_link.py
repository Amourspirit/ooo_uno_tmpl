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
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XAreaLink(XInterface_8f010a43):
    """
    provides methods to change the settings of a linked cell range.

    See Also:
        `API XAreaLink <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XAreaLink.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XAreaLink'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XAreaLink'

    @abstractmethod
    def getDestArea(self) -> 'CellRangeAddress_ec450d43':
        """
        returns the position of the linked range in the destination document.
        """
        ...
    @abstractmethod
    def getSourceArea(self) -> str:
        """
        returns the source of the range within the source document.
        
        This can be the address of a cell or range in the form \"Sheet1.A1:C5\", or the name of a named range or database range.
        """
        ...
    @abstractmethod
    def setDestArea(self, aDestArea: 'CellRangeAddress_ec450d43') -> None:
        """
        sets the position of the linked range in the destination document.
        """
        ...
    @abstractmethod
    def setSourceArea(self, aSourceArea: str) -> None:
        """
        sets the source of the range within the source document.
        
        This can be the address of a cell or range in the form \"Sheet1.A1:C5\", or the name of a named range or database range.
        """
        ...

__all__ = ['XAreaLink']


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
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .general_function import GeneralFunction as GeneralFunction_e2280d25
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XConsolidationDescriptor(XInterface_8f010a43):
    """
    provides access to the settings of a consolidation descriptor.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XConsolidationDescriptor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XConsolidationDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XConsolidationDescriptor'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XConsolidationDescriptor'

    @abstractmethod
    def getFunction(self) -> 'GeneralFunction_e2280d25':
        """
        returns the function by which the ranges are consolidated.
        """
        ...
    @abstractmethod
    def getInsertLinks(self) -> bool:
        """
        returns, whether links to the original data are inserted in the output area or not.
        """
        ...
    @abstractmethod
    def getSources(self) -> 'typing.Tuple[CellRangeAddress_ec450d43, ...]':
        """
        returns the cell ranges which are consolidated.
        """
        ...
    @abstractmethod
    def getStartOutputPosition(self) -> 'CellAddress_ae5f0b56':
        """
        returns the position of the top left cell of the cell range where the consolidated data are copied.
        """
        ...
    @abstractmethod
    def getUseColumnHeaders(self) -> bool:
        """
        returns, whether column headers from the cell ranges are used to find matching data or not.
        """
        ...
    @abstractmethod
    def getUseRowHeaders(self) -> bool:
        """
        returns, whether row headers from the cell ranges are used to find matching data or not.
        """
        ...
    @abstractmethod
    def setFunction(self, nFunction: 'GeneralFunction_e2280d25') -> None:
        """
        sets the function by which the ranges are consolidated.
        """
        ...
    @abstractmethod
    def setInsertLinks(self, bInsertLinks: bool) -> None:
        """
        specifies if links to the original data are inserted in the output area.
        """
        ...
    @abstractmethod
    def setSources(self, aSources: 'typing.Tuple[CellRangeAddress_ec450d43, ...]') -> None:
        """
        sets the cell ranges which are consolidated.
        """
        ...
    @abstractmethod
    def setStartOutputPosition(self, aStartOutputPosition: 'CellAddress_ae5f0b56') -> None:
        """
        sets the position of the top left cell of the cell range where the consolidated data are copied.
        """
        ...
    @abstractmethod
    def setUseColumnHeaders(self, bUseColumnHeaders: bool) -> None:
        """
        specifies if column headers from the cell ranges are used to find matching data.
        """
        ...
    @abstractmethod
    def setUseRowHeaders(self, bUseRowHeaders: bool) -> None:
        """
        specifies if row headers from the cell ranges are used to find matching data.
        """
        ...

__all__ = ['XConsolidationDescriptor']


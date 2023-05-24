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
from abc import abstractmethod
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
if typing.TYPE_CHECKING:
    from .x_data_pilot_descriptor import XDataPilotDescriptor as XDataPilotDescriptor_27650f1a
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56

class XDataPilotTables(XNameAccess_e2ab0cf6):
    """
    provides access to the data pilot tables via name and inserting and removing data pilot tables.
    
    This interface extends the interface com.sun.star.container.XNameAccess which provides access to existing data pilot tables in the collection.

    See Also:
        `API XDataPilotTables <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XDataPilotTables.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XDataPilotTables'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XDataPilotTables'

    @abstractmethod
    def createDataPilotDescriptor(self) -> XDataPilotDescriptor_27650f1a:
        """
        creates a data pilot descriptor.
        
        This descriptor can be used with XDataPilotTables.addTable().
        """
        ...
    @abstractmethod
    def insertNewByName(self, aName: str, OutputAddress: CellAddress_ae5f0b56, xDescriptor: XDataPilotDescriptor_27650f1a) -> None:
        """
        creates a new data pilot table and adds it to the collection.
        """
        ...
    @abstractmethod
    def removeByName(self, aName: str) -> None:
        """
        deletes a data pilot table from the collection.
        """
        ...

__all__ = ['XDataPilotTables']


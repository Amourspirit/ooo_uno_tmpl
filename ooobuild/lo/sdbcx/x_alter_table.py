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
# Namespace: com.sun.star.sdbcx
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XAlterTable(XInterface_8f010a43):
    """
    is used for creating and appending new objects to a specific container.

    See Also:
        `API XAlterTable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbcx_1_1XAlterTable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.XAlterTable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbcx.XAlterTable'

    @abstractmethod
    def alterColumnByIndex(self, index: int, descriptor: XPropertySet_bc180bfa) -> None:
        """
        is intended to alter an existing column identified by its position.
        
        This operation must be atomic, in that it is done in one step.s

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def alterColumnByName(self, colName: str, descriptor: XPropertySet_bc180bfa) -> None:
        """
        is intended to alter an existing column identified by its name.
        
        This operation must be atomic, in that it is done in one step.s

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...

__all__ = ['XAlterTable']


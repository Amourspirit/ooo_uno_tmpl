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
# Namespace: com.sun.star.sdb.tools
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_connection_supplier import XConnectionSupplier as XConnectionSupplier_57f3105c
if typing.TYPE_CHECKING:
    from ...beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XViewAccess(XConnectionSupplier_57f3105c):
    """
    allows to fetch and to change the sql statements of views
    
    **since**
    
        OOo 3.3

    See Also:
        `API XViewAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1tools_1_1XViewAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb.tools'
    __ooo_full_ns__: str = 'com.sun.star.sdb.tools.XViewAccess'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.tools.XViewAccess'

    @abstractmethod
    def alterCommand(self, view: XPropertySet_bc180bfa, command: str) -> None:
        """
        allows to alter the SQL statement of a view

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getCommand(self, view: XPropertySet_bc180bfa) -> str:
        """
        returns the SQL statement of the view

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...

__all__ = ['XViewAccess']



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
from abc import abstractproperty
from ...lang.x_initialization import XInitialization as XInitialization_d46c0cca
if typing.TYPE_CHECKING:
    from ...sdbc.x_connection import XConnection as XConnection_a36a0b0c

class XConnectionSupplier(XInitialization_d46c0cca):
    """
    allows to access the active connection
    
    **since**
    
        OOo 3.3

    See Also:
        `API XConnectionSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1tools_1_1XConnectionSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb.tools'
    __ooo_full_ns__: str = 'com.sun.star.sdb.tools.XConnectionSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.tools.XConnectionSupplier'

    @abstractproperty
    def ActiveConnection(self) -> XConnection_a36a0b0c:
        """
        returns the source connection.
        """
        ...


__all__ = ['XConnectionSupplier']



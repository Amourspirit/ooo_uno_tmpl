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
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_connection import XConnection as XConnection_a36a0b0c

class XDriverManager(XInterface_8f010a43):
    """
    is the basic interface for managing a set of SDBC drivers.
    
    When the method com.sun.star.sdbc.XDriverManager.getConnection() is called, the DriverManager will attempt to locate a suitable driver.

    See Also:
        `API XDriverManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XDriverManager.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdbc.XDriverManager']

    def getConnection(self, url: str) -> 'XConnection_a36a0b0c':
        """
        attempts to establish a connection to the given database URL.
        
        The DriverManager attempts to select an appropriate driver from the set of registered JDBC/SDBC drivers.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getConnectionWithInfo(self, url: str, info: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'XConnection_a36a0b0c':
        """
        attempts to establish a connection to the given database URL.
        
        The DriverManager attempts to select an appropriate driver from the set of registered JDBC/SDBC drivers.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getLoginTimeout(self) -> int:
        """
        gets the maximum time in seconds that a driver can wait when attempting to login to a database.
        """
        ...
    def setLoginTimeout(self, seconds: int) -> None:
        """
        sets the maximum time in seconds that a driver will wait while attempting to connect to a database.
        """
        ...



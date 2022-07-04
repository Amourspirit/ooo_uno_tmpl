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
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_connection import XConnection as XConnection_a36a0b0c
    from .x_result_set import XResultSet as XResultSet_98e30aa7

class XStatement(XInterface_8f010a43):
    """
    is used for executing a static SQL statement and obtaining the results produced by it.
    
    Only one ResultSet per Statement can be open at any point in time; therefore, if the reading of one ResultSet is interleaved with the reading of another, each must have been generated by different Statements. All statement execute methods implicitly close a statement's current ResultSet if an open one exists.

    See Also:
        `API XStatement <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XStatement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XStatement'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XStatement'

    @abstractmethod
    def execute(self, sql: str) -> bool:
        """
        executes a SQL statement that may return multiple results.
        
        Under some (uncommon) situations a single SQL statement may return multiple result sets and/or update counts. Normally you can ignore this unless you are (1) executing a stored procedure that you know may return multiple results or (2) you are dynamically executing an unknown SQL string. The navigation through multiple results is covered by com.sun.star.sdbc.XMultipleResults.
        
        The execute method executes a SQL statement and indicates the form of the first result. You can then use com.sun.star.sdbc.XMultipleResults.getResultSet() or com.sun.star.sdbc.XMultipleResults.getUpdateCount() to retrieve the result, and com.sun.star.sdbc.XMultipleResults.getMoreResults() to move to any subsequent result(s).

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def executeQuery(self, sql: str) -> 'XResultSet_98e30aa7':
        """
        executes a SQL statement that returns a single ResultSet.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def executeUpdate(self, sql: str) -> int:
        """
        executes an SQL INSERT, UPDATE, or DELETE statement.
        
        In addition, SQL statements that return nothing, such as SQL DDL statements, can be executed.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getConnection(self) -> 'XConnection_a36a0b0c':
        """
        returns the com.sun.star.sdbc.Connection object that produced this Statement object.

        Raises:
            SQLException: ``SQLException``
        """
        ...

__all__ = ['XStatement']


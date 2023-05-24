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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from __future__ import annotations
import typing
from .result_set import ResultSet as ResultSet_847b09ec
from .x_completed_execution import XCompletedExecution as XCompletedExecution_fb8c0dea
from .x_parameters_supplier import XParametersSupplier as XParametersSupplier_fc7c0e01
from .x_result_set_access import XResultSetAccess as XResultSetAccess_d34d0c96
from .x_row_set_approve_broadcaster import XRowSetApproveBroadcaster as XRowSetApproveBroadcaster_56601044
from ..sdbc.row_set import RowSet as RowSet_70fd0908
from ..sdbc.x_result_set_update import XResultSetUpdate as XResultSetUpdate_e0fb0d0a
from ..sdbcx.x_delete_rows import XDeleteRows as XDeleteRows_af5c0b72
if typing.TYPE_CHECKING:
    from ..sdbc.x_connection import XConnection as XConnection_a36a0b0c

class RowSet(ResultSet_847b09ec, RowSet_70fd0908, XCompletedExecution_fb8c0dea, XParametersSupplier_fc7c0e01, XResultSetAccess_d34d0c96, XRowSetApproveBroadcaster_56601044, XResultSetUpdate_e0fb0d0a, XDeleteRows_af5c0b72):
    """
    Service Class

    is a client side RowSet, which use retrieves is data based on a database table, a query or a SQL command or by a row set reader, who mustn't support SQL.
    
    The connection of the row set is typically a named DataSource or a DataAccess component or a previous instantiated connection.
    
    Depending on the com.sun.star.sdbc.ResultSetConcurrency , the RowSet caches all data or uses an optimized way for retrieving the data, such as, refetching rows by their keys or if provided, by their bookmarks.
    
    In addition, it provides events for RowSet navigation and RowSet modifications to approve the actions and to react on them.
    
    A row set is able to be operated in various ways, and additionally it notifies various changes in its state. Clients of this service can rely on a fixed order of notifications, depending on how they operate on the component.The following describes the general order of all possible notifications which you can encounter when working with a row set:
    
    The following matrix shows the notifications which apply to the different operations:
    
    Via com.sun.star.sdbc.XResultSetUpdate.deleteRow(), you can delete the current row of a RowSet. This deleted row then doesn't vanish immediately, but is still present, and subsequent calls to com.sun.star.sdbc.XResultSet.rowDeleted() will return TRUE. The deleted row \"vanishes\" from the RowSet as soon as the cursor is moved away from it.As a consequence, the behavior of several other methods is affected:

    See Also:
        `API RowSet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1RowSet.html>`_
    """
    @property
    def ActiveCommand(self) -> str:
        """
        is the command which is currently used.
        """
        ...
    @ActiveCommand.setter
    def ActiveCommand(self, value: str) -> None:
        ...
    @property
    def ActiveConnection(self) -> XConnection_a36a0b0c:
        """
        is the connection generated by a DataSource or by a URL.
        
        It could also be set from outside. When set from outside the RowSet is not responsible for the closing of the connection.
        """
        ...
    @ActiveConnection.setter
    def ActiveConnection(self, value: XConnection_a36a0b0c) -> None:
        ...
    @property
    def ApplyFilter(self) -> bool:
        """
        indicates whether the filter should be applied or not, default is FALSE.
        """
        ...
    @ApplyFilter.setter
    def ApplyFilter(self, value: bool) -> None:
        ...
    @property
    def Command(self) -> str:
        """
        is the command which should be executed, the type of command depends on the CommandType.
        
        In case of a CommandType of CommandType.COMMAND, means in case the Command specifies an SQL statement, the inherited com.sun.star.sdbc.RowSet.EscapeProcessing becomes relevant:It then can be to used to specify whether the SQL statement should be analyzed on the client side before sending it to the database server.The default value for com.sun.star.sdbc.RowSet.EscapeProcessing is TRUE. By switching it to FALSE, you can pass backend-specific SQL statements, which are not standard SQL, to your database.
        """
        ...
    @Command.setter
    def Command(self, value: str) -> None:
        ...
    @property
    def CommandType(self) -> int:
        """
        is the type of the command.
        """
        ...
    @CommandType.setter
    def CommandType(self, value: int) -> None:
        ...
    @property
    def DataSourceName(self) -> str:
        """
        is the name of the datasource to use, this could be a named datasource or the URL of a data access component.
        """
        ...
    @DataSourceName.setter
    def DataSourceName(self, value: str) -> None:
        ...
    @property
    def Filter(self) -> str:
        """
        additional filter for a row set.
        """
        ...
    @Filter.setter
    def Filter(self, value: str) -> None:
        ...
    @property
    def GroupBy(self) -> str:
        """
        additional group by for the row set
        """
        ...
    @GroupBy.setter
    def GroupBy(self, value: str) -> None:
        ...
    @property
    def HavingClause(self) -> str:
        """
        additional having clause for the row set
        """
        ...
    @HavingClause.setter
    def HavingClause(self, value: str) -> None:
        ...
    @property
    def IgnoreResult(self) -> bool:
        """
        indicates whether all results should be discarded or not.
        """
        ...
    @IgnoreResult.setter
    def IgnoreResult(self, value: bool) -> None:
        ...
    @property
    def IsModified(self) -> bool:
        """
        indicates that the current row is modified.
        """
        ...
    @IsModified.setter
    def IsModified(self, value: bool) -> None:
        ...
    @property
    def IsNew(self) -> bool:
        """
        indicates that the current row is going to be inserted to the database.
        """
        ...
    @IsNew.setter
    def IsNew(self, value: bool) -> None:
        ...
    @property
    def IsRowCountFinal(self) -> bool:
        """
        indicates that all rows of the row set have been counted.
        """
        ...
    @IsRowCountFinal.setter
    def IsRowCountFinal(self, value: bool) -> None:
        ...
    @property
    def Order(self) -> str:
        """
        is an additional sort order definition for a row set.
        """
        ...
    @Order.setter
    def Order(self, value: str) -> None:
        ...
    @property
    def Privileges(self) -> int:
        """
        indicates the privileges for insert, update, and delete.
        """
        ...
    @Privileges.setter
    def Privileges(self, value: int) -> None:
        ...
    @property
    def RowCount(self) -> int:
        """
        contains the number of rows accessed in the data source.
        """
        ...
    @RowCount.setter
    def RowCount(self, value: int) -> None:
        ...
    @property
    def UpdateCatalogName(self) -> str:
        """
        is the name of the table catalog
        """
        ...
    @UpdateCatalogName.setter
    def UpdateCatalogName(self, value: str) -> None:
        ...
    @property
    def UpdateSchemaName(self) -> str:
        """
        is the name of the table schema.
        """
        ...
    @UpdateSchemaName.setter
    def UpdateSchemaName(self, value: str) -> None:
        ...
    @property
    def UpdateTableName(self) -> str:
        """
        is the name of the table which should be updated, this is usually used for queries which relate to more than one table.
        """
        ...
    @UpdateTableName.setter
    def UpdateTableName(self, value: str) -> None:
        ...


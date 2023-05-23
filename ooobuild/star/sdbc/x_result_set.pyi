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
# Namespace: com.sun.star.sdbc
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XResultSet(XInterface_8f010a43):
    """
    provides the navigation on a table of data.
    
    A com.sun.star.sdbc.ResultSet object is usually generated by executing a com.sun.star.sdbc.Statement.
    
    A ResultSet maintains a cursor pointing to its current row of data. Initially the cursor is positioned before the first row. The \"next\" method moves the cursor to the next row.

    See Also:
        `API XResultSet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XResultSet.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdbc.XResultSet'

    def absolute(self, row: int) -> bool:
        """
        moves the cursor to the given row number in the result set.
        
        If the row number is positive, the cursor moves to the given row number with respect to the beginning of the result set. The first row is row 1, the second is row 2, and so on.
        
        If the given row number is negative, the cursor moves to an absolute row position with respect to the end of the result set. For example, calling absolute(-1) positions the cursor on the last row, absolute(-2) indicates the next-to-last row, and so on.
        
        An attempt to position the cursor beyond the first/last row in the result set leaves the cursor before/after the first/last row, respectively.
        
        Note: Calling absolute(1) is the same as calling com.sun.star.sdbc.XResultSet.first(). Calling moveToPosition(-1) is the same as calling moveToLast().

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def afterLast(self) -> None:
        """
        moves the cursor to the end of the result set, just after the last row.
        
        Has no effect if the result set contains no rows.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def beforeFirst(self) -> None:
        """
        moves the cursor to the front of the result set, just before the first row.
        
        Has no effect if the result set contains no rows.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def first(self) -> bool:
        """
        moves the cursor to the first row in the result set.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getRow(self) -> int:
        """
        retrieves the current row number.
        
        The first row is number 1, the second number 2, and so on.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getStatement(self) -> 'XInterface_8f010a43':
        """
        returns the Statement that produced this com.sun.star.sdbc.ResultSet object.
        
        If the result set was generated some other way, such as by an com.sun.star.sdbc.XDatabaseMetaData method, this method returns NULL.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def isAfterLast(self) -> bool:
        """
        indicates whether the cursor is after the last row in the result set.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def isBeforeFirst(self) -> bool:
        """
        indicates whether the cursor is before the first row in the result set.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def isFirst(self) -> bool:
        """
        indicates whether the cursor is on the first row of the result set.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def isLast(self) -> bool:
        """
        indicates whether the cursor is on the last row of the result set.
        
        Note:  Calling the method isAtLast may be expensive because the SDBC driver might need to fetch ahead one row in order to determine whether the current row is the last row in the result set.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def last(self) -> bool:
        """
        moves the cursor to the last row in the result set.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def next(self) -> bool:
        """
        moves the cursor down one row from its current position.
        
        A ResultSet cursor is initially positioned before the first row; the first call to next makes the first row the current row; the second call makes the second row the current row, and so on.
        
        If an input stream is open for the current row, a call to the method next will implicitly close it. The ResultSet's warning chain is cleared when a new row is read.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def previous(self) -> bool:
        """
        moves the cursor to the previous row in the result set.
        
        Note: previous() is not the same as relative(-1) because it makes sense to call previous() when there is no current row.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def refreshRow(self) -> None:
        """
        refreshes the current row with its most recent value in the database.
        
        Cannot be called when on the insert row. The refreshRow method provides a way for an application to explicitly tell the SDBC driver to refetch a row(s) from the database. An application may want to call refreshRow when caching or prefetching is being done by the SDBC driver to fetch the latest value of a row from the database. The SDBC driver may actually refresh multiple rows at once if the fetch size is greater than one. All values are refetched subject to the transaction isolation level and cursor sensitivity. If refreshRow is called after calling updateXXX , but before calling com.sun.star.sdbc.XResultSet.updateRow() , then the updates made to the row are lost. Calling the method refreshRow frequently will likely slow performance.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def relative(self, rows: int) -> bool:
        """
        moves the cursor a relative number of rows, either positive or negative.
        
        Attempting to move beyond the first/last row in the result set positions the cursor before/after the first/last row. Calling relative(0) is valid, but does not change the cursor position.
        
        Note: Calling relative(1) is different from calling com.sun.star.sdbc.XResultSet.next() because is makes sense to call next() when there is no current row, for example, when the cursor is positioned before the first row or after the last row of the result set.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def rowDeleted(self) -> bool:
        """
        indicates whether a row has been deleted.
        
        A deleted row may leave a visible \"hole\" in a result set. This method can be used to detect holes in a result set. The value returned depends on whether or not the result set can detect deletions.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def rowInserted(self) -> bool:
        """
        indicates whether the current row has had an insertion.
        
        The value returned depends on whether or not the result set can detect visible inserts.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def rowUpdated(self) -> bool:
        """
        indicates whether the current row has been updated.
        
        The value returned depends on whether or not the result set can detect updates.

        Raises:
            SQLException: ``SQLException``
        """
        ...


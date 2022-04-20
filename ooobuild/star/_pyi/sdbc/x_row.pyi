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
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from .x_array import XArray as XArray_708108fb
    from .x_blob import XBlob as XBlob_6773087b
    from .x_clob import XClob as XClob_6777087c
    from .x_ref import XRef as XRef_5f110819
    from ..util.date import Date as Date_60040844
    from ..util.date_time import DateTime as DateTime_84de09d3
    from ..util.time import Time as Time_604e0855

class XRow(XInterface_8f010a43):
    """
    is used to access data which is collected in a row.
    
    All methods raise a com.sun.star.sdbc.SQLException if a database access error occurs.

    See Also:
        `API XRow <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XRow.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdbc.XRow']

    def getArray(self, columnIndex: int) -> 'XArray_708108fb':
        """
        gets a SQL ARRAY value from the current row of this ResultSet object.

        Raises:
            SQLException: ``SQLException``
        """
    def getBinaryStream(self, columnIndex: int) -> 'XInputStream_98d40ab4':
        """
        gets the value of a column in the current row as a stream of uninterpreted bytes.
        
        The value can then be read in chunks from the stream. This method is particularly suitable for retrieving large LONGVARBINARY values.
        
        Note: All the data in the returned stream must be read prior to getting the value of any other column. The next call to a get method implicitly closes the stream. Also, a stream may return 0 when the method com.sun.star.io.XInputStream.available() is called whether there is data available or not.

        Raises:
            SQLException: ``SQLException``
        """
    def getBlob(self, columnIndex: int) -> 'XBlob_6773087b':
        """
        gets a BLOB value in the current row.

        Raises:
            SQLException: ``SQLException``
        """
    def getBoolean(self, columnIndex: int) -> bool:
        """
        gets the value of a column in the current row as boolean.

        Raises:
            SQLException: ``SQLException``
        """
    def getByte(self, columnIndex: int) -> int:
        """
        get the value of a column in the current row as a byte.

        Raises:
            SQLException: ``SQLException``
        """
    def getBytes(self, columnIndex: int) -> 'typing.Tuple[int, ...]':
        """
        gets the value of a column in the current row as a byte array.
        
        The bytes represent the raw values returned by the driver.

        Raises:
            SQLException: ``SQLException``
        """
    def getCharacterStream(self, columnIndex: int) -> 'XInputStream_98d40ab4':
        """
        gets the value of a column in the current row as a stream of uninterpreted bytes.
        
        The value can then be read in chunks from the stream. This method is particularly suitable for retrieving large LONGVARBINARY or LONGVARCHAR values.
        
        Note: All the data in the returned stream must be read prior to getting the value of any other column. The next call to a get method implicitly closes the stream. Also, a stream may return 0 when the method com.sun.star.io.XInputStream.available() is called whether there is data available or not.

        Raises:
            SQLException: ``SQLException``
        """
    def getClob(self, columnIndex: int) -> 'XClob_6777087c':
        """
        gets a CLOB value in the current row of this ResultSet object.

        Raises:
            SQLException: ``SQLException``
        """
    def getDate(self, columnIndex: int) -> 'Date_60040844':
        """
        gets the value of a column in the current row as a date object.

        Raises:
            SQLException: ``SQLException``
        """
    def getDouble(self, columnIndex: int) -> float:
        """
        gets the value of a column in the current row as a double.

        Raises:
            SQLException: ``SQLException``
        """
    def getFloat(self, columnIndex: int) -> float:
        """
        gets the value of a column in the current row as a float.

        Raises:
            SQLException: ``SQLException``
        """
    def getInt(self, columnIndex: int) -> int:
        """
        get the value of a column in the current row as an integer.

        Raises:
            SQLException: ``SQLException``
        """
    def getLong(self, columnIndex: int) -> int:
        """
        get the value of a column in the current row as a long.

        Raises:
            SQLException: ``SQLException``
        """
    def getObject(self, columnIndex: int, typeMap: 'XNameAccess_e2ab0cf6') -> object:
        """
        returns the value of a column in the current row as an object.
        
        This method uses the given Map object for the custom mapping of the SQL structure or distinct type that is being retrieved.

        Raises:
            SQLException: ``SQLException``
        """
    def getRef(self, columnIndex: int) -> 'XRef_5f110819':
        """
        gets a REF(&lt;structured-type&gt;) column value from the current row.

        Raises:
            SQLException: ``SQLException``
        """
    def getShort(self, columnIndex: int) -> int:
        """
        gets the value of a column in the current row as a short.

        Raises:
            SQLException: ``SQLException``
        """
    def getString(self, columnIndex: int) -> str:
        """
        gets the value of a column in the current row as a string.

        Raises:
            SQLException: ``SQLException``
        """
    def getTime(self, columnIndex: int) -> 'Time_604e0855':
        """
        gets the value of a column in the current row as a time object.

        Raises:
            SQLException: ``SQLException``
        """
    def getTimestamp(self, columnIndex: int) -> 'DateTime_84de09d3':
        """
        gets the value of a column in the current row as a datetime object.

        Raises:
            SQLException: ``SQLException``
        """
    def wasNull(self) -> bool:
        """
        reports whether the last column read had a value of SQL NULL.
        
        Note that you must first call getXXX on a column to try to read its value and then call wasNull() to see if the value read was SQL NULL.

        Raises:
            SQLException: ``SQLException``
        """


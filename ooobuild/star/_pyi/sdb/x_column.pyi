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
# Namespace: com.sun.star.sdb
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..sdbc.x_array import XArray as XArray_708108fb
    from ..sdbc.x_blob import XBlob as XBlob_6773087b
    from ..sdbc.x_clob import XClob as XClob_6777087c
    from ..sdbc.x_ref import XRef as XRef_5f110819
    from ..util.date import Date as Date_60040844
    from ..util.date_time import DateTime as DateTime_84de09d3
    from ..util.time import Time as Time_604e0855

class XColumn(XInterface_8f010a43):
    """
    is used to access data which is collected in a row.

    See Also:
        `API XColumn <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XColumn.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdb.XColumn']

    def getArray(self) -> 'XArray_708108fb':
        """
        gets a SQL ARRAY value from the current row.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getBinaryStream(self) -> 'XInputStream_98d40ab4':
        """
        gets the value of a column in the current row as a stream of uninterpreted bytes.
        
        The value can then be read in chunks from the stream. This method is particularly suitable for retrieving large LONGVARBINARY or LONGVARCHAR values.
        
        Note: All the data in the returned stream must be read prior to getting the value of any other column. The next call to a get method implicitly closes the stream. Also, a stream may return 0 when the method com.sun.star.io.XInputStream.available() is called whether there is data available or not.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getBlob(self) -> 'XBlob_6773087b':
        """
        gets a BLOB (Binary Large OBject) value in the current row.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getBoolean(self) -> bool:
        """
        gets the value of a column in the current row as boolean.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getByte(self) -> int:
        """
        gets the value of a column in the current row as a byte.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getBytes(self) -> 'typing.Tuple[int, ...]':
        """
        gets the value of a column in the current row as a byte array.
        
        The bytes represent the raw values returned by the driver.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getCharacterStream(self) -> 'XInputStream_98d40ab4':
        """
        gets the value of a column in the current row as a stream of uninterpreted bytes.
        
        The value can then be read in chunks from the stream. This method is particularly suitable for retrieving large LONGVARCHAR values.
        
        Note: All the data in the returned stream must be read prior to getting the value of any other column. The next call to a get method implicitly closes the stream. Also, a stream may return 0 when the method com.sun.star.io.XInputStream.available() is called whether there is data available or not.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getClob(self) -> 'XClob_6777087c':
        """
        gets a CLOB value in the current row of this ResultSet object.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getDate(self) -> 'Date_60040844':
        """
        gets the value of a column in the current row as a date object.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getDouble(self) -> float:
        """
        gets the value of a column in the current row as a double.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getFloat(self) -> float:
        """
        gets the value of a column in the current row as a float.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getInt(self) -> int:
        """
        gets the value of a column in the current row as a long.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getLong(self) -> int:
        """
        gets the value of a column in the current row as a hyper.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getObject(self, typeMap: 'XNameAccess_e2ab0cf6') -> object:
        """

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getRef(self) -> 'XRef_5f110819':
        """
        gets a REF(<structured-type&gt) column value from the current row.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getShort(self) -> int:
        """
        gets the value of a column in the current row as a short.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getString(self) -> str:
        """
        gets the value of a column in the current row as a String.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getTime(self) -> 'Time_604e0855':
        """
        gets the value of a column in the current row as a time object.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def getTimestamp(self) -> 'DateTime_84de09d3':
        """
        gets the value of a column in the current row as a datetime object.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
    def wasNull(self) -> bool:
        """
        reports whether the last column read had a value of SQL NULL.
        
        Note that you must first call getXXX on a column to try to read its value and then call wasNull() to see if the value read was SQL NULL.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """


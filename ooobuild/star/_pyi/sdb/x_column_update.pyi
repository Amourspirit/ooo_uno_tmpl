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
import uno
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..util.date import Date as Date_60040844
    from ..util.date_time import DateTime as DateTime_84de09d3
    from ..util.time import Time as Time_604e0855

class XColumnUpdate(XInterface_8f010a43):
    """
    is used to update data which is collected in a row.

    See Also:
        `API XColumnUpdate <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XColumnUpdate.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdb.XColumnUpdate']

    def updateBinaryStream(self, x: 'XInputStream_98d40ab4', length: int) -> None:
        """
        updates a column with a stream value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateBoolean(self, x: bool) -> None:
        """
        updates a column with a boolean value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateByte(self, x: int) -> None:
        """
        updates a column with a byte value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateBytes(self, x: uno.ByteSequence) -> None:
        """
        updates a column with a byte array value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateCharacterStream(self, x: 'XInputStream_98d40ab4', length: int) -> None:
        """
        updates a column with a stream value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateDate(self, x: 'Date_60040844') -> None:
        """
        updates a column with a Date value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateDouble(self, x: float) -> None:
        """
        updates a column with a double value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateFloat(self, x: float) -> None:
        """
        updates a column with a float value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateInt(self, x: int) -> None:
        """
        updates a column with a long value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateLong(self, x: int) -> None:
        """
        updates a column with a hyper value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateNull(self) -> None:
        """
        gives a nullable column a null value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateNumericObject(self, x: object, scale: int) -> None:
        """
        updates a column with an Object value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateObject(self, x: object) -> None:
        """
        updates a column with an Object value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateShort(self, x: int) -> None:
        """
        updates a column with a short value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateString(self, x: str) -> None:
        """
        updates a column with a string value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateTime(self, x: 'Time_604e0855') -> None:
        """
        updates a column with a Time value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def updateTimestamp(self, x: 'DateTime_84de09d3') -> None:
        """
        updates a column with a Timestamp value.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...



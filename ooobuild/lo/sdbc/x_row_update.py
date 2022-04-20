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
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..util.date import Date as Date_60040844
    from ..util.date_time import DateTime as DateTime_84de09d3
    from ..util.time import Time as Time_604e0855

class XRowUpdate(XInterface_8f010a43):
    """
    is used to update data which is collected in a row.

    See Also:
        `API XRowUpdate <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XRowUpdate.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XRowUpdate'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XRowUpdate'

    @abstractmethod
    def updateBinaryStream(self, columnIndex: int, x: 'XInputStream_98d40ab4', length: int) -> None:
        """
        updates a column with a stream value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateBoolean(self, columnIndex: int, x: bool) -> None:
        """
        updates a column with a boolean value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateByte(self, columnIndex: int, x: int) -> None:
        """
        updates a column with a byte value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateBytes(self, columnIndex: int, x: 'typing.Tuple[int, ...]') -> None:
        """
        updates a column with a byte array value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateCharacterStream(self, columnIndex: int, x: 'XInputStream_98d40ab4', length: int) -> None:
        """
        updates a column with a stream value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateDate(self, columnIndex: int, x: 'Date_60040844') -> None:
        """
        updates a column with a date value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateDouble(self, columnIndex: int, x: float) -> None:
        """
        updates a column with a double value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateFloat(self, columnIndex: int, x: float) -> None:
        """
        updates a column with a float value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateInt(self, columnIndex: int, x: int) -> None:
        """
        updates a column with an long value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateLong(self, columnIndex: int, x: int) -> None:
        """
        updates a column with a hyper value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateNull(self, columnIndex: int) -> None:
        """
        gives a nullable column a null value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateNumericObject(self, columnIndex: int, x: object, scale: int) -> None:
        """
        updates a column with an object value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateObject(self, columnIndex: int, x: object) -> None:
        """
        updates a column with an object value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateShort(self, columnIndex: int, x: int) -> None:
        """
        updates a column with a short value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateString(self, columnIndex: int, x: str) -> None:
        """
        updates a column with a string value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateTime(self, columnIndex: int, x: 'Time_604e0855') -> None:
        """
        updates a column with a time value.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def updateTimestamp(self, columnIndex: int, x: 'DateTime_84de09d3') -> None:
        """
        updates a column with a timestamp value.

        Raises:
            SQLException: ``SQLException``
        """

__all__ = ['XRowUpdate']


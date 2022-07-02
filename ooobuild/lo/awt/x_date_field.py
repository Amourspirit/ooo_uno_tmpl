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
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..util.date import Date as Date_60040844

class XDateField(XInterface_8f010a43):
    """
    gives access to the value and settings of a date field.

    See Also:
        `API XDateField <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XDateField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XDateField'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XDateField'

    @abstractmethod
    def getDate(self) -> 'Date_60040844':
        """
        returns the date value which is currently displayed in the date field.
        """
        ...
    @abstractmethod
    def getFirst(self) -> 'Date_60040844':
        """
        returns the currently set first value which is set on POS1 key.
        """
        ...
    @abstractmethod
    def getLast(self) -> 'Date_60040844':
        """
        returns the currently set last value which is set on END key.
        """
        ...
    @abstractmethod
    def getMax(self) -> 'Date_60040844':
        """
        returns the currently set maximum date value that can be entered by the user.
        """
        ...
    @abstractmethod
    def getMin(self) -> 'Date_60040844':
        """
        returns the currently set minimum date value that can be entered by the user.
        """
        ...
    @abstractmethod
    def isEmpty(self) -> bool:
        """
        returns whether currently an empty value is set for the date.
        """
        ...
    @abstractmethod
    def isLongFormat(self) -> bool:
        """
        determines if the long date format is currently used.
        """
        ...
    @abstractmethod
    def isStrictFormat(self) -> bool:
        """
        returns whether the format is currently checked during user input.
        """
        ...
    @abstractmethod
    def setDate(self, Date: 'Date_60040844') -> None:
        """
        sets the date value which is displayed in the date field.
        """
        ...
    @abstractmethod
    def setEmpty(self) -> None:
        """
        sets an empty value for the date.
        """
        ...
    @abstractmethod
    def setFirst(self, Date: 'Date_60040844') -> None:
        """
        sets the first value to be set on POS1 key.
        """
        ...
    @abstractmethod
    def setLast(self, Date: 'Date_60040844') -> None:
        """
        sets the last value to be set on END key.
        """
        ...
    @abstractmethod
    def setLongFormat(self, bLong: bool) -> None:
        """
        determines if the long date format is to be used.
        """
        ...
    @abstractmethod
    def setMax(self, Date: 'Date_60040844') -> None:
        """
        sets the maximum date value that can be entered by the user.
        """
        ...
    @abstractmethod
    def setMin(self, Date: 'Date_60040844') -> None:
        """
        sets the minimum date value that can be entered by the user.
        """
        ...
    @abstractmethod
    def setStrictFormat(self, bStrict: bool) -> None:
        """
        determines if the format is checked during user input.
        """
        ...

__all__ = ['XDateField']


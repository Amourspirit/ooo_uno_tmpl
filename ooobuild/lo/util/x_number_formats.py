# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.util
from __future__ import annotations
import typing
import uno
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from ..lang.locale import Locale as Locale_70d308fa

class XNumberFormats(XInterface_8f010a43):
    """
    provides access to multiple NumberFormats.
    
    The number formats are managed by their unique key in the document.

    See Also:
        `API XNumberFormats <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XNumberFormats.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XNumberFormats'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XNumberFormats'

    @abstractmethod
    def addNew(self, aFormat: str, nLocale: Locale_70d308fa) -> int:
        """
        adds a new number format to the list, using a format string.

        Raises:
            com.sun.star.util.MalformedNumberFormatException: ``MalformedNumberFormatException``
        """
        ...
    @abstractmethod
    def addNewConverted(self, aFormat: str, nLocale: Locale_70d308fa, nNewLocale: Locale_70d308fa) -> int:
        """
        adds a new number format to the list, using a format string in a different locale than the desired locale of the resulting number format.

        Raises:
            com.sun.star.util.MalformedNumberFormatException: ``MalformedNumberFormatException``
        """
        ...
    @abstractmethod
    def generateFormat(self, nBaseKey: int, nLocale: Locale_70d308fa, bThousands: bool, bRed: bool, nDecimals: int, nLeading: int) -> str:
        """
        generates a format string from several parameters without creating an actual number format.
        """
        ...
    @abstractmethod
    def getByKey(self, nKey: int) -> XPropertySet_bc180bfa:
        """
        """
        ...
    @abstractmethod
    def queryKey(self, aFormat: str, nLocale: Locale_70d308fa, bScan: bool) -> int:
        """
        finds a number format by its format string and returns its key.
        """
        ...
    @abstractmethod
    def queryKeys(self, nType: int, nLocale: Locale_70d308fa, bCreate: bool) -> uno.ByteSequence:
        """
        """
        ...
    @abstractmethod
    def removeByKey(self, nKey: int) -> None:
        """
        removes a number format from the list.
        """
        ...

__all__ = ['XNumberFormats']


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
# Namespace: com.sun.star.linguistic2
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa
    from .conversion_direction import ConversionDirection as ConversionDirection_7dfe113c

class XConversionDictionary(XInterface_8f010a43):
    """
    Allows the user to access a conversion dictionary.
    
    The dictionary consists of entries (pairs) of the form ( aLeftText, aRightText ). Those pairs can be added and removed. Also it can be looked for all entries where the left text or the right text matches a given text. Thus it can be used for conversions in both directions.
    
    Restrictions to what has to be the left and right text are usually given by specific services implementing this interface.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XConversionDictionary <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XConversionDictionary.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XConversionDictionary'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XConversionDictionary'

    @abstractmethod
    def addEntry(self, aLeftText: str, aRightText: str) -> None:
        """
        is used to add a conversion pair to the dictionary.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
    @abstractmethod
    def clear(self) -> None:
        """
        removes all entries from the dictionary.
        """
    @abstractmethod
    def getConversionEntries(self, eDirection: 'ConversionDirection_7dfe113c') -> 'typing.Tuple[str, ...]':
        """
        """
    @abstractmethod
    def getConversionType(self) -> int:
        """
        """
    @abstractmethod
    def getConversions(self, aText: str, nStartPos: int, nLength: int, eDirection: 'ConversionDirection_7dfe113c', nTextConversionOptions: int) -> 'typing.Tuple[str, ...]':
        """
        searches for entries or conversions that match the given text.
        
        The exact string to be looked for is the substring from the aText parameter that starts at position nStartPos and has the length nLength.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def getLocale(self) -> 'Locale_70d308fa':
        """
        """
    @abstractmethod
    def getMaxCharCount(self, eDirection: 'ConversionDirection_7dfe113c') -> int:
        """
        returns the maximum number of characters used as left or right text in entries.
        """
    @abstractmethod
    def getName(self) -> str:
        """
        """
    @abstractmethod
    def isActive(self) -> bool:
        """
        """
    @abstractmethod
    def removeEntry(self, aLeftText: str, aRightText: str) -> None:
        """
        removes a conversion pair from the dictionary.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    @abstractmethod
    def setActive(self, bActivate: bool) -> None:
        """
        specifies whether the dictionary should be used or not .
        """

__all__ = ['XConversionDictionary']


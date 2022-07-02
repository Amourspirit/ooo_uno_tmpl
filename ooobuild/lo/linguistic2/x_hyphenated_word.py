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
# Namespace: com.sun.star.linguistic2
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XHyphenatedWord(XInterface_8f010a43):
    """
    gives information obtained by a successful hyphenation attempt.
    
    This interface is used as a return value for some of the hyphenator functions.

    See Also:
        `API XHyphenatedWord <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XHyphenatedWord.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XHyphenatedWord'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XHyphenatedWord'

    @abstractmethod
    def getHyphenPos(self) -> int:
        """
        The value has to be in the range from 0 (after the first character) to m-2 (before the last character) where m is the length of the hyphenated word.
        """
        ...
    @abstractmethod
    def getHyphenatedWord(self) -> str:
        """
        """
        ...
    @abstractmethod
    def getHyphenationPos(self) -> int:
        """
        The value has to be in the range from 0 (after the first character) to n-2 (before the last character) where n is the length of the word.
        """
        ...
    @abstractmethod
    def getLocale(self) -> 'Locale_70d308fa':
        """
        """
        ...
    @abstractmethod
    def getWord(self) -> str:
        """
        """
        ...
    @abstractmethod
    def isAlternativeSpelling(self) -> bool:
        """
        is used to query if the hyphenation result is an alternative spelling.
        
        A hyphenation result is an alternative spelling if the hyphenated word is different from the word that was hyphenated.
        """
        ...

__all__ = ['XHyphenatedWord']


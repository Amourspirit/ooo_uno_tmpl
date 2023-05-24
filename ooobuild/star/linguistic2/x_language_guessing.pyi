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
# Namespace: com.sun.star.linguistic2
from __future__ import annotations
import typing

from abc import ABC
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa


class XLanguageGuessing(ABC):
    """
    This interface allows to guess the language of a text.
    
    The current set of supported languages is:
    
    **since**
    
        OOo 2.2

    See Also:
        `API XLanguageGuessing <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XLanguageGuessing.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.linguistic2.XLanguageGuessing'

    def disableLanguages(self, aLanguages: typing.Tuple[Locale_70d308fa, ...]) -> None:
        """
        allows to explicitly discard some languages from the set of languages possibly returned.
        
        By default all languages are enabled.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def enableLanguages(self, aLanguages: typing.Tuple[Locale_70d308fa, ...]) -> None:
        """
        allows to explicitly re-enable some languages that got previously disabled.
        
        By default all languages are enabled.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getAvailableLanguages(self) -> typing.Tuple[Locale_70d308fa, ...]:
        """
        returns a list of all supported languages.
        
        This should be the same as the mathematical union of all enabled and disabled languages.
        """
        ...
    def getDisabledLanguages(self) -> typing.Tuple[Locale_70d308fa, ...]:
        """
        returns the list of all disabled languages
        """
        ...
    def getEnabledLanguages(self) -> typing.Tuple[Locale_70d308fa, ...]:
        """
        returns the list of all enabled languages
        """
        ...
    def guessPrimaryLanguage(self, aText: str, nStartPos: int, nLen: int) -> Locale_70d308fa:
        """
        determines the single most probable language of a sub-string.
        
        Please note that because statistical analysis is part of the algorithm the likelihood to get the correct result increases with the length of the sub-string. A word is much less likely guessed correctly compared to a sentence or even a whole paragraph.
        
        Also note that some languages are that \"close\" to each other that it will be quite unlikely to find a difference in them, e.g. English (UK), English (IE) and English (AUS) and most likely English (US) as well. And thus the result may be arbitrary.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...



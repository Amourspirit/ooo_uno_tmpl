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
from abc import abstractmethod
from .x_supported_locales import XSupportedLocales as XSupportedLocales_5bda1056
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from ..lang.locale import Locale as Locale_70d308fa
    from .x_hyphenated_word import XHyphenatedWord as XHyphenatedWord_3a880f73
    from .x_possible_hyphens import XPossibleHyphens as XPossibleHyphens_4aa50fed

class XHyphenator(XSupportedLocales_5bda1056):
    """
    provides functionality for hyphenation of single words.
    
    Its three main functionalities are to provide a suitable position for breaking lines within a word, query about the existence of an alternative spelling at a specific position of a word and provide a list of possible hyphenation positions within a word.
    
    A hyphenation position for a word with n characters is represented by a value in the range from 0 to n-2, indicating the position of the character after which the hyphenation is done. That is, it is after the first and before the last character.
    
    A valid hyphenation position is a hyphenation position that fulfills all the restrictions implied by the properties MinLeading, MinTrailing and MinWordLength.

    See Also:
        `API XHyphenator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XHyphenator.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XHyphenator'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XHyphenator'

    @abstractmethod
    def createPossibleHyphens(self, aWord: str, aLocale: Locale_70d308fa, aProperties: PropertyValues_d6470ce6) -> XPossibleHyphens_4aa50fed:
        """
        returns information about all possible hyphenation positions of a word.
        
        If the language is not supported, an IllegalArgumentException exception is raised.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def hyphenate(self, aWord: str, aLocale: Locale_70d308fa, nMaxLeading: int, aProperties: PropertyValues_d6470ce6) -> XHyphenatedWord_3a880f73:
        """
        tries to find a valid hyphenation position relative to the beginning of a word.
        
        Note: Some languages, for example Arabic, are written from right to left.
        
        If the language is not supported, an IllegalArgumentException exception is raised.
        
        It has to be greater than or equal to 0.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def queryAlternativeSpelling(self, aWord: str, aLocale: Locale_70d308fa, nIndex: int, aProperties: PropertyValues_d6470ce6) -> XHyphenatedWord_3a880f73:
        """
        checks whether hyphenation at a position in a word will result in an alternative spelling or not.
        
        An alternative spelling position is a hyphen position where, if hyphenation is done here, the writing of the word changes. Example: \"B&auml;cker\" in German pre spelling-reform becomes \"B&auml;kker\" if hyphenation is done after the \"c\".
        
        The hyphenation position does not need to be a valid one to be an alternative spelling position.
        
        If the language is not supported, an IllegalArgumentException exception is raised.
        
        If the length of the word is n, the value of this parameter has to be in the range from 0 to n-2.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XHyphenator']



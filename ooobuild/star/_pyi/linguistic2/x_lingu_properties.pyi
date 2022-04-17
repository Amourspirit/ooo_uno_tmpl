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
from typing_extensions import Literal
import typing
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XLinguProperties(XPropertySet_bc180bfa):
    """
    Interface for LinguProperties service.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XLinguProperties <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XLinguProperties.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.linguistic2.XLinguProperties']

    @property
    def DefaultLocale(self) -> 'Locale_70d308fa':
        """
        the default western language for new documents.
        """

    @property
    def DefaultLocale_CJK(self) -> 'Locale_70d308fa':
        """
        the default language for CJK languages.
        """

    @property
    def DefaultLocale_CTL(self) -> 'Locale_70d308fa':
        """
        the default language for CTL languages.
        """

    @property
    def HyphMinLeading(self) -> int:
        """
        the minimum number of characters of a word to remain before the hyphen when doing hyphenation.
        """

    @property
    def HyphMinTrailing(self) -> int:
        """
        the minimum number of characters of a word to remain after the hyphen when doing hyphenation.
        """

    @property
    def HyphMinWordLength(self) -> int:
        """
        the minimum length of a word in order to be hyphenated.
        """

    @property
    def IsHyphAuto(self) -> bool:
        """
        defines whether interactive hyphenation should be performed without requiring the user to select every hyphenation position after the user has triggered the hyphenation.
        """

    @property
    def IsHyphSpecial(self) -> bool:
        """
        defines whether hyphenation should be done in special regions of documents or not.
        """

    @property
    def IsIgnoreControlCharacters(self) -> bool:
        """
        defines if control characters should be ignored or not, by the linguistic (i.e., spell checker, hyphenator and thesaurus).
        """

    @property
    def IsSpellAuto(self) -> bool:
        """
        indicates whether spell checking should be done automatically or not.
        """

    @property
    def IsSpellCapitalization(self) -> bool:
        """
        defines if the capitalization of words should be checked or not.
        """

    @property
    def IsSpellSpecial(self) -> bool:
        """
        defines whether spell checking should be done in special regions of documents or not.
        """

    @property
    def IsSpellUpperCase(self) -> bool:
        """
        defines if words with only uppercase letters should be subject to spell checking or not.
        """

    @property
    def IsSpellWithDigits(self) -> bool:
        """
        defines if words containing digits (or numbers) should be subject to spell checking or not.
        """

    @property
    def IsUseDictionaryList(self) -> bool:
        """
        defines if the dictionary-list should be used for spell checking and hyphenation or not.
        """

    @property
    def IsWrapReverse(self) -> bool:
        """
        defines whether spell checking should be done in reverse direction or not.
        """



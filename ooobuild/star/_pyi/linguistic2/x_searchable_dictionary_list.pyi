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
from typing_extensions import Literal
import typing
from .x_dictionary_list import XDictionaryList as XDictionaryList_3a070f7f
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa
    from .x_dictionary_entry import XDictionaryEntry as XDictionaryEntry_49ef0ff5

class XSearchableDictionaryList(XDictionaryList_3a070f7f):
    """
    allows searching for an entry in all dictionaries of the dictionary-list.
    
    Only active dictionaries of a suitable language will be searched for the entry. The language is suitable if it is the same as the dictionary's language or the dictionary may hold entries of all languages.

    See Also:
        `API XSearchableDictionaryList <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XSearchableDictionaryList.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.linguistic2.XSearchableDictionaryList']

    def queryDictionaryEntry(self, aWord: str, aLocale: 'Locale_70d308fa', bSearchPosDics: bool, bSpellEntry: bool) -> 'XDictionaryEntry_49ef0ff5':
        """
        looks for an entry for a given word in the list of dictionaries.
        """


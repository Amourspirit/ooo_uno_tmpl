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
from .x_dictionary import XDictionary as XDictionary_fea70de3
if typing.TYPE_CHECKING:
    from .x_dictionary_entry import XDictionaryEntry as XDictionaryEntry_49ef0ff5

class XSearchableDictionary(XDictionary_fea70de3):
    """
    This interfaces allows to retrieve suggestions for spell checking from a dictionary.
    
    **since**
    
        OOo 3.0.1

    See Also:
        `API XSearchableDictionary <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XSearchableDictionary.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.linguistic2.XSearchableDictionary']

    def searchSimilarEntries(self, aWord: str) -> 'typing.Tuple[XDictionaryEntry_49ef0ff5, ...]':
        """
        search for similar entries in the dictionary.
        
        **since**
        
            OOo 3.0.1
        """

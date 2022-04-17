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
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa
    from .dictionary_type import DictionaryType as DictionaryType_2ba50f2d
    from .x_dictionary import XDictionary as XDictionary_fea70de3
    from .x_dictionary_list_event_listener import XDictionaryListEventListener as XDictionaryListEventListener_279814c7

class XDictionaryList(XInterface_8f010a43):
    """
    is used to manage and maintain a list of dictionaries.
    
    A dictionary-list may be given to a spell checker or hyphenator service implementation on their creation in order to supply a set of dictionaries and additional information to be used for those purposes.

    See Also:
        `API XDictionaryList <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XDictionaryList.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.linguistic2.XDictionaryList']

    def addDictionary(self, xDictionary: 'XDictionary_fea70de3') -> bool:
        """
        adds a dictionary to the list.
        
        Additionally, the dictionary-list will add itself to the list of dictionary event listeners of that dictionary.
        """
    def addDictionaryListEventListener(self, xListener: 'XDictionaryListEventListener_279814c7', bReceiveVerbose: bool) -> bool:
        """
        adds an entry to the list of dictionary-list event listeners.
        
        On dictionary-list events, each entry in the listener list will be notified via a call to com.sun.star.linguistic2.XDictionaryListEventListener.processDictionaryListEvent().
        """
    def beginCollectEvents(self) -> int:
        """
        increases request level for event buffering by one.
        
        The request level for event buffering is an integer counter that is initially set to 0. As long as the request level is not 0, events will be buffered until the next flushing of the buffer.
        """
    def createDictionary(self, aName: str, aLocale: 'Locale_70d308fa', eDicType: 'DictionaryType_2ba50f2d', aURL: str) -> 'XDictionary_fea70de3':
        """
        creates a new dictionary.
        """
    def endCollectEvents(self) -> int:
        """
        flushes the event buffer and decreases the request level for event buffering by one.
        
        There should be one matching endCollectEvents call for every beginCollectEvents call. Usually you will group these around some code where you do not wish to get notified of every single event.
        """
    def flushEvents(self) -> int:
        """
        notifies the listeners of all buffered events and then clears that buffer.
        """
    def getCount(self) -> int:
        """
        """
    def getDictionaries(self) -> 'typing.Tuple[XDictionary_fea70de3, ...]':
        """
        """
    def getDictionaryByName(self, aDictionaryName: str) -> 'XDictionary_fea70de3':
        """
        searches the list for a dictionary with a given name.
        """
    def removeDictionary(self, xDictionary: 'XDictionary_fea70de3') -> bool:
        """
        removes a single dictionary from the list.
        
        If the dictionary is still active, it will be deactivated first. The dictionary-list will remove itself from the list of dictionary event listeners of the dictionary.
        """
    def removeDictionaryListEventListener(self, xListener: 'XDictionaryListEventListener_279814c7') -> bool:
        """
        removes an entry from the list of dictionary-list event listeners.
        """


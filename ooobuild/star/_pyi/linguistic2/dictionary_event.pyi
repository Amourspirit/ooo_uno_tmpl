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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.linguistic2
# Libre Office Version: 7.3
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .x_dictionary_entry import XDictionaryEntry as XDictionaryEntry_49ef0ff5


class DictionaryEvent(EventObject_a3d70b03):
    """
    Struct Class

    represents a dictionary event.
    
    This type of event is used by a dictionary to inform its listeners about changes in its properties or its entry list. It consists of an event type and may supply an affected dictionary entry.

    See Also:
        `API DictionaryEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1linguistic2_1_1DictionaryEvent.html>`_
    """
    typeName: Literal['com.sun.star.linguistic2.DictionaryEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., nEvent: typing.Optional[int] = ..., xDictionaryEntry: typing.Optional[XDictionaryEntry_49ef0ff5] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            nEvent (int, optional): nEvent value.
            xDictionaryEntry (XDictionaryEntry, optional): xDictionaryEntry value.
        """
        ...


    @property
    def nEvent(self) -> int:
        """
        is the type of event.
        
        This must be the value of a single flag. No combinations are allowed.
        """
        ...

    @nEvent.setter
    def nEvent(self, value: int) -> None:
        ...

    @property
    def xDictionaryEntry(self) -> XDictionaryEntry_49ef0ff5:
        """
        is the affected dictionary entry (if any).
        
        It must be set if an entry was added or deleted, otherwise it should be empty.
        """
        ...

    @xDictionaryEntry.setter
    def xDictionaryEntry(self, value: XDictionaryEntry_49ef0ff5) -> None:
        ...


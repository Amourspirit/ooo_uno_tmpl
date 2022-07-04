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
from .dictionary_event import DictionaryEvent as DictionaryEvent_3ae00f8d


class DictionaryListEvent(EventObject_a3d70b03):
    """
    Struct Class

    structure representing a dictionary-list event.
    
    This structure is used by the dictionary-list to inform its listeners about certain events. Since the dictionary-list is able to collect several single events before broadcasting them to its listeners the integer argument may be a combination (logical or) of several event types. If more specific information about the events is requested by a listener, a sequence of all dictionary-list events since the last broadcasting will be supplied. Otherwise, that list will be empty.

    See Also:
        `API DictionaryListEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1linguistic2_1_1DictionaryListEvent.html>`_
    """
    typeName: Literal['com.sun.star.linguistic2.DictionaryListEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., aDictionaryEvents: typing.Optional[typing.Tuple[DictionaryEvent_3ae00f8d, ...]] = ..., nCondensedEvent: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            aDictionaryEvents (typing.Tuple[DictionaryEvent, ...], optional): aDictionaryEvents value.
            nCondensedEvent (int, optional): nCondensedEvent value.
        """
        ...


    @property
    def aDictionaryEvents(self) -> typing.Tuple[DictionaryEvent_3ae00f8d, ...]:
        """
        list of accumulated dictionary events.
        
        It will be empty if all com.sun.star.linguistic2.XDictionaryListEventListener are satisfied with the condensed representation of the com.sun.star.linguistic2.DictionaryListEvent.nCondensedEvent().
        """
        ...


    @property
    def nCondensedEvent(self) -> int:
        """
        the combined type of the accumulated events.
        
        The value can be the combination of multiple com.sun.star.linguistic2.DictionaryListEventFlags by applying the logical OR to them.
        """
        ...



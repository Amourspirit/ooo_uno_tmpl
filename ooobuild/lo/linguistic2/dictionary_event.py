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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.linguistic2
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
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
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.DictionaryEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.linguistic2.DictionaryEvent'
    """Literal Constant ``com.sun.star.linguistic2.DictionaryEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, nEvent: typing.Optional[int] = 0, xDictionaryEntry: typing.Optional[XDictionaryEntry_49ef0ff5] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            nEvent (int, optional): nEvent value.
            xDictionaryEntry (XDictionaryEntry, optional): xDictionaryEntry value.
        """

        if isinstance(Source, DictionaryEvent):
            oth: DictionaryEvent = Source
            self.Source = oth.Source
            self.nEvent = oth.nEvent
            self.xDictionaryEntry = oth.xDictionaryEntry
            return

        kargs = {
            "Source": Source,
            "nEvent": nEvent,
            "xDictionaryEntry": xDictionaryEntry,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._n_event = kwargs["nEvent"]
        self._x_dictionary_entry = kwargs["xDictionaryEntry"]
        inst_keys = ('nEvent', 'xDictionaryEntry')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def nEvent(self) -> int:
        """
        is the type of event.
        
        This must be the value of a single flag. No combinations are allowed.
        """
        return self._n_event

    @nEvent.setter
    def nEvent(self, value: int) -> None:
        self._n_event = value

    @property
    def xDictionaryEntry(self) -> XDictionaryEntry_49ef0ff5:
        """
        is the affected dictionary entry (if any).
        
        It must be set if an entry was added or deleted, otherwise it should be empty.
        """
        return self._x_dictionary_entry

    @xDictionaryEntry.setter
    def xDictionaryEntry(self, value: XDictionaryEntry_49ef0ff5) -> None:
        self._x_dictionary_entry = value


__all__ = ['DictionaryEvent']

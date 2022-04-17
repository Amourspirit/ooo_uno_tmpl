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
# Namespace: com.sun.star.form.binding
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing


class ListEntryEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies the event which is notified when a change in a string entry list occurred

    See Also:
        `API ListEntryEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1form_1_1binding_1_1ListEntryEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.binding'
    __ooo_full_ns__: str = 'com.sun.star.form.binding.ListEntryEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.form.binding.ListEntryEvent'
    """Literal Constant ``com.sun.star.form.binding.ListEntryEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Entries: typing.Optional[typing.Tuple[str, ...]] = UNO_NONE, Position: typing.Optional[int] = 0, Count: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Entries (typing.Tuple[str, ...], optional): Entries value.
            Position (int, optional): Position value.
            Count (int, optional): Count value.
        """

        if isinstance(Source, ListEntryEvent):
            oth: ListEntryEvent = Source
            self.Source = oth.Source
            self.Entries = oth.Entries
            self.Position = oth.Position
            self.Count = oth.Count
            return

        kargs = {
            "Source": Source,
            "Entries": Entries,
            "Position": Position,
            "Count": Count,
        }
        if kargs["Entries"] is UNO_NONE:
            kargs["Entries"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._entries = kwargs["Entries"]
        self._position = kwargs["Position"]
        self._count = kwargs["Count"]
        inst_keys = ('Entries', 'Position', 'Count')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Entries(self) -> typing.Tuple[str, ...]:
        """
        denotes the changed entries
        
        The concrete semantics of the value depends on the concrete event being notified.
        """
        return self._entries
    
    @Entries.setter
    def Entries(self, value: typing.Tuple[str, ...]) -> None:
        self._entries = value

    @property
    def Position(self) -> int:
        """
        denotes the position where a change occurred.
        
        The concrete semantics of the value depends on the concrete event being notified.
        """
        return self._position
    
    @Position.setter
    def Position(self, value: int) -> None:
        self._position = value

    @property
    def Count(self) -> int:
        """
        denotes the number of changed entries, in case a change of an entry range is being notified.
        """
        return self._count
    
    @Count.setter
    def Count(self, value: int) -> None:
        self._count = value


__all__ = ['ListEntryEvent']

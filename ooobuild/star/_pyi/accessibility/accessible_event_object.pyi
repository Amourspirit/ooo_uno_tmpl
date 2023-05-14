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
# Namespace: com.sun.star.accessibility
# Libre Office Version: 7.3
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class AccessibleEventObject(EventObject_a3d70b03):
    """
    Struct Class

    this struct describes an accessible event, that is broadcasted from the XAccessibleEventBroadcaster and notified to XAccessibleEventListener.
    
    It is usually implemented by AccessibleContext.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleEventObject <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1accessibility_1_1AccessibleEventObject.html>`_
    """
    typeName: Literal['com.sun.star.accessibility.AccessibleEventObject']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., EventId: typing.Optional[int] = ..., NewValue: typing.Optional[object] = ..., OldValue: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            EventId (int, optional): EventId value.
            NewValue (object, optional): NewValue value.
            OldValue (object, optional): OldValue value.
        """
        ...


    @property
    def EventId(self) -> int:
        """
        specifies the type of this event.
        
        For a list of possible events see AccessibleEventId.
        """
        ...

    @EventId.setter
    def EventId(self, value: int) -> None:
        ...

    @property
    def NewValue(self) -> object:
        """
        for events that specifies a value change, this is the new value.
        
        Depending on the EventId, this can be void.
        """
        ...

    @NewValue.setter
    def NewValue(self, value: object) -> None:
        ...

    @property
    def OldValue(self) -> object:
        """
        for events that specifies a value change, this is the old value.
        
        Depending on the EventId, this can be void.
        """
        ...

    @OldValue.setter
    def OldValue(self, value: object) -> None:
        ...


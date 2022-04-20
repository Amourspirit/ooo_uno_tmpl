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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from typing_extensions import Literal
from .input_event import InputEvent as InputEvent_8f520a66
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class MouseEvent(InputEvent_8f520a66):
    """
    Struct Class

    specifies an event from the mouse.
    
    This event is also used for pop-up menu requests on objects. See PopupTrigger for details.

    See Also:
        `API MouseEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1MouseEvent.html>`_
    """
    typeName: Literal['com.sun.star.awt.MouseEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Modifiers: typing.Optional[int] = ..., Buttons: typing.Optional[int] = ..., X: typing.Optional[int] = ..., Y: typing.Optional[int] = ..., ClickCount: typing.Optional[int] = ..., PopupTrigger: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Modifiers (int, optional): Modifiers value.
            Buttons (int, optional): Buttons value.
            X (int, optional): X value.
            Y (int, optional): Y value.
            ClickCount (int, optional): ClickCount value.
            PopupTrigger (bool, optional): PopupTrigger value.
        """


    @property
    def Buttons(self) -> int:
        """
        contains the pressed mouse buttons.
        
        Zero ore more constants from the com.sun.star.awt.MouseButton group.
        """


    @property
    def X(self) -> int:
        """
        contains the x coordinate location of the mouse.
        """


    @property
    def Y(self) -> int:
        """
        contains the y coordinate location of the mouse.
        """


    @property
    def ClickCount(self) -> int:
        """
        contains the number of mouse clicks associated with event.
        """


    @property
    def PopupTrigger(self) -> bool:
        """
        specifies if this event is a pop-up menu trigger event.
        
        If this member is TRUE, the event describes a request for a pop-up menu, also known as context menu, on an object.
        
        In this case, X and Y describe the position where the request was issued. If those members are -1, then the request was issued using the keyboard, by pressing the operating-system dependent key combination for this purpose.
        """



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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .rectangle import Rectangle as Rectangle_84b109e9


class PaintEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies the paint event for a component.
    
    This event is a special type which is used to ensure that paint/update method calls are serialized along with the other events delivered from the event queue.

    See Also:
        `API PaintEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1PaintEvent.html>`_
    """
    typeName: Literal['com.sun.star.awt.PaintEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., UpdateRect: typing.Optional[Rectangle_84b109e9] = ..., Count: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            UpdateRect (Rectangle, optional): UpdateRect value.
            Count (int, optional): Count value.
        """
        ...


    @property
    def UpdateRect(self) -> Rectangle_84b109e9:
        """
        contains the rectangle area which needs to be repainted.
        """
        ...


    @property
    def Count(self) -> int:
        """
        contains the number of paint events that follows this event if it is a multiple PaintEvent.
        
        You can collect the PaintEvent until Count is zero.
        """
        ...



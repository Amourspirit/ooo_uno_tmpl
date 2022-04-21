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
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .rectangle import Rectangle as Rectangle_84b109e9


class EndDockingEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies an end docking event.

    See Also:
        `API EndDockingEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1EndDockingEvent.html>`_
    """
    typeName: Literal['com.sun.star.awt.EndDockingEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., WindowRectangle: typing.Optional[Rectangle_84b109e9] = ..., bFloating: typing.Optional[bool] = ..., bCancelled: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            WindowRectangle (Rectangle, optional): WindowRectangle value.
            bFloating (bool, optional): bFloating value.
            bCancelled (bool, optional): bCancelled value.
        """


    @property
    def WindowRectangle(self) -> Rectangle_84b109e9:
        """
        specifies the new bounding rectangle of the window
        """


    @property
    def bFloating(self) -> bool:
        """
        specifies if the window is now floating TRUE or docked FALSE
        """


    @property
    def bCancelled(self) -> bool:
        """
        specifies that the docking procedure was canceled
        """



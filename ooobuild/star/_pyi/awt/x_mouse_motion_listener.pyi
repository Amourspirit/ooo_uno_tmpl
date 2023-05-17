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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .mouse_event import MouseEvent as MouseEvent_8f430a5f


class XMouseMotionListener(XEventListener_c7230c4a):
    """
    makes it possible to receive mouse motion events on a window.

    See Also:
        `API XMouseMotionListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XMouseMotionListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XMouseMotionListener']

    def mouseDragged(self, e: 'MouseEvent_8f430a5f') -> None:
        """
        is invoked when a mouse button is pressed on a window and then dragged.
        
        Mouse drag events will continue to be delivered to the window where the first event originated until the mouse button is released (regardless of whether the mouse position is within the bounds of the window).
        """
        ...
    def mouseMoved(self, e: 'MouseEvent_8f430a5f') -> None:
        """
        is invoked when the mouse pointer has been moved on a window (with no buttons down).
        """
        ...



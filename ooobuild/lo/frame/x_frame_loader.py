# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_frame import XFrame as XFrame_7a570956
    from .x_load_event_listener import XLoadEventListener as XLoadEventListener_9140e33

class XFrameLoader(XInterface_8f010a43):
    """
    load components into a frame
    
    It's an asynchronous loading. For synchronous processes use XSynchronousFrameLoader instead of this one. The generic load algorithm of the office supports both ones - but preferred the synchronous interface.

    See Also:
        `API XFrameLoader <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFrameLoader.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XFrameLoader'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XFrameLoader'

    @abstractmethod
    def cancel(self) -> None:
        """
        cancels the loading process.
        
        After returning from this call, neither the frame nor the load-event-listener specified in XFrameLoader.load() may be called back. Because only the owner of this process who called load method before can cancel this process. And he doesn't need any notification about that. On the other hand - nobody then this owner himself can be registered as an XLoadEventListener here.
        """
        ...
    @abstractmethod
    def load(self, Frame: XFrame_7a570956, URL: str, Arguments: typing.Tuple[PropertyValue_c9610c73, ...], Listener: XLoadEventListener_9140e33) -> None:
        """
        starts the loading of the specified resource into the specified Frame.
        """
        ...

__all__ = ['XFrameLoader']


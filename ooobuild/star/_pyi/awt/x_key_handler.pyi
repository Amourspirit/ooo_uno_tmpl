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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .key_event import KeyEvent as KeyEvent_7a78097f

class XKeyHandler(XEventListener_c7230c4a):
    """
    This key handler is similar to com.sun.star.awt.XKeyListener but allows the consumption of key events.
    
    If a key event is consumed by one handler both the following handlers, with respect to the list of key handlers of the broadcaster, and a following handling by the broadcaster will not take place.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XKeyHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XKeyHandler.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XKeyHandler']

    def keyPressed(self, aEvent: 'KeyEvent_7a78097f') -> bool:
        """
        This function is called by the broadcaster, an com.sun.star.awt.XExtendedToolkit for instance, after a key has been pressed but before it is released.
        
        The return value decides about whether other handlers will be called and a handling by the broadcaster will take place.
        
        Consume the event if the action performed by the implementation is mutually exclusive with the default action of the broadcaster or, when known, with that of other handlers.
        
        Consuming this event does not prevent the pending key-release event from being broadcasted.
        """
    def keyReleased(self, aEvent: 'KeyEvent_7a78097f') -> bool:
        """
        This function is called by the broadcaster, an com.sun.star.awt.XExtendedToolkit for instance, after a key has been pressed and released.
        
        The return value decides about whether other handlers will be called and a handling by the broadcaster will take place.
        
        Consume the event if the action performed by the implementation is mutually exclusive with the default action of the broadcaster or, when known, with that of other handlers.
        """


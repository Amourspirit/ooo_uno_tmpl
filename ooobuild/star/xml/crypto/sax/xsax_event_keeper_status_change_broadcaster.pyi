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
# Namespace: com.sun.star.xml.crypto.sax
from __future__ import annotations
import typing

from ....uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .xsax_event_keeper_status_change_listener import XSAXEventKeeperStatusChangeListener as XSAXEventKeeperStatusChangeListener_fece1854


class XSAXEventKeeperStatusChangeBroadcaster(XInterface_8f010a43):
    """
    Interface of SAXEventKeeper Status Change Broadcaster.
    
    This interface is used to manipulate SAXEventKeeper status change listener.

    See Also:
        `API XSAXEventKeeperStatusChangeBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax_1_1XSAXEventKeeperStatusChangeBroadcaster.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.xml.crypto.sax.XSAXEventKeeperStatusChangeBroadcaster'

    def addSAXEventKeeperStatusChangeListener(self, listener: XSAXEventKeeperStatusChangeListener_fece1854) -> None:
        """
        Adds a new status change listener.
        
        When the SAXEventKeeper's status changes, the listener will receive a notification.
        """
        ...
    def removeSAXEventKeeperStatusChangeListener(self, listener: XSAXEventKeeperStatusChangeListener_fece1854) -> None:
        """
        Removes a status change listener.
        
        After a listener is removed, no status change notification will be sent to it.
        """
        ...




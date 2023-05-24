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
# Namespace: com.sun.star.connection
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..io.x_stream_listener import XStreamListener as XStreamListener_baf80bea

class XConnectionBroadcaster(XInterface_8f010a43):
    """
    allows to add listeners to a connection.
    
    Maybe supported by connections returned from XAcceptor.accept() or XConnector.connect().

    See Also:
        `API XConnectionBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1connection_1_1XConnectionBroadcaster.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.connection'
    __ooo_full_ns__: str = 'com.sun.star.connection.XConnectionBroadcaster'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.connection.XConnectionBroadcaster'

    @abstractmethod
    def addStreamListener(self, aListener: XStreamListener_baf80bea) -> None:
        """
        registers an object to receive events from this connection.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
        ...
    @abstractmethod
    def removeStreamListener(self, aListener: XStreamListener_baf80bea) -> None:
        """
        unregisters an object to receive events from this connection.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
        ...

__all__ = ['XConnectionBroadcaster']


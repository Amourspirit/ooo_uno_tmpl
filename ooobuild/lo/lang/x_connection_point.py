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
# Namespace: com.sun.star.lang
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_connection_point_container import XConnectionPointContainer as XConnectionPointContainer_688110bf

class XConnectionPoint(XInterface_8f010a43):
    """
    supports connection points for connectable objects.
    
    Connectable objects support the following features:
    
    To create a connectable object, you need to implement objects that provide two related interfaces:
    
    The XConnectionPointContainer interface is implemented on the connectable object to indicate the existence of the outgoing interfaces. It provides a sequence of sub-objects. It also provides access to all the connection point sub-objects, each of which implements the XConnectionPoint interface. The XConnectionPoint interface provides a sequence of sub-objects.
    
    Each connection point is a separate sub-object to avoid circular reference counting problems. A connection point controls how many connections (one or more) it will allow in its implementation of XConnectionPoint.advise().
    
    A client can use the XConnectionPointContainer interface:

    See Also:
        `API XConnectionPoint <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XConnectionPoint.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.lang'
    __ooo_full_ns__: str = 'com.sun.star.lang.XConnectionPoint'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.lang.XConnectionPoint'

    @abstractmethod
    def advise(self, xListener: 'XInterface_8f010a43') -> None:
        """
        creates a connection between a connection point and a client's sink, where the sink implements the outgoing interface supported by this connection point.
        
        A few add...Listener methods need additional parameters to add listeners or throw exceptions. One of these methods is com.sun.star.beans.XPropertySet.addPropertyChangeListener(). We ignore the problem in this interface. A solution must be provided in an additional XConnectionPoint interface.

        Raises:
            com.sun.star.lang.ListenerExistException: ``ListenerExistException``
            com.sun.star.lang.InvalidListenerException: ``InvalidListenerException``
        """
        ...
    @abstractmethod
    def getConnectionPointContainer(self) -> 'XConnectionPointContainer_688110bf':
        """
        """
        ...
    @abstractmethod
    def getConnectionType(self) -> object:
        """
        Using the XConnectionPointContainer.getConnectionPoints() method, a client can obtain an XConnectionPoint interface. Using that interface and this method, the client can determine the type of each connection point enumerated. The type returned from this method must enable the caller to access this same connection point through XConnectionPointContainer.findConnectionPoint().
        """
        ...
    @abstractmethod
    def getConnections(self) -> 'typing.Tuple[XInterface_8f010a43, ...]':
        """
        """
        ...
    @abstractmethod
    def unadvise(self, xListener: 'XInterface_8f010a43') -> None:
        """
        terminates a notification previously set up with advise.
        
        A few remove...Listener methods need additional parameters to add listeners or throw exceptions. One of these methods is com.sun.star.beans.XPropertySet.removePropertyChangeListener(). We ignore the problem in this interface. A solution must be provided in an additional XConnectionPoint interface.
        """
        ...

__all__ = ['XConnectionPoint']


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
# Namespace: com.sun.star.datatransfer.dnd
from __future__ import annotations
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43

class XDragSourceContext(XInterface_8f010a43):
    """
    The drag source context class is responsible for managing the initiator side of the Drag and Drop protocol.
    
    In particular, it is responsible for managing event notifications to the DragSourceListener and providing the Transferable state to enable the data transfer.
    
    An instance of this class is created as a result of the method XDragSource.startDrag() being successfully invoked. This instance is responsible for tracking the state of the operation on behalf of the drag source and dispatching state changes to the drag source listener.

    See Also:
        `API XDragSourceContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1XDragSourceContext.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.XDragSourceContext'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.datatransfer.dnd.XDragSourceContext'

    @abstractmethod
    def getCurrentCursor(self) -> int:
        """
        Get the identifier of the currently used cursor.
        """
        ...
    @abstractmethod
    def setCursor(self, cursorId: int) -> None:
        """
        This method sets the current drag cursor.
        
        This method should only be called to set another cursor than the default one for drag action currently selected by the user.
        
        Invalid cursor identifiers will be ignored.
        """
        ...
    @abstractmethod
    def setImage(self, imageId: int) -> None:
        """
        This method sets the current drag image.
        """
        ...
    @abstractmethod
    def transferablesFlavorsChanged(self) -> None:
        """
        This method notifies the context that the com.sun.star.datatransfer.DataFlavor types of the transferable object have changed.
        """
        ...

__all__ = ['XDragSourceContext']



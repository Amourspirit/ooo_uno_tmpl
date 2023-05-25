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
# Namespace: com.sun.star.document
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_event_broadcaster import XEventBroadcaster as XEventBroadcaster_2b120f2b
if typing.TYPE_CHECKING:
    from .x_shape_event_listener import XShapeEventListener as XShapeEventListener_4a2d0ff8
    from ..drawing.x_shape import XShape as XShape_8fd00a3d

class XShapeEventBroadcaster(XEventBroadcaster_2b120f2b):
    """
    Used to link a listener to a specific shape.
    
    **since**
    
        LibreOffice 6.4

    See Also:
        `API XShapeEventBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XShapeEventBroadcaster.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XShapeEventBroadcaster'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XShapeEventBroadcaster'

    @abstractmethod
    def addShapeEventListener(self, Shape: XShape_8fd00a3d, Listener: XShapeEventListener_4a2d0ff8) -> None:
        """
        registers the given listener
        """
        ...
    @abstractmethod
    def removeShapeEventListener(self, Shape: XShape_8fd00a3d, Listener: XShapeEventListener_4a2d0ff8) -> None:
        """
        unregisters the given listener
        """
        ...

__all__ = ['XShapeEventBroadcaster']



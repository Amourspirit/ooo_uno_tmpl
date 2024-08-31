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
    from ..container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
    from .x_frame import XFrame as XFrame_7a570956
    from .x_terminate_listener import XTerminateListener as XTerminateListener_b760e5a
    from ..lang.x_component import XComponent as XComponent_98dc0ab5

class XDesktop(XInterface_8f010a43):
    """
    This is the main interface of a desktop service.
    
    A desktop is an environment for components which can be viewed in frames. Frames are like frames in HTML framesets. This does not imply that a desktop can handle framesets; the frames may be top frames only.

    See Also:
        `API XDesktop <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XDesktop.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XDesktop'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XDesktop'

    @abstractmethod
    def addTerminateListener(self, Listener: XTerminateListener_b760e5a) -> None:
        """
        registers an event listener to the desktop, which is called when the desktop is queried to terminate, and when it really terminates.
        """
        ...
    @abstractmethod
    def getComponents(self) -> XEnumerationAccess_4bac0ffc:
        """
        provides read access to collection of all currently loaded components inside the frame tree
        
        The component is, by definition, the model of the control which is loaded into a frame, or if no model exists, into the control itself. The service Components which is available from this method is a collection of all components of the desktop which are open within a frame of the desktop.
        """
        ...
    @abstractmethod
    def getCurrentComponent(self) -> XComponent_98dc0ab5:
        """
        provides read access to the component inside the tree which has the UI focus
        
        Normally, the component is the model part of the active component. If no model exists it is the active controller (view) itself.
        """
        ...
    @abstractmethod
    def getCurrentFrame(self) -> XFrame_7a570956:
        """
        provides read access to the frame which contains the current component
        """
        ...
    @abstractmethod
    def removeTerminateListener(self, Listener: XTerminateListener_b760e5a) -> None:
        """
        unregisters an event listener for termination events.
        """
        ...
    @abstractmethod
    def terminate(self) -> bool:
        """
        tries to terminate the desktop.
        
        First, every terminate listener is called by his XTerminateListener.queryTermination() method. Throwing of a TerminationVetoException can break the termination process and the listener how has done that will be the new \"controller\" of the desktop lifetime. He should try to terminate it by himself after his own processes will be finished. If nobody disagree with the termination request, every listener will be called by his XTerminateListener.notifyTermination() method.
        """
        ...

__all__ = ['XDesktop']


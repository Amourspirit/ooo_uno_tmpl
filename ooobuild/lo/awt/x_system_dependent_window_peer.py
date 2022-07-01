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
import uno
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XSystemDependentWindowPeer(XInterface_8f010a43):
    """
    provides access to the system dependent implementation of the window.

    See Also:
        `API XSystemDependentWindowPeer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XSystemDependentWindowPeer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XSystemDependentWindowPeer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XSystemDependentWindowPeer'

    @abstractmethod
    def getWindowHandle(self, ProcessId: uno.ByteSequence, SystemType: int) -> object:
        """
        returns a system-specific window handle.
        
        You must check the machine ID and the process ID.WIN32: Returns an HWND if possible, otherwise 0.WIN16: Returns an HWND if possible, otherwise 0.
        
        JAVA: Returns a global reference to a java.awt.Component object provided from the JNI-API.
        
        MAC: Returns a ptr to the NSView implementing the window.
        
        XWINDOW: Returns a structure SystemDependentXWindow or void if it is not reachable.
        """

__all__ = ['XSystemDependentWindowPeer']


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
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_vcl_container_listener import XVclContainerListener as XVclContainerListener_190e0eba
    from .x_window import XWindow as XWindow_713b0924

class XVclContainer(XInterface_8f010a43):
    """
    represents a VCL container window.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XVclContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XVclContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XVclContainer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XVclContainer'

    @abstractmethod
    def addVclContainerListener(self, l: XVclContainerListener_190e0eba) -> None:
        """
        adds the specified container listener to receive container events from this container.
        """
        ...
    @abstractmethod
    def getWindows(self) -> typing.Tuple[XWindow_713b0924, ...]:
        """
        returns all windows.
        """
        ...
    @abstractmethod
    def removeVclContainerListener(self, l: XVclContainerListener_190e0eba) -> None:
        """
        removes the specified container listener so that it no longer receives container events from this container.
        """
        ...

__all__ = ['XVclContainer']



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
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_key_handler import XKeyHandler as XKeyHandler_98520a93
    from .x_mouse_click_handler import XMouseClickHandler as XMouseClickHandler_edcb0d59

class XUserInputInterception(XInterface_8f010a43):
    """
    Interface to add handlers for key and mouse events.
    
    A handler is not a passive listener, it can even consume the event.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XUserInputInterception <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XUserInputInterception.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XUserInputInterception'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XUserInputInterception'

    @abstractmethod
    def addKeyHandler(self, xHandler: 'XKeyHandler_98520a93') -> None:
        """
        Add a new listener that is called on com.sun.star.awt.KeyEvent.
        
        Every listener is given the opportunity to consume the event, i.e. prevent the not yet called listeners from being called.
        """
        ...
    @abstractmethod
    def addMouseClickHandler(self, xHandler: 'XMouseClickHandler_edcb0d59') -> None:
        """
        Add a new listener that is called on com.sun.star.awt.MouseEvent.
        
        Every listener is given the opportunity to consume the event, i.e. prevent the not yet called listeners from being called.
        """
        ...
    @abstractmethod
    def removeKeyHandler(self, xHandler: 'XKeyHandler_98520a93') -> None:
        """
        Remove the specified listener from the list of listeners.
        """
        ...
    @abstractmethod
    def removeMouseClickHandler(self, xHandler: 'XMouseClickHandler_edcb0d59') -> None:
        """
        Remove the specified listener from the list of listeners.
        """
        ...

__all__ = ['XUserInputInterception']


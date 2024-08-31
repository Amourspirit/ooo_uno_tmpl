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
# Namespace: com.sun.star.inspection
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924
    from .x_property_control_context import XPropertyControlContext as XPropertyControlContext_b94c12c7

class XPropertyControl(ABC):
    """
    defines the interface for a single control in an ObjectInspector
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API XPropertyControl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XPropertyControl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.inspection'
    __ooo_full_ns__: str = 'com.sun.star.inspection.XPropertyControl'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.inspection.XPropertyControl'

    @abstractmethod
    def isModified(self) -> bool:
        """
        determines whether the control content is currently modified
        
        An XPropertyControl internally manages a flag indicating whether its content is modified. This flag is reset to FALSE every time our ControlContext is notified of our current value. Also, the control implementation must set this flag to TRUE if and only if the user changed the control content.
        """
        ...
    @abstractmethod
    def notifyModifiedValue(self) -> None:
        """
        notifies the context in which the control lives of the current control value, if this value is currently modified
        """
        ...
    @property
    @abstractmethod
    def ControlContext(self) -> XPropertyControlContext_b94c12c7:
        """
        specifies the context of the control within the ObjectInspector.
        
        The property control should actively notify its state changes to the context. In particular, changes in the focus and the value of the control must be notified.
        """
        ...

    @property
    @abstractmethod
    def ControlType(self) -> int:
        """
        denotes the type of the control, as one of the PropertyControlType constants
        """
        ...

    @property
    @abstractmethod
    def ControlWindow(self) -> XWindow_713b0924:
        """
        denotes the window which is the real UI representation of the property control.
        
        The ObjectInspector will automatically position and size this control as needed, care for its Z-order, and so on.
        
        This Window must not be NULL, else the whole control is not usable.
        """
        ...

    @property
    @abstractmethod
    def Value(self) -> object:
        """
        denotes the current content of the control.
        
        At every point in time, this value is either VOID, or of the type described by ValueType.
        """
        ...

    @property
    @abstractmethod
    def ValueType(self) -> object:
        """
        denotes the value type of the control.
        """
        ...


__all__ = ['XPropertyControl']


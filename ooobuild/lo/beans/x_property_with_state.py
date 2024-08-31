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
# Namespace: com.sun.star.beans
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from com.sun.star.beans.PropertyState import PropertyStateProto  # type: ignore

class XPropertyWithState(XInterface_8f010a43):
    """
    makes it possible to query information about the state of this object, seen as a property contained in a property set.
    
    This interface provides direct access to operations that are available if the containing property set implements XPropertyState.
    
    The state contains the information if:
    
    Generally objects that implement this interface also implement XProperty.

    See Also:
        `API XPropertyWithState <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertyWithState.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.XPropertyWithState'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.beans.XPropertyWithState'

    @abstractmethod
    def getDefaultAsProperty(self) -> XInterface_8f010a43:
        """
        If no default exists, is not known or is void, then the return value is NULL.

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def getStateAsProperty(self) -> PropertyStateProto:
        """
        """
        ...
    @abstractmethod
    def setToDefaultAsProperty(self) -> None:
        """
        sets this to its default value.
        
        The value depends on the implementation of this interface. If this is a bound property, the value changes before the change events are fired. If this is a constrained property, the vetoable event is fired before the property value changes.

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...

__all__ = ['XPropertyWithState']
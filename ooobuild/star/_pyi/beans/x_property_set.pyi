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
# Namespace: com.sun.star.beans
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_property_change_listener import XPropertyChangeListener as XPropertyChangeListener_58e4105a
    from .x_property_set_info import XPropertySetInfo as XPropertySetInfo_efa90d86
    from .x_vetoable_change_listener import XVetoableChangeListener as XVetoableChangeListener_55a41027

class XPropertySet(XInterface_8f010a43):
    """
    provides information about and access to the properties from an implementation.
    
    There are three types of properties:
    
    You can listen to changes of bound properties with the XPropertyChangeListener and you can veto changes of constrained properties with the XVetoableChangeListener.
    
    To implement inaccurate name access, you must support the interface XExactName.

    See Also:
        `API XPropertySet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertySet.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.beans.XPropertySet']

    def addPropertyChangeListener(self, aPropertyName: str, xListener: 'XPropertyChangeListener_58e4105a') -> None:
        """
        adds an XPropertyChangeListener to the specified property.
        
        An empty name (\"\") registers the listener to all bound properties. If the property is not bound, the behavior is not specified.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    def addVetoableChangeListener(self, PropertyName: str, aListener: 'XVetoableChangeListener_55a41027') -> None:
        """
        adds an XVetoableChangeListener to the specified property with the name PropertyName.
        
        An empty name (\"\") registers the listener to all constrained properties. If the property is not constrained, the behavior is not specified.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    def getPropertySetInfo(self) -> 'XPropertySetInfo_efa90d86':
        """
        """
    def getPropertyValue(self, PropertyName: str) -> object:
        """

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    def removePropertyChangeListener(self, aPropertyName: str, aListener: 'XPropertyChangeListener_58e4105a') -> None:
        """
        removes an XPropertyChangeListener from the listener list.
        
        It is a \"noop\" if the listener is not registered.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    def removeVetoableChangeListener(self, PropertyName: str, aListener: 'XVetoableChangeListener_55a41027') -> None:
        """
        removes an XVetoableChangeListener from the listener list.
        
        It is a \"noop\" if the listener is not registered.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    def setPropertyValue(self, aPropertyName: str, aValue: object) -> None:
        """
        sets the value of the property with the specified name.
        
        If it is a bound property the value will be changed before the change event is fired. If it is a constrained property a vetoable event is fired before the property value can be changed.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """


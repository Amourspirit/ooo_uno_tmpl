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
# Namespace: com.sun.star.beans
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_hierarchical_property_set_info import XHierarchicalPropertySetInfo as XHierarchicalPropertySetInfo_ae271245


class XHierarchicalPropertySet(XInterface_8f010a43):
    """
    provides information about and access to the a hierarchy of properties from an implementation.
    
    Usually an object that implements this interface also implements XPropertySet and at least some of the properties have subproperties.
    
    This interface allows direct access to subsubproperties, ... up to an arbitrary nesting depth. Often the intermediate elements of the hierarchy implement XProperty.
    
    Each implementation specifies how the hierarchical property names, that are used to access the elements of the hierarchy, are formed.
    
    Commonly a notation similar to filesystem paths (separated by '/' slashes) or nested module names (separated by dots '.' or '.') is used.

    See Also:
        `API XHierarchicalPropertySet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XHierarchicalPropertySet.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.beans.XHierarchicalPropertySet'

    def getHierarchicalPropertySetInfo(self) -> 'XHierarchicalPropertySetInfo_ae271245':
        """
        retrieve information about the hierarchy of properties
        """
        ...
    def getHierarchicalPropertyValue(self, aHierarchicalPropertyName: str) -> typing.Any:
        """

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def setHierarchicalPropertyValue(self, aHierarchicalPropertyName: str, aValue: typing.Any) -> None:
        """
        sets the value of the property with the specified nested name.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...


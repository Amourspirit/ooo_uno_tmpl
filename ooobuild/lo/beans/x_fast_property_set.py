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
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XFastPropertySet(XInterface_8f010a43):
    """
    provides a fast way of accessing and changing property values.
    
    This interface is an extension to the XPropertySet interface. The get and set methods use handles to access the property values instead of character strings.

    See Also:
        `API XFastPropertySet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XFastPropertySet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.XFastPropertySet'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.beans.XFastPropertySet'

    @abstractmethod
    def getFastPropertyValue(self, nHandle: int) -> object:
        """

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def setFastPropertyValue(self, nHandle: int, aValue: object) -> None:
        """
        sets the value to the property with the specified name.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...

__all__ = ['XFastPropertySet']


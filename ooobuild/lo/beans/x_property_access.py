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
    from .property_value import PropertyValue as PropertyValue_c9610c73

class XPropertyAccess(XInterface_8f010a43):
    """
    makes it possible to access all property values and to set them at once.
    
    In most cases this interface will be in addition to XPropertySet. It is especially useful for remote communication because it lessens the number of calls for getting property values; that is especially important because these calls are necessarily synchronous.
    
    Another advantage of this method is that conflicts are avoided if property value restrictions depend on the value of other properties.

    See Also:
        `API XPropertyAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertyAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.XPropertyAccess'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.beans.XPropertyAccess'

    @abstractmethod
    def getPropertyValues(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        """
        ...
    @abstractmethod
    def setPropertyValues(self, aProps: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        sets the values of given properties.
        
        All properties which are not contained in the sequence aProps will be left unchanged.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...

__all__ = ['XPropertyAccess']


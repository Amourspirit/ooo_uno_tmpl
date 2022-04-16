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
# Namespace: com.sun.star.linguistic2
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XConversionPropertyType(XInterface_8f010a43):
    """
    allows set and retrieve the property type of an entry in a conversion dictionary
    
    The property type must be one of com.sun.star.linguistic2.ConversionPropertyType
    
    **since**
    
        OOo 2.0

    See Also:
        `API XConversionPropertyType <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XConversionPropertyType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.linguistic2'
    __ooo_full_ns__: str = 'com.sun.star.linguistic2.XConversionPropertyType'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.linguistic2.XConversionPropertyType'

    @abstractmethod
    def getPropertyType(self, aLeftText: str, aRightText: str) -> int:
        """
        returns the property type for the specified entry.
        
        The conversion entry is specified by the pair ( aLeftText, aRightText ).

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
    @abstractmethod
    def setPropertyType(self, aLeftText: str, aRightText: str, nPropertyType: int) -> None:
        """
        sets the property type for the specified entry.
        
        The conversion entry is specified by the pair ( aLeftText, aRightText ).

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XConversionPropertyType']


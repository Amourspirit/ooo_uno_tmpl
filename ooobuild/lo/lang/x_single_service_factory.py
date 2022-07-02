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
# Namespace: com.sun.star.lang
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XSingleServiceFactory(XInterface_8f010a43):
    """
    Factory interface to produce instances of an implementation of a service specification.
    
    This interface is deprecated. Please use XSingleComponentFactory.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XSingleServiceFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XSingleServiceFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.lang'
    __ooo_full_ns__: str = 'com.sun.star.lang.XSingleServiceFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.lang.XSingleServiceFactory'

    @abstractmethod
    def createInstance(self) -> 'XInterface_8f010a43':
        """
        Creates an instance of a service implementation.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def createInstanceWithArguments(self, aArguments: 'typing.Tuple[object, ...]') -> 'XInterface_8f010a43':
        """
        Creates an instance of a service implementation initialized with some arguments.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XSingleServiceFactory']


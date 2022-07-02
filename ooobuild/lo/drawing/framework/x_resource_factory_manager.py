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
# Namespace: com.sun.star.drawing.framework
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_resource_factory import XResourceFactory as XResourceFactory_b3561268

class XResourceFactoryManager(ABC):
    """
    The XResourceFactoryManager is part of the configuration controller and manages the set of registered resource factories.

    See Also:
        `API XResourceFactoryManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XResourceFactoryManager.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing.framework'
    __ooo_full_ns__: str = 'com.sun.star.drawing.framework.XResourceFactoryManager'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.framework.XResourceFactoryManager'

    @abstractmethod
    def addResourceFactory(self, sResourceURL: str, xResourceFactory: 'XResourceFactory_b3561268') -> None:
        """
        Register a new resource factory for the given URL.
        
        When one factory is responsible for more than one type of resource then this method has to be called for each type. If this method is called multiple times for the same URL then a previously registered factory is removed for the URL.
        """
        ...
    @abstractmethod
    def getResourceFactory(self, sResourceURL: str) -> 'XResourceFactory_b3561268':
        """
        Return the resource factory that was previously registered for the given resource type.
        
        This method is typically called by one of the resource controllers.
        """
        ...
    @abstractmethod
    def removeResourceFactoryForReference(self, xResourceFactory: 'XResourceFactory_b3561268') -> None:
        """
        Remove a resource factory for all resource types it has been registered for.
        
        Use removeResourceFactoryForURL() to remove a factory just for one resource type and to leave it registered for others.
        """
        ...
    @abstractmethod
    def removeResourceFactoryForURL(self, sResourceURL: str) -> None:
        """
        Remove a resource factory for one type of resource.
        
        When the factory has been registered for other URLs as well then it remains registered for them. Use the removeResourceFactoryForReference() to remove a factory completely.
        """
        ...

__all__ = ['XResourceFactoryManager']


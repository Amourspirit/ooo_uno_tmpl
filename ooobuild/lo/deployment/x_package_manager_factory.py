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
# Namespace: com.sun.star.deployment
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_package_manager import XPackageManager as XPackageManager_2bc50f08

class XPackageManagerFactory(ABC):
    """
    The XPackageManagerFactory interface is used to obtain XPackageManager instances.
    
    You have to use the singleton  /singletons/com.sun.star.deployment.thePackageManagerFactory  exclusively.
    
    **since**
    
        OOo 2.0
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XPackageManagerFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1deployment_1_1XPackageManagerFactory.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.deployment'
    __ooo_full_ns__: str = 'com.sun.star.deployment.XPackageManagerFactory'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.deployment.XPackageManagerFactory'

    @abstractmethod
    def getPackageManager(self, context: str) -> XPackageManager_2bc50f08:
        """
        Method to create (or reusing and already existing) XPackageManager object to add or remove UNO packages persistently.
        
        Packages for context strings \"user\" and \"shared\" will be registered and revoked persistently.
        
        Context strings other than \"user\", \"shared\" will last in an com.sun.star.lang.IllegalArgumentException.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XPackageManagerFactory']


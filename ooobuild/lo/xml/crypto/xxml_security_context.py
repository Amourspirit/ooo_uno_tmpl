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
# Namespace: com.sun.star.xml.crypto
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_security_environment import XSecurityEnvironment as XSecurityEnvironment_7ead116d

class XXMLSecurityContext(XInterface_8f010a43):
    """
    Interface of XML security context.
    
    This interface specifies a certain signature context. By signature context, the signer or verifier retrieves key specification.

    See Also:
        `API XXMLSecurityContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1XXMLSecurityContext.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.XXMLSecurityContext'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.crypto.XXMLSecurityContext'

    @abstractmethod
    def addSecurityEnvironment(self, aSecurityEnvironment: 'XSecurityEnvironment_7ead116d') -> int:
        """
        Add personal security environment , and return the index of the added environment.

        Raises:
            com.sun.star.security.SecurityInfrastructureException: ``SecurityInfrastructureException``
        """
    @abstractmethod
    def getDefaultSecurityEnvironmentIndex(self) -> int:
        """
        Get the ID of the internal security environment.
        """
    @abstractmethod
    def getSecurityEnvironment(self) -> 'XSecurityEnvironment_7ead116d':
        """
        An handy method to get the first personal security environment.
        
        In XMLSec/NSS, the first personal security environment should be the \"internal slot\"
        """
    @abstractmethod
    def getSecurityEnvironmentByIndex(self, index: int) -> 'XSecurityEnvironment_7ead116d':
        """
        Get personal security environment.
        """
    @abstractmethod
    def getSecurityEnvironmentNumber(self) -> int:
        """
        Get the number of security environments.
        """
    @abstractmethod
    def setDefaultSecurityEnvironmentIndex(self, index: int) -> None:
        """
        set the ID of the internal security environment
        """

__all__ = ['XXMLSecurityContext']


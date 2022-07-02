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
# Namespace: com.sun.star.ucb
from abc import abstractmethod
from .x_interaction_supply_authentication import XInteractionSupplyAuthentication as XInteractionSupplyAuthentication_d8611367

class XInteractionSupplyAuthentication2(XInteractionSupplyAuthentication_d8611367):
    """
    An interaction continuation handing back some authentication data.
    
    This continuation is typically used in conjunction with AuthenticationRequest.
    
    **since**
    
        OOo 3.2

    See Also:
        `API XInteractionSupplyAuthentication2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XInteractionSupplyAuthentication2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.XInteractionSupplyAuthentication2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ucb.XInteractionSupplyAuthentication2'

    @abstractmethod
    def canUseSystemCredentials(self, Default: bool) -> bool:
        """
        Specifies if \"system credentials\" can be obtained and used by the issuer of the authentication request.

        * ``Default`` is an out direction argument.
        """
        ...
    @abstractmethod
    def setUseSystemCredentials(self, UseSystemCredentials: bool) -> None:
        """
        Set a new \"use system credentials\" value to hand back.
        """
        ...

__all__ = ['XInteractionSupplyAuthentication2']


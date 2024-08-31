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
# Namespace: com.sun.star.ucb
from __future__ import annotations
import typing

from ..task.x_interaction_continuation import XInteractionContinuation as XInteractionContinuation_5af0108e
if typing.TYPE_CHECKING:
    from com.sun.star.ucb.RememberAuthentication import RememberAuthenticationProto  # type: ignore


class XInteractionSupplyAuthentication(XInteractionContinuation_5af0108e):
    """
    An interaction continuation handing back some authentication data.
    
    This continuation is typically used in conjunction with AuthenticationRequest.

    See Also:
        `API XInteractionSupplyAuthentication <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XInteractionSupplyAuthentication.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.ucb.XInteractionSupplyAuthentication'

    def canSetAccount(self) -> bool:
        """
        Specifies if an \"account\" value can be handed back.
        """
        ...
    def canSetPassword(self) -> bool:
        """
        Specifies if a \"password\" value can be handed back.
        """
        ...
    def canSetRealm(self) -> bool:
        """
        Specifies if a new \"realm\" value can be handed back.
        """
        ...
    def canSetUserName(self) -> bool:
        """
        Specifies if a \"user name\" value can be handed back.
        """
        ...
    def getRememberAccountModes(self, Default: RememberAuthenticationProto) -> typing.Tuple[RememberAuthenticationProto, ...]:
        """
        Specifies the available modes of how long to remember the account.

        * ``Default`` is an out direction argument.
        """
        ...
    def getRememberPasswordModes(self, Default: RememberAuthenticationProto) -> typing.Tuple[RememberAuthenticationProto, ...]:
        """
        Specifies the available modes of how long to remember the password.

        * ``Default`` is an out direction argument.
        """
        ...
    def setAccount(self, Account: str) -> None:
        """
        Set a new \"account\" value to hand back.
        
        This method should be called before com.sun.star.task.XInteractionContinuation.select(), and should only be called if XInteractionSupplyAuthentication.canSetAccount() returned TRUE.
        """
        ...
    def setPassword(self, Password: str) -> None:
        """
        Set a new \"password\" value to hand back.
        
        This method should be called before com.sun.star.task.XInteractionContinuation.select(), and should only be called if XInteractionSupplyAuthentication.canSetPassword() returned TRUE.
        """
        ...
    def setRealm(self, Realm: str) -> None:
        """
        Set a new \"realm\" value to hand back.
        
        This method should be called before com.sun.star.task.XInteractionContinuation.select(), and should only be called if XInteractionSupplyAuthentication.canSetRealm() returned TRUE.
        """
        ...
    def setRememberAccount(self, Remember: RememberAuthenticationProto) -> None:
        """
        Set a new mode of how long to remember the account.
        
        This method should be called before com.sun.star.task.XInteractionContinuation.select(), and should only be called if XInteractionSupplyAuthentication.setAccount() is also called.
        """
        ...
    def setRememberPassword(self, Remember: RememberAuthenticationProto) -> None:
        """
        Set a new mode of how long to remember the password.
        
        This method should be called before com.sun.star.task.XInteractionContinuation.select(), and should only be called if XInteractionSupplyAuthentication.setPassword() is also called.
        """
        ...
    def setUserName(self, UserName: str) -> None:
        """
        Set a new \"user name\" value to hand back.
        
        This method should be called before com.sun.star.task.XInteractionContinuation.select(), and should only be called if XInteractionSupplyAuthentication.canSetUserName() returned TRUE.
        """
        ...

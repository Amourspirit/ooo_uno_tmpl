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
# Namespace: com.sun.star.security
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XPolicy(XInterface_8f010a43):
    """
    Interface for getting sets of permissions of a specified user or the default permissions if no user is given.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XPolicy <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1security_1_1XPolicy.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.security'
    __ooo_full_ns__: str = 'com.sun.star.security.XPolicy'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.security.XPolicy'

    @abstractmethod
    def getDefaultPermissions(self) -> typing.Tuple[object, ...]:
        """
        Gets the default permissions granted to all users.
        """
        ...
    @abstractmethod
    def getPermissions(self, userId: str) -> typing.Tuple[object, ...]:
        """
        Gets the permissions of the specified user excluding the default permissions granted to all users.
        """
        ...
    @abstractmethod
    def refresh(self) -> None:
        """
        Refreshes the policy configuration.
        """
        ...

__all__ = ['XPolicy']


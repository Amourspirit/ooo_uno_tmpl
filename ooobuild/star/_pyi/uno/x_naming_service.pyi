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
# Namespace: com.sun.star.uno
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .x_interface import XInterface as XInterface_8f010a43


class XNamingService(XInterface_8f010a43):
    """
    allows to insert, remove and access named objects.

    See Also:
        `API XNamingService <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XNamingService.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.uno.XNamingService']

    def getRegisteredObject(self, Name: str) -> 'XInterface_8f010a43':
        """
        provides a previous registered object.

        Raises:
            Exception: ``Exception``
        """
        ...
    def registerObject(self, Name: str, Object: 'XInterface_8f010a43') -> None:
        """
        registers one object under the specified name.
        
        If any object is registered before, then this object is revoked automatically.

        Raises:
            Exception: ``Exception``
        """
        ...
    def revokeObject(self, Name: str) -> None:
        """
        revokes the registration of an object.
        
        If the object was not previously registered, then this call does nothing.

        Raises:
            Exception: ``Exception``
        """
        ...



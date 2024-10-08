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
# Namespace: com.sun.star.configuration.backend
from __future__ import annotations
import typing

from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_layer import XLayer as XLayer_4cd50fcb
    from .x_update_handler import XUpdateHandler as XUpdateHandler_d8f512ef


class XBackend(XInterface_8f010a43):
    """
    Handles access to layered data stored in a repository.
    
    Data can be retrieved on behalf of one or more entities.
    
    There is an implied owner entity associated to the object when it is created. This entity should be used for normal data access. For administrative operations data of other entities can be accessed.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XBackend <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XBackend.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.configuration.backend.XBackend'

    def getOwnUpdateHandler(self, aComponent: str) -> XUpdateHandler_d8f512ef:
        """
        creates an update handler for the owner entity layer for a component.

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getUpdateHandler(self, aComponent: str, aEntity: str) -> XUpdateHandler_d8f512ef:
        """
        creates an update handler on an entity's layer for a component.

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def listLayers(self, aComponent: str, aEntity: str) -> typing.Tuple[XLayer_4cd50fcb, ...]:
        """
        retrieves the layers associated to an entity for a component.

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def listOwnLayers(self, aComponent: str) -> typing.Tuple[XLayer_4cd50fcb, ...]:
        """
        retrieves the layers associated to the owner entity for a component.

        Raises:
            BackendAccessException: ``BackendAccessException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...



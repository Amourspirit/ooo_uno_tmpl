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
# Namespace: com.sun.star.registry
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_registry_key import XRegistryKey as XRegistryKey_e61a0d5b


class XSimpleRegistry(XInterface_8f010a43):
    """
    allows access to a registry (a persistent data source).
    
    The data is stored in a hierarchical key structure beginning with a root key. Each key can store a value and can have multiple subkeys.

    See Also:
        `API XSimpleRegistry <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1registry_1_1XSimpleRegistry.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.registry.XSimpleRegistry'

    def close(self) -> None:
        """
        disconnects the registry from the data-source.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
        ...
    def destroy(self) -> None:
        """
        destroys the registry and the data source.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
        ...
    def getRootKey(self) -> 'XRegistryKey_e61a0d5b':
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
        ...
    def getURL(self) -> str:
        """
        returns the URL of the current data source of the registry.
        """
        ...
    def isReadOnly(self) -> bool:
        """
        checks if the registry is readonly.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
        ...
    def isValid(self) -> bool:
        """
        checks if the registry points to a valid data-source.
        """
        ...
    def mergeKey(self, aKeyName: str, aUrl: str) -> None:
        """
        DEPRECATED: this method lacks a registry key (better than a URL).
        
        merges a registry under the specified key.
        
        If the key does not exist it will be created. Existing keys will be overridden from keys of registry specified by aUrl.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
            com.sun.star.registry.MergeConflictException: ``MergeConflictException``
        """
        ...
    def open(self, rURL: str, bReadOnly: bool, bCreate: bool) -> None:
        """
        connects the registry to a persistent data source represented by a URL.
        
        If a local registry is already open, this function will close the currently open registry.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
        ...


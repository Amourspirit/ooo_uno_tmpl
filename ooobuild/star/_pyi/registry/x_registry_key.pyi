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
# Namespace: com.sun.star.registry
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .registry_key_type import RegistryKeyType as RegistryKeyType_11940ea5
    from .registry_value_type import RegistryValueType as RegistryValueType_30390f79

class XRegistryKey(XInterface_8f010a43):
    """
    makes structural information (except regarding tree structures) of a single registry key accessible.
    
    This is the main interface for registry keys.

    See Also:
        `API XRegistryKey <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1registry_1_1XRegistryKey.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.registry.XRegistryKey']

    def closeKey(self) -> None:
        """
        closes a key in the registry.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def createKey(self, aKeyName: str) -> 'XRegistryKey':
        """
        creates a new key in the registry.
        
        If the key already exists, the function will open the key.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def createLink(self, aLinkName: str, aLinkTarget: str) -> bool:
        """
        creates a new link in the registry.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def deleteKey(self, rKeyName: str) -> None:
        """
        deletes a key from the registry.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def deleteLink(self, rLinkName: str) -> None:
        """
        deletes a link from the registry.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def getAsciiListValue(self) -> 'typing.Tuple[str, ...]':
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
            com.sun.star.registry.InvalidValueException: ``InvalidValueException``
        """
    def getAsciiValue(self) -> str:
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
            com.sun.star.registry.InvalidValueException: ``InvalidValueException``
        """
    def getBinaryValue(self) -> 'typing.Tuple[int, ...]':
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
            com.sun.star.registry.InvalidValueException: ``InvalidValueException``
        """
    def getKeyNames(self) -> 'typing.Tuple[str, ...]':
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def getKeyType(self, rKeyName: str) -> 'RegistryKeyType_11940ea5':
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def getLinkTarget(self, rLinkName: str) -> str:
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def getLongListValue(self) -> 'typing.Tuple[int, ...]':
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
            com.sun.star.registry.InvalidValueException: ``InvalidValueException``
        """
    def getLongValue(self) -> int:
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
            com.sun.star.registry.InvalidValueException: ``InvalidValueException``
        """
    def getResolvedName(self, aKeyName: str) -> str:
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def getStringListValue(self) -> 'typing.Tuple[str, ...]':
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
            com.sun.star.registry.InvalidValueException: ``InvalidValueException``
        """
    def getStringValue(self) -> str:
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
            com.sun.star.registry.InvalidValueException: ``InvalidValueException``
        """
    def getValueType(self) -> 'RegistryValueType_30390f79':
        """

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def isReadOnly(self) -> bool:
        """
        checks if the key can be overwritten.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def isValid(self) -> bool:
        """
        checks if the key points to an open valid key in the data-source.
        """
    def openKey(self, aKeyName: str) -> 'XRegistryKey':
        """
        opens a sub key of the key.
        
        If the sub key does not exist, the function returns a NULL-interface.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def openKeys(self) -> 'typing.Tuple[XRegistryKey, ...]':
        """
        opens all subkeys of the key.
        
        If a subkey is a link, the link will be resolved and the appropriate key will be opened.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def setAsciiListValue(self, seqValue: 'typing.Tuple[str, ...]') -> None:
        """
        sets an ASCII string list value to the key.
        
        The high byte of the string should be NULL. If not, there is no guarantee that the string will be correctly transported. If the key already has a value, the value will be overridden.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def setAsciiValue(self, value: str) -> None:
        """
        sets an ASCII string value to the key.
        
        The high byte of the string should be NULL. If not, there is no guarantee that the string will be correctly transported. If the key already has a value, the value will be overridden.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def setBinaryValue(self, value: 'typing.Tuple[int, ...]') -> None:
        """
        sets a binary value to the key.
        
        If the key already has a value, the value will be overridden.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def setLongListValue(self, seqValue: 'typing.Tuple[int, ...]') -> None:
        """
        sets a long list value to the key.
        
        If the key already has a value, the value will be overridden.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def setLongValue(self, value: int) -> None:
        """
        sets a long value to the key.
        
        If the key already has a value, the value will be overridden.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def setStringListValue(self, seqValue: 'typing.Tuple[str, ...]') -> None:
        """
        sets a unicode string value to the key.
        
        If the key already has a value, the value will be overridden.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    def setStringValue(self, value: str) -> None:
        """
        sets a unicode string value to the key.
        
        If the key already has a value, the value will be overridden.

        Raises:
            com.sun.star.registry.InvalidRegistryException: ``InvalidRegistryException``
        """
    @property
    def KeyName(self) -> str:
        """
        This is the key of the entry relative to its parent.
        
        The access path starts with the root \"/\" and all parent entry names are delimited with slashes \"/\" too, like in a UNIX (R) file system. Slashes which are part of single names are represented as hexadecimals preceded with a \"%\" like in URL syntax.
        """



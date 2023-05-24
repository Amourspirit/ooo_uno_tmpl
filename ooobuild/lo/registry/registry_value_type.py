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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.registry
# Libre Office Version: 7.4
from __future__ import annotations
from typing import cast, TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from com.sun.star.registry.RegistryValueType import RegistryValueTypeProto

class RegistryValueType(Enum):
    """
    Enum Class


    See Also:
        `API RegistryValueType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1registry.html#a62fb96939bafde3da828f782a8433ac3>`_
    """
    __ooo_ns__: str = 'com.sun.star.registry'
    __ooo_full_ns__: str = 'com.sun.star.registry.RegistryValueType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.registry.RegistryValueType'

    ASCII = cast("RegistryValueTypeProto", 'ASCII')
    """
    the type of the key is ASCII.
    """
    ASCIILIST = cast("RegistryValueTypeProto", 'ASCIILIST')
    """
    the type of the key is an ASCIILIST.
    """
    BINARY = cast("RegistryValueTypeProto", 'BINARY')
    """
    the type of the key is binary.
    """
    LONG = cast("RegistryValueTypeProto", 'LONG')
    """
    the type of the key is long.
    """
    LONGLIST = cast("RegistryValueTypeProto", 'LONGLIST')
    """
    the type of the key is LONGLIST.
    """
    NOT_DEFINED = cast("RegistryValueTypeProto", 'NOT_DEFINED')
    """
    the type of the key is not defined.
    """
    STRING = cast("RegistryValueTypeProto", 'STRING')
    """
    the type of the key is a string.
    """
    STRINGLIST = cast("RegistryValueTypeProto", 'STRINGLIST')
    """
    the type of the key is a STRINGLIST.
    """

__all__ = ['RegistryValueType']


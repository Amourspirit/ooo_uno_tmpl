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
# Namespace: com.sun.star.uno
# Libre Office Version: 7.4
from typing import cast
from enum import Enum
from com.sun.star.uno.TypeClass import TypeClassProto

class TypeClass(Enum):
    """
    Enum Class


    See Also:
        `API TypeClass <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1uno.html#a00683ed3ec24b47c36ead10a20d6f328>`_
    """
    __ooo_ns__: str = 'com.sun.star.uno'
    __ooo_full_ns__: str = 'com.sun.star.uno.TypeClass'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.uno.TypeClass'

    ANY = cast(TypeClassProto, 'ANY')
    """
    reflecting the any type; anys can carry any UNO value except of any values
    """
    ARRAY = cast(TypeClassProto, 'ARRAY')
    """
    Deprecated, UNOIDL does not have an array concept.
    """
    BOOLEAN = cast(TypeClassProto, 'BOOLEAN')
    """
    reflecting the boolean type; true and false
    """
    BYTE = cast(TypeClassProto, 'BYTE')
    """
    reflecting the 8-bit ordinal type
    """
    CHAR = cast(TypeClassProto, 'CHAR')
    """
    reflecting the 16-bit unicode character type
    """
    CONSTANT = cast(TypeClassProto, 'CONSTANT')
    """
    reflecting constants
    """
    CONSTANTS = cast(TypeClassProto, 'CONSTANTS')
    """
    reflecting constants groups
    """
    DOUBLE = cast(TypeClassProto, 'DOUBLE')
    """
    reflecting the 64-bit floating point type
    """
    ENUM = cast(TypeClassProto, 'ENUM')
    """
    reflecting enum types
    """
    EXCEPTION = cast(TypeClassProto, 'EXCEPTION')
    """
    reflecting exception types
    """
    FLOAT = cast(TypeClassProto, 'FLOAT')
    """
    reflecting the 32-bit floating point type
    """
    HYPER = cast(TypeClassProto, 'HYPER')
    """
    reflecting the signed 64-bit ordinal type
    """
    INTERFACE = cast(TypeClassProto, 'INTERFACE')
    """
    reflecting interface types
    """
    INTERFACE_ATTRIBUTE = cast(TypeClassProto, 'INTERFACE_ATTRIBUTE')
    """
    reflecting interface attributes
    """
    INTERFACE_METHOD = cast(TypeClassProto, 'INTERFACE_METHOD')
    """
    reflecting interface methods
    """
    LONG = cast(TypeClassProto, 'LONG')
    """
    reflecting the signed 32-bit ordinal type
    """
    MODULE = cast(TypeClassProto, 'MODULE')
    """
    reflecting modules
    """
    PROPERTY = cast(TypeClassProto, 'PROPERTY')
    """
    reflecting properties
    """
    SEQUENCE = cast(TypeClassProto, 'SEQUENCE')
    """
    reflecting sequence types
    """
    SERVICE = cast(TypeClassProto, 'SERVICE')
    """
    reflecting services
    """
    SHORT = cast(TypeClassProto, 'SHORT')
    """
    reflecting the signed 16-bit ordinal type
    """
    SINGLETON = cast(TypeClassProto, 'SINGLETON')
    """
    reflecting singletons
    """
    STRING = cast(TypeClassProto, 'STRING')
    """
    reflecting the string type; strings of unicode characters
    """
    STRUCT = cast(TypeClassProto, 'STRUCT')
    """
    reflecting compound types
    """
    TYPE = cast(TypeClassProto, 'TYPE')
    """
    reflecting the meta type
    """
    TYPEDEF = cast(TypeClassProto, 'TYPEDEF')
    """
    reflecting typedefed types referencing other types
    """
    UNION = cast(TypeClassProto, 'UNION')
    """
    Deprecated, UNOIDL does not have a union concept.
    """
    UNKNOWN = cast(TypeClassProto, 'UNKNOWN')
    """
    reflecting the unreflectable type
    """
    UNSIGNED_HYPER = cast(TypeClassProto, 'UNSIGNED_HYPER')
    """
    reflecting the unsigned 64-bit ordinal type
    """
    UNSIGNED_LONG = cast(TypeClassProto, 'UNSIGNED_LONG')
    """
    reflecting the unsigned 32-bit type
    """
    UNSIGNED_SHORT = cast(TypeClassProto, 'UNSIGNED_SHORT')
    """
    reflecting the unsigned 16-bit ordinal type
    """
    VOID = cast(TypeClassProto, 'VOID')
    """
    reflecting the void type; denotes no type
    """

__all__ = ['TypeClass']


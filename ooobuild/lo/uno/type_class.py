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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.uno
# Libre Office Version: 7.2
from enum import Enum


class TypeClass(Enum):
    """
    Enum Class

    

    See Also:
        `API TypeClass <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1uno.html#a00683ed3ec24b47c36ead10a20d6f328>`_
    """
    __ooo_ns__: str = 'com.sun.star.uno'
    __ooo_full_ns__: str = 'com.sun.star.uno.TypeClass'
    __ooo_type_name__: str = 'enum'

    ANY = 'ANY'
    """
    reflecting the any type; anys can carry any UNO value except of any values
    """
    ARRAY = 'ARRAY'
    """
    Deprecated, UNOIDL does not have an array concept.
    """
    BOOLEAN = 'BOOLEAN'
    """
    reflecting the boolean type; true and false
    """
    BYTE = 'BYTE'
    """
    reflecting the 8-bit ordinal type
    """
    CHAR = 'CHAR'
    """
    reflecting the 16-bit unicode character type
    """
    CONSTANT = 'CONSTANT'
    """
    reflecting constants
    """
    CONSTANTS = 'CONSTANTS'
    """
    reflecting constants groups
    """
    DOUBLE = 'DOUBLE'
    """
    reflecting the 64-bit floating point type
    """
    ENUM = 'ENUM'
    """
    reflecting enum types
    """
    EXCEPTION = 'EXCEPTION'
    """
    reflecting exception types
    """
    FLOAT = 'FLOAT'
    """
    reflecting the 32-bit floating point type
    """
    HYPER = 'HYPER'
    """
    reflecting the signed 64-bit ordinal type
    """
    INTERFACE = 'INTERFACE'
    """
    reflecting interface types
    """
    INTERFACE_ATTRIBUTE = 'INTERFACE_ATTRIBUTE'
    """
    reflecting interface attributes
    """
    INTERFACE_METHOD = 'INTERFACE_METHOD'
    """
    reflecting interface methods
    """
    LONG = 'LONG'
    """
    reflecting the signed 32-bit ordinal type
    """
    MODULE = 'MODULE'
    """
    reflecting modules
    """
    PROPERTY = 'PROPERTY'
    """
    reflecting properties
    """
    SEQUENCE = 'SEQUENCE'
    """
    reflecting sequence types
    """
    SERVICE = 'SERVICE'
    """
    reflecting services
    """
    SHORT = 'SHORT'
    """
    reflecting the signed 16-bit ordinal type
    """
    SINGLETON = 'SINGLETON'
    """
    reflecting singletons
    """
    STRING = 'STRING'
    """
    reflecting the string type; strings of unicode characters
    """
    STRUCT = 'STRUCT'
    """
    reflecting compound types
    """
    TYPE = 'TYPE'
    """
    reflecting the meta type
    """
    TYPEDEF = 'TYPEDEF'
    """
    reflecting typedefed types referencing other types
    """
    UNION = 'UNION'
    """
    Deprecated, UNOIDL does not have a union concept.
    """
    UNKNOWN = 'UNKNOWN'
    """
    reflecting the unreflectable type
    """
    UNSIGNED_HYPER = 'UNSIGNED_HYPER'
    """
    reflecting the unsigned 64-bit ordinal type
    """
    UNSIGNED_LONG = 'UNSIGNED_LONG'
    """
    reflecting the unsigned 32-bit type
    """
    UNSIGNED_SHORT = 'UNSIGNED_SHORT'
    """
    reflecting the unsigned 16-bit ordinal type
    """
    VOID = 'VOID'
    """
    reflecting the void type; denotes no type
    """

__all__ = ['TypeClass']


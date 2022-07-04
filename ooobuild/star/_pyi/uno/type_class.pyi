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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.uno
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class TypeClass(Enum):
    """
    Enum

    

    See Also:
        `API TypeClass <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1uno.html#a00683ed3ec24b47c36ead10a20d6f328>`_
    """
    typeName: str = 'com.sun.star.uno.TypeClass'

    ANY: 'uno.Enum'
    """
    reflecting the any type; anys can carry any UNO value except of any values
    """
    ARRAY: 'uno.Enum'
    """
    Deprecated, UNOIDL does not have an array concept.
    """
    BOOLEAN: 'uno.Enum'
    """
    reflecting the boolean type; true and false
    """
    BYTE: 'uno.Enum'
    """
    reflecting the 8-bit ordinal type
    """
    CHAR: 'uno.Enum'
    """
    reflecting the 16-bit unicode character type
    """
    CONSTANT: 'uno.Enum'
    """
    reflecting constants
    """
    CONSTANTS: 'uno.Enum'
    """
    reflecting constants groups
    """
    DOUBLE: 'uno.Enum'
    """
    reflecting the 64-bit floating point type
    """
    ENUM: 'uno.Enum'
    """
    reflecting enum types
    """
    EXCEPTION: 'uno.Enum'
    """
    reflecting exception types
    """
    FLOAT: 'uno.Enum'
    """
    reflecting the 32-bit floating point type
    """
    HYPER: 'uno.Enum'
    """
    reflecting the signed 64-bit ordinal type
    """
    INTERFACE: 'uno.Enum'
    """
    reflecting interface types
    """
    INTERFACE_ATTRIBUTE: 'uno.Enum'
    """
    reflecting interface attributes
    """
    INTERFACE_METHOD: 'uno.Enum'
    """
    reflecting interface methods
    """
    LONG: 'uno.Enum'
    """
    reflecting the signed 32-bit ordinal type
    """
    MODULE: 'uno.Enum'
    """
    reflecting modules
    """
    PROPERTY: 'uno.Enum'
    """
    reflecting properties
    """
    SEQUENCE: 'uno.Enum'
    """
    reflecting sequence types
    """
    SERVICE: 'uno.Enum'
    """
    reflecting services
    """
    SHORT: 'uno.Enum'
    """
    reflecting the signed 16-bit ordinal type
    """
    SINGLETON: 'uno.Enum'
    """
    reflecting singletons
    """
    STRING: 'uno.Enum'
    """
    reflecting the string type; strings of unicode characters
    """
    STRUCT: 'uno.Enum'
    """
    reflecting compound types
    """
    TYPE: 'uno.Enum'
    """
    reflecting the meta type
    """
    TYPEDEF: 'uno.Enum'
    """
    reflecting typedefed types referencing other types
    """
    UNION: 'uno.Enum'
    """
    Deprecated, UNOIDL does not have a union concept.
    """
    UNKNOWN: 'uno.Enum'
    """
    reflecting the unreflectable type
    """
    UNSIGNED_HYPER: 'uno.Enum'
    """
    reflecting the unsigned 64-bit ordinal type
    """
    UNSIGNED_LONG: 'uno.Enum'
    """
    reflecting the unsigned 32-bit type
    """
    UNSIGNED_SHORT: 'uno.Enum'
    """
    reflecting the unsigned 16-bit ordinal type
    """
    VOID: 'uno.Enum'
    """
    reflecting the void type; denotes no type
    """


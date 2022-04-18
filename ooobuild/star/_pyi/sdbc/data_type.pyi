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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal
"""
Const

These constants are used to specify database data types which are used to identify the generic SQL types.

The definition is based on JDBC 3.0.

The actual type constant values are equivalent to those in the X/Open CLI.

Precise information about the specific types can be got from XDatabaseMetaData.getTypeInfo().

**since**

    OOo 2.0

See Also:
    `API DataType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1DataType.html>`_
"""
BIT: Literal[-7]
TINYINT: Literal[-6]
SMALLINT: Literal[5]
INTEGER: Literal[4]
BIGINT: Literal[-5]
FLOAT: Literal[6]
REAL: Literal[7]
DOUBLE: Literal[8]
NUMERIC: Literal[2]
DECIMAL: Literal[3]
CHAR: Literal[1]
VARCHAR: Literal[12]
LONGVARCHAR: Literal[-1]
DATE: Literal[91]
TIME: Literal[92]
TIMESTAMP: Literal[93]
BINARY: Literal[-2]
VARBINARY: Literal[-3]
LONGVARBINARY: Literal[-4]
SQLNULL: Literal[0]
OTHER: Literal[1111]
"""
indicates that the SQL type is database-specific and gets mapped to an object that can be accessed via the method com.sun.star.sdbc.XRow.getObject().
"""
OBJECT: Literal[2000]
"""
indicates a type which is represented by an object which implements this type.
"""
DISTINCT: Literal[2001]
"""
describes a type based on a built-in type.

It is a user-defined data type (UDT).
"""
STRUCT: Literal[2002]
"""
indicates a type consisting of attributes that may be any type.

It is a user-defined data type (UDT).
"""
ARRAY: Literal[2003]
"""
indicates a type representing an SQL ARRAY.
"""
BLOB: Literal[2004]
"""
indicates a type representing an SQL Binary Large Object.
"""
CLOB: Literal[2005]
"""
indicates a type representing an SQL Character Large Object.
"""
REF: Literal[2006]
"""
indicates a type representing an SQL REF, a referencing type.
"""
BOOLEAN: Literal[16]
"""
identifies the generic SQL type BOOLEAN.

**since**

    OOo 2.0
"""


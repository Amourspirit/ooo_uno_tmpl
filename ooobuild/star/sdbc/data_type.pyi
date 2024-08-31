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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdbc
import typing


class DataType:
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
    BIT: int = ...
    TINYINT: int = ...
    SMALLINT: int = ...
    INTEGER: int = ...
    BIGINT: int = ...
    FLOAT: int = ...
    REAL: int = ...
    DOUBLE: int = ...
    NUMERIC: int = ...
    DECIMAL: int = ...
    CHAR: int = ...
    VARCHAR: int = ...
    LONGVARCHAR: int = ...
    DATE: int = ...
    TIME: int = ...
    TIMESTAMP: int = ...
    BINARY: int = ...
    VARBINARY: int = ...
    LONGVARBINARY: int = ...
    SQLNULL: int = ...
    OTHER: int = ...
    """
    indicates that the SQL type is database-specific and gets mapped to an object that can be accessed via the method com.sun.star.sdbc.XRow.getObject().
    """
    OBJECT: int = ...
    """
    indicates a type which is represented by an object which implements this type.
    """
    DISTINCT: int = ...
    """
    describes a type based on a built-in type.
    
    It is a user-defined data type (UDT).
    """
    STRUCT: int = ...
    """
    indicates a type consisting of attributes that may be any type.
    
    It is a user-defined data type (UDT).
    """
    ARRAY: int = ...
    """
    indicates a type representing an SQL ARRAY.
    """
    BLOB: int = ...
    """
    indicates a type representing an SQL Binary Large Object.
    """
    CLOB: int = ...
    """
    indicates a type representing an SQL Character Large Object.
    """
    REF: int = ...
    """
    indicates a type representing an SQL REF, a referencing type.
    """
    BOOLEAN: int = ...
    """
    identifies the generic SQL type BOOLEAN.
    
    **since**
    
        OOo 2.0
    """
    DATALINK: int = ...
    """
    indicates a type representing an SQL DATALINK.
    
    **since**
    
        LibreOffice 24.2
    """
    ROWID: int = ...
    """
    indicates a type representing an SQL ROWID.
    
    **since**
    
        LibreOffice 24.2
    """
    NCHAR: int = ...
    """
    indicates a type representing an SQL NCHAR.
    
    **since**
    
        LibreOffice 24.2
    """
    NVARCHAR: int = ...
    """
    indicates a type representing an SQL NVARCHAR.
    
    **since**
    
        LibreOffice 24.2
    """
    LONGNVARCHAR: int = ...
    """
    indicates a type representing an SQL LONGNVARCHAR.
    
    **since**
    
        LibreOffice 24.2
    """
    NCLOB: int = ...
    """
    indicates a type representing an SQL NCLOB.
    
    **since**
    
        LibreOffice 24.2
    """
    SQLXML: int = ...
    """
    indicates a type representing an SQL XML.
    
    **since**
    
        LibreOffice 24.2
    """
    REF_CURSOR: int = ...
    """
    indicates a type representing an SQL REF CURSOR.
    
    **since**
    
        LibreOffice 24.2
    """
    TIME_WITH_TIMEZONE: int = ...
    """
    indicates a type representing an SQL TIME WITH TIMEZONE.
    
    **since**
    
        LibreOffice 24.2
    """
    TIMESTAMP_WITH_TIMEZONE: int = ...
    """
    indicates a type representing an SQL TIMESTAMP WITH TIMEZONE.
    
    **since**
    
        LibreOffice 24.2
    """


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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sdbc
import typing
from abc import abstractproperty
from .connection_properties import ConnectionProperties as ConnectionProperties_1a9f0ee1
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3

class JDBCConnectionProperties(ConnectionProperties_1a9f0ee1):
    """
    Service Class

    represents the properties for a JDBC connection (session) with a specific database.
    
    These properties can be used when calling the method com.sun.star.sdbc.XDriver.connect() or com.sun.star.sdbc.XDriverManager.getConnectionWithInfo().
    
    The properties for a connection contain additional information about how to connect to a database and how to control the behavior of the resulting connection should be.
    
    **since**
    
        OOo 2.3

    See Also:
        `API JDBCConnectionProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbc_1_1JDBCConnectionProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.JDBCConnectionProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def SystemProperties(self) -> 'typing.Tuple[NamedValue_a37a0af3, ...]':
        """
        specifies a set of properties to pass to java.lang.System.setProperty before loading the system's JDBC driver.
        """
        ...

    @abstractproperty
    def TypeInfoSettings(self) -> 'typing.Tuple[object, ...]':
        """
        specifies how the type info returned by com.sun.star.sdbc.XDatabaseMetaData.getTypeInfo() will be modified.
        
        The sequence contains an even amount of string values. Each pair describes what should be searched for and what should be replaced if found. The syntax is:
        
        COLUMN(X) defines the column which will be compared and the column which will be replaced. In the example above column 2 will be compared with the value -5. If this is true than column 6 will now return the value PRECISION.
        """
        ...

    @abstractproperty
    def AutoRetrievingStatement(self) -> str:
        """
        specifies the statement which should be executed when asking an \"INSERT\" statement for the XGeneratedResultSet (future concept) interface.
        """
        ...

    @abstractproperty
    def IsAutoRetrievingEnabled(self) -> bool:
        """
        specifies if retrieving of auto generated values should be enabled or not.
        
        If TRUE than the statement will support the XGeneratedResultSet (future concept) interface, otherwise not.
        """
        ...

    @abstractproperty
    def JavaDriverClass(self) -> str:
        """
        which JDBC driver class should be loaded to create the connection.
        """
        ...

    @abstractproperty
    def JavaDriverClassPath(self) -> str:
        """
        an optional class path to locate the com.sun.star.sdbc.JDBCConnectionProperties.JavaDriverClass
        
        The class path is a list of zero or more internal (see the com.sun.star.uri.ExternalUriReferenceTranslator service) URI references, where any space characters (U+0020) are ignored (and, in particular, separate adjacent URI references). Any “vnd.sun.star.expand” URL references in the list are expanded using the com.sun.star.util.theMacroExpander singleton.
        
        **since**
        
            OOo 2.3
        """
        ...



__all__ = ['JDBCConnectionProperties']


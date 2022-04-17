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
# Libre Office Version: 7.3
# Namespace: com.sun.star.sdbc
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .xsql_input import XSQLInput as XSQLInput_8c4109fc
    from .xsql_output import XSQLOutput as XSQLOutput_96fb0a7d

class XSQLData(XInterface_8f010a43):
    """
    is used for the custom mapping of SQL user-defined types.
    
    This interface must be implemented by a service that is registered in a type mapping. It is expected that this interface will normally be implemented by a tool. The methods in this interface are called by the driver and are never called by a programmer directly.

    See Also:
        `API XSQLData <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XSQLData.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XSQLData'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XSQLData'

    @abstractmethod
    def getSQLTypeName(self) -> str:
        """
        returns the fully-qualified name of the SQL user-defined type that this object represents.
        
        This method is called by the SDBC driver to get the name of the UDT instance that is being mapped to this instance of SQLData.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def readSQL(self, stream: 'XSQLInput_8c4109fc', typeName: str) -> None:
        """
        populates this object with data read from the database.
        
        The implementation of the method must follow this protocol:
        It must read each of the attributes or elements of the SQL type from the given input stream. This is done by calling a method of the input stream to read each item, in the order that they appear in the SQL definition of the type. The method readSQL then assigns the data to appropriate fields or elements (of this or other objects).
        Specifically, it must call the appropriate XSQLInput.readXXX method(s) to do the following: for a Distinct Type, read its single data element; for a Structured Type, read a value for each attribute of the SQL type.
        
        The SDBC driver initializes the input stream with a type map before calling this method, which is used by the appropriate SQLInput.readXXX method on the stream.

        Raises:
            SQLException: ``SQLException``
        """
    @abstractmethod
    def writeSQL(self, stream: 'XSQLOutput_96fb0a7d') -> None:
        """
        writes this object to the given SQL data stream.
        
        The implementation of the method must follow this protocol:
        It must write each of the attributes of the SQL type to the given output stream. This is done by calling a method of the output stream to write each item, in the order that they appear in the SQL definition of the type. Specifically, it must call the appropriate XSQLOutput.writeXXX method(s) to do the following:
        for a Distinct Type, write its single data element; for a Structured Type, write a value for each attribute of the SQL type.

        Raises:
            SQLException: ``SQLException``
        """

__all__ = ['XSQLData']


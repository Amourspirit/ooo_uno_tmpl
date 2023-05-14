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
# Namespace: com.sun.star.sdbc
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4

class XClob(XInterface_8f010a43):
    """
    is the mapping for the SQL CLOB type.
    
    A SQL CLOB is a built-in type that stores a Character Large Object as a column value in a row of a database table. The driver implements a Clob object using a SQL locator(CLOB) , which means that a Clob object contains a logical pointer to the SQL CLOB data rather than the data itself. A Clob object is valid for the duration of the transaction in which it was created.
    
    The Clob interface provides methods for getting the length of a SQL CLOB (Character Large Object) value, for materializing a CLOB value on the client, and for searching for a substring or CLOB object within a CLOB value.
    
    Methods in the interfaces com.sun.star.sdbc.XResultSet , and com.sun.star.sdbc.XPreparedStatement , such as getClob and setClob allow a programmer to access the SQL CLOB.

    See Also:
        `API XClob <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XClob.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XClob'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XClob'

    @abstractmethod
    def getCharacterStream(self) -> 'XInputStream_98d40ab4':
        """
        gets the Clob contents as a stream.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getSubString(self, pos: int, length: int) -> str:
        """
        returns a copy of the specified substring in the Clob value designated by this Clob object.
        
        The substring begins at position pos and has up to length consecutive characters.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def length(self) -> int:
        """
        returns the number of characters in the CLOB value designated by this Clob object.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def position(self, searchstr: str, start: int) -> int:
        """
        determines the character position at which the specified substring searchstr appears in the Clob.
        
        The search begins at position start.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def positionOfClob(self, pattern: 'XClob', start: int) -> int:
        """
        determines the position at which the specified Clob object pattern appears in this Clob object.
        
        The search begins at position start.

        Raises:
            SQLException: ``SQLException``
        """
        ...

__all__ = ['XClob']


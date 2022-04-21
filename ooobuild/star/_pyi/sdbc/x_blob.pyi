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
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4

class XBlob(XInterface_8f010a43):
    """
    is the representation (mapping) of an SQL BLOB.
    
    A SQL  BLOB  is a built-in type that stores a Binary Large Object as a column value in a row of a database table. The driver implements  BLOB  using a SQL locator(BLOB) , which means that a Blob object contains a logical pointer to the SQL  BLOB  data rather than the data itself.
    A Blob object is valid for the duration of the transaction in which is was created.
    
    Methods in the interfaces com.sun.star.sdbc.XResultSet , and com.sun.star.sdbc.XPreparedStatement , such as getBlob and setBlob allow a programmer to access the SQL BLOB.
    The Blob interface provides methods for getting the length of a SQL  BLOB  (Binary Large Object) value, for materializing a  BLOB  value on the client and for determining the position of a pattern of bytes within a  BLOB  value.

    See Also:
        `API XBlob <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XBlob.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdbc.XBlob']

    def getBinaryStream(self) -> 'XInputStream_98d40ab4':
        """
        retrieves the  BLOB  designated by this Blob instance as a stream.

        Raises:
            SQLException: ``SQLException``
        """
    def getBytes(self, pos: int, length: int) -> 'typing.Tuple[int, ...]':
        """
        returns as an array of bytes part or all of the  BLOB  value that this Blob object designates.
        
        The byte array contains up to length consecutive bytes starting at position pos.

        Raises:
            SQLException: ``SQLException``
        """
    def length(self) -> int:
        """
        returns the number of bytes in the  BLOB  value designated by this Blob object.

        Raises:
            SQLException: ``SQLException``
        """
    def position(self, pattern: 'typing.Tuple[int, ...]', start: int) -> int:
        """
        determines the byte position at which the specified byte pattern begins within the  BLOB  value that this Blob object represents.
        
        The search for pattern begins at position start.

        Raises:
            SQLException: ``SQLException``
        """
    def positionOfBlob(self, pattern: 'XBlob', start: int) -> int:
        """
        determines the byte position in the  BLOB  value designated by this Blob object at which pattern begins.
        
        The search begins at position start.

        Raises:
            SQLException: ``SQLException``
        """


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
# Namespace: com.sun.star.io
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XInputStream(XInterface_8f010a43):
    """
    This is the basic interface to read data from a stream.
    
    See the streaming document for further information on chaining and piping streams.

    See Also:
        `API XInputStream <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XInputStream.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.io.XInputStream']

    def available(self) -> int:
        """
        states how many bytes can be read or skipped without blocking.
        
        Note: This method offers no information on whether the EOF has been reached.

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
            com.sun.star.io.IOException: ``IOException``
        """
    def closeInput(self) -> None:
        """
        closes the stream.
        
        Users must close the stream explicitly when no further reading should be done. (There may exist ring references to chained objects that can only be released during this call. Thus not calling this method would result in a leak of memory or external resources.)

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
            com.sun.star.io.IOException: ``IOException``
        """
    def readBytes(self, aData: 'typing.Tuple[int, ...]', nBytesToRead: int) -> int:
        """
        reads the specified number of bytes in the given sequence.
        
        The return value specifies the number of bytes which have been put into the sequence. A difference between nBytesToRead and the return value indicates that EOF has been reached. This means that the method blocks until the specified number of bytes are available or the EOF is reached.

        * ``aData`` is an out direction argument.

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
            com.sun.star.io.BufferSizeExceededException: ``BufferSizeExceededException``
            com.sun.star.io.IOException: ``IOException``
        """
    def readSomeBytes(self, aData: 'typing.Tuple[int, ...]', nMaxBytesToRead: int) -> int:
        """
        reads the available number of bytes, at maximum nMaxBytesToRead.
        
        This method is very similar to the readBytes method, except that it has different blocking behaviour. The method blocks as long as at least 1 byte is available or EOF has been reached. EOF has only been reached, when the method returns 0 and the corresponding byte sequence is empty. Otherwise, after the call, aData contains the available, but no more than nMaxBytesToRead, bytes.

        * ``aData`` is an out direction argument.

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
            com.sun.star.io.BufferSizeExceededException: ``BufferSizeExceededException``
            com.sun.star.io.IOException: ``IOException``
        """
    def skipBytes(self, nBytesToSkip: int) -> None:
        """
        skips the next nBytesToSkip bytes (must be positive).
        
        It is up to the implementation whether this method is blocking the thread or not.

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
            com.sun.star.io.BufferSizeExceededException: ``BufferSizeExceededException``
            com.sun.star.io.IOException: ``IOException``
        """


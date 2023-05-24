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
# Namespace: com.sun.star.io
from __future__ import annotations
import typing

from .x_input_stream import XInputStream as XInputStream_98d40ab4


class XDataInputStream(XInputStream_98d40ab4):
    """
    makes it possible to read machine-independent simple data types from a stream.

    See Also:
        `API XDataInputStream <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XDataInputStream.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.io.XDataInputStream'

    def readBoolean(self) -> int:
        """
        reads in a boolean.
        
        It is an 8-bit value. 0 means FALSE; all other values mean TRUE.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def readByte(self) -> int:
        """
        reads an 8-bit byte.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def readChar(self) -> str:
        """
        reads a 16-bit unicode character.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def readDouble(self) -> float:
        """
        reads a 64-bit IEEE double.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def readFloat(self) -> float:
        """
        reads a 32-bit IEEE float.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def readHyper(self) -> int:
        """
        reads a 64-bit big endian integer.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def readLong(self) -> int:
        """
        reads a 32-bit big endian integer.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def readShort(self) -> int:
        """
        reads a 16-bit big endian integer.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def readUTF(self) -> str:
        """
        reads a string of UTF encoded characters.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...



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
from abc import abstractmethod
from .x_output_stream import XOutputStream as XOutputStream_a4e00b35

class XDataOutputStream(XOutputStream_a4e00b35):
    """
    makes it possible to write machine-independent simple data types to a stream.

    See Also:
        `API XDataOutputStream <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XDataOutputStream.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.XDataOutputStream'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.io.XDataOutputStream'

    @abstractmethod
    def writeBoolean(self, Value: bool) -> None:
        """
        writes a boolean.
        
        It is an 8-bit value. 0 means FALSE; all other values mean TRUE.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def writeByte(self, Value: int) -> None:
        """
        writes an 8-bit byte.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def writeChar(self, Value: str) -> None:
        """
        writes a 16-bit character.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def writeDouble(self, Value: float) -> None:
        """
        writes a 64-bit IEEE double.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def writeFloat(self, Value: float) -> None:
        """
        writes a 32-bit IEEE float.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def writeHyper(self, Value: int) -> None:
        """
        writes a 64-bit big endian integer.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def writeLong(self, Value: int) -> None:
        """
        writes a 32-bit big endian integer.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def writeShort(self, Value: int) -> None:
        """
        writes a 16-bit big endian integer.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def writeUTF(self, Value: str) -> None:
        """
        writes a string in UTF format.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...

__all__ = ['XDataOutputStream']


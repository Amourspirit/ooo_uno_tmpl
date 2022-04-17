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
# Namespace: com.sun.star.io
from typing_extensions import Literal
import typing
from .x_input_stream import XInputStream as XInputStream_98d40ab4

class XTextInputStream(XInputStream_98d40ab4):
    """
    Interface to read strings from a stream.
    
    This interfaces allows to read strings separated by delimiters and to read lines. The character encoding to be used can be set by setEncoding(). Default encoding is \"utf8\".

    See Also:
        `API XTextInputStream <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XTextInputStream.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.io.XTextInputStream']

    def isEOF(self) -> bool:
        """
        Returns the EOF status.
        
        This method has to be used to detect if the end of the stream is reached.
        
        Important: This cannot be detected by asking for an empty string because that can be a valid return value of readLine() (if the line is empty) and readString() (if a delimiter is directly followed by the next one).

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
    def readLine(self) -> str:
        """
        reads text until a line break (CR, LF, or CR/LF) or EOF is found and returns it as string (without CR, LF).
        
        The read characters are converted according to the encoding defined by setEncoding(). If EOF is already reached before calling this method an empty string is returned.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
    def readString(self, Delimiters: 'typing.Tuple[str, ...]', bRemoveDelimiter: bool) -> str:
        """
        reads text until one of the given delimiter characters or EOF is found and returns it as string (without delimiter).
        
        Important: CR/LF is not used as default delimiter! So if no delimiter is defined or none of the delimiters is found, the stream will be read to EOF. The read characters are converted according to the encoding defined by setEncoding(). If EOF is already reached before calling this method an empty string is returned.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
    def setEncoding(self, Encoding: str) -> None:
        """
        sets character encoding.
        """


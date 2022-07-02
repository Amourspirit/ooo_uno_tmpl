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
# Namespace: com.sun.star.packages
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4

class XDataSinkEncrSupport(XInterface_8f010a43):
    """
    Allows to get access to the stream of a PackageStream.

    See Also:
        `API XDataSinkEncrSupport <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1packages_1_1XDataSinkEncrSupport.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.packages.XDataSinkEncrSupport']

    def getDataStream(self) -> 'XInputStream_98d40ab4':
        """
        Allows to get access to the data of the PackageStream.
        
        In case stream is encrypted one and the key for the stream is not set, an exception must be thrown.

        Raises:
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.packages.zip.ZipException: ``ZipException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def getPlainRawStream(self) -> 'XInputStream_98d40ab4':
        """
        Allows to get access to the raw data of the stream as it is stored in the package.

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.packages.NoEncryptionException: ``NoEncryptionException``
        """
        ...
    def getRawStream(self) -> 'XInputStream_98d40ab4':
        """
        Allows to get access to the data of the PackageStream as to raw stream.
        
        In case stream is not encrypted an exception will be thrown.
        
        The difference of raw stream is that it contains header for encrypted data, so an encrypted stream can be copied from one PackageStream to another one without decryption.

        Raises:
            com.sun.star.packages.NoEncryptionException: ``NoEncryptionException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def setDataStream(self, aStream: 'XInputStream_98d40ab4') -> None:
        """
        Allows to set a data stream for the PackageStream.
        
        In case PackageStream is marked as encrypted the data stream will be encrypted on storing.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def setRawStream(self, aStream: 'XInputStream_98d40ab4') -> None:
        """
        Allows to set raw stream for the PackageStream.
        
        The PackageStream object can not be marked as encrypted one, an exception will be thrown in such case.

        Raises:
            com.sun.star.packages.EncryptionNotAllowedException: ``EncryptionNotAllowedException``
            com.sun.star.packages.NoRawFormatException: ``NoRawFormatException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...



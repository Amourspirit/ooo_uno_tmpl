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
# Namespace: com.sun.star.embed
import typing
from abc import abstractmethod
from .x_storage import XStorage as XStorage_8e460a32
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
    from ..io.x_stream import XStream as XStream_678908a4

class XStorage2(XStorage_8e460a32):
    """
    This interface extends the base XStorage interface.

    See Also:
        `API XStorage2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XStorage2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XStorage2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XStorage2'

    @abstractmethod
    def cloneEncryptedStream(self, sStreamName: str, aEncryptionData: 'typing.Tuple[NamedValue_a37a0af3, ...]') -> 'XStream_678908a4':
        """
        allows to get readonly copy of a child encrypted stream with encryption data.
        
        If storage does not allow any encryption this method will always throw com.sun.star.packages.NoEncryptionException.
        
        The stream is open in readonly mode so the com.sun.star.io.XStream.getOutputStream() method will return an empty reference.
        
        This method allows to specify encryption data for the child stream explicitly.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.NoEncryptionException: ``NoEncryptionException``
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...
    @abstractmethod
    def openEncryptedStream(self, sStreamName: str, nOpenMode: int, aEncryptionData: 'typing.Tuple[NamedValue_a37a0af3, ...]') -> 'XStream_678908a4':
        """
        allows to get access to a child encrypted stream with EncryptionData.
        
        If storage does not allow any encryption this method will always throw com.sun.star.packages.NoEncryptionException.
        
        In case the stream is open in readonly mode the com.sun.star.io.XStream.getOutputStream() method will return an empty reference.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.NoEncryptionException: ``NoEncryptionException``
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...

__all__ = ['XStorage2']


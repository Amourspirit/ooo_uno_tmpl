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
# Namespace: com.sun.star.embed
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .x_extended_storage_stream import XExtendedStorageStream as XExtendedStorageStream_46750fcf

class XHierarchicalStorageAccess(ABC):
    """
    This interface allows hierarchical access to storage tree.
    
    Currently only streams can be opened using this interface.
    
    The hierarchical access can not be mixed with a normal access. Thus when in a storage a stream with a path \"a/b/c\" is accessed using hierarchical access, another stream \"a/b/d\" can also be opened with hierarchical access ( if it is still not opened ), but the substorage \"a\" can not be opened ( it is locked by hierarchical access ).

    See Also:
        `API XHierarchicalStorageAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XHierarchicalStorageAccess.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.embed.XHierarchicalStorageAccess']

    def openEncryptedStreamElementByHierarchicalName(self, sStreamName: str, nOpenMode: int, sPassword: str) -> 'XExtendedStorageStream_46750fcf':
        """
        allows to get access to a child encrypted stream with password using hierarchical path.
        
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
    def openStreamElementByHierarchicalName(self, sStreamPath: str, nOpenMode: int) -> 'XExtendedStorageStream_46750fcf':
        """
        allows to get access to a child stream of the storage, using hierarchical path.
        
        In case the stream is open in readonly mode the com.sun.star.io.XStream.getOutputStream() method will return an empty reference.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
    def removeStreamElementByHierarchicalName(self, sElementPath: str) -> None:
        """
        removes a stream specified by hierarchical name from a storage.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """


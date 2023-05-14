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
from typing_extensions import Literal
import typing
from .x_hierarchical_storage_access import XHierarchicalStorageAccess as XHierarchicalStorageAccess_876b1143
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3
    from .x_extended_storage_stream import XExtendedStorageStream as XExtendedStorageStream_46750fcf

class XHierarchicalStorageAccess2(XHierarchicalStorageAccess_876b1143):
    """
    This interface extends XHierarchicalStorageAccess interface.

    See Also:
        `API XHierarchicalStorageAccess2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XHierarchicalStorageAccess2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.embed.XHierarchicalStorageAccess2']

    def openEncryptedStreamByHierarchicalName(self, sStreamName: str, nOpenMode: int, aEncryptionData: 'typing.Tuple[NamedValue_a37a0af3, ...]') -> 'XExtendedStorageStream_46750fcf':
        """
        allows to get access to a child encrypted stream with encryption data using hierarchical path.
        
        If storage does not allow any encryption this method will always throw com.sun.star.packages.NoEncryptionException.
        
        In case the stream is open in readonly mode the com.sun.star.io.XStream.getOutputStream() method will return an empty reference.

        Raises:
            com.sun.star.embed.InvalidStorageException: ``InvalidStorageException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.packages.NoEncryptionException: ``NoEncryptionException``
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.embed.StorageWrappedTargetException: ``StorageWrappedTargetException``
        """
        ...



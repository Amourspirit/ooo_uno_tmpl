# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.embed
from __future__ import annotations
import typing

from .x_encryption_protected_source2 import XEncryptionProtectedSource2 as XEncryptionProtectedSource2_9eb411d5
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3


class XEncryptionProtectedStorage(XEncryptionProtectedSource2_9eb411d5):
    """
    This interface allows to set a password for an object.
    
    **since**
    
        OOo 3.4

    See Also:
        `API XEncryptionProtectedStorage <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XEncryptionProtectedStorage.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.embed.XEncryptionProtectedStorage'

    def getEncryptionAlgorithms(self) -> typing.Tuple[NamedValue_a37a0af3, ...]:
        """
        allows to get the encryption algorithms of the object.
        """
        ...
    def setEncryptionAlgorithms(self, aAlgorithms: typing.Tuple[NamedValue_a37a0af3, ...]) -> None:
        """
        allows to set the encryption algorithms for the object.
        
        The algorithms will of course be used only for streams that have been marked to be encrypted. If no stream in the storage is marked to be encrypted, the algorithms-related information may have no effect to the result package.
        
        The following values could be part of the provided sequence:

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def setGpgProperties(self, aProps: typing.Tuple[typing.Tuple[NamedValue_a37a0af3, ...], ...]) -> None:
        """
        set OpenPGP-specific encryption properties
        
        When provided, switch ODF package encryption to OpenPGP.
        
        For each recipient, add one sequence of named values, each of the same structure. The following values could be part of that provided sequence:
        
        **since**
        
            LibreOffice 6.0

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...



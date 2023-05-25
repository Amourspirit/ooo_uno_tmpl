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
# Namespace: com.sun.star.xml.crypto.sax
from __future__ import annotations
import typing
from abc import abstractmethod
from ....uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from com.sun.star.xml.crypto.SecurityOperationStatus import SecurityOperationStatusProto  # type: ignore

class XSignatureVerifyResultListener(XInterface_8f010a43):
    """
    Interface of Signature Verify Result Listener.
    
    This interface is used to receive the result information of a signature verification.

    See Also:
        `API XSignatureVerifyResultListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax_1_1XSignatureVerifyResultListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.sax.XSignatureVerifyResultListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.crypto.sax.XSignatureVerifyResultListener'

    @abstractmethod
    def signatureVerified(self, securityId: int, verifyResult: SecurityOperationStatusProto) -> None:
        """
        Notifies the signature verify result.
        """
        ...

__all__ = ['XSignatureVerifyResultListener']

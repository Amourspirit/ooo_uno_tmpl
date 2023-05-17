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
# Namespace: com.sun.star.xml.crypto
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_security_environment import XSecurityEnvironment as XSecurityEnvironment_7ead116d
    from .xxml_security_context import XXMLSecurityContext as XXMLSecurityContext_681010ae
    from .xxml_signature_template import XXMLSignatureTemplate as XXMLSignatureTemplate_89fe115f


class XXMLSignature(XInterface_8f010a43):
    """
    Interface of XML signature.
    
    This interface represents a XML signer or verifier.
    
    The signer or verifier concrete a key by retrieve signature context and signature template.
    
    In some cases, the signer or verifier can determine and locate the contents to be signed from the signature template by dereference the URI.
    
    In some cases, the contents to be signed need to be clearly pointed out by the signature template.

    See Also:
        `API XXMLSignature <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1XXMLSignature.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.crypto.XXMLSignature']

    def generate(self, aTemplate: 'XXMLSignatureTemplate_89fe115f', aEnvironment: 'XSecurityEnvironment_7ead116d') -> 'XXMLSignatureTemplate_89fe115f':
        """
        Perform signature in the environment of signature template and context.

        Raises:
            : ````
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
        ...
    def validate(self, aTemplate: 'XXMLSignatureTemplate_89fe115f', aContext: 'XXMLSecurityContext_681010ae') -> 'XXMLSignatureTemplate_89fe115f':
        """
        Perform validation in the environment of signature template and context.

        Raises:
            : ````
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
        ...



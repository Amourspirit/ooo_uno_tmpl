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
# Namespace: com.sun.star.xml.crypto
import typing
from abc import abstractmethod
from .xxml_security_template import XXMLSecurityTemplate as XXMLSecurityTemplate_79221105
if typing.TYPE_CHECKING:
    from .x_uri_binding import XUriBinding as XUriBinding_f04e0d6b
    from ..wrapper.xxml_element_wrapper import XXMLElementWrapper as XXMLElementWrapper_66c0107c

class XXMLSignatureTemplate(XXMLSecurityTemplate_79221105):
    """
    Interface of XML signature template.
    
    This interface represents a signature template, which is the same as the desired XML signature element but some of the nodes may be empty. The empty entities include digest value and signature value. Empty entities are not allowed in a signature template when performing validation.
    
    In some cases, the signer or verifier can determine and locate the contents to be signed from the template by dereference the URI.
    
    With the help of signature context, the signer or verifier specifies the key from the KeyInfo in the signature template.

    See Also:
        `API XXMLSignatureTemplate <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1XXMLSignatureTemplate.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.XXMLSignatureTemplate'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.crypto.XXMLSignatureTemplate'

    @abstractmethod
    def getBinding(self) -> 'XUriBinding_f04e0d6b':
        """
        Get the dynamic URI binding.
        """
    @abstractmethod
    def getTargets(self) -> 'typing.Tuple[XXMLElementWrapper_66c0107c, ...]':
        """
        Get the target XML element, i.e.
        
        the element to be signed
        """
    @abstractmethod
    def setBinding(self, aUriBinding: 'XUriBinding_f04e0d6b') -> None:
        """
        Set the dynamic URI binding.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XXMLSignatureTemplate']


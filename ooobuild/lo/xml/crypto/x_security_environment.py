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
# Namespace: com.sun.star.xml.crypto
import typing
import uno
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...security.x_certificate import XCertificate as XCertificate_e55b0d3b

class XSecurityEnvironment(XInterface_8f010a43):
    """
    Interface of Security Environment.
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API XSecurityEnvironment <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1XSecurityEnvironment.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.XSecurityEnvironment'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.crypto.XSecurityEnvironment'

    @abstractmethod
    def buildCertificatePath(self, beginCert: 'XCertificate_e55b0d3b') -> 'typing.Tuple[XCertificate_e55b0d3b, ...]':
        """
        Build certificate path from a certain certificate.

        Raises:
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
    @abstractmethod
    def createCertificateFromAscii(self, asciiCertificate: str) -> 'XCertificate_e55b0d3b':
        """
        Create certificate interface from a Base64 encoded certificate.

        Raises:
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
    @abstractmethod
    def createCertificateFromRaw(self, rawCertificate: uno.ByteSequence) -> 'XCertificate_e55b0d3b':
        """
        Create certificate interface from raw DER encoded certificate.

        Raises:
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
    @abstractmethod
    def getAllCertificates(self) -> 'typing.Tuple[XCertificate_e55b0d3b, ...]':
        """
        List all certificates, private (as returned by getPersonalCertificates) as well as those of other people/orgas.
        
        **since**
        
            LibreOffice 6.0

        Raises:
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
    @abstractmethod
    def getCertificate(self, issuerName: str, serialNumber: uno.ByteSequence) -> 'XCertificate_e55b0d3b':
        """
        Get certificate from the environment by issuer name and serial number.

        Raises:
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
    @abstractmethod
    def getCertificateCharacters(self, xCertificate: 'XCertificate_e55b0d3b') -> int:
        """
        Get a certificate characters.
        
        The method provides a way to get certificate characters like:
        
        The certificate characters is defined as bit-wise long, please refer to CertificateCharacters definition.

        Raises:
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
    @abstractmethod
    def getPersonalCertificates(self) -> 'typing.Tuple[XCertificate_e55b0d3b, ...]':
        """
        Get personal certificates from the environment.

        Raises:
            com.sun.star.uno.SecurityException: ``SecurityException``
        """
    @abstractmethod
    def getSecurityEnvironmentInformation(self) -> str:
        """
        Get the Environment detail information.
        """
    @abstractmethod
    def verifyCertificate(self, xEECertificate: 'XCertificate_e55b0d3b', intermediateCertificates: 'typing.Tuple[XCertificate_e55b0d3b, ...]') -> int:
        """
        Verify a certificate.
        
        The method provides a way to verify a certificate.

        Raises:
            com.sun.star.uno.SecurityException: ``SecurityException``
        """

__all__ = ['XSecurityEnvironment']


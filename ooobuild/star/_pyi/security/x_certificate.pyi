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
# Namespace: com.sun.star.security
from typing_extensions import Literal
import typing
import uno
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .certificate_kind import CertificateKind as CertificateKind_ffd0e69
    from .x_certificate_extension import XCertificateExtension as XCertificateExtension_6ead10f8
    from ..util.date_time import DateTime as DateTime_84de09d3

class XCertificate(XInterface_8f010a43):
    """
    Interface of a PKI Certificate.
    
    This interface represents a certificate (X.509 or OpenPGP) .
    
    **since**
    
        LibreOffice 5.4

    See Also:
        `API XCertificate <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1security_1_1XCertificate.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.security.XCertificate']

    def findCertificateExtension(self, oid: uno.ByteSequence) -> 'XCertificateExtension_6ead10f8':
        """
        Find an extension with an object identifier.
        """
        ...
    def getCertificateUsage(self) -> int:
        """
        get the certificate usage.
        
        The return value is a set of bits, as defined in RFC3280 for the KeyUsage BIT STRING. Note the bit and byte order used in ASN.1, so for instance the bit dataEncipherment in KeyUsage, \"bit 3\", corresponds to CERT_DATA_ENCIPHERMENT_KEY_USAGE in Win32 and KU_DATA_ENCIPHERMENT in NSS, both with value 0x10.
        """
        ...

    @property
    def Encoded(self) -> uno.ByteSequence:
        """
        the DER encoded form of the certificate
        """
        ...

    @property
    def Extensions(self) -> 'typing.Tuple[XCertificateExtension_6ead10f8, ...]':
        """
        all extensions of a certificate.
        """
        ...

    @property
    def IssuerUniqueID(self) -> uno.ByteSequence:
        """
        the issuer unique ID attribute of the certificate.
        """
        ...

    @property
    def MD5Thumbprint(self) -> uno.ByteSequence:
        """
        the MD5 thumbprint
        """
        ...

    @property
    def SHA1Thumbprint(self) -> uno.ByteSequence:
        """
        the SHA-1 thumbprint
        """
        ...

    @property
    def SerialNumber(self) -> uno.ByteSequence:
        """
        the serial number attribute of the certificate.
        """
        ...

    @property
    def SubjectPublicKeyValue(self) -> uno.ByteSequence:
        """
        the value of the subject public key
        """
        ...

    @property
    def SubjectUniqueID(self) -> uno.ByteSequence:
        """
        the subject unique ID attribute of the certificate.
        """
        ...

    @property
    def CertificateKind(self) -> 'CertificateKind_ffd0e69':
        """
        the kind of certificate, X.509 or OpenPGP
        
        **since**
        
            LibreOffice 5.4
        """
        ...

    @property
    def IssuerName(self) -> str:
        """
        the issuer name attribute of the certificate.
        """
        ...

    @property
    def NotValidAfter(self) -> 'DateTime_84de09d3':
        """
        the validity NotAfter date attribute of the certificate.
        """
        ...

    @property
    def NotValidBefore(self) -> 'DateTime_84de09d3':
        """
        the validity NotBefore date attribute of the certificate.
        """
        ...

    @property
    def SignatureAlgorithm(self) -> str:
        """
        the signature algorithm
        """
        ...

    @property
    def SubjectName(self) -> str:
        """
        the subject name attribute of the certificate.
        """
        ...

    @property
    def SubjectPublicKeyAlgorithm(self) -> str:
        """
        the algorithm of the subject public key
        """
        ...

    @property
    def Version(self) -> int:
        """
        the version number attribute of the certificate.
        """
        ...



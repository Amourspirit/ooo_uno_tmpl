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
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..embed.x_storage import XStorage as XStorage_8e460a32
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from ..io.x_stream import XStream as XStream_678908a4
    from .certificate_kind import CertificateKind as CertificateKind_ffd0e69
    from .document_signature_information import DocumentSignatureInformation as DocumentSignatureInformation_f36c13f7
    from .x_certificate import XCertificate as XCertificate_e55b0d3b

class XDocumentDigitalSignatures(XInterface_8f010a43):
    """
    Interface for signing and verifying digital signatures in office documents.
    
    This interface can be used to digitally sign different content in an office document. It can also be used to verify digital signatures.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API XDocumentDigitalSignatures <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1security_1_1XDocumentDigitalSignatures.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.security'
    __ooo_full_ns__: str = 'com.sun.star.security.XDocumentDigitalSignatures'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.security.XDocumentDigitalSignatures'

    @abstractmethod
    def addAuthorToTrustedSources(self, Author: 'XCertificate_e55b0d3b') -> None:
        """
        """
    @abstractmethod
    def addLocationToTrustedSources(self, Location: str) -> None:
        """
        """
    @abstractmethod
    def chooseCertificate(self, Description: str) -> 'XCertificate_e55b0d3b':
        """
        This method shows the CertificateChooser dialog, used by document and PDF signing Shows only private certificates.
        
        **since**
        
            LibreOffice 5.3

        * ``Description`` is an out direction argument.
        """
    @abstractmethod
    def chooseCertificateWithProps(self, Properties: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'XCertificate_e55b0d3b':
        """
        This method shows the CertificateChooser dialog, used by document and PDF signing Shows only private certificates and returns usage string in addition to description.
        
        **since**
        
            LibreOffice 6.0

        * ``Properties`` is an out direction argument.
        """
    @abstractmethod
    def chooseEncryptionCertificate(self) -> 'typing.Tuple[XCertificate_e55b0d3b, ...]':
        """
        This method shows the CertificateChooser dialog with all certificates, private and other people's.
        
        Useful when choosing certificate/key for encryption
        
        **since**
        
            LibreOffice 6.0
        """
    @abstractmethod
    def chooseSigningCertificate(self, Description: str) -> 'XCertificate_e55b0d3b':
        """
        This is an alias for 'chooseCertificate', shows the CertificateChooser dialog with private certificates.
        
        **since**
        
            LibreOffice 6.0

        * ``Description`` is an out direction argument.
        """
    @abstractmethod
    def getDocumentContentSignatureDefaultStreamName(self) -> str:
        """
        allows to get the default stream name for storing of the signature of the document content.
        """
    @abstractmethod
    def getPackageSignatureDefaultStreamName(self) -> str:
        """
        allows to get the default stream name for storing of the signature of the package.
        """
    @abstractmethod
    def getScriptingContentSignatureDefaultStreamName(self) -> str:
        """
        allows to get the default stream name for storing of the signature of the scripting content.
        """
    @abstractmethod
    def isAuthorTrusted(self, Author: 'XCertificate_e55b0d3b') -> bool:
        """
        """
    @abstractmethod
    def isLocationTrusted(self, Location: str) -> bool:
        """
        """
    @abstractmethod
    def manageTrustedSources(self) -> None:
        """
        manages trusted sources (Authors and paths )
        """
    @abstractmethod
    def selectSigningCertificate(self, Description: str) -> 'XCertificate_e55b0d3b':
        """
        This shows the certificate selection dialog and allows to only select the certificate without actually signing the document.
        
        **since**
        
            LibreOffice 6.1

        * ``Description`` is an out direction argument.
        """
    @abstractmethod
    def selectSigningCertificateWithType(self, certificateKind: 'CertificateKind_ffd0e69', Description: str) -> 'XCertificate_e55b0d3b':
        """
        This shows the certificate selection dialog and allows to only select the certificate without actually signing the document.
        
        Only certificates of the given type will be shown.
        
        **since**
        
            LibreOffice 6.2

        * ``Description`` is an out direction argument.
        """
    @abstractmethod
    def setParentWindow(self, xParentWindow: 'XWindow_713b0924') -> None:
        """
        Set parent window to use when showing dialogs.
        
        **since**
        
            LibreOffice 6.3
        """
    @abstractmethod
    def showCertificate(self, Certificate: 'XCertificate_e55b0d3b') -> None:
        """
        """
    @abstractmethod
    def showDocumentContentSignatures(self, xStorage: 'XStorage_8e460a32', xSignInStream: 'XInputStream_98d40ab4') -> None:
        """
        shows the digital signatures of the document content
        """
    @abstractmethod
    def showPackageSignatures(self, xStorage: 'XStorage_8e460a32', xSignInStream: 'XInputStream_98d40ab4') -> None:
        """
        shows the digital signatures of the package
        """
    @abstractmethod
    def showScriptingContentSignatures(self, xStorage: 'XStorage_8e460a32', xSignInStream: 'XInputStream_98d40ab4') -> None:
        """
        shows the digital signatures of the scripting content
        """
    @abstractmethod
    def signDocumentContent(self, xStorage: 'XStorage_8e460a32', xSignStream: 'XStream_678908a4') -> bool:
        """
        signs the content of the document including text and pictures.
        
        Macros will not be signed.
        """
    @abstractmethod
    def signDocumentWithCertificate(self, xCertificate: 'XCertificate_e55b0d3b', xStorage: 'XStorage_8e460a32', xStream: 'XStream_678908a4') -> bool:
        """
        Signs the content of the document with the provided certificate.
        
        **since**
        
            LibreOffice 6.2
        """
    @abstractmethod
    def signPackage(self, Storage: 'XStorage_8e460a32', xSignStream: 'XStream_678908a4') -> bool:
        """
        signs the full Package, which means everything in the storage except the content of META-INF
        """
    @abstractmethod
    def signPackageWithCertificate(self, xCertificate: 'XCertificate_e55b0d3b', xStorage: 'XStorage_8e460a32', xStream: 'XStream_678908a4') -> bool:
        """
        signs the full Package, which means everything in the storage except the content of META-INF with the provided certificate.
        
        **since**
        
            LibreOffice 7.0
        """
    @abstractmethod
    def signScriptingContent(self, xStorage: 'XStorage_8e460a32', xSignStream: 'XStream_678908a4') -> bool:
        """
        signs the content of the Scripting including macros and basic dialogs
        
        The rest of document content will not be signed.
        """
    @abstractmethod
    def signScriptingContentWithCertificate(self, xCertificate: 'XCertificate_e55b0d3b', xStorage: 'XStorage_8e460a32', xStream: 'XStream_678908a4') -> bool:
        """
        signs the content of the Scripting including macros and basic dialogs with the provided certificate.
        
        The rest of document content will not be signed.
        
        **since**
        
            LibreOffice 7.0
        """
    @abstractmethod
    def signSignatureLine(self, xStorage: 'XStorage_8e460a32', xSignStream: 'XStream_678908a4', signatureLineId: str, xCertificate: 'XCertificate_e55b0d3b', xValidGraphic: 'XGraphic_a4da0afc', xInvalidGraphic: 'XGraphic_a4da0afc', comment: str) -> bool:
        """
        Signs the content of the document including text and pictures using the given XCertificate.
        
        Also adds the given Signature Line Id and the signed and unsigned graphics to the signature.
        
        Macros will not be signed.
        
        **since**
        
            LibreOffice 6.1
        """
    @abstractmethod
    def verifyDocumentContentSignatures(self, xStorage: 'XStorage_8e460a32', xSignInStream: 'XInputStream_98d40ab4') -> 'typing.Tuple[DocumentSignatureInformation_f36c13f7, ...]':
        """
        checks for digital signatures and their status.
        
        Only document content will be checked.
        """
    @abstractmethod
    def verifyPackageSignatures(self, Storage: 'XStorage_8e460a32', xSignInStream: 'XInputStream_98d40ab4') -> 'typing.Tuple[DocumentSignatureInformation_f36c13f7, ...]':
        """
        checks for digital signatures and their status.
        
        Only Package content will be checked.
        """
    @abstractmethod
    def verifyScriptingContentSignatures(self, xStorage: 'XStorage_8e460a32', xSignInStream: 'XInputStream_98d40ab4') -> 'typing.Tuple[DocumentSignatureInformation_f36c13f7, ...]':
        """
        checks for digital signatures and their status.
        
        Only Scripting content will be checked.
        """

__all__ = ['XDocumentDigitalSignatures']

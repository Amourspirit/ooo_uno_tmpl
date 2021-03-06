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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.security
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
from .x_certificate import XCertificate as XCertificate_e55b0d3b


class DocumentSignatureInformation(object):
    """
    Struct Class

    Status of digital signatures in a document.
    
    This structure has the information about a digital signature in a document, and the status if the signature is valid.
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API DocumentSignatureInformation <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1security_1_1DocumentSignatureInformation.html>`_
    """
    typeName: Literal['com.sun.star.security.DocumentSignatureInformation']

    def __init__(self, Signer: typing.Optional[XCertificate_e55b0d3b] = ..., SignatureDate: typing.Optional[int] = ..., SignatureTime: typing.Optional[int] = ..., SignatureIsValid: typing.Optional[bool] = ..., CertificateStatus: typing.Optional[int] = ..., PartialDocumentSignature: typing.Optional[bool] = ..., SignatureLineId: typing.Optional[str] = ..., ValidSignatureLineImage: typing.Optional[XGraphic_a4da0afc] = ..., InvalidSignatureLineImage: typing.Optional[XGraphic_a4da0afc] = ...) -> None:
        """
        Constructor

        Arguments:
            Signer (XCertificate, optional): Signer value.
            SignatureDate (int, optional): SignatureDate value.
            SignatureTime (int, optional): SignatureTime value.
            SignatureIsValid (bool, optional): SignatureIsValid value.
            CertificateStatus (int, optional): CertificateStatus value.
            PartialDocumentSignature (bool, optional): PartialDocumentSignature value.
            SignatureLineId (str, optional): SignatureLineId value.
            ValidSignatureLineImage (XGraphic, optional): ValidSignatureLineImage value.
            InvalidSignatureLineImage (XGraphic, optional): InvalidSignatureLineImage value.
        """
        ...


    @property
    def Signer(self) -> XCertificate_e55b0d3b:
        ...


    @property
    def SignatureDate(self) -> int:
        ...


    @property
    def SignatureTime(self) -> int:
        """
        Time of day, in 100th of seconds.
        """
        ...


    @property
    def SignatureIsValid(self) -> bool:
        ...


    @property
    def CertificateStatus(self) -> int:
        """
        Reflects the validity of the certificate.
        
        Contains a value from the constants of com.sun.star.security.CertificateValidity.
        """
        ...


    @property
    def PartialDocumentSignature(self) -> bool:
        """
        Indicates what content of a document is signed.
        
        This value can be ignored when this struct is returned as part of a macro signature validation. As of OpenOffice.org 3.2 and ODF 1.2 the document signature comprises all files except the signature file itself. Signatures in OOo 2.x were only applied to the files in the root of the document, except mimetype, the Pictures and ObjectReplacements/Objects folder. That is, macros were not part of the document signature. OOo 3.0 signed everything, except mimetype and the META-INF folder.
        
        If PartialDocumentSignature is true, then the signature was created by OOo with a version lower than 3.2. In this case, not all files are signed. The signature can still be regarded as valid, as long as SignatureIsValid is true and the certificate could be validated. However, users should be notified about the fact, that not everything in this document is signed.
        """
        ...


    @property
    def SignatureLineId(self) -> str:
        """
        The ID of the Signature Line.
        
        **since**
        
            LibreOffice 6.0
        """
        ...


    @property
    def ValidSignatureLineImage(self) -> XGraphic_a4da0afc:
        """
        The Signature Line Image which is shown when the signature is valid.
        
        **since**
        
            LibreOffice 6.0
        """
        ...


    @property
    def InvalidSignatureLineImage(self) -> XGraphic_a4da0afc:
        """
        The Signature Line Image which is shown when the signature is invalid.
        
        **since**
        
            LibreOffice 6.0
        """
        ...



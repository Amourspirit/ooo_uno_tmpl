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
# Namespace: com.sun.star.security
from __future__ import annotations
import typing

from .x_certificate_extension import XCertificateExtension as XCertificateExtension_6ead10f8
if typing.TYPE_CHECKING:
    from .cert_alt_name_entry import CertAltNameEntry as CertAltNameEntry_1ce50ec2


class XSanExtension(XCertificateExtension_6ead10f8):
    """
    Interface of a X509 Subject Alternative Name Certificate Extension.
    
    This interface represents a x509 certificate extension.

    See Also:
        `API XSanExtension <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1security_1_1XSanExtension.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.security.XSanExtension'

    @property
    def AlternativeNames(self) -> typing.Tuple[CertAltNameEntry_1ce50ec2, ...]:
        """
        Contains the alternative names of a certificate.
        """
        ...
    @AlternativeNames.setter
    def AlternativeNames(self, value: typing.Tuple[CertAltNameEntry_1ce50ec2, ...]) -> None:
        ...


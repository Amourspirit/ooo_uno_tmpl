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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.security
# Libre Office Version: 7.4
from __future__ import annotations
from typing import cast, TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from com.sun.star.security.CertificateKind import CertificateKindProto

class CertificateKind(Enum):
    """
    Enum Class


    See Also:
        `API CertificateKind <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1security.html#a15fb2a8475364a68c176c7789e3611cc>`_
    """
    __ooo_ns__: str = 'com.sun.star.security'
    __ooo_full_ns__: str = 'com.sun.star.security.CertificateKind'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.security.CertificateKind'

    NONE = cast("CertificateKindProto", 'NONE')
    """
    No format specified.
    """
    OPENPGP = cast("CertificateKindProto", 'OPENPGP')
    """
    OpenPGP format of a certificate.
    """
    X509 = cast("CertificateKindProto", 'X509')
    """
    X.509 format of a certificate.
    """

__all__ = ['CertificateKind']


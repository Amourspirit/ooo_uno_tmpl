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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.security
# Libre Office Version: 7.2
from enum import Enum


class CertificateContainerStatus(Enum):
    """
    Enum Class

    

    See Also:
        `API CertificateContainerStatus <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1security.html#abd9126083ddb902b337383198d342e9f>`_
    """
    __ooo_ns__: str = 'com.sun.star.security'
    __ooo_full_ns__: str = 'com.sun.star.security.CertificateContainerStatus'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.security.CertificateContainerStatus'

    NOCERT = 'NOCERT'
    """
    The certificate was not found.
    """
    TRUSTED = 'TRUSTED'
    """
    The certificate was found and is trusted.
    """
    UNTRUSTED = 'UNTRUSTED'
    """
    The certificate was found but is untrusted.
    """

__all__ = ['CertificateContainerStatus']


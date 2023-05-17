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
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.security.CertificateContainerStatus import NOCERT as CERTIFICATE_CONTAINER_STATUS_NOCERT
    from com.sun.star.security.CertificateContainerStatus import TRUSTED as CERTIFICATE_CONTAINER_STATUS_TRUSTED
    from com.sun.star.security.CertificateContainerStatus import UNTRUSTED as CERTIFICATE_CONTAINER_STATUS_UNTRUSTED

    class CertificateContainerStatus(uno.Enum):
        """
        Enum Class


        See Also:
            `API CertificateContainerStatus <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1security.html#abd9126083ddb902b337383198d342e9f>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.security.CertificateContainerStatus', value)

        __ooo_ns__: str = 'com.sun.star.security'
        __ooo_full_ns__: str = 'com.sun.star.security.CertificateContainerStatus'
        __ooo_type_name__: str = 'enum'

        NOCERT: CertificateContainerStatus = CERTIFICATE_CONTAINER_STATUS_NOCERT
        """
        The certificate was not found.
        """
        TRUSTED: CertificateContainerStatus = CERTIFICATE_CONTAINER_STATUS_TRUSTED
        """
        The certificate was found and is trusted.
        """
        UNTRUSTED: CertificateContainerStatus = CERTIFICATE_CONTAINER_STATUS_UNTRUSTED
        """
        The certificate was found but is untrusted.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class CertificateContainerStatus(metaclass=UnoEnumMeta, type_name="com.sun.star.security.CertificateContainerStatus", name_space="com.sun.star.security"):
        """Dynamically created class that represents ``com.sun.star.security.CertificateContainerStatus`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['CertificateContainerStatus']

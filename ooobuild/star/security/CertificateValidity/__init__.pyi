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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.security
from typing_extensions import Literal
"""
Const

Constant definition of a certificate characters.

The certificate characters will be defined as bit-wise constants.

See Also:
    `API CertificateValidity <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1security_1_1CertificateValidity.html>`_
"""
VALID: Literal[0]
INVALID: Literal[1]
"""
The certificate is invalid.
"""
UNTRUSTED: Literal[2]
"""
The certificate itself is untrusted.
"""
TIME_INVALID: Literal[4]
"""
The current time is not in the range of time for which the certificate is valid.
"""
NOT_TIME_NESTED: Literal[8]
"""
The time range of a certificate does not fall within the time range of the issuing certificate.
"""
REVOKED: Literal[16]
"""
It is a revoked certificate.
"""
UNKNOWN_REVOKATION: Literal[32]
"""
The certificate revocation status is unknown.
"""
SIGNATURE_INVALID: Literal[64]
"""
The certificate signature is invalid.
"""
EXTENSION_INVALID: Literal[128]
"""
The certificate has invalid extensions.
"""
EXTENSION_UNKNOWN: Literal[256]
"""
The certificate has critical unknown extensions.
"""
ISSUER_UNKNOWN: Literal[512]
"""
The certificate issuer is unknown.
"""
ISSUER_UNTRUSTED: Literal[1024]
"""
The certificate issuer is untrusted.
"""
ISSUER_INVALID: Literal[4096]
"""
The certificate issuer is invalid.
"""
ROOT_UNKNOWN: Literal[8192]
"""
The root certificate is unknown.
"""
ROOT_UNTRUSTED: Literal[16384]
"""
The root certificate is untrusted.
"""
ROOT_INVALID: Literal[65536]
"""
The root certificate is invalid.
"""
CHAIN_INCOMPLETE: Literal[131072]
"""
The certificate chain is incomplete.
"""


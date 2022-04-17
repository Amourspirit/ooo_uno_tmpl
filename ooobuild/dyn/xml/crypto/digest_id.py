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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.xml.crypto
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.xml.crypto import DigestID as DigestID
    if hasattr(DigestID, '_constants') and isinstance(DigestID._constants, dict):
        DigestID._constants['__ooo_ns__'] = 'com.sun.star.xml.crypto'
        DigestID._constants['__ooo_full_ns__'] = 'com.sun.star.xml.crypto.DigestID'
        DigestID._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global DigestIDEnum
        ls = [f for f in dir(DigestID) if not callable(getattr(DigestID, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(DigestID, name)
        DigestIDEnum = IntEnum('DigestIDEnum', _dict)
    build_enum()
else:
    from ....lo.xml.crypto.digest_id import DigestID as DigestID

    class DigestIDEnum(IntEnum):
        """
        Enum of Const Class DigestID

        The constant set contains identifiers of supported digest-creation algorithms.
        
        **since**
        
            OOo 3.4
        """
        SHA1 = DigestID.SHA1
        """
        identifier of SHA-1 algorithm
        """
        SHA256 = DigestID.SHA256
        """
        identifier of SHA-256 algorithm
        """
        SHA1_1K = DigestID.SHA1_1K
        """
        identifier of SHA-1 algorithm that is applied to the first kilobyte of data.
        """
        SHA256_1K = DigestID.SHA256_1K
        """
        identifier of SHA-256 algorithm that is applied to the first kilobyte of data.
        """
        SHA512 = DigestID.SHA512
        """
        identifier of SHA-512 algorithm
        
        **since**
        
            LibreOffice 6.0
        """
        SHA512_1K = DigestID.SHA512_1K
        """
        identifier of SHA-512 algorithm that is applied to the first kilobyte of data.
        
        **since**
        
            LibreOffice 6.0
        """

__all__ = ['DigestID', 'DigestIDEnum']
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
# Namespace: com.sun.star.xml.crypto.sax
# Libre Office Version: 7.4
from __future__ import annotations
from typing import cast, TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from com.sun.star.xml.crypto.sax.ElementMarkPriority import ElementMarkPriorityProto

class ElementMarkPriority(Enum):
    """
    Enum Class


    See Also:
        `API ElementMarkPriority <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax.html#a513614abfcc788af5f4afd633a9f5d0a>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.sax.ElementMarkPriority'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.xml.crypto.sax.ElementMarkPriority'

    AFTERMODIFY = cast("ElementMarkPriorityProto", 'AFTERMODIFY')
    """
    """
    BEFOREMODIFY = cast("ElementMarkPriorityProto", 'BEFOREMODIFY')
    """
    """
    MINIMUM = cast("ElementMarkPriorityProto", 'MINIMUM')
    """
    """

__all__ = ['ElementMarkPriority']


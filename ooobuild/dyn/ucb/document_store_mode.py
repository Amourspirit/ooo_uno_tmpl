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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.ucb.DocumentStoreMode import LOCAL as DOCUMENT_STORE_MODE_LOCAL
    from com.sun.star.ucb.DocumentStoreMode import REMOTE as DOCUMENT_STORE_MODE_REMOTE

    class DocumentStoreMode(uno.Enum):
        """
        Enum Class


        See Also:
            `API DocumentStoreMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#aea1ce806e915d3505569f7679447ecc2>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.ucb.DocumentStoreMode', value)

        __ooo_ns__: str = 'com.sun.star.ucb'
        __ooo_full_ns__: str = 'com.sun.star.ucb.DocumentStoreMode'
        __ooo_type_name__: str = 'enum'

        LOCAL: DocumentStoreMode = DOCUMENT_STORE_MODE_LOCAL
        """
        Document contents are stored locally.
        """
        REMOTE: DocumentStoreMode = DOCUMENT_STORE_MODE_REMOTE
        """
        Document contents are not stored locally.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class DocumentStoreMode(metaclass=UnoEnumMeta, type_name="com.sun.star.ucb.DocumentStoreMode", name_space="com.sun.star.ucb"):
        """Dynamically created class that represents ``com.sun.star.ucb.DocumentStoreMode`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['DocumentStoreMode']

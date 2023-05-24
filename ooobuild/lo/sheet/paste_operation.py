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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from __future__ import annotations
from typing import cast, TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from com.sun.star.sheet.PasteOperation import PasteOperationProto

class PasteOperation(Enum):
    """
    Enum Class


    See Also:
        `API PasteOperation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#af53d63b24461405946937e0b962a8a9b>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.PasteOperation'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.sheet.PasteOperation'

    ADD = cast("PasteOperationProto", 'ADD')
    """
    old and new values are added.
    """
    DIVIDE = cast("PasteOperationProto", 'DIVIDE')
    """
    new values are divided by the new values.
    """
    MULTIPLY = cast("PasteOperationProto", 'MULTIPLY')
    """
    old and new values are multiplied.
    """
    NONE = cast("PasteOperationProto", 'NONE')
    """
    no cells are moved.
    
    sheet is not linked.
    
    new values are used without changes.
    
    nothing is calculated.
    
    nothing is imported.
    
    no condition is specified.
    """
    SUBTRACT = cast("PasteOperationProto", 'SUBTRACT')
    """
    new values are subtracted from the old values.
    """

__all__ = ['PasteOperation']


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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from __future__ import annotations
import uno


class PasteOperation(uno.Enum):
    """
    Enum


    See Also:
        `API PasteOperation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#af53d63b24461405946937e0b962a8a9b>`_
    """
    typeName: str = 'com.sun.star.sheet.PasteOperation'

    ADD: PasteOperation = ...
    """
    old and new values are added.
    """
    DIVIDE: PasteOperation = ...
    """
    new values are divided by the new values.
    """
    MULTIPLY: PasteOperation = ...
    """
    old and new values are multiplied.
    """
    NONE: PasteOperation = ...
    """
    no cells are moved.
    
    sheet is not linked.
    
    new values are used without changes.
    
    nothing is calculated.
    
    nothing is imported.
    
    no condition is specified.
    """
    SUBTRACT: PasteOperation = ...
    """
    new values are subtracted from the old values.
    """


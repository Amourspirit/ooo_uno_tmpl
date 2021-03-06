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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class ValidationType(Enum):
    """
    Enum

    

    See Also:
        `API ValidationType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#aa5aa6dbecaeb5e18a476b0a58279c57a>`_
    """
    typeName: str = 'com.sun.star.sheet.ValidationType'

    ANY: 'uno.Enum'
    """
    any cell content is valid; no conditions are used.
    """
    CUSTOM: 'uno.Enum'
    """
    The specified formula determines which contents are valid.
    """
    DATE: 'uno.Enum'
    """
    specifies an arithmetic series for date values.
    
    any date value matching the specified condition is valid.
    """
    DECIMAL: 'uno.Enum'
    """
    any number matching the specified condition is valid.
    """
    LIST: 'uno.Enum'
    """
    Only strings from a specified list are valid.
    """
    TEXT_LEN: 'uno.Enum'
    """
    string is valid if its length matches the specified condition.
    """
    TIME: 'uno.Enum'
    """
    any time value matching the specified condition is valid.
    """
    WHOLE: 'uno.Enum'
    """
    any whole number matching the specified condition is valid.
    """


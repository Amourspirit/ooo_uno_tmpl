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
# Namespace: com.sun.star.style
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API BreakType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#a3ae28cb49c180ec160a0984600b2b925>`_
"""
typeName: str = 'com.sun.star.style.BreakType'

COLUMN_AFTER: 'uno.Enum'
"""
A column break is applied after the object to which it belongs.
"""
COLUMN_BEFORE: 'uno.Enum'
"""
A column break is applied before the object to which it belongs.
"""
COLUMN_BOTH: 'uno.Enum'
"""
A column break is applied before and after the object to which it belongs.
"""
NONE: 'uno.Enum'
"""
No column or page break is applied.

This value specifies that a location is not yet assigned.
"""
PAGE_AFTER: 'uno.Enum'
"""
A page break is applied after the object to which it belongs.
"""
PAGE_BEFORE: 'uno.Enum'
"""
A page break is applied before the object to which it belongs.
"""
PAGE_BOTH: 'uno.Enum'
"""
A page break is applied before and after the object to which it belongs.
"""


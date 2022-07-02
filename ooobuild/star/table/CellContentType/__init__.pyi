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
# Namespace: com.sun.star.table
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API CellContentType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1table.html#affea688ab9e00781fa35d8a790d10f0e>`_
"""
typeName: str = 'com.sun.star.table.CellContentType'

EMPTY: 'uno.Enum'
"""
cell is empty.
"""
FORMULA: 'uno.Enum'
"""
cell contains a formula.
"""
TEXT: 'uno.Enum'
"""
cell contains text.
"""
VALUE: 'uno.Enum'
"""
cell contains a constant value.
"""


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
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API SheetLinkMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a34cdda19a5183f39256021e0c2bc46cc>`_
"""

NONE: 'uno.Enum'
"""
no cells are moved.

sheet is not linked.

new values are used without changes.

nothing is calculated.

nothing is imported.

no condition is specified.
"""
NORMAL: 'uno.Enum'
"""
all contents (values and formulas) are copied.
"""
VALUE: 'uno.Enum'
"""
instead of using formulas, the result values are copied.
"""


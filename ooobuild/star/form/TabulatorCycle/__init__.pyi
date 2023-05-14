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
# Namespace: com.sun.star.form
# Libre Office Version: 7.4
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API TabulatorCycle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form.html#acb5251eb1c7e6ff2149158596346de94>`_
"""
typeName: str = 'com.sun.star.form.TabulatorCycle'

CURRENT: 'uno.Enum'
"""
a navigation bar is provided and navigation will be performed on the current/active form.

pressing the TAB key from the last control moves the focus to the first control in the tab order of the same record.

This is the default and most often encountered mode.
"""
PAGE: 'uno.Enum'
"""
pressing the TAB key from the last control of a form moves the focus to the first control of the next form in the tab order.
"""
RECORDS: 'uno.Enum'
"""
pressing the TAB key from the last control moves the focus to the first control in the tab order of the next record.
"""


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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API RememberAuthentication <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#a7b9847f348fd7f6a0fc461f821c08173>`_
"""
typeName: str = 'com.sun.star.ucb.RememberAuthentication'

NO: 'uno.Enum'
"""
Do not remember the authentication data (use it once and immediately forget about it).
"""
PERSISTENT: 'uno.Enum'
"""
Remember the authentication data \"forever\".
"""
SESSION: 'uno.Enum'
"""
Remember the authentication data, but only until the end of the current session.
"""


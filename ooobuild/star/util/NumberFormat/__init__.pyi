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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.util
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
"""
Const

contains constants that are used to specify the type of a number format.

See Also:
    `API NumberFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1util_1_1NumberFormat.html>`_
"""
ALL: Literal[0]
"""
selects all number formats.
"""
DEFINED: Literal[1]
"""
selects only user-defined number formats.
"""
DATE: Literal[2]
"""
selects date formats.
"""
TIME: Literal[4]
"""
selects time formats.
"""
CURRENCY: Literal[8]
"""
selects currency formats.
"""
NUMBER: Literal[16]
"""
selects decimal number formats.
"""
SCIENTIFIC: Literal[32]
"""
selects scientific number formats.
"""
FRACTION: Literal[64]
"""
selects number formats for fractions.
"""
PERCENT: Literal[128]
"""
selects percentage number formats.
"""
TEXT: Literal[256]
"""
selects text number formats.
"""
DATETIME: Literal[6]
"""
selects number formats which contain date and time.
"""
LOGICAL: Literal[1024]
"""
selects boolean number formats.
"""
UNDEFINED: Literal[2048]
"""
is used as a return value if no format exists.
"""
EMPTY: Literal[4096]
DURATION: Literal[8196]


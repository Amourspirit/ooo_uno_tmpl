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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
"""
Const

specifies the type of a single condition in a filter descriptor.

This constants group extends the FilterOperator enum by additional filter operators.

**since**

    OOo 3.2

See Also:
    `API FilterOperator2 <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1FilterOperator2.html>`_
"""
EMPTY: Literal[0]
"""
selects empty entries.
"""
NOT_EMPTY: Literal[1]
"""
selects non-empty entries.
"""
EQUAL: Literal[2]
"""
value has to be equal to the specified value.
"""
NOT_EQUAL: Literal[3]
"""
value must not be equal to the specified value.
"""
GREATER: Literal[4]
"""
value has to be greater than the specified value.
"""
GREATER_EQUAL: Literal[5]
"""
value has to be greater than or equal to the specified value.
"""
LESS: Literal[6]
"""
value has to be less than the specified value.
"""
LESS_EQUAL: Literal[7]
"""
value has to be less than or equal to the specified value.
"""
TOP_VALUES: Literal[8]
"""
selects a specified number of entries with the greatest values.
"""
TOP_PERCENT: Literal[9]
"""
selects a specified percentage of entries with the greatest values.
"""
BOTTOM_VALUES: Literal[10]
"""
selects a specified number of entries with the lowest values.
"""
BOTTOM_PERCENT: Literal[11]
"""
selects a specified percentage of entries with the lowest values.
"""
CONTAINS: Literal[12]
"""
selects contains entries.
"""
DOES_NOT_CONTAIN: Literal[13]
"""
selects does-not-contain entries.
"""
BEGINS_WITH: Literal[14]
"""
selects begins-with entries.
"""
DOES_NOT_BEGIN_WITH: Literal[15]
"""
selects does-not-begin-with entries.
"""
ENDS_WITH: Literal[16]
"""
selects ends-with entries.
"""
DOES_NOT_END_WITH: Literal[17]
"""
selects does-not-end-with entries.
"""


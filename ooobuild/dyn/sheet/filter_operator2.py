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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sheet import FilterOperator2 as FilterOperator2
    if hasattr(FilterOperator2, '_constants') and isinstance(FilterOperator2._constants, dict):
        FilterOperator2._constants['__ooo_ns__'] = 'com.sun.star.sheet'
        FilterOperator2._constants['__ooo_full_ns__'] = 'com.sun.star.sheet.FilterOperator2'
        FilterOperator2._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global FilterOperator2Enum
        ls = [f for f in dir(FilterOperator2) if not callable(getattr(FilterOperator2, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(FilterOperator2, name)
        FilterOperator2Enum = IntEnum('FilterOperator2Enum', _dict)
    build_enum()
else:
    from ...lo.sheet.filter_operator2 import FilterOperator2 as FilterOperator2

    class FilterOperator2Enum(IntEnum):
        """
        Enum of Const Class FilterOperator2

        specifies the type of a single condition in a filter descriptor.
        
        This constants group extends the FilterOperator enum by additional filter operators.
        
        **since**
        
            OOo 3.2
        """
        EMPTY = FilterOperator2.EMPTY
        """
        selects empty entries.
        """
        NOT_EMPTY = FilterOperator2.NOT_EMPTY
        """
        selects non-empty entries.
        """
        EQUAL = FilterOperator2.EQUAL
        """
        value has to be equal to the specified value.
        """
        NOT_EQUAL = FilterOperator2.NOT_EQUAL
        """
        value must not be equal to the specified value.
        """
        GREATER = FilterOperator2.GREATER
        """
        value has to be greater than the specified value.
        """
        GREATER_EQUAL = FilterOperator2.GREATER_EQUAL
        """
        value has to be greater than or equal to the specified value.
        """
        LESS = FilterOperator2.LESS
        """
        value has to be less than the specified value.
        """
        LESS_EQUAL = FilterOperator2.LESS_EQUAL
        """
        value has to be less than or equal to the specified value.
        """
        TOP_VALUES = FilterOperator2.TOP_VALUES
        """
        selects a specified number of entries with the greatest values.
        """
        TOP_PERCENT = FilterOperator2.TOP_PERCENT
        """
        selects a specified percentage of entries with the greatest values.
        """
        BOTTOM_VALUES = FilterOperator2.BOTTOM_VALUES
        """
        selects a specified number of entries with the lowest values.
        """
        BOTTOM_PERCENT = FilterOperator2.BOTTOM_PERCENT
        """
        selects a specified percentage of entries with the lowest values.
        """
        CONTAINS = FilterOperator2.CONTAINS
        """
        selects contains entries.
        """
        DOES_NOT_CONTAIN = FilterOperator2.DOES_NOT_CONTAIN
        """
        selects does-not-contain entries.
        """
        BEGINS_WITH = FilterOperator2.BEGINS_WITH
        """
        selects begins-with entries.
        """
        DOES_NOT_BEGIN_WITH = FilterOperator2.DOES_NOT_BEGIN_WITH
        """
        selects does-not-begin-with entries.
        """
        ENDS_WITH = FilterOperator2.ENDS_WITH
        """
        selects ends-with entries.
        """
        DOES_NOT_END_WITH = FilterOperator2.DOES_NOT_END_WITH
        """
        selects does-not-end-with entries.
        """

__all__ = ['FilterOperator2', 'FilterOperator2Enum']

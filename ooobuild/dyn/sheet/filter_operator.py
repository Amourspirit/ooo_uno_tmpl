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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import TYPE_CHECKING


if TYPE_CHECKING:

    class FilterOperator(uno.Enum):
        """
        Enum Class


        See Also:
            `API FilterOperator <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#af9e5fd8fd26fc252748d97ebd68ea6b1>`_
        """
        __ooo_ns__: str = ...
        __ooo_full_ns__: str = ...
        __ooo_type_name__: str = ...

        @property
        def typeName(self) -> str:
            ...

        BOTTOM_PERCENT: FilterOperator = ...
        """
        selects a specified percentage of entries with the lowest values.
        """
        BOTTOM_VALUES: FilterOperator = ...
        """
        selects a specified number of entries with the lowest values.
        """
        EMPTY: FilterOperator = ...
        """
        selects empty entries.
        """
        EQUAL: FilterOperator = ...
        """
        value has to be equal to the specified value.
        
        The cell value is equal to the specified value.
        """
        GREATER: FilterOperator = ...
        """
        the value has to be greater than the specified value.
        
        value has to be greater than the specified value.
        """
        GREATER_EQUAL: FilterOperator = ...
        """
        the value has to be greater than or equal to the specified value.
        
        The cell value is greater or equal to the specified value.
        
        value has to be greater than or equal to the specified value.
        """
        LESS: FilterOperator = ...
        """
        the value has to be less than the specified value.
        
        value has to be less than the specified value.
        """
        LESS_EQUAL: FilterOperator = ...
        """
        the value has to be less than or equal to the specified value.
        
        The cell value is less or equal to the specified value.
        
        value has to be less than or equal to the specified value.
        """
        NOT_EMPTY: FilterOperator = ...
        """
        selects non-empty entries.
        """
        NOT_EQUAL: FilterOperator = ...
        """
        the value must not be equal to the specified value.
        
        value must not be equal to the specified value.
        """
        TOP_PERCENT: FilterOperator = ...
        """
        selects a specified percentage of entries with the greatest values.
        """
        TOP_VALUES: FilterOperator = ...
        """
        selects a specified number of entries with the greatest values.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class FilterOperator(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.FilterOperator", name_space="com.sun.star.sheet"):
        """Dynamically created class that represents ``com.sun.star.sheet.FilterOperator`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['FilterOperator']


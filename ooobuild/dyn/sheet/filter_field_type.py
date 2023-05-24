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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class FilterFieldType(metaclass=UnoConstMeta, type_name="com.sun.star.sheet.FilterFieldType", name_space="com.sun.star.sheet"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sheet.FilterFieldType``"""
        pass

    class FilterFieldTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sheet.FilterFieldType", name_space="com.sun.star.sheet"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sheet.FilterFieldType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.sheet import FilterFieldType as FilterFieldType
    else:
        # keep document generators happy
        from ...lo.sheet.filter_field_type import FilterFieldType as FilterFieldType

    class FilterFieldTypeEnum(IntEnum):
        """
        Enum of Const Class FilterFieldType

        
        **since**
        
            LibreOffice 7.2
        """
        NUMERIC = FilterFieldType.NUMERIC
        """
        Filter by numeric value.
        """
        STRING = FilterFieldType.STRING
        """
        Filter by string value.
        """
        DATE = FilterFieldType.DATE
        """
        Filter by date.
        """
        TEXT_COLOR = FilterFieldType.TEXT_COLOR
        """
        Filter by text color.
        """
        BACKGROUND_COLOR = FilterFieldType.BACKGROUND_COLOR
        """
        Filter by background color.
        """

__all__ = ['FilterFieldType', 'FilterFieldTypeEnum']

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
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class DateDisplayFormat(metaclass=UnoConstMeta, type_name="com.sun.star.text.DateDisplayFormat", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.DateDisplayFormat``"""
        pass

    class DateDisplayFormatEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.DateDisplayFormat", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.DateDisplayFormat`` as Enum values"""
        pass

else:
    from ...lo.text.date_display_format import DateDisplayFormat as DateDisplayFormat

    class DateDisplayFormatEnum(IntEnum):
        """
        Enum of Const Class DateDisplayFormat

        This constants define how a date field is formatted before it is displayed.
        
        The format may also depend on the system or document locale. The samples are in German.
        
        .. deprecated::
        
            Class is deprecated.
        """
        STANDARD_SHORT = DateDisplayFormat.STANDARD_SHORT
        """
        the shortest system standard
        """
        STANDARD_LONG = DateDisplayFormat.STANDARD_LONG
        """
        the longest system standard
        """
        MMDDYY = DateDisplayFormat.MMDDYY
        """
        22.11.73
        """
        MMDDYYYY = DateDisplayFormat.MMDDYYYY
        """
        22.11.1973
        """
        DDMMMYYYY = DateDisplayFormat.DDMMMYYYY
        DDMMMMYYYY = DateDisplayFormat.DDMMMMYYYY
        NNDDMMMMYYYY = DateDisplayFormat.NNDDMMMMYYYY
        """
        Do, 22.
        
        November 1973
        """
        NNNNDDMMMMYYYY = DateDisplayFormat.NNNNDDMMMMYYYY
        """
        Donnerstag, 22.
        
        November 1973
        """

__all__ = ['DateDisplayFormat', 'DateDisplayFormatEnum']

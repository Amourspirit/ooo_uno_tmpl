# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.i18n
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

    class CalendarDisplayCode(metaclass=UnoConstMeta, type_name="com.sun.star.i18n.CalendarDisplayCode", name_space="com.sun.star.i18n"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.i18n.CalendarDisplayCode``"""
        pass

    class CalendarDisplayCodeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.i18n.CalendarDisplayCode", name_space="com.sun.star.i18n"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.i18n.CalendarDisplayCode`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.i18n import CalendarDisplayCode as CalendarDisplayCode
    else:
        # keep document generators happy
        from ...lo.i18n.calendar_display_code import CalendarDisplayCode as CalendarDisplayCode

    class CalendarDisplayCodeEnum(IntEnum):
        """
        Enum of Const Class CalendarDisplayCode

        Constants to use with XExtendedCalendar.getDisplayString().
        
        The examples given are for an English Gregorian calendar, note that other calendars or locales may return completely different strings, for example not a four digit year but a CJK name instead.
        
        **since**
        
            OOo 1.1.2
        """
        SHORT_DAY = CalendarDisplayCode.SHORT_DAY
        """
        Day of month, one or two digits, no leading zero.
        """
        LONG_DAY = CalendarDisplayCode.LONG_DAY
        """
        Day of month, two digits, with leading zero.
        """
        SHORT_DAY_NAME = CalendarDisplayCode.SHORT_DAY_NAME
        """
        Day of week, abbreviated name.
        """
        LONG_DAY_NAME = CalendarDisplayCode.LONG_DAY_NAME
        """
        Day of week, full name.
        """
        SHORT_MONTH = CalendarDisplayCode.SHORT_MONTH
        """
        Month of year, one or two digits, no leading zero.
        """
        LONG_MONTH = CalendarDisplayCode.LONG_MONTH
        """
        Month of year, with leading zero.
        """
        SHORT_MONTH_NAME = CalendarDisplayCode.SHORT_MONTH_NAME
        """
        Abbreviated month name.
        """
        LONG_MONTH_NAME = CalendarDisplayCode.LONG_MONTH_NAME
        """
        Full month name.
        """
        SHORT_YEAR = CalendarDisplayCode.SHORT_YEAR
        """
        Year, two digits.
        """
        LONG_YEAR = CalendarDisplayCode.LONG_YEAR
        """
        Year, four digits.
        """
        SHORT_ERA = CalendarDisplayCode.SHORT_ERA
        """
        Abbreviated era name, for example, BC or AD.
        """
        LONG_ERA = CalendarDisplayCode.LONG_ERA
        """
        Full era name, for example, \"Before Christ\" or \"Anno Dominus\".
        """
        SHORT_YEAR_AND_ERA = CalendarDisplayCode.SHORT_YEAR_AND_ERA
        """
        Combined short year and era, order depends on locale/calendar.
        """
        LONG_YEAR_AND_ERA = CalendarDisplayCode.LONG_YEAR_AND_ERA
        """
        Combined full year and era, order depends on locale/calendar.
        """
        SHORT_QUARTER = CalendarDisplayCode.SHORT_QUARTER
        """
        Short quarter, for example, \"Q1\".
        """
        LONG_QUARTER = CalendarDisplayCode.LONG_QUARTER
        """
        Long quarter, for example, \"1st quarter\".
        """
        SHORT_GENITIVE_MONTH_NAME = CalendarDisplayCode.SHORT_GENITIVE_MONTH_NAME
        """
        Abbreviated possessive genitive case month name.
        
        **since**
        
            LibreOffice 3.5
        """
        LONG_GENITIVE_MONTH_NAME = CalendarDisplayCode.LONG_GENITIVE_MONTH_NAME
        """
        Full possessive genitive case month name.
        
        **since**
        
            LibreOffice 3.5
        """
        NARROW_GENITIVE_MONTH_NAME = CalendarDisplayCode.NARROW_GENITIVE_MONTH_NAME
        """
        Narrow possessive genitive case month name.
        
        **since**
        
            LibreOffice 3.5
        """
        SHORT_PARTITIVE_MONTH_NAME = CalendarDisplayCode.SHORT_PARTITIVE_MONTH_NAME
        """
        Abbreviated partitive case month name.
        
        **since**
        
            LibreOffice 3.5
        """
        LONG_PARTITIVE_MONTH_NAME = CalendarDisplayCode.LONG_PARTITIVE_MONTH_NAME
        """
        Full partitive case month name.
        
        **since**
        
            LibreOffice 3.5
        """
        NARROW_PARTITIVE_MONTH_NAME = CalendarDisplayCode.NARROW_PARTITIVE_MONTH_NAME
        """
        Narrow partitive case month name.
        
        **since**
        
            LibreOffice 3.5
        """
        NARROW_DAY_NAME = CalendarDisplayCode.NARROW_DAY_NAME
        """
        Day of week, narrow name.
        
        **since**
        
            LibreOffice 3.5
        """
        NARROW_MONTH_NAME = CalendarDisplayCode.NARROW_MONTH_NAME
        """
        Narrow month name.
        
        **since**
        
            LibreOffice 3.5
        """

__all__ = ['CalendarDisplayCode', 'CalendarDisplayCodeEnum']

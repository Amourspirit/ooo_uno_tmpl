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
# Namespace: com.sun.star.i18n
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.i18n import CalendarFieldIndex as CalendarFieldIndex
    if hasattr(CalendarFieldIndex, '_constants') and isinstance(CalendarFieldIndex._constants, dict):
        CalendarFieldIndex._constants['__ooo_ns__'] = 'com.sun.star.i18n'
        CalendarFieldIndex._constants['__ooo_full_ns__'] = 'com.sun.star.i18n.CalendarFieldIndex'
        CalendarFieldIndex._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global CalendarFieldIndexEnum
        ls = [f for f in dir(CalendarFieldIndex) if not callable(getattr(CalendarFieldIndex, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(CalendarFieldIndex, name)
        CalendarFieldIndexEnum = IntEnum('CalendarFieldIndexEnum', _dict)
    build_enum()
else:
    from ...lo.i18n.calendar_field_index import CalendarFieldIndex as CalendarFieldIndex

    class CalendarFieldIndexEnum(IntEnum):
        """
        Enum of Const Class CalendarFieldIndex

        Field indices to be passed to various XCalendar methods.
        
        Field is writable only if marked both Get/Set.
        
        ZONE_OFFSET and DST_OFFSET cooperate such that both values are added, for example, ZoneOffset=1*60 and DstOffset=1*60 results in a time difference of GMT+2. The calculation in minutes is GMT = LocalTime - ZoneOffset - DstOffset
        
        With introduction of ZONE_OFFSET_SECOND_MILLIS and DST_OFFSET_SECOND_MILLIS the exact calculation in milliseconds is GMT = LocalTime
        
        **since**
        
            OOo 3.1
        """
        AM_PM = CalendarFieldIndex.AM_PM
        """
        Get AmPmValue.
        """
        DAY_OF_MONTH = CalendarFieldIndex.DAY_OF_MONTH
        """
        Get/Set day of month [1-31].
        """
        DAY_OF_WEEK = CalendarFieldIndex.DAY_OF_WEEK
        """
        Get day of week [0-6].
        """
        DAY_OF_YEAR = CalendarFieldIndex.DAY_OF_YEAR
        """
        Get day of year.
        """
        DST_OFFSET = CalendarFieldIndex.DST_OFFSET
        """
        Get daylight saving time offset in minutes, e.g.
        
        [0*60..1*60]
        
        The DST offset value depends on the actual date set at the calendar and is determined according to the timezone rules of the locale used with the calendar.
        
        Note that there is a bug in OpenOffice.org 1.0 / StarOffice 6.0 that prevents interpreting this value correctly.
        """
        HOUR = CalendarFieldIndex.HOUR
        """
        Get/Set hour [0-23].
        """
        MINUTE = CalendarFieldIndex.MINUTE
        """
        Get/Set minute [0-59].
        """
        SECOND = CalendarFieldIndex.SECOND
        """
        Get/Set second [0-59].
        """
        MILLISECOND = CalendarFieldIndex.MILLISECOND
        """
        Get/Set milliseconds [0-999].
        """
        WEEK_OF_MONTH = CalendarFieldIndex.WEEK_OF_MONTH
        """
        Get week of month.
        """
        WEEK_OF_YEAR = CalendarFieldIndex.WEEK_OF_YEAR
        """
        Get week of year.
        """
        YEAR = CalendarFieldIndex.YEAR
        """
        Get/Set year.
        """
        MONTH = CalendarFieldIndex.MONTH
        """
        Get/Set month [0-...].
        
        Note that the maximum value is not necessarily 11 for December but depends on the calendar used instead.
        """
        ERA = CalendarFieldIndex.ERA
        """
        Get/Set era, for example, 0:= Before Christ, 1:= After Christ.
        """
        ZONE_OFFSET = CalendarFieldIndex.ZONE_OFFSET
        """
        Get/Set time zone offset in minutes, e.g. [-14*60..14*60].
        """
        FIELD_COUNT = CalendarFieldIndex.FIELD_COUNT
        """
        Total number of fields for < OOo 3.1.
        """
        ZONE_OFFSET_SECOND_MILLIS = CalendarFieldIndex.ZONE_OFFSET_SECOND_MILLIS
        """
        Get/Set additional offset in milliseconds that adds to the value of ZONE_OFFSET.
        
        This may be necessary to correctly interpret historical timezone data that consists of fractions of minutes, e.g. seconds. 1 minute == 60000 milliseconds.
        
        **since**
        
            OOo 3.1
        """
        DST_OFFSET_SECOND_MILLIS = CalendarFieldIndex.DST_OFFSET_SECOND_MILLIS
        """
        Get additional offset in milliseconds that adds to the value of DST_OFFSET.
        
        This may be necessary to correctly interpret historical timezone data that consists of fractions of minutes, e.g. seconds. 1 minute == 60000 milliseconds.
        
        **since**
        
            OOo 3.1
        """
        FIELD_COUNT2 = CalendarFieldIndex.FIELD_COUNT2
        """
        Total number of fields as of OOo 3.1.
        
        **since**
        
            OOo 3.1
        """

__all__ = ['CalendarFieldIndex', 'CalendarFieldIndexEnum']
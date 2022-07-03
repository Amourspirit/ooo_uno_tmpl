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
# Namespace: com.sun.star.i18n
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class Months(metaclass=UnoConstMeta, type_name="com.sun.star.i18n.Months", name_space="com.sun.star.i18n"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.i18n.Months``"""
        pass

    class MonthsEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.i18n.Months", name_space="com.sun.star.i18n"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.i18n.Months`` as Enum values"""
        pass

else:
    from ...lo.i18n.months import Months as Months

    class MonthsEnum(IntEnum):
        """
        Enum of Const Class Months

        Constants for month names used in calls to XCalendar.getDisplayName().
        """
        JANUARY = Months.JANUARY
        """
        January.
        """
        FEBURARY = Months.FEBURARY
        """
        February.
        """
        MARCH = Months.MARCH
        """
        March.
        """
        APRIL = Months.APRIL
        """
        April.
        """
        MAY = Months.MAY
        """
        May.
        """
        JUNE = Months.JUNE
        """
        June.
        """
        JULY = Months.JULY
        """
        July.
        """
        AUGUST = Months.AUGUST
        """
        August.
        """
        SEPTEMBER = Months.SEPTEMBER
        """
        September.
        """
        OCTOBER = Months.OCTOBER
        """
        October.
        """
        NOVEMBER = Months.NOVEMBER
        """
        November.
        """
        DECEMBER = Months.DECEMBER
        """
        December.
        """

__all__ = ['Months', 'MonthsEnum']

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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from .calendar_item import CalendarItem as CalendarItem_a86c0af1


class Calendar(object):
    """
    Struct Class

    A calendar as returned in a sequence by XLocaleData.getAllCalendars().

    See Also:
        `API Calendar <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1Calendar.html>`_
    """
    typeName: Literal['com.sun.star.i18n.Calendar']

    def __init__(self, Days: typing.Optional[typing.Tuple[CalendarItem_a86c0af1, ...]] = ..., Months: typing.Optional[typing.Tuple[CalendarItem_a86c0af1, ...]] = ..., Eras: typing.Optional[typing.Tuple[CalendarItem_a86c0af1, ...]] = ..., StartOfWeek: typing.Optional[str] = ..., MinimumNumberOfDaysForFirstWeek: typing.Optional[int] = ..., Default: typing.Optional[bool] = ..., Name: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Days (typing.Tuple[CalendarItem, ...], optional): Days value.
            Months (typing.Tuple[CalendarItem, ...], optional): Months value.
            Eras (typing.Tuple[CalendarItem, ...], optional): Eras value.
            StartOfWeek (str, optional): StartOfWeek value.
            MinimumNumberOfDaysForFirstWeek (int, optional): MinimumNumberOfDaysForFirstWeek value.
            Default (bool, optional): Default value.
            Name (str, optional): Name value.
        """
        ...


    @property
    def Days(self) -> typing.Tuple[CalendarItem_a86c0af1, ...]:
        """
        the days of the week, see also CalendarItem.
        """
        ...


    @property
    def Months(self) -> typing.Tuple[CalendarItem_a86c0af1, ...]:
        """
        the months of the year, see also CalendarItem.
        """
        ...


    @property
    def Eras(self) -> typing.Tuple[CalendarItem_a86c0af1, ...]:
        """
        the possible eras, see also CalendarItem.
        """
        ...


    @property
    def StartOfWeek(self) -> str:
        """
        the ID of the day with which the week begins.
        """
        ...


    @property
    def MinimumNumberOfDaysForFirstWeek(self) -> int:
        """
        how many days must reside in the first week of a year.
        """
        ...


    @property
    def Default(self) -> bool:
        """
        if this is the default calendar for a given locale.
        """
        ...


    @property
    def Name(self) -> str:
        """
        the name of the calendar, for example, Gregorian.
        """
        ...



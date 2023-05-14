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
# Namespace: com.sun.star.util
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class Duration(object):
    """
    Struct Class

    represents a duration.
    
    A duration is the difference of 2 DateTimes.
    
    Note that there are no constraints on the ranges of the members, except that every member must be non-negative: for example, a Duration of 400 Days is valid.
    
    **since**
    
        OOo 3.3

    See Also:
        `API Duration <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1Duration.html>`_
    """
    typeName: Literal['com.sun.star.util.Duration']

    def __init__(self, Negative: typing.Optional[bool] = ..., Years: typing.Optional[int] = ..., Months: typing.Optional[int] = ..., Days: typing.Optional[int] = ..., Hours: typing.Optional[int] = ..., Minutes: typing.Optional[int] = ..., Seconds: typing.Optional[int] = ..., NanoSeconds: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Negative (bool, optional): Negative value.
            Years (int, optional): Years value.
            Months (int, optional): Months value.
            Days (int, optional): Days value.
            Hours (int, optional): Hours value.
            Minutes (int, optional): Minutes value.
            Seconds (int, optional): Seconds value.
            NanoSeconds (int, optional): NanoSeconds value.
        """
        ...


    @property
    def Negative(self) -> bool:
        """
        explicit sign bit.
        """
        ...

    @Negative.setter
    def Negative(self, value: bool) -> None:
        ...

    @property
    def Years(self) -> int:
        """
        contains the years.
        """
        ...

    @Years.setter
    def Years(self, value: int) -> None:
        ...

    @property
    def Months(self) -> int:
        """
        contains the months.
        """
        ...

    @Months.setter
    def Months(self, value: int) -> None:
        ...

    @property
    def Days(self) -> int:
        """
        contains the days.
        """
        ...

    @Days.setter
    def Days(self, value: int) -> None:
        ...

    @property
    def Hours(self) -> int:
        """
        contains the hours.
        """
        ...

    @Hours.setter
    def Hours(self, value: int) -> None:
        ...

    @property
    def Minutes(self) -> int:
        """
        contains the minutes.
        """
        ...

    @Minutes.setter
    def Minutes(self, value: int) -> None:
        ...

    @property
    def Seconds(self) -> int:
        """
        contains the seconds.
        """
        ...

    @Seconds.setter
    def Seconds(self, value: int) -> None:
        ...

    @property
    def NanoSeconds(self) -> int:
        """
        contains the nanoseconds.
        """
        ...

    @NanoSeconds.setter
    def NanoSeconds(self, value: int) -> None:
        ...


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


class Date(object):
    """
    Struct Class

    represents a date value.
    
    The time zone is unknown.

    See Also:
        `API Date <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1Date.html>`_
    """
    typeName: Literal['com.sun.star.util.Date']

    def __init__(self, Day: typing.Optional[int] = ..., Month: typing.Optional[int] = ..., Year: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Day (int, optional): Day value.
            Month (int, optional): Month value.
            Year (int, optional): Year value.
        """
        ...


    @property
    def Day(self) -> int:
        """
        contains the day of month (1-31 or 0 for a void date).
        """
        ...


    @property
    def Month(self) -> int:
        """
        contains the month of year (1-12 or 0 for a void date).
        """
        ...


    @property
    def Year(self) -> int:
        """
        contains the year.
        """
        ...



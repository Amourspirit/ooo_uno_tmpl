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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.3
from typing_extensions import Literal
from .calendar_item import CalendarItem as CalendarItem_a86c0af1
import typing


class CalendarItem2(CalendarItem_a86c0af1):
    """
    Struct Class

    One entry in a calendar, for example, a day of week or a month or an era.
    
    Derived from com.sun.star.i18n.CalendarItem this provides an additional member for narrow names.
    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API CalendarItem2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1CalendarItem2.html>`_
    """
    typeName: Literal['com.sun.star.i18n.CalendarItem2']

    def __init__(self, ID: typing.Optional[str] = ..., AbbrevName: typing.Optional[str] = ..., FullName: typing.Optional[str] = ..., NarrowName: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            ID (str, optional): ID value.
            AbbrevName (str, optional): AbbrevName value.
            FullName (str, optional): FullName value.
            NarrowName (str, optional): NarrowName value.
        """


    @property
    def NarrowName(self) -> str:
        """
        The narrow name, for example, \"S\" for Sunday or \"J\" for January.
        """



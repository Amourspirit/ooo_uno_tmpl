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
# Libre Office Version: 7.2
from typing_extensions import Literal
from .locale_data_item import LocaleDataItem as LocaleDataItem_beff0ba1
import typing


class LocaleDataItem2(LocaleDataItem_beff0ba1):
    """
    Struct Class

    Locale specific data, derived from LocaleDataItem adding an alternative input decimal separator.
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API LocaleDataItem2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1LocaleDataItem2.html>`_
    """
    typeName: Literal['com.sun.star.i18n.LocaleDataItem2']

    def __init__(self, unoID: typing.Optional[str] = ..., dateSeparator: typing.Optional[str] = ..., thousandSeparator: typing.Optional[str] = ..., decimalSeparator: typing.Optional[str] = ..., timeSeparator: typing.Optional[str] = ..., time100SecSeparator: typing.Optional[str] = ..., listSeparator: typing.Optional[str] = ..., quotationStart: typing.Optional[str] = ..., quotationEnd: typing.Optional[str] = ..., doubleQuotationStart: typing.Optional[str] = ..., doubleQuotationEnd: typing.Optional[str] = ..., timeAM: typing.Optional[str] = ..., timePM: typing.Optional[str] = ..., measurementSystem: typing.Optional[str] = ..., LongDateDayOfWeekSeparator: typing.Optional[str] = ..., LongDateDaySeparator: typing.Optional[str] = ..., LongDateMonthSeparator: typing.Optional[str] = ..., LongDateYearSeparator: typing.Optional[str] = ..., decimalSeparatorAlternative: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            unoID (str, optional): unoID value.
            dateSeparator (str, optional): dateSeparator value.
            thousandSeparator (str, optional): thousandSeparator value.
            decimalSeparator (str, optional): decimalSeparator value.
            timeSeparator (str, optional): timeSeparator value.
            time100SecSeparator (str, optional): time100SecSeparator value.
            listSeparator (str, optional): listSeparator value.
            quotationStart (str, optional): quotationStart value.
            quotationEnd (str, optional): quotationEnd value.
            doubleQuotationStart (str, optional): doubleQuotationStart value.
            doubleQuotationEnd (str, optional): doubleQuotationEnd value.
            timeAM (str, optional): timeAM value.
            timePM (str, optional): timePM value.
            measurementSystem (str, optional): measurementSystem value.
            LongDateDayOfWeekSeparator (str, optional): LongDateDayOfWeekSeparator value.
            LongDateDaySeparator (str, optional): LongDateDaySeparator value.
            LongDateMonthSeparator (str, optional): LongDateMonthSeparator value.
            LongDateYearSeparator (str, optional): LongDateYearSeparator value.
            decimalSeparatorAlternative (str, optional): decimalSeparatorAlternative value.
        """


    @property
    def decimalSeparatorAlternative(self) -> str:
        """
        Alternative input decimal separator, for example, \".\" if the regular locale dependent separator usually is not present on keyboards used with that locale.
        
        This separator is optional, an empty string denotes no alternative decimal separator shall be used.
        """



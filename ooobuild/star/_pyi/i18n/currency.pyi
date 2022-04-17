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
import typing


class Currency(object):
    """
    Struct Class

    Symbols, names, and attributes of a specific currency, returned in a sequence by XLocaleData.getAllCurrencies().

    See Also:
        `API Currency <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1Currency.html>`_
    """
    typeName: Literal['com.sun.star.i18n.Currency']

    def __init__(self, ID: typing.Optional[str] = ..., Symbol: typing.Optional[str] = ..., BankSymbol: typing.Optional[str] = ..., Name: typing.Optional[str] = ..., Default: typing.Optional[bool] = ..., UsedInCompatibleFormatCodes: typing.Optional[bool] = ..., DecimalPlaces: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            ID (str, optional): ID value.
            Symbol (str, optional): Symbol value.
            BankSymbol (str, optional): BankSymbol value.
            Name (str, optional): Name value.
            Default (bool, optional): Default value.
            UsedInCompatibleFormatCodes (bool, optional): UsedInCompatibleFormatCodes value.
            DecimalPlaces (int, optional): DecimalPlaces value.
        """


    @property
    def ID(self) -> str:
        """
        ISO 4217 currency code identifier, for example, EUR or USD.
        """


    @property
    def Symbol(self) -> str:
        """
        Currency symbol, for example, $.
        """


    @property
    def BankSymbol(self) -> str:
        """
        Currency abbreviation used by banks and in money exchange, for example, EUR or USD.
        
        This usually should be identical to the ISO 4217 currency code also used in the ID, but doesn't necessarily have to be.
        """


    @property
    def Name(self) -> str:
        """
        Name of the currency, for example, Euro or US Dollar.
        
        Should be the localized name.
        """


    @property
    def Default(self) -> bool:
        """
        If this currency is the default currency for a given locale.
        """


    @property
    def UsedInCompatibleFormatCodes(self) -> bool:
        """
        If this currency is the one used in compatible number format codes with FormatElement.formatIndex() values in the range 12..17.
        
        Those format codes are used to generate some old style currency format codes for compatibility with StarOffice5 and StarOffice4.
        """


    @property
    def DecimalPlaces(self) -> int:
        """
        The number of decimal places, for example, 2 for US Dollar or 0 for Italian Lira.
        """



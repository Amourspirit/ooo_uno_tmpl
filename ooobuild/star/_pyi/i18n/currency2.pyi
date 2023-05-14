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
from .currency import Currency as Currency_80230993
import typing


class Currency2(Currency_80230993):
    """
    Struct Class

    Symbols, names, and attributes of a specific currency, returned in a sequence by XLocaleData2.getAllCurrencies2().
    
    It is derived from com.sun.star.i18n.Currency and provides an additional flag for currency entries that are available only for legacy reasons in context of loaded documents that use them, but otherwise should not be offered to the user to be selectable.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API Currency2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1Currency2.html>`_
    """
    typeName: Literal['com.sun.star.i18n.Currency2']

    def __init__(self, ID: typing.Optional[str] = ..., Symbol: typing.Optional[str] = ..., BankSymbol: typing.Optional[str] = ..., Name: typing.Optional[str] = ..., Default: typing.Optional[bool] = ..., UsedInCompatibleFormatCodes: typing.Optional[bool] = ..., DecimalPlaces: typing.Optional[int] = ..., LegacyOnly: typing.Optional[bool] = ...) -> None:
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
            LegacyOnly (bool, optional): LegacyOnly value.
        """
        ...


    @property
    def LegacyOnly(self) -> bool:
        """
        If set, the currency and/or its symbol is only to be used in legacy context.
        
        **since**
        
            OOo 2.0.3
        """
        ...



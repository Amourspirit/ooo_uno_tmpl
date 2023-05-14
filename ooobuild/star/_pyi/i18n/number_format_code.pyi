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


class NumberFormatCode(object):
    """
    Struct Class

    Number format code information returned by various XNumberFormatCode methods.

    See Also:
        `API NumberFormatCode <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1NumberFormatCode.html>`_
    """
    typeName: Literal['com.sun.star.i18n.NumberFormatCode']

    def __init__(self, Type: typing.Optional[int] = ..., Usage: typing.Optional[int] = ..., Code: typing.Optional[str] = ..., DefaultName: typing.Optional[str] = ..., NameID: typing.Optional[str] = ..., Index: typing.Optional[int] = ..., Default: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Type (int, optional): Type value.
            Usage (int, optional): Usage value.
            Code (str, optional): Code value.
            DefaultName (str, optional): DefaultName value.
            NameID (str, optional): NameID value.
            Index (int, optional): Index value.
            Default (bool, optional): Default value.
        """
        ...


    @property
    def Type(self) -> int:
        """
        One of KNumberFormatType values.
        """
        ...

    @Type.setter
    def Type(self, value: int) -> None:
        ...

    @property
    def Usage(self) -> int:
        """
        One of KNumberFormatUsage values.
        """
        ...

    @Usage.setter
    def Usage(self, value: int) -> None:
        ...

    @property
    def Code(self) -> str:
        """
        Format code, for example, \"YYYY-MM-DD\".
        """
        ...

    @Code.setter
    def Code(self, value: str) -> None:
        ...

    @property
    def DefaultName(self) -> str:
        """
        Descriptive name of the format for this locale.
        """
        ...

    @DefaultName.setter
    def DefaultName(self, value: str) -> None:
        ...

    @property
    def NameID(self) -> str:
        """
        Message identifier to be used if the name of the format is localized.
        """
        ...

    @NameID.setter
    def NameID(self, value: str) -> None:
        ...

    @property
    def Index(self) -> int:
        """
        Index of the code as defined in NumberFormatIndex.
        """
        ...

    @Index.setter
    def Index(self, value: int) -> None:
        ...

    @property
    def Default(self) -> bool:
        """
        If this format is the default format of the Usage group.
        """
        ...

    @Default.setter
    def Default(self, value: bool) -> None:
        ...


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
# Namespace: com.sun.star.style
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from .tab_align import TabAlign as TabAlign_8fc90a3b


class TabStop(object):
    """
    Struct Class

    This structure is used to specify a single tabulator stop.

    See Also:
        `API TabStop <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1style_1_1TabStop.html>`_
    """
    typeName: Literal['com.sun.star.style.TabStop']

    def __init__(self, Position: typing.Optional[int] = ..., Alignment: typing.Optional[TabAlign_8fc90a3b] = ..., DecimalChar: typing.Optional[str] = ..., FillChar: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Position (int, optional): Position value.
            Alignment (TabAlign, optional): Alignment value.
            DecimalChar (str, optional): DecimalChar value.
            FillChar (str, optional): FillChar value.
        """
        ...


    @property
    def Position(self) -> int:
        """
        This field specifies the position of the tabulator in relation to the left border.
        """
        ...

    @Position.setter
    def Position(self, value: int) -> None:
        ...

    @property
    def Alignment(self) -> TabAlign_8fc90a3b:
        """
        This field specifies the alignment of the text range before the tabulator.
        """
        ...

    @Alignment.setter
    def Alignment(self, value: TabAlign_8fc90a3b) -> None:
        ...

    @property
    def DecimalChar(self) -> str:
        """
        This field specifies which delimiter is used for the decimal.
        """
        ...

    @DecimalChar.setter
    def DecimalChar(self, value: str) -> None:
        ...

    @property
    def FillChar(self) -> str:
        """
        This field specifies the character that is used to fill up the space between the text in the text range and the tabulators.
        """
        ...

    @FillChar.setter
    def FillChar(self, value: str) -> None:
        ...


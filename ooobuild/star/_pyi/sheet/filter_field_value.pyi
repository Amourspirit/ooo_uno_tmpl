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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..util.color import Color as Color_68e908c5


class FilterFieldValue(object):
    """
    Struct Class

    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API FilterFieldValue <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1FilterFieldValue.html>`_
    """
    typeName: Literal['com.sun.star.sheet.FilterFieldValue']

    def __init__(self, IsNumeric: typing.Optional[bool] = ..., NumericValue: typing.Optional[float] = ..., StringValue: typing.Optional[str] = ..., FilterType: typing.Optional[int] = ..., ColorValue: typing.Optional[Color_68e908c5] = ...) -> None:
        """
        Constructor

        Arguments:
            IsNumeric (bool, optional): IsNumeric value.
            NumericValue (float, optional): NumericValue value.
            StringValue (str, optional): StringValue value.
            FilterType (int, optional): FilterType value.
            ColorValue (Color, optional): ColorValue value.
        """
        ...


    @property
    def IsNumeric(self) -> bool:
        """
        selects whether the TableFilterFieldValue.NumericValue or the TableFilterFieldValue.StringValue is used.
        """
        ...

    @IsNumeric.setter
    def IsNumeric(self, value: bool) -> None:
        ...

    @property
    def NumericValue(self) -> float:
        """
        specifies a numeric value for the condition.
        """
        ...

    @NumericValue.setter
    def NumericValue(self, value: float) -> None:
        ...

    @property
    def StringValue(self) -> str:
        """
        specifies a string value for the condition.
        """
        ...

    @StringValue.setter
    def StringValue(self, value: str) -> None:
        ...

    @property
    def FilterType(self) -> int:
        """
        Which field should be used for filtering:
        
        **since**
        
            LibreOffice 7.2
        """
        ...

    @FilterType.setter
    def FilterType(self, value: int) -> None:
        ...

    @property
    def ColorValue(self) -> Color_68e908c5:
        """
        The color which is used for filtering.
        
        **since**
        
            LibreOffice 7.2
        """
        ...

    @ColorValue.setter
    def ColorValue(self, value: Color_68e908c5) -> None:
        ...


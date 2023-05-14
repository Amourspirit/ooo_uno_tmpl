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
# Namespace: com.sun.star.table
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .border_line import BorderLine as BorderLine_a3f80af6


class TableBorder(object):
    """
    Struct Class

    contains the style settings of the border lines of all cells in a cell range.
    
    In a queried structure, the flags in TableBorder.Is...LineValid indicate that not all lines of the boxes have the same values.
    
    In a structure which is used for setting, these flags determine if the corresponding line should be set or if the old value should be kept.

    See Also:
        `API TableBorder <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1TableBorder.html>`_
    """
    typeName: Literal['com.sun.star.table.TableBorder']

    def __init__(self, TopLine: typing.Optional[BorderLine_a3f80af6] = ..., IsTopLineValid: typing.Optional[bool] = ..., BottomLine: typing.Optional[BorderLine_a3f80af6] = ..., IsBottomLineValid: typing.Optional[bool] = ..., LeftLine: typing.Optional[BorderLine_a3f80af6] = ..., IsLeftLineValid: typing.Optional[bool] = ..., RightLine: typing.Optional[BorderLine_a3f80af6] = ..., IsRightLineValid: typing.Optional[bool] = ..., HorizontalLine: typing.Optional[BorderLine_a3f80af6] = ..., IsHorizontalLineValid: typing.Optional[bool] = ..., VerticalLine: typing.Optional[BorderLine_a3f80af6] = ..., IsVerticalLineValid: typing.Optional[bool] = ..., Distance: typing.Optional[int] = ..., IsDistanceValid: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            TopLine (BorderLine, optional): TopLine value.
            IsTopLineValid (bool, optional): IsTopLineValid value.
            BottomLine (BorderLine, optional): BottomLine value.
            IsBottomLineValid (bool, optional): IsBottomLineValid value.
            LeftLine (BorderLine, optional): LeftLine value.
            IsLeftLineValid (bool, optional): IsLeftLineValid value.
            RightLine (BorderLine, optional): RightLine value.
            IsRightLineValid (bool, optional): IsRightLineValid value.
            HorizontalLine (BorderLine, optional): HorizontalLine value.
            IsHorizontalLineValid (bool, optional): IsHorizontalLineValid value.
            VerticalLine (BorderLine, optional): VerticalLine value.
            IsVerticalLineValid (bool, optional): IsVerticalLineValid value.
            Distance (int, optional): Distance value.
            IsDistanceValid (bool, optional): IsDistanceValid value.
        """
        ...


    @property
    def TopLine(self) -> BorderLine_a3f80af6:
        """
        determines the line style at the top edge.
        """
        ...

    @TopLine.setter
    def TopLine(self, value: BorderLine_a3f80af6) -> None:
        ...

    @property
    def IsTopLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder.TopLine is used.
        """
        ...

    @IsTopLineValid.setter
    def IsTopLineValid(self, value: bool) -> None:
        ...

    @property
    def BottomLine(self) -> BorderLine_a3f80af6:
        """
        determines the line style at the bottom edge.
        """
        ...

    @BottomLine.setter
    def BottomLine(self, value: BorderLine_a3f80af6) -> None:
        ...

    @property
    def IsBottomLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder.BottomLine is used.
        """
        ...

    @IsBottomLineValid.setter
    def IsBottomLineValid(self, value: bool) -> None:
        ...

    @property
    def LeftLine(self) -> BorderLine_a3f80af6:
        """
        determines the line style at the left edge.
        """
        ...

    @LeftLine.setter
    def LeftLine(self, value: BorderLine_a3f80af6) -> None:
        ...

    @property
    def IsLeftLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder.LeftLine is used.
        """
        ...

    @IsLeftLineValid.setter
    def IsLeftLineValid(self, value: bool) -> None:
        ...

    @property
    def RightLine(self) -> BorderLine_a3f80af6:
        """
        determines the line style at the right edge.
        """
        ...

    @RightLine.setter
    def RightLine(self, value: BorderLine_a3f80af6) -> None:
        ...

    @property
    def IsRightLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder.RightLine is used.
        """
        ...

    @IsRightLineValid.setter
    def IsRightLineValid(self, value: bool) -> None:
        ...

    @property
    def HorizontalLine(self) -> BorderLine_a3f80af6:
        """
        determines the line style of horizontal lines for the inner part of a cell range.
        """
        ...

    @HorizontalLine.setter
    def HorizontalLine(self, value: BorderLine_a3f80af6) -> None:
        ...

    @property
    def IsHorizontalLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder.HorizontalLine is used.
        """
        ...

    @IsHorizontalLineValid.setter
    def IsHorizontalLineValid(self, value: bool) -> None:
        ...

    @property
    def VerticalLine(self) -> BorderLine_a3f80af6:
        """
        determines the line style of vertical lines for the inner part of a cell range.
        """
        ...

    @VerticalLine.setter
    def VerticalLine(self, value: BorderLine_a3f80af6) -> None:
        ...

    @property
    def IsVerticalLineValid(self) -> bool:
        """
        specifies whether the value of TableBorder.VerticalLine is used.
        """
        ...

    @IsVerticalLineValid.setter
    def IsVerticalLineValid(self, value: bool) -> None:
        ...

    @property
    def Distance(self) -> int:
        """
        contains the distance between the lines and other contents.
        """
        ...

    @Distance.setter
    def Distance(self, value: int) -> None:
        ...

    @property
    def IsDistanceValid(self) -> bool:
        """
        specifies whether the value of TableBorder.Distance is used.
        """
        ...

    @IsDistanceValid.setter
    def IsDistanceValid(self, value: bool) -> None:
        ...


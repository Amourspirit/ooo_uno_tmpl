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
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class TableBorderDistances(object):
    """
    Struct Class

    contains the distance settings of the border lines of all cells in a cell range.
    
    In a queried structure, the flags in TableBorderDistances.Is...DistanceValid indicate that not all lines of the boxes have the same values.
    
    In a structure which is used for setting, these flags determine if the corresponding distance should be set or if the old value should be kept.

    See Also:
        `API TableBorderDistances <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1TableBorderDistances.html>`_
    """
    typeName: Literal['com.sun.star.table.TableBorderDistances']

    def __init__(self, TopDistance: typing.Optional[int] = ..., IsTopDistanceValid: typing.Optional[bool] = ..., BottomDistance: typing.Optional[int] = ..., IsBottomDistanceValid: typing.Optional[bool] = ..., LeftDistance: typing.Optional[int] = ..., IsLeftDistanceValid: typing.Optional[bool] = ..., RightDistance: typing.Optional[int] = ..., IsRightDistanceValid: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            TopDistance (int, optional): TopDistance value.
            IsTopDistanceValid (bool, optional): IsTopDistanceValid value.
            BottomDistance (int, optional): BottomDistance value.
            IsBottomDistanceValid (bool, optional): IsBottomDistanceValid value.
            LeftDistance (int, optional): LeftDistance value.
            IsLeftDistanceValid (bool, optional): IsLeftDistanceValid value.
            RightDistance (int, optional): RightDistance value.
            IsRightDistanceValid (bool, optional): IsRightDistanceValid value.
        """
        ...


    @property
    def TopDistance(self) -> int:
        """
        contains the distance between the top lines and other contents.
        """
        ...


    @property
    def IsTopDistanceValid(self) -> bool:
        """
        specifies whether the value of TableBorder.TopDistance is used.
        """
        ...


    @property
    def BottomDistance(self) -> int:
        """
        contains the distance between the bottom lines and other contents.
        """
        ...


    @property
    def IsBottomDistanceValid(self) -> bool:
        """
        specifies whether the value of TableBorder.BottomDistance is used.
        """
        ...


    @property
    def LeftDistance(self) -> int:
        """
        contains the distance between the left lines and other contents.
        """
        ...


    @property
    def IsLeftDistanceValid(self) -> bool:
        """
        specifies whether the value of TableBorder.LeftDistance is used.
        """
        ...


    @property
    def RightDistance(self) -> int:
        """
        contains the distance between the right lines and other contents.
        """
        ...


    @property
    def IsRightDistanceValid(self) -> bool:
        """
        specifies whether the value of TableBorder.RightDistance is used.
        """
        ...



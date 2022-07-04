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


class CellRangeAddress(object):
    """
    Struct Class

    contains a cell range address within a spreadsheet document.

    See Also:
        `API CellRangeAddress <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1CellRangeAddress.html>`_
    """
    typeName: Literal['com.sun.star.table.CellRangeAddress']

    def __init__(self, Sheet: typing.Optional[int] = ..., StartColumn: typing.Optional[int] = ..., StartRow: typing.Optional[int] = ..., EndColumn: typing.Optional[int] = ..., EndRow: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Sheet (int, optional): Sheet value.
            StartColumn (int, optional): StartColumn value.
            StartRow (int, optional): StartRow value.
            EndColumn (int, optional): EndColumn value.
            EndRow (int, optional): EndRow value.
        """
        ...


    @property
    def Sheet(self) -> int:
        """
        is the index of the sheet that contains the cell range.
        """
        ...


    @property
    def StartColumn(self) -> int:
        """
        is the index of the column of the left edge of the range.
        """
        ...


    @property
    def StartRow(self) -> int:
        """
        is the index of the row of the top edge of the range.
        """
        ...


    @property
    def EndColumn(self) -> int:
        """
        is the index of the column of the right edge of the range.
        """
        ...


    @property
    def EndRow(self) -> int:
        """
        is the index of the row of the bottom edge of the range.
        """
        ...



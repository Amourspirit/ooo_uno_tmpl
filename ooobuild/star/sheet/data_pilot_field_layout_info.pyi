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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
import typing


class DataPilotFieldLayoutInfo(object):
    """
    Struct Class

    contains the layout information of a DataPilotField.

    See Also:
        `API DataPilotFieldLayoutInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldLayoutInfo.html>`_
    """
    typeName: str = 'com.sun.star.sheet.DataPilotFieldLayoutInfo'

    def __init__(self, LayoutMode: typing.Optional[int] = ..., AddEmptyLines: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            LayoutMode (int, optional): LayoutMode value.
            AddEmptyLines (bool, optional): AddEmptyLines value.
        """
        ...

    @property
    def LayoutMode(self) -> int:
        """
        specifies the layout mode.
        """
        ...
    @LayoutMode.setter
    def LayoutMode(self, value: int) -> None:
        ...
    @property
    def AddEmptyLines(self) -> bool:
        """
        If TRUE, an empty row is inserted in the DataPilotTable result table after the data (including the subtotals) for each item of the field.
        """
        ...
    @AddEmptyLines.setter
    def AddEmptyLines(self, value: bool) -> None:
        ...

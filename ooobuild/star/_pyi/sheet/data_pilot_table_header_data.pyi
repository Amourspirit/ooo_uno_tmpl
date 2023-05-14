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
from typing_extensions import Literal
import typing


class DataPilotTableHeaderData(object):
    """
    Struct Class

    information about a cell within the column or row header area of a DataPilot table.
    
    This struct contains information about a particular cell located within the column or row header area of a DataPilot table. This is the type that is contained in DataPilotTablePositionData.PositionData when the value of DataPilotTablePositionData.PositionType is either DataPilotTablePositionType.ROW_HEADER or DataPilotTablePositionType.COLUMN_HEADER.
    
    **since**
    
        OOo 3.0

    See Also:
        `API DataPilotTableHeaderData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotTableHeaderData.html>`_
    """
    typeName: Literal['com.sun.star.sheet.DataPilotTableHeaderData']

    def __init__(self, Dimension: typing.Optional[int] = ..., Hierarchy: typing.Optional[int] = ..., Level: typing.Optional[int] = ..., Flags: typing.Optional[int] = ..., MemberName: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Dimension (int, optional): Dimension value.
            Hierarchy (int, optional): Hierarchy value.
            Level (int, optional): Level value.
            Flags (int, optional): Flags value.
            MemberName (str, optional): MemberName value.
        """
        ...


    @property
    def Dimension(self) -> int:
        """
        number of dimensions
        """
        ...


    @property
    def Hierarchy(self) -> int:
        """
        hierarchy
        """
        ...


    @property
    def Level(self) -> int:
        """
        level
        """
        ...


    @property
    def Flags(self) -> int:
        """
        flag
        """
        ...


    @property
    def MemberName(self) -> str:
        """
        member name
        """
        ...



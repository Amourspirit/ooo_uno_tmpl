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


class DataPilotTablePositionData(object):
    """
    Struct Class

    This structure contains information on a cell within a DataPilot table.
    
    This structure contains information on a particular cell within a DataPilot table, and is used to retrieve its metadata. The PositionType member specifies in which sub-area of the table the cell is positioned, which in turn determines the type of metadata contained in the PositionData member.
    
    **since**
    
        OOo 3.0

    See Also:
        `API DataPilotTablePositionData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotTablePositionData.html>`_
    """
    typeName: str = 'com.sun.star.sheet.DataPilotTablePositionData'

    def __init__(self, PositionType: typing.Optional[int] = ..., PositionData: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            PositionType (int, optional): PositionType value.
            PositionData (object, optional): PositionData value.
        """
        ...

    @property
    def PositionType(self) -> int:
        """
        This parameter specifies which sub-area of a DataPilot table a given cell is positioned.
        
        See DataPilotTablePositionType for how to interpret the value of this parameter.
        """
        ...
    @PositionType.setter
    def PositionType(self, value: int) -> None:
        ...
    @property
    def PositionData(self) -> object:
        """
        This member contains a structure of different types depending on the position type specified in PositionType member.
        
        When the value of PositionType is DataPilotTablePositionType.RESULT, DataPilotTablePositionData.PositionData contains an instance of type DataPilotTableResultData, whereas when the value of DataPilotTablePositionData.PositionType is either DataPilotTablePositionType.ROW_HEADER or DataPilotTablePositionType.COLUMN_HEADER, then the PositionData member contains an instance of type DataPilotTableHeaderData.
        """
        ...
    @PositionData.setter
    def PositionData(self, value: object) -> None:
        ...

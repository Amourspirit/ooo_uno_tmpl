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
# Namespace: com.sun.star.chart2.data
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class PivotTableFieldEntry(object):
    """
    Struct Class

    Pivot table field entry data.
    
    **since**
    
        LibreOffice 5.4

    See Also:
        `API PivotTableFieldEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1data_1_1PivotTableFieldEntry.html>`_
    """
    typeName: Literal['com.sun.star.chart2.data.PivotTableFieldEntry']

    def __init__(self, Name: typing.Optional[str] = ..., DimensionIndex: typing.Optional[int] = ..., DimensionPositionIndex: typing.Optional[int] = ..., HasHiddenMembers: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            DimensionIndex (int, optional): DimensionIndex value.
            DimensionPositionIndex (int, optional): DimensionPositionIndex value.
            HasHiddenMembers (bool, optional): HasHiddenMembers value.
        """


    @property
    def Name(self) -> str:
        """
        Name of the field entry.
        """


    @property
    def DimensionIndex(self) -> int:
        """
        The index of the field entry.
        """


    @property
    def DimensionPositionIndex(self) -> int:
        """
        The output position of the field entry in its field type.
        """


    @property
    def HasHiddenMembers(self) -> bool:
        """
        Does it have some members that are hidden (filtered).
        """



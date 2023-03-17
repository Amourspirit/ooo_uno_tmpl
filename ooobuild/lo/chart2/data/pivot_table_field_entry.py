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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
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
    __ooo_ns__: str = 'com.sun.star.chart2.data'
    __ooo_full_ns__: str = 'com.sun.star.chart2.data.PivotTableFieldEntry'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart2.data.PivotTableFieldEntry'
    """Literal Constant ``com.sun.star.chart2.data.PivotTableFieldEntry``"""

    def __init__(self, Name: typing.Optional[str] = '', DimensionIndex: typing.Optional[int] = 0, DimensionPositionIndex: typing.Optional[int] = 0, HasHiddenMembers: typing.Optional[bool] = False) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            DimensionIndex (int, optional): DimensionIndex value.
            DimensionPositionIndex (int, optional): DimensionPositionIndex value.
            HasHiddenMembers (bool, optional): HasHiddenMembers value.
        """
        super().__init__()

        if isinstance(Name, PivotTableFieldEntry):
            oth: PivotTableFieldEntry = Name
            self.Name = oth.Name
            self.DimensionIndex = oth.DimensionIndex
            self.DimensionPositionIndex = oth.DimensionPositionIndex
            self.HasHiddenMembers = oth.HasHiddenMembers
            return

        kargs = {
            "Name": Name,
            "DimensionIndex": DimensionIndex,
            "DimensionPositionIndex": DimensionPositionIndex,
            "HasHiddenMembers": HasHiddenMembers,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._dimension_index = kwargs["DimensionIndex"]
        self._dimension_position_index = kwargs["DimensionPositionIndex"]
        self._has_hidden_members = kwargs["HasHiddenMembers"]


    @property
    def Name(self) -> str:
        """
        Name of the field entry.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def DimensionIndex(self) -> int:
        """
        The index of the field entry.
        """
        return self._dimension_index
    
    @DimensionIndex.setter
    def DimensionIndex(self, value: int) -> None:
        self._dimension_index = value

    @property
    def DimensionPositionIndex(self) -> int:
        """
        The output position of the field entry in its field type.
        """
        return self._dimension_position_index
    
    @DimensionPositionIndex.setter
    def DimensionPositionIndex(self, value: int) -> None:
        self._dimension_position_index = value

    @property
    def HasHiddenMembers(self) -> bool:
        """
        Does it have some members that are hidden (filtered).
        """
        return self._has_hidden_members
    
    @HasHiddenMembers.setter
    def HasHiddenMembers(self, value: bool) -> None:
        self._has_hidden_members = value


__all__ = ['PivotTableFieldEntry']

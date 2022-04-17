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
# Namespace: com.sun.star.accessibility
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class AccessibleTableModelChange(object):
    """
    Struct Class

    This structure lets an event give access to a change of a table model.
    
    The data members of the AccessibleTableModelChange structure give access to the type and cell range of a change of a table model. See AccessibleTableModelChangeType for details of the change type. The range of the affected rows, columns, and/or cells can be obtained by accessing the other four data members.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleTableModelChange <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1accessibility_1_1AccessibleTableModelChange.html>`_
    """
    typeName: Literal['com.sun.star.accessibility.AccessibleTableModelChange']

    def __init__(self, Type: typing.Optional[int] = ..., FirstRow: typing.Optional[int] = ..., LastRow: typing.Optional[int] = ..., FirstColumn: typing.Optional[int] = ..., LastColumn: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Type (int, optional): Type value.
            FirstRow (int, optional): FirstRow value.
            LastRow (int, optional): LastRow value.
            FirstColumn (int, optional): FirstColumn value.
            LastColumn (int, optional): LastColumn value.
        """


    @property
    def Type(self) -> int:
        """
        The type of the event as defined in AccessibleTableModelChangeType.
        
        The model change either inserted or deleted one or more rows and/or columns or modified the content of a number of cells. See AccessibleTableModelChangeType for details of the type of the model change.
        """


    @property
    def FirstRow(self) -> int:
        """
        The lowest index of a row that has changed.
        
        The first row that has been changed or that contains modified cells.
        """


    @property
    def LastRow(self) -> int:
        """
        The highest index of a row that has changed.
        
        The last row that has been changed or that contains modified cells.
        """


    @property
    def FirstColumn(self) -> int:
        """
        The lowest index of a column that has changed.
        
        The first column that has been changed or contains modified cells.
        """


    @property
    def LastColumn(self) -> int:
        """
        The highest index of a column that has changed.
        
        The last column that has been changed or contains modified cells.
        """



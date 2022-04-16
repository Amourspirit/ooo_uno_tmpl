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
# Namespace: com.sun.star.awt.grid
# Libre Office Version: 7.3
from typing_extensions import Literal
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing


class GridColumnEvent(EventObject_a3d70b03):
    """
    Struct Class

    An event used by a XGridColumn to notify changes in the column.
    
    **since**
    
        OOo 3.3

    See Also:
        `API GridColumnEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1grid_1_1GridColumnEvent.html>`_
    """
    typeName: Literal['com.sun.star.awt.grid.GridColumnEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., AttributeName: typing.Optional[str] = ..., OldValue: typing.Optional[object] = ..., NewValue: typing.Optional[object] = ..., ColumnIndex: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            AttributeName (str, optional): AttributeName value.
            OldValue (object, optional): OldValue value.
            NewValue (object, optional): NewValue value.
            ColumnIndex (int, optional): ColumnIndex value.
        """


    @property
    def AttributeName(self) -> str:
        """
        Contains the name of the attributes whose value changed.
        """


    @property
    def OldValue(self) -> object:
        """
        Contains the old value.
        """


    @property
    def NewValue(self) -> object:
        """
        Contains the new value.
        """


    @property
    def ColumnIndex(self) -> int:
        """
        Contains the index of the changed column.
        """



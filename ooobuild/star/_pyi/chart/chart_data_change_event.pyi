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
# Namespace: com.sun.star.chart
# Libre Office Version: 7.3
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .chart_data_change_type import ChartDataChangeType as ChartDataChangeType_16cc0e6e


class ChartDataChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    describes a change that was applied to the data.

    See Also:
        `API ChartDataChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1ChartDataChangeEvent.html>`_
    """
    typeName: Literal['com.sun.star.chart.ChartDataChangeEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Type: typing.Optional[ChartDataChangeType_16cc0e6e] = ..., StartColumn: typing.Optional[int] = ..., EndColumn: typing.Optional[int] = ..., StartRow: typing.Optional[int] = ..., EndRow: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Type (ChartDataChangeType, optional): Type value.
            StartColumn (int, optional): StartColumn value.
            EndColumn (int, optional): EndColumn value.
            StartRow (int, optional): StartRow value.
            EndRow (int, optional): EndRow value.
        """


    @property
    def Type(self) -> ChartDataChangeType_16cc0e6e:
        """
        specifies the type of change to the data.
        """


    @property
    def StartColumn(self) -> int:
        """
        specifies the column number in which the changes begin.
        """


    @property
    def EndColumn(self) -> int:
        """
        specifies the column number in which the changes end.
        """


    @property
    def StartRow(self) -> int:
        """
        specifies the row number in which the changes begin.
        """


    @property
    def EndRow(self) -> int:
        """
        specifies the row number in which the changes end.
        """


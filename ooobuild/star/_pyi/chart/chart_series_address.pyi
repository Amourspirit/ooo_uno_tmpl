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
import typing


class ChartSeriesAddress(object):
    """
    Struct Class

    This structure describes a single data row, specified by its name and a sequence of data points.
    
    The cell addresses are in the format of the application that contains this chart.

    See Also:
        `API ChartSeriesAddress <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1ChartSeriesAddress.html>`_
    """
    typeName: Literal['com.sun.star.chart.ChartSeriesAddress']

    def __init__(self, DomainRangeAddresses: typing.Optional[typing.Tuple[str, ...]] = ..., DataRangeAddress: typing.Optional[str] = ..., LabelAddress: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            DomainRangeAddresses (typing.Tuple[str, ...], optional): DomainRangeAddresses value.
            DataRangeAddress (str, optional): DataRangeAddress value.
            LabelAddress (str, optional): LabelAddress value.
        """


    @property
    def DomainRangeAddresses(self) -> typing.Tuple[str, ...]:
        """
        contains cell addresses for each domain of this series.
        
        For XY (scatter) diagrams at least one series has a domain. Most of the other chart types use an empty sequence here.
        """


    @property
    def DataRangeAddress(self) -> str:
        """
        contains the cell range address of the data for this series.
        """


    @property
    def LabelAddress(self) -> str:
        """
        contains the cell address of label (i.e.
        
        name) of this series.
        """



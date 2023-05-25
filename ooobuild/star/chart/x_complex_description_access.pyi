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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart
from __future__ import annotations
import typing

from .x_chart_data_array import XChartDataArray as XChartDataArray_df4c0cdd


class XComplexDescriptionAccess(XChartDataArray_df4c0cdd):
    """
    Offers access to complex column and row descriptions.
    
    Can be obtained from interface XChartDocument via method getData().
    
    **since**
    
        OOo 3.3

    See Also:
        `API XComplexDescriptionAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart_1_1XComplexDescriptionAccess.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.chart.XComplexDescriptionAccess'

    def getComplexColumnDescriptions(self) -> typing.Tuple[typing.Tuple[str, ...], ...]:
        """
        retrieves the description texts for all columns.
        """
        ...
    def getComplexRowDescriptions(self) -> typing.Tuple[typing.Tuple[str, ...], ...]:
        """
        retrieves the description texts for all rows.
        """
        ...
    def setComplexColumnDescriptions(self, rColumnDescriptions: typing.Tuple[typing.Tuple[str, ...], ...]) -> None:
        """
        sets the description texts for all columns.
        """
        ...
    def setComplexRowDescriptions(self, rRowDescriptions: typing.Tuple[typing.Tuple[str, ...], ...]) -> None:
        """
        sets the description texts for all rows.
        """
        ...




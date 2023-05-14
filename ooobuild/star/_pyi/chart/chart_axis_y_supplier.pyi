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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart
from .x_axis_y_supplier import XAxisYSupplier as XAxisYSupplier_d4430cb4

class ChartAxisYSupplier(XAxisYSupplier_d4430cb4):
    """
    Service Class

    A helper service for the y-axis.

    See Also:
        `API ChartAxisYSupplier <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartAxisYSupplier.html>`_
    """
    @property
    def HasYAxis(self) -> bool:
        """
        Determines if the y-axis is shown or hidden.
        """
        ...
    @HasYAxis.setter
    def HasYAxis(self, value: bool) -> None:
        ...
    @property
    def HasYAxisDescription(self) -> bool:
        """
        Determines if the description of the y-axis is shown or hidden.
        """
        ...
    @HasYAxisDescription.setter
    def HasYAxisDescription(self, value: bool) -> None:
        ...
    @property
    def HasYAxisGrid(self) -> bool:
        """
        Determines if the major grid of the y-axis is shown or hidden.
        """
        ...
    @HasYAxisGrid.setter
    def HasYAxisGrid(self, value: bool) -> None:
        ...
    @property
    def HasYAxisHelpGrid(self) -> bool:
        """
        Determines if the minor grid of the y-axis is shown or hidden.
        """
        ...
    @HasYAxisHelpGrid.setter
    def HasYAxisHelpGrid(self, value: bool) -> None:
        ...
    @property
    def HasYAxisTitle(self) -> bool:
        """
        Determines if the title of the y-axis is shown or hidden.
        """
        ...
    @HasYAxisTitle.setter
    def HasYAxisTitle(self, value: bool) -> None:
        ...


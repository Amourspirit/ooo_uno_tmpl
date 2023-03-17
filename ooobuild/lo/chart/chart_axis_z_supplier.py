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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart
from abc import abstractproperty
from .x_axis_z_supplier import XAxisZSupplier as XAxisZSupplier_d44c0cb5

class ChartAxisZSupplier(XAxisZSupplier_d44c0cb5):
    """
    Service Class

    A helper service for chart documents which supply a z-axis.

    See Also:
        `API ChartAxisZSupplier <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartAxisZSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartAxisZSupplier'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def HasZAxis(self) -> bool:
        """
        Determines if the z-axis is shown or hidden.
        """
        ...

    @abstractproperty
    def HasZAxisDescription(self) -> bool:
        """
        Determines if the description of the z-axis is shown or hidden.
        """
        ...

    @abstractproperty
    def HasZAxisGrid(self) -> bool:
        """
        Determines if the major grid of the z-axis is shown or hidden.
        """
        ...

    @abstractproperty
    def HasZAxisHelpGrid(self) -> bool:
        """
        Determines if the minor grid of the z-axis is shown or hidden.
        """
        ...

    @abstractproperty
    def HasZAxisTitle(self) -> bool:
        """
        Determines if the title of the z-axis is shown or hidden.
        """
        ...



__all__ = ['ChartAxisZSupplier']


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
# Namespace: com.sun.star.chart2
from abc import abstractproperty
from .x_chart_type_container import XChartTypeContainer as XChartTypeContainer_23c30edb
from .x_coordinate_system import XCoordinateSystem as XCoordinateSystem_7ff0e31
from ..util.x_cloneable import XCloneable as XCloneable_99d00aa3

class CoordinateSystem(XChartTypeContainer_23c30edb, XCoordinateSystem_7ff0e31, XCloneable_99d00aa3):
    """
    Service Class


    See Also:
        `API CoordinateSystem <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1CoordinateSystem.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.CoordinateSystem'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def SwapXAndYAxis(self) -> bool:
        """
        """
        ...



__all__ = ['CoordinateSystem']


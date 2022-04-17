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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.chart
from typing_extensions import Literal


class ChartSolidType:
    """
    Const Class

    These values specify the type of solid shapes for data points of 3D bar charts.

    See Also:
        `API ChartSolidType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart_1_1ChartSolidType.html>`_
    """
    RECTANGULAR_SOLID: Literal[0]
    """
    extruded rectangle, i.e., a cuboid
    """
    CYLINDER: Literal[1]
    """
    cylinder with a circle as base
    """
    CONE: Literal[2]
    """
    cone with a circle as base
    """
    PYRAMID: Literal[3]
    """
    pyramidal with a square as base
    """

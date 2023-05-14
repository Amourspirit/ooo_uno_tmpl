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
# Namespace: com.sun.star.chart2
from .x_scaling import XScaling as XScaling_97500a65

class LinearScaling(XScaling_97500a65):
    """
    Service Class

    Scaling that scales a value x by calculating m ⋅ x + t.
    
    If not mentioned explicitly, the parameter m is 1.0 and t is 0.0, which means the transformation is an identical mapping.

    See Also:
        `API LinearScaling <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1LinearScaling.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.LinearScaling'
    __ooo_type_name__: str = 'service'


__all__ = ['LinearScaling']


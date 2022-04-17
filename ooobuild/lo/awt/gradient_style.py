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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 7.3
from enum import Enum


class GradientStyle(Enum):
    """
    Enum Class

    

    See Also:
        `API GradientStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#aa6b9d577a1700f29923f49f7b77d165f>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.GradientStyle'
    __ooo_type_name__: str = 'enum'

    AXIAL = 'AXIAL'
    """
    specifies an axial gradient.
    """
    ELLIPTICAL = 'ELLIPTICAL'
    """
    specifies an elliptical gradient.
    """
    LINEAR = 'LINEAR'
    """
    specifies a linear gradient.
    """
    RADIAL = 'RADIAL'
    """
    specifies a radial gradient.
    """
    RECT = 'RECT'
    """
    specifies a gradient in the shape of a rectangle.
    """
    SQUARE = 'SQUARE'
    """
    specifies a gradient in the shape of a square.
    """

__all__ = ['GradientStyle']

# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.geometry
# Libre Office Version: 2024.2
import typing


class RealSize2D(object):
    """
    Struct Class

    This structure contains data representing a two-dimensional size.
    
    The data is stored real-valued.
    
    **since**
    
        OOo 2.0

    See Also:
        `API RealSize2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1RealSize2D.html>`_
    """
    typeName: str = 'com.sun.star.geometry.RealSize2D'

    def __init__(self, Width: typing.Optional[float] = ..., Height: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            Width (float, optional): Width value.
            Height (float, optional): Height value.
        """
        ...

    @property
    def Width(self) -> float:
        """
        Amount of space occupied in the x direction.
        """
        ...
    @Width.setter
    def Width(self, value: float) -> None:
        ...
    @property
    def Height(self) -> float:
        """
        Amount of space occupied in the y direction.
        """
        ...
    @Height.setter
    def Height(self, value: float) -> None:
        ...


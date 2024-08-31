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
# Namespace: com.sun.star.drawing
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .position3_d import Position3D as Position3D_bddc0bc0


class BoundVolume(object):
    """
    Struct Class

    specifies a three-dimensional boundary volume with two positions.

    See Also:
        `API BoundVolume <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1BoundVolume.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.BoundVolume'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.BoundVolume'
    """Literal Constant ``com.sun.star.drawing.BoundVolume``"""

    def __init__(self, min: typing.Optional[Position3D_bddc0bc0] = UNO_NONE, max: typing.Optional[Position3D_bddc0bc0] = UNO_NONE) -> None:
        """
        Constructor

        Arguments:
            min (Position3D, optional): min value.
            max (Position3D, optional): max value.
        """
        super().__init__()

        if isinstance(min, BoundVolume):
            oth: BoundVolume = min
            self.min = oth.min
            self.max = oth.max
            return

        kargs = {
            "min": min,
            "max": max,
        }
        if kargs["min"] is UNO_NONE:
            kargs["min"] = None
        if kargs["max"] is UNO_NONE:
            kargs["max"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._min = kwargs["min"]
        self._max = kwargs["max"]


    @property
    def min(self) -> Position3D_bddc0bc0:
        """
        this is the minimum position inside the boundary volume.
        """
        return self._min

    @min.setter
    def min(self, value: Position3D_bddc0bc0) -> None:
        self._min = value

    @property
    def max(self) -> Position3D_bddc0bc0:
        """
        this is the maximum position inside the boundary volume.
        """
        return self._max

    @max.setter
    def max(self, value: Position3D_bddc0bc0) -> None:
        self._max = value


__all__ = ['BoundVolume']

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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing


class Direction3D(object):
    """
    Struct Class

    specifies a 3-dimensional vector.

    See Also:
        `API Direction3D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1Direction3D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.Direction3D'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.Direction3D'
    """Literal Constant ``com.sun.star.drawing.Direction3D``"""

    def __init__(self, DirectionX: typing.Optional[float] = 0.0, DirectionY: typing.Optional[float] = 0.0, DirectionZ: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            DirectionX (float, optional): DirectionX value.
            DirectionY (float, optional): DirectionY value.
            DirectionZ (float, optional): DirectionZ value.
        """
        super().__init__()

        if isinstance(DirectionX, Direction3D):
            oth: Direction3D = DirectionX
            self.DirectionX = oth.DirectionX
            self.DirectionY = oth.DirectionY
            self.DirectionZ = oth.DirectionZ
            return

        kargs = {
            "DirectionX": DirectionX,
            "DirectionY": DirectionY,
            "DirectionZ": DirectionZ,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._direction_x = kwargs["DirectionX"]
        self._direction_y = kwargs["DirectionY"]
        self._direction_z = kwargs["DirectionZ"]


    @property
    def DirectionX(self) -> float:
        return self._direction_x
    
    @DirectionX.setter
    def DirectionX(self, value: float) -> None:
        self._direction_x = value

    @property
    def DirectionY(self) -> float:
        return self._direction_y
    
    @DirectionY.setter
    def DirectionY(self, value: float) -> None:
        self._direction_y = value

    @property
    def DirectionZ(self) -> float:
        return self._direction_z
    
    @DirectionZ.setter
    def DirectionZ(self, value: float) -> None:
        self._direction_z = value


__all__ = ['Direction3D']

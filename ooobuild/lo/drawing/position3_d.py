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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class Position3D(object):
    """
    Struct Class

    specifies a 3-dimensional point.

    See Also:
        `API Position3D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1Position3D.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.Position3D'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.Position3D'
    """Literal Constant ``com.sun.star.drawing.Position3D``"""

    def __init__(self, PositionX: typing.Optional[float] = 0.0, PositionY: typing.Optional[float] = 0.0, PositionZ: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            PositionX (float, optional): PositionX value.
            PositionY (float, optional): PositionY value.
            PositionZ (float, optional): PositionZ value.
        """
        super().__init__()

        if isinstance(PositionX, Position3D):
            oth: Position3D = PositionX
            self.PositionX = oth.PositionX
            self.PositionY = oth.PositionY
            self.PositionZ = oth.PositionZ
            return

        kargs = {
            "PositionX": PositionX,
            "PositionY": PositionY,
            "PositionZ": PositionZ,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._position_x = kwargs["PositionX"]
        self._position_y = kwargs["PositionY"]
        self._position_z = kwargs["PositionZ"]


    @property
    def PositionX(self) -> float:
        """
        the position on the X-Axis in the 3D room in 100th of millimeters
        """
        return self._position_x
    
    @PositionX.setter
    def PositionX(self, value: float) -> None:
        self._position_x = value

    @property
    def PositionY(self) -> float:
        """
        the position on the Y-Axis in the 3D room in 100th of millimeters
        """
        return self._position_y
    
    @PositionY.setter
    def PositionY(self, value: float) -> None:
        self._position_y = value

    @property
    def PositionZ(self) -> float:
        """
        the position on the Z-Axis in the 3D room in 100th of millimeters
        """
        return self._position_z
    
    @PositionZ.setter
    def PositionZ(self, value: float) -> None:
        self._position_z = value


__all__ = ['Position3D']

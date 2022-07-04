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
from .flag_sequence_sequence import FlagSequenceSequence as FlagSequenceSequence_49130fe0
from .point_sequence_sequence import PointSequenceSequence as PointSequenceSequence_5c591070


class PolyPolygonBezierCoords(object):
    """
    Struct Class

    specifies the coordinates for a poly polygon Bezier.

    See Also:
        `API PolyPolygonBezierCoords <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1PolyPolygonBezierCoords.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.PolyPolygonBezierCoords'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.drawing.PolyPolygonBezierCoords'
    """Literal Constant ``com.sun.star.drawing.PolyPolygonBezierCoords``"""

    def __init__(self, Coordinates: typing.Optional[PointSequenceSequence_5c591070] = PointSequenceSequence_5c591070(()), Flags: typing.Optional[FlagSequenceSequence_49130fe0] = FlagSequenceSequence_49130fe0(())) -> None:
        """
        Constructor

        Arguments:
            Coordinates (PointSequenceSequence, optional): Coordinates value.
            Flags (FlagSequenceSequence, optional): Flags value.
        """
        super().__init__()

        if isinstance(Coordinates, PolyPolygonBezierCoords):
            oth: PolyPolygonBezierCoords = Coordinates
            self.Coordinates = oth.Coordinates
            self.Flags = oth.Flags
            return

        kargs = {
            "Coordinates": Coordinates,
            "Flags": Flags,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._coordinates = kwargs["Coordinates"]
        self._flags = kwargs["Flags"]


    @property
    def Coordinates(self) -> PointSequenceSequence_5c591070:
        return self._coordinates
    
    @Coordinates.setter
    def Coordinates(self, value: PointSequenceSequence_5c591070) -> None:
        self._coordinates = value

    @property
    def Flags(self) -> FlagSequenceSequence_49130fe0:
        return self._flags
    
    @Flags.setter
    def Flags(self, value: FlagSequenceSequence_49130fe0) -> None:
        self._flags = value


__all__ = ['PolyPolygonBezierCoords']

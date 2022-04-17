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
from typing_extensions import Literal
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
    typeName: Literal['com.sun.star.drawing.PolyPolygonBezierCoords']

    def __init__(self, Coordinates: typing.Optional[PointSequenceSequence_5c591070] = ..., Flags: typing.Optional[FlagSequenceSequence_49130fe0] = ...) -> None:
        """
        Constructor

        Arguments:
            Coordinates (PointSequenceSequence, optional): Coordinates value.
            Flags (FlagSequenceSequence, optional): Flags value.
        """


    @property
    def Coordinates(self) -> PointSequenceSequence_5c591070:
        ...


    @property
    def Flags(self) -> FlagSequenceSequence_49130fe0:
        ...



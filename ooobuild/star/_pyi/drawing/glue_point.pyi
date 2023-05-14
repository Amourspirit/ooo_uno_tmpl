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
from ..awt.point import Point as Point_5fb2085e


class GluePoint(object):
    """
    Struct Class

    A GluePoint could be attached to a shape or to a page.
    
    If a GluePoint is attached to a shape, it is moved when the shape moves. The ends of connectors can be attached to GluePoint.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API GluePoint <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1GluePoint.html>`_
    """
    typeName: Literal['com.sun.star.drawing.GluePoint']

    def __init__(self, Position: typing.Optional[Point_5fb2085e] = ..., EscapeDirection: typing.Optional[int] = ..., PositionAbsolute: typing.Optional[bool] = ..., Alignment: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Position (Point, optional): Position value.
            EscapeDirection (int, optional): EscapeDirection value.
            PositionAbsolute (bool, optional): PositionAbsolute value.
            Alignment (int, optional): Alignment value.
        """
        ...


    @property
    def Position(self) -> Point_5fb2085e:
        """
        This is the position of this GluePoint.
        """
        ...

    @Position.setter
    def Position(self, value: Point_5fb2085e) -> None:
        ...

    @property
    def EscapeDirection(self) -> int:
        """
        This is the direction in which the connector line leaves the GluePoint.
        """
        ...

    @EscapeDirection.setter
    def EscapeDirection(self, value: int) -> None:
        ...

    @property
    def PositionAbsolute(self) -> bool:
        """
        If this is TRUE, then the position of this GluePoint is absolute on a page and is not relative to a shape.
        """
        ...

    @PositionAbsolute.setter
    def PositionAbsolute(self, value: bool) -> None:
        ...

    @property
    def Alignment(self) -> int:
        """
        The alignment of a GluePoint defines how the position of the point is affected by resizing the parent Shape.
        """
        ...

    @Alignment.setter
    def Alignment(self, value: int) -> None:
        ...


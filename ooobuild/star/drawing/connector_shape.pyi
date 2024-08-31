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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
from __future__ import annotations
import typing
from .connector_properties import ConnectorProperties as ConnectorProperties_3c5e0fcc
from .line_properties import LineProperties as LineProperties_f13f0da9
from .rotation_descriptor import RotationDescriptor as RotationDescriptor_2cec0f63
from .shadow_properties import ShadowProperties as ShadowProperties_e350e87
from .shape import Shape as Shape_85cc09e5
from .text import Text as Text_7c140999
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from .x_shape import XShape as XShape_8fd00a3d

class ConnectorShape(ConnectorProperties_3c5e0fcc, LineProperties_f13f0da9, RotationDescriptor_2cec0f63, ShadowProperties_e350e87, Shape_85cc09e5, Text_7c140999):
    """
    Service Class

    This service is for a ConnectorShape, a specialized Shape, which can be connected to other Shapes or GluePoints.

    See Also:
        `API ConnectorShape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1ConnectorShape.html>`_
    """
    @property
    def EdgeLine1Delta(self) -> int:
        """
        This property contains the distance of line 1.
        """
        ...
    @EdgeLine1Delta.setter
    def EdgeLine1Delta(self, value: int) -> None:
        ...
    @property
    def EdgeLine2Delta(self) -> int:
        """
        This property contains the distance of line 2.
        """
        ...
    @EdgeLine2Delta.setter
    def EdgeLine2Delta(self, value: int) -> None:
        ...
    @property
    def EdgeLine3Delta(self) -> int:
        """
        This property contains the distance of line 3.
        """
        ...
    @EdgeLine3Delta.setter
    def EdgeLine3Delta(self, value: int) -> None:
        ...
    @property
    def EndGluePointIndex(self) -> int:
        """
        this is the position of the connectors end point in 100th/mm.
        
        For unconnected end points you can get and set the position. For connected end points you can only get the position.
        """
        ...
    @EndGluePointIndex.setter
    def EndGluePointIndex(self, value: int) -> None:
        ...
    @property
    def EndPosition(self) -> Point_5fb2085e:
        """
        this property holds the index of the gluepoint the end point of this connector is glued on.
        """
        ...
    @EndPosition.setter
    def EndPosition(self, value: Point_5fb2085e) -> None:
        ...
    @property
    def EndShape(self) -> XShape_8fd00a3d:
        """
        this property either holds the shape that the end point of this connector is connected to, or is empty when the end point of the connector is not connected to a shape.
        """
        ...
    @EndShape.setter
    def EndShape(self, value: XShape_8fd00a3d) -> None:
        ...
    @property
    def StartGluePointIndex(self) -> int:
        """
        this property holds the index of the gluepoint the start point of this connector is glued on.
        """
        ...
    @StartGluePointIndex.setter
    def StartGluePointIndex(self, value: int) -> None:
        ...
    @property
    def StartPosition(self) -> Point_5fb2085e:
        """
        this is the position of the connectors start point in 100th/mm.
        
        For unconnected start points you can get and set the position. For connected start points you can only get the position.
        """
        ...
    @StartPosition.setter
    def StartPosition(self, value: Point_5fb2085e) -> None:
        ...
    @property
    def StartShape(self) -> XShape_8fd00a3d:
        """
        this property either holds the shape that the start point of this connector is connected to, or is empty when the start point of the connector is not connected to a shape.
        """
        ...
    @StartShape.setter
    def StartShape(self, value: XShape_8fd00a3d) -> None:
        ...


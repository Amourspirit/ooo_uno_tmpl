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
# Namespace: com.sun.star.drawing
from __future__ import annotations
from abc import ABC

class RotationDescriptor(ABC):
    """
    Service Class

    This abstract service specifies the general characteristics of an optional rotation and shearing for a Shape.
    
    This service is deprecated, instead please use the Transformation property of the service Shape.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API RotationDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1RotationDescriptor.html>`_
    """
    @property
    def RotateAngle(self) -> int:
        """
        This is the angle for rotation of this Shape.
        
        The shape is rotated counter-clockwise around the center of the bounding box.
        
        This property contains an error, the rotation angle is mathematically inverted when You take into account that the Y-Axis of the coordinate system is pointing down. Please use the Transformation property of the service Shape instead.
        """
        ...
    @RotateAngle.setter
    def RotateAngle(self, value: int) -> None:
        ...
    @property
    def ShearAngle(self) -> int:
        """
        This is the amount of shearing for this Shape.
        
        The shape is sheared counter-clockwise around the center of the bounding box
        """
        ...
    @ShearAngle.setter
    def ShearAngle(self, value: int) -> None:
        ...


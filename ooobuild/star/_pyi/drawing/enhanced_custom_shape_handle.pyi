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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.drawing
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .enhanced_custom_shape_parameter import EnhancedCustomShapeParameter as EnhancedCustomShapeParameter_d6171317
    from .enhanced_custom_shape_parameter_pair import EnhancedCustomShapeParameterPair as EnhancedCustomShapeParameterPair_262914a3

class EnhancedCustomShapeHandle(ABC):
    """
    Service Class

    This service may be represented by a com.sun.star.beans.PropertyValue [].

    See Also:
        `API EnhancedCustomShapeHandle <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeHandle.html>`_
    """
    @property
    def MirroredX(self) -> bool:
        """
        Specifies if the x position of the handle is mirrored.
        """
        ...

    @MirroredX.setter
    def MirroredX(self, value: bool) -> None:
        ...
    @property
    def MirroredY(self) -> bool:
        """
        Specifies if the y position of the handle is mirrored.
        """
        ...

    @MirroredY.setter
    def MirroredY(self, value: bool) -> None:
        ...
    @property
    def Polar(self) -> 'EnhancedCustomShapeParameterPair_262914a3':
        """
        If this attribute is set, the handle is a polar handle.
        
        The property specifies the center position of the handle. If this attribute is set, the attributes RangeX and RangeY are ignored, instead the attribute RadiusRange is used.
        """
        ...

    @Polar.setter
    def Polar(self, value: 'EnhancedCustomShapeParameterPair_262914a3') -> None:
        ...
    @property
    def Position(self) -> 'EnhancedCustomShapeParameterPair_262914a3':
        """
        If the property Polar is set, then the first value specifies the radius and the second parameter the angle of the handle.
        
        Otherwise, if the handle is not polar, the first parameter specifies the horizontal handle position, the vertical handle position is described by the second parameter.
        """
        ...

    @Position.setter
    def Position(self, value: 'EnhancedCustomShapeParameterPair_262914a3') -> None:
        ...
    @property
    def RadiusRangeMaximum(self) -> 'EnhancedCustomShapeParameter_d6171317':
        """
        If this attribute is set, it specifies the maximum radius range that can be used for a polar handle.
        """
        ...

    @RadiusRangeMaximum.setter
    def RadiusRangeMaximum(self, value: 'EnhancedCustomShapeParameter_d6171317') -> None:
        ...
    @property
    def RadiusRangeMinimum(self) -> 'EnhancedCustomShapeParameter_d6171317':
        """
        If this attribute is set, it specifies the minimum radius range that can be used for a polar handle.
        """
        ...

    @RadiusRangeMinimum.setter
    def RadiusRangeMinimum(self, value: 'EnhancedCustomShapeParameter_d6171317') -> None:
        ...
    @property
    def RangeXMaximum(self) -> 'EnhancedCustomShapeParameter_d6171317':
        """
        If the attribute RangeXMaximum is set, it specifies the horizontal maximum range of the handle.
        """
        ...

    @RangeXMaximum.setter
    def RangeXMaximum(self, value: 'EnhancedCustomShapeParameter_d6171317') -> None:
        ...
    @property
    def RangeXMinimum(self) -> 'EnhancedCustomShapeParameter_d6171317':
        """
        If the attribute RangeXMinimum is set, it specifies the horizontal minimum range of the handle.
        """
        ...

    @RangeXMinimum.setter
    def RangeXMinimum(self, value: 'EnhancedCustomShapeParameter_d6171317') -> None:
        ...
    @property
    def RangeYMaximum(self) -> 'EnhancedCustomShapeParameter_d6171317':
        """
        If the attribute RangeYMaximum is set, it specifies the vertical maximum range of the handle.
        """
        ...

    @RangeYMaximum.setter
    def RangeYMaximum(self, value: 'EnhancedCustomShapeParameter_d6171317') -> None:
        ...
    @property
    def RangeYMinimum(self) -> 'EnhancedCustomShapeParameter_d6171317':
        """
        If the attribute RangeYMinimum is set, it specifies the vertical minimum range of the handle.
        """
        ...

    @RangeYMinimum.setter
    def RangeYMinimum(self, value: 'EnhancedCustomShapeParameter_d6171317') -> None:
        ...
    @property
    def RefAngle(self) -> int:
        """
        RefAngle, if this attribute is set, it specifies the index of the adjustment value which is connected to the angle of the handle.
        """
        ...

    @RefAngle.setter
    def RefAngle(self, value: int) -> None:
        ...
    @property
    def RefR(self) -> int:
        """
        RefR, if this attribute is set, it specifies the index of the adjustment value which is connected to the radius of the handle.
        """
        ...

    @RefR.setter
    def RefR(self, value: int) -> None:
        ...
    @property
    def RefX(self) -> int:
        """
        RefX, if this attribute is set, it specifies the index of the adjustment value which is connected to the horizontal position of the handle.
        """
        ...

    @RefX.setter
    def RefX(self, value: int) -> None:
        ...
    @property
    def RefY(self) -> int:
        """
        RefY, if this attribute is set, it specifies the index of the adjustment value which is connected to the vertical position of the handle.
        """
        ...

    @RefY.setter
    def RefY(self, value: int) -> None:
        ...
    @property
    def Switched(self) -> bool:
        """
        Specifies if the handle directions are swapped if the shape is taller than wide.
        """
        ...

    @Switched.setter
    def Switched(self, value: bool) -> None:
        ...


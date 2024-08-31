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
from abc import abstractproperty, ABC
if typing.TYPE_CHECKING:
    from com.sun.star.drawing.MeasureKind import MeasureKindProto  # type: ignore
    from com.sun.star.drawing.MeasureTextHorzPos import MeasureTextHorzPosProto  # type: ignore
    from com.sun.star.drawing.MeasureTextVertPos import MeasureTextVertPosProto  # type: ignore

class MeasureProperties(ABC):
    """
    Service Class

    This service describes a MeasureShape.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API MeasureProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1MeasureProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.MeasureProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def MeasureBelowReferenceEdge(self) -> bool:
        """
        If this property is TRUE, the measure is drawn below the reference edge instead of above it.
        """
        ...

    @abstractproperty
    def MeasureDecimalPlaces(self) -> int:
        """
        This value is the number of decimal places that is used to format the measure value.
        
        **since**
        
            OOo 1.1.2
        """
        ...

    @abstractproperty
    def MeasureHelpLine1Length(self) -> int:
        """
        This is the length of the first help line.
        """
        ...

    @abstractproperty
    def MeasureHelpLine2Length(self) -> int:
        """
        This is the length of the second help line.
        """
        ...

    @abstractproperty
    def MeasureHelpLineDistance(self) -> int:
        """
        This is the distance from the measure line to the start of the help lines.
        """
        ...

    @abstractproperty
    def MeasureHelpLineOverhang(self) -> int:
        """
        This is the overhang of the two help lines.
        """
        ...

    @abstractproperty
    def MeasureKind(self) -> MeasureKindProto:
        """
        This enumeration specifies the MeasureKind.
        """
        ...

    @abstractproperty
    def MeasureLineDistance(self) -> int:
        """
        This is the distance from the reference edge to the measure line.
        """
        ...

    @abstractproperty
    def MeasureOverhang(self) -> int:
        """
        This is the overhang of the reference line over the help lines.
        """
        ...

    @abstractproperty
    def MeasureShowUnit(self) -> bool:
        """
        If this is TRUE, the unit of measure is shown in the measure text.
        """
        ...

    @abstractproperty
    def MeasureTextAutoAngle(self) -> bool:
        """
        If this is TRUE, the angle of the measure is set automatically.
        """
        ...

    @abstractproperty
    def MeasureTextAutoAngleView(self) -> int:
        """
        This is the automatic angle.
        """
        ...

    @abstractproperty
    def MeasureTextFixedAngle(self) -> int:
        """
        This is the fixed angle.
        """
        ...

    @abstractproperty
    def MeasureTextHorizontalPosition(self) -> MeasureTextHorzPosProto:
        """
        This is the horizontal position of the measure text.
        """
        ...

    @abstractproperty
    def MeasureTextIsFixedAngle(self) -> bool:
        """
        If this value is TRUE, the measure has a fixed angle.
        """
        ...

    @abstractproperty
    def MeasureTextRotate90(self) -> bool:
        """
        If this value is TRUE, the text is rotated 90 degrees.
        """
        ...

    @abstractproperty
    def MeasureTextUpsideDown(self) -> bool:
        """
        If this value is TRUE, the text is printed upside down.
        """
        ...

    @abstractproperty
    def MeasureTextVerticalPosition(self) -> MeasureTextVertPosProto:
        """
        This is the vertical position of the text.
        """
        ...


__all__ = ['MeasureProperties']
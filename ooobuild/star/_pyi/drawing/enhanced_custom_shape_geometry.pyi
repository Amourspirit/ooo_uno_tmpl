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
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from .enhanced_custom_shape_adjustment_value import EnhancedCustomShapeAdjustmentValue as EnhancedCustomShapeAdjustmentValue_517b1592

class EnhancedCustomShapeGeometry(ABC):
    """
    Service Class

    This service may be represented by a com.sun.star.beans.PropertyValue [].

    See Also:
        `API EnhancedCustomShapeGeometry <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeGeometry.html>`_
    """
    @property
    def AdjustmentValues(self) -> 'typing.Tuple[EnhancedCustomShapeAdjustmentValue_517b1592, ...]':
        """
        This property specifies a sequence of Adjustment values.
        """
    @property
    def Equations(self) -> 'typing.Tuple[str, ...]':
        """
        This property is describing the equations that are used, each equation can be referenced by com.sun.star.drawing.EnhancedCustomShapeParameter which are often used in Path, Extrusion and or Handle descriptions.
        """
    @property
    def Extrusion(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        This property sequence is including the extrusion description, the properties are as same as specified in the service com.sun.star:drawing.EnhancedCustomShapeExtrusion.
        """
    @property
    def Handles(self) -> 'typing.Tuple[PropertyValues_d6470ce6, ...]':
        """
        This property is describing the interaction handles that are used, each inner property sequence is having the same properties as they are specified in the service com.sun.star:drawing.EnhancedCustomShapeHandle.
        """
    @property
    def Path(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        This property sequence is including the path description, the properties are as same as specified in the service com.sun.star:drawing.EnhancedCustomShapePath.
        """
    @property
    def TextPath(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        This property sequence is including the text path description, the properties are as same as specified in the service com.sun.star:drawing.EnhancedCustomShapeTextPath.
        """
    @property
    def MirroredX(self) -> bool:
        """
        This property specifies if the orientation of the shape is horizontal mirrored.
        """
    @property
    def MirroredY(self) -> bool:
        """
        This property specifies if the orientation of the shape is vertical mirrored.
        """
    @property
    def TextRotateAngle(self) -> float:
        """
        This property specifies the text rotation angle in degrees.
        
        The text rotation is added to the shape geometry rotation.
        """
    @property
    def Type(self) -> str:
        """
        The Type attribute contains the name of a shape type.
        
        This name can be used to offer specialized user interfaces for certain classes of shapes, like for arrows, smileys, etc. The shape type is rendering engine dependent and does not influence the geometry of the shape. If the value of the draw:type attribute is non-primitive, then no shape type is available.
        """
    @property
    def ViewBox(self) -> 'Rectangle_84b109e9':
        """
        This property describes the user space of the shape in its canonical form.
        """



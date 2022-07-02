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
# Libre Office Version: 7.2
# Namespace: com.sun.star.drawing
import typing
from abc import abstractproperty
from .fill_properties import FillProperties as FillProperties_f1200da8
from .line_properties import LineProperties as LineProperties_f13f0da9
from .rotation_descriptor import RotationDescriptor as RotationDescriptor_2cec0f63
from .shadow_properties import ShadowProperties as ShadowProperties_e350e87
from .shape import Shape as Shape_85cc09e5
from .text import Text as Text_7c140999
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class CustomShape(FillProperties_f1200da8, LineProperties_f13f0da9, RotationDescriptor_2cec0f63, ShadowProperties_e350e87, Shape_85cc09e5, Text_7c140999):
    """
    Service Class

    This service is for a CustomShape.

    See Also:
        `API CustomShape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1CustomShape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.CustomShape'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CustomShapeGeometry(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        This property describes the geometry of the CustomShape.
        
        The CustomShapeEngine that is used should be able to get on with the content of this property.
        
        If the CustomShapeEngine property is \"com.sun.star.drawing.EnhancedCustomShapeEngine\", then this property is containing properties as they are specified in the service com.sun.star.drawing.EnhancedCustomShapeGeometry
        """
        ...

    @abstractproperty
    def CustomShapeData(self) -> str:
        """
        This property can be used to store data that the CustomShapeEngine may use for rendering.
        """
        ...

    @abstractproperty
    def CustomShapeEngine(self) -> str:
        """
        This property contains the CustomShapeEngine service name that has to be used for rendering.
        """
        ...

    @abstractproperty
    def CustomShapeReplacementURL(self) -> str:
        """
        This property describes the URL to a replacement graphic that could be displayed if the CustomShape engine is not available.
        """
        ...



__all__ = ['CustomShape']


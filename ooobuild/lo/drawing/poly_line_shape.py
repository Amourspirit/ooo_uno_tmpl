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
from .line_properties import LineProperties as LineProperties_f13f0da9
from .poly_polygon_descriptor import PolyPolygonDescriptor as PolyPolygonDescriptor_5d38109f
from .rotation_descriptor import RotationDescriptor as RotationDescriptor_2cec0f63
from .shadow_properties import ShadowProperties as ShadowProperties_e350e87
from .shape import Shape as Shape_85cc09e5
from .text import Text as Text_7c140999

class PolyLineShape(LineProperties_f13f0da9, PolyPolygonDescriptor_5d38109f, RotationDescriptor_2cec0f63, ShadowProperties_e350e87, Shape_85cc09e5, Text_7c140999):
    """
    Service Class

    This service is for a polyline shape.
    
    A polyline has one or more straight lines.

    See Also:
        `API PolyLineShape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1PolyLineShape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.PolyLineShape'
    __ooo_type_name__: str = 'service'



__all__ = ['PolyLineShape']


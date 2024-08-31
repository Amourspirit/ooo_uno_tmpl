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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.rendering
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..geometry.real_point2_d import RealPoint2D as RealPoint2D_d6e70c78
    from .color_component import ColorComponent as ColorComponent_e4c0e78
    from .x_color_space import XColorSpace as XColorSpace_e3940d09
    from .x_poly_polygon2_d import XPolyPolygon2D as XPolyPolygon2D_e1b0e20


class XParametricPolyPolygon2D(XInterface_8f010a43):
    """
    Interface to a dynamic poly-polygon generator, that generates poly-polygons depending on a given parameter value.
    
    The returned poly-polygon should normally be contained in the [0,1]x[0,1] rectangle. At least that is the dimension expected at other places. e.g. Texture.

    See Also:
        `API XParametricPolyPolygon2D <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XParametricPolyPolygon2D.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.rendering.XParametricPolyPolygon2D'

    def getColor(self, t: float) -> typing.Tuple[ColorComponent_e4c0e78, ...]:
        """
        Query the color value for the polygonal area at the specified parameter value.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getColorSpace(self) -> XColorSpace_e3940d09:
        """
        Query the color space employed by this object.
        """
        ...
    def getOutline(self, t: float) -> XPolyPolygon2D_e1b0e20:
        """
        Query the polygonal outline at the specified value.
        
        The returned outline should be clipped to the [0,1]x[0,1] rectangle.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getPointColor(self, point: RealPoint2D_d6e70c78) -> typing.Tuple[ColorComponent_e4c0e78, ...]:
        """
        Query the color for a dedicated point in the plane.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...



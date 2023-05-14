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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering
from typing_extensions import Literal
import typing
from .x_poly_polygon2_d import XPolyPolygon2D as XPolyPolygon2D_e1b0e20
if typing.TYPE_CHECKING:
    from ..geometry.real_bezier_segment2_d import RealBezierSegment2D as RealBezierSegment2D_4a970fa2

class XBezierPolyPolygon2D(XPolyPolygon2D_e1b0e20):
    """
    This is a specialized interface for a 2D poly-polygon containing straight line and Bezier segments.
    
    This poly-polygon can contain polygons consisting of a mixture of cubic Bezier curves and straight lines. As the straight line is a special case of a cubic Bezier curve (control points collinear with the line through start and end point), this can be expressed uniformly with a sequence of RealBezierSegment2Ds.
    
    By convention, a RealBezierSegment2D is a straight line segment, if all three contained points are strictly equal.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XBezierPolyPolygon2D <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XBezierPolyPolygon2D.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.rendering.XBezierPolyPolygon2D']

    def getBezierSegment(self, nPolygonIndex: int, nPointIndex: int) -> 'RealBezierSegment2D_4a970fa2':
        """
        Get a single point from the poly-polygon.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getBezierSegments(self, nPolygonIndex: int, nNumberOfPolygons: int, nPointIndex: int, nNumberOfPoints: int) -> 'typing.Tuple[typing.Tuple[RealBezierSegment2D_4a970fa2, ...], ...]':
        """
        Query subset of this poly-polygon.
        
        Query subset of this poly-polygon, starting at the given polygon and the given point within that polygon, and containing the specified number of polygons and points in the last polygon.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def setBezierSegment(self, point: 'RealBezierSegment2D_4a970fa2', nPolygonIndex: int, nPointIndex: int) -> None:
        """
        Set a single point on the poly-polygon.
        
        The remaining points of the poly-polygon will not be changed by this method. Use XBezierPolyPolygon2D.getNumberOfPolygons() or XBezierPolyPolygon2D.getNumberOfPolygonPoints() to append points or polygons, respectively.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def setBezierSegments(self, points: 'typing.Tuple[typing.Tuple[RealBezierSegment2D_4a970fa2, ...], ...]', nPolygonIndex: int) -> None:
        """
        Set the specified sequence of Bezier segments to the poly-polygon.
        
        This method can either set the whole poly-polygon to the new data, or insert the segments at the given index

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...



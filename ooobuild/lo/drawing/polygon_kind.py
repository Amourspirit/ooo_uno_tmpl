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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
from enum import Enum


class PolygonKind(Enum):
    """
    Enum Class

    

    See Also:
        `API PolygonKind <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#adec70dcaa1fdfc08f03cf30ccee65ef6>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.PolygonKind'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.drawing.PolygonKind'

    FREEFILL = 'FREEFILL'
    """
    This is the PolygonKind for a ClosedFreeHandShape.
    """
    FREELINE = 'FREELINE'
    """
    This is the PolygonKind for an OpenFreeHandShape.
    """
    LINE = 'LINE'
    """
    the ConnectorShape is drawn as a straight line
    
    This is the PolygonKind for a LineShape.
    """
    PATHFILL = 'PATHFILL'
    """
    This is the PolygonKind for a ClosedBezierShape.
    """
    PATHLINE = 'PATHLINE'
    """
    This is the PolygonKind for an OpenBezierShape.
    """
    PATHPLIN = 'PATHPLIN'
    """
    This is the PolygonKind for a PolyLinePathShape.
    """
    PATHPOLY = 'PATHPOLY'
    """
    This is the PolygonKind for a PolyPolygonPathShape.
    """
    PLIN = 'PLIN'
    """
    This is the PolygonKind for a PolyLineShape.
    """
    POLY = 'POLY'
    """
    This is the PolygonKind for a PolyPolygonShape.
    """

__all__ = ['PolygonKind']


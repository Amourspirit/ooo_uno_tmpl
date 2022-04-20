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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.geometry
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class IntegerBezierSegment2D(object):
    """
    Struct Class

    This structure contains the relevant data for a cubic Bezier curve.
    
    The data is stored integer-valued. The last point of the segment is taken from the first point of the following segment, and thus not included herein. That is, when forming a polygon out of cubic Bezier segments, each two consecutive IntegerBezierSegment2Ds define the actual curve, with the very last segment providing only the end point of the last curve, and the remaining members ignored.
    
    **since**
    
        OOo 2.0

    See Also:
        `API IntegerBezierSegment2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1IntegerBezierSegment2D.html>`_
    """
    typeName: Literal['com.sun.star.geometry.IntegerBezierSegment2D']

    def __init__(self, Px: typing.Optional[int] = ..., Py: typing.Optional[int] = ..., C1x: typing.Optional[int] = ..., C1y: typing.Optional[int] = ..., C2x: typing.Optional[int] = ..., C2y: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Px (int, optional): Px value.
            Py (int, optional): Py value.
            C1x (int, optional): C1x value.
            C1y (int, optional): C1y value.
            C2x (int, optional): C2x value.
            C2y (int, optional): C2y value.
        """


    @property
    def Px(self) -> int:
        """
        The x coordinate of the start point.
        """


    @property
    def Py(self) -> int:
        """
        The y coordinate of the start point.
        """


    @property
    def C1x(self) -> int:
        """
        The x coordinate of the first control point.
        """


    @property
    def C1y(self) -> int:
        """
        The y coordinate of the first control point.
        """


    @property
    def C2x(self) -> int:
        """
        The x coordinate of the second control point.
        """


    @property
    def C2y(self) -> int:
        """
        The y coordinate of the second control point.
        """



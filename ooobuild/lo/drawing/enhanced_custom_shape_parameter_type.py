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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.drawing


class EnhancedCustomShapeParameterType(object):
    """
    Const Class

    defines how an EnhancedCustomShapeParameter has to be interpreted

    See Also:
        `API EnhancedCustomShapeParameterType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeParameterType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.EnhancedCustomShapeParameterType'
    __ooo_type_name__: str = 'const'

    NORMAL = 0
    """
    the value of the point component is normal, the Coordinate is taken as it is
    """
    EQUATION = 1
    """
    the value of the point component has to be interpreted as index to an Equation
    """
    ADJUSTMENT = 2
    """
    the value of the point component has to be interpreted as index into the list of AdjustmentValues
    """
    LEFT = 3
    """
    the logical left border of the CustomShape is used
    """
    TOP = 4
    """
    the logical top border of the CustomShape is used
    """
    RIGHT = 5
    """
    the logical right border of the CustomShape is used
    """
    BOTTOM = 6
    """
    the logical bottom border of the CustomShape is used
    """
    XSTRETCH = 7
    """
    the x value of the stretch point is used
    """
    YSTRETCH = 8
    """
    the y value of the stretch point is used
    """
    HASSTROKE = 9
    """
    If the shape has a line style, a value of 1 is used.
    """
    HASFILL = 10
    """
    If the shape has a fill style, a value of 1 is used.
    """
    WIDTH = 11
    """
    The width of the svg:viewBox is used.
    """
    HEIGHT = 12
    """
    The height of the svg:viewBox is used.
    """
    LOGWIDTH = 13
    """
    The logical width of the shape is used.
    """
    LOGHEIGHT = 14
    """
    The logical height of the shape is used.
    """

__all__ = ['EnhancedCustomShapeParameterType']

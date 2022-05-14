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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.animations
from typing_extensions import Literal


class AnimationCalcMode(object):
    """
    Const

    Specifies the interpolation mode for the animation.

    See Also:
        `API AnimationCalcMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1animations_1_1AnimationCalcMode.html>`_
    """
    DISCRETE: Literal[0]
    """
    This specifies that the animation function will jump from one value to the next without any interpolation.
    """
    LINEAR: Literal[1]
    """
    Simple linear interpolation between values is used to calculate the animation function.
    
    This is the default.
    """
    PACED: Literal[2]
    """
    Defines interpolation to produce an even pace of change across the animation.
    
    This is only supported for values that define a linear numeric range, and for which some notion of \"distance\" between points can be calculated (e.g. position, width, height, etc.).
    """
    SPLINE: Literal[3]
    """
    Interpolates from one value in the values list to the next according to a time function defined by a cubic Bezier spline.
    
    The points of the spline are defined in the XAnimate.KeyTimes attribute, and the control points for each interval are defined in the XAnimate.TimeFilter attribute.
    """


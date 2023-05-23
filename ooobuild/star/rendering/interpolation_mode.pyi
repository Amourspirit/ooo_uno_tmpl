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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering
import typing


class InterpolationMode:
    """
    Const

    These constants specify the interpolation type for animation frames.
    
    With this constants, one specifies the way of interpolation that takes place between two consecutive frames of a discrete animation sequence.
    
    **since**
    
        OOo 2.0

    See Also:
        `API InterpolationMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1InterpolationMode.html>`_
    """
    NEAREST_NEIGHBOR: int = ...
    """
    Perform a nearest neighbor interpolation.
    
    That is, when interpolating between two values v0 and v1, positioned at t0 and t1, take the one which has the closest t coordinate.
    """
    LINEAR: int = ...
    """
    Perform a linear interpolation.
    
    That is, when interpolating at position t between two values v0 and v1, positioned at t0 and t1, take the sum of v0 weighted with (t-t0) and v1 weighted with (t1-t).
    """
    CUBIC: int = ...
    """
    Perform a cubic interpolation.
    
    That is, when interpolating at position t, take the four closest data points v0, v1, v2, and v3, fit a cubic curve through them, and take the interpolated value from this cubic curve.
    """
    BEZIERSPLINE3: int = ...
    """
    Perform a cubic Bezier spline interpolation.
    
    That is, when interpolating at position t, take the three closest data points v0, v1, and v2, fit a cubic Bezier spline through them, and take the interpolated value from this cubic curve.
    """
    BEZIERSPLINE4: int = ...
    """
    Perform a quadric Bezier spline interpolation.
    
    That is, when interpolating at position t, take the four closest data points v0, v1, v2, and v3, fit a quadric Bezier spline through them, and take the interpolated value from this quadric curve.
    """


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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 2024.2
from .gradient import Gradient as Gradient_7a8a0982
from .gradient_style import GradientStyle as GradientStyle_b02b0b93
from ..util.color import Color as Color_68e908c5
from ..util.color import Color as Color_68e908c5
import typing
from .color_stop_sequence import ColorStopSequence as ColorStopSequence_e2d70d32


class Gradient2(Gradient_7a8a0982):
    """
    Struct Class

    This struct extends the Gradient definition by adding a sequence of ColorStops to allow definition of multi-color gradients.

    See Also:
        `API Gradient2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Gradient2.html>`_
    """
    typeName: str = 'com.sun.star.awt.Gradient2'

    def __init__(self, Style: typing.Optional[GradientStyle_b02b0b93] = ..., StartColor: typing.Optional[Color_68e908c5] = ..., EndColor: typing.Optional[Color_68e908c5] = ..., Angle: typing.Optional[int] = ..., Border: typing.Optional[int] = ..., XOffset: typing.Optional[int] = ..., YOffset: typing.Optional[int] = ..., StartIntensity: typing.Optional[int] = ..., EndIntensity: typing.Optional[int] = ..., StepCount: typing.Optional[int] = ..., ColorStops: typing.Optional[ColorStopSequence_e2d70d32] = ...) -> None:
        """
        Constructor

        Arguments:
            Style (GradientStyle, optional): Style value.
            StartColor (Color, optional): StartColor value.
            EndColor (Color, optional): EndColor value.
            Angle (int, optional): Angle value.
            Border (int, optional): Border value.
            XOffset (int, optional): XOffset value.
            YOffset (int, optional): YOffset value.
            StartIntensity (int, optional): StartIntensity value.
            EndIntensity (int, optional): EndIntensity value.
            StepCount (int, optional): StepCount value.
            ColorStops (ColorStopSequence, optional): ColorStops value.
        """
        ...

    @property
    def ColorStops(self) -> ColorStopSequence_e2d70d32:
        """
        contains the full multi-color gradient definition.
        """
        ...
    @ColorStops.setter
    def ColorStops(self, value: ColorStopSequence_e2d70d32) -> None:
        ...

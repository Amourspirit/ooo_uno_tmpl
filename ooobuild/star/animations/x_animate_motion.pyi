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
# Namespace: com.sun.star.animations
from __future__ import annotations
import typing

from .x_animate import XAnimate as XAnimate_ca680c52


class XAnimateMotion(XAnimate_ca680c52):
    """
    Interface for animation by defining motion on a path.

    See Also:
        `API XAnimateMotion <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XAnimateMotion.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.animations.XAnimateMotion'

    @property
    def Origin(self) -> object:
        """
        Specifies the origin of motion for the animation.
        
        The values and semantics of this attribute are dependent upon the used animation engine.
        """
        ...
    @Origin.setter
    def Origin(self, value: object) -> None:
        ...
    @property
    def Path(self) -> object:
        """
        Specifies an optional path.
        
        If a path is used, the From, To and By members are ignored. The value type of the path depends on the used rendering system. Possible types maybe a svg:d path encoded in a string.
        """
        ...
    @Path.setter
    def Path(self, value: object) -> None:
        ...


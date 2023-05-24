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


class XAnimatePhysics(XAnimate_ca680c52):
    """
    Interface for physics animation.
    
    **since**
    
        LibreOffice 7.1

    See Also:
        `API XAnimatePhysics <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XAnimatePhysics.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.animations.XAnimatePhysics'

    @property
    def Bounciness(self) -> object:
        """
        Specifies an optional bounciness value.
        
        Takes a value between [0,1], 1 being no energy loss on collisions Has a default value of 0.1
        """
        ...
    @Bounciness.setter
    def Bounciness(self, value: object) -> None:
        ...
    @property
    def Density(self) -> object:
        """
        Specifies an optional density value.
        
        Expressed in kg/m^2. Should be non-negative. Has a default value of 1.
        """
        ...
    @Density.setter
    def Density(self, value: object) -> None:
        ...
    @property
    def StartVelocityX(self) -> object:
        """
        Specifies an optional horizontal starting velocity.
        
        Expressed in 1/100 mm.
        """
        ...
    @StartVelocityX.setter
    def StartVelocityX(self, value: object) -> None:
        ...
    @property
    def StartVelocityY(self) -> object:
        """
        Specifies an optional vertical starting velocity.
        
        Expressed in 1/100 mm.
        """
        ...
    @StartVelocityY.setter
    def StartVelocityY(self, value: object) -> None:
        ...


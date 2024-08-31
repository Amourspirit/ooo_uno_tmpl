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
# Namespace: com.sun.star.animations
from __future__ import annotations
from abc import abstractmethod
from .x_animate import XAnimate as XAnimate_ca680c52

class XTransitionFilter(XAnimate_ca680c52):
    """
    Base members XAnimate.Values, XAnimate.From, XAnimate.To and XAnimate.By can be used with double values that set the transition progress the specific amount of time.

    See Also:
        `API XTransitionFilter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1animations_1_1XTransitionFilter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.animations'
    __ooo_full_ns__: str = 'com.sun.star.animations.XTransitionFilter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.animations.XTransitionFilter'

    @property
    @abstractmethod
    def Direction(self) -> bool:
        """
        This specifies the direction the transition will run.
        
        The legal values are TRUE for forward and FALSE for reverse. The default value is TRUE. Note that this does not impact the media being transitioned to, but only affects the geometry of the transition. Transitions which do not have a reverse interpretation should ignore the direction attribute and assume the default value of TRUE.
        """
        ...

    @property
    @abstractmethod
    def FadeColor(self) -> int:
        """
        If the value of the Type attribute is TransitionType.FADE and the value of the Subtype attribute is TransitionSubType.FADETOCOLOR or TransitionSubType.FADEFROMCOLOR, then this attribute specifies the starting or ending color of the fade.
        
        The default value is 0 (black).
        """
        ...

    @property
    @abstractmethod
    def Mode(self) -> bool:
        """
        Indicates whether the transitionFilter's parent element will transition in or out.
        
        Legal values are TRUE indicating that the parent media will become more visible as the transition progress increases and FALSE indicating that the parent media will become less visible as the transition progress increases.
        
        The default value is TRUE.
        """
        ...

    @property
    @abstractmethod
    def Subtype(self) -> int:
        """
        This is the subtype of the transition.
        
        This must be one of the transition subtypes appropriate for the specified Type as listed in TransitionSubType. TransitionSubType.DEFAULT is the default.
        """
        ...

    @property
    @abstractmethod
    def Transition(self) -> int:
        """
        This is the type or family of transition.
        
        This attribute is required and must be one of the transition families listed in TransitionType.
        """
        ...


__all__ = ['XTransitionFilter']


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
# Namespace: com.sun.star.animations
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class AnimationRestart(metaclass=UnoConstMeta, type_name="com.sun.star.animations.AnimationRestart", name_space="com.sun.star.animations"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.animations.AnimationRestart``"""
        pass

    class AnimationRestartEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.animations.AnimationRestart", name_space="com.sun.star.animations"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.animations.AnimationRestart`` as Enum values"""
        pass

else:
    from ...lo.animations.animation_restart import AnimationRestart as AnimationRestart

    class AnimationRestartEnum(IntEnum):
        """
        Enum of Const Class AnimationRestart

        defines the restart behavior
        """
        DEFAULT = AnimationRestart.DEFAULT
        """
        The restart behavior for the element is determined by the value of the XTiming.RestartDefault attribute.
        
        This is the default value for the XTiming.Restart attribute.
        """
        INHERIT = AnimationRestart.INHERIT
        """
        Specifies that the value of this attribute (and of the restart behavior) are inherited from the XTiming.RestartDefault value of the parent element.
        
        If there is no parent element, the value is AnimationRestart.ALWAYS. This is the default value for the XTiming.RestartDefault attribute.
        """
        ALWAYS = AnimationRestart.ALWAYS
        """
        The element can be restarted at any time.
        """
        WHEN_NOT_ACTIVE = AnimationRestart.WHEN_NOT_ACTIVE
        """
        The element can only be restarted when it is not active (i.e.
        
        it can be restarted after the active end). Attempts to restart the element during its active duration are ignored.
        """
        NEVER = AnimationRestart.NEVER
        """
        The element cannot be restarted for the remainder of the current simple duration of the parent time container.
        """

__all__ = ['AnimationRestart', 'AnimationRestartEnum']

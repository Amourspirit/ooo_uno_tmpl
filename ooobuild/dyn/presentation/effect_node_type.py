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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.presentation
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class EffectNodeType(metaclass=UnoConstMeta, type_name="com.sun.star.presentation.EffectNodeType", name_space="com.sun.star.presentation"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.presentation.EffectNodeType``"""
        pass

    class EffectNodeTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.presentation.EffectNodeType", name_space="com.sun.star.presentation"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.presentation.EffectNodeType`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.presentation import EffectNodeType as EffectNodeType
    else:
        # keep document generators happy
        from ...lo.presentation.effect_node_type import EffectNodeType as EffectNodeType

    class EffectNodeTypeEnum(IntEnum):
        """
        Enum of Const Class EffectNodeType

        This constants defines a type for an animation effect node.
        
        This is stored with the name node-type inside the com.sun.star.animations.XAnimationNode.UserData sequence. This does not manipulate the timing or synchronization. It can be used to quickly identify semantic blocks inside an animation hierarchy.
        """
        DEFAULT = EffectNodeType.DEFAULT
        """
        This node has no special meaning.
        """
        ON_CLICK = EffectNodeType.ON_CLICK
        """
        This node contains an effect that starts on click.
        """
        WITH_PREVIOUS = EffectNodeType.WITH_PREVIOUS
        """
        This node contains an effect that starts with a previous effect.
        """
        AFTER_PREVIOUS = EffectNodeType.AFTER_PREVIOUS
        """
        This node contains an effect that starts after a previous effect has finished.
        """
        MAIN_SEQUENCE = EffectNodeType.MAIN_SEQUENCE
        """
        This is the main sequence for effects that is automatically started.
        """
        TIMING_ROOT = EffectNodeType.TIMING_ROOT
        """
        This is the root sequence.
        """
        INTERACTIVE_SEQUENCE = EffectNodeType.INTERACTIVE_SEQUENCE
        """
        This is a sequence with effects that starts due to user interaction.
        """

__all__ = ['EffectNodeType', 'EffectNodeTypeEnum']

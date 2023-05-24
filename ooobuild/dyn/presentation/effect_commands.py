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

    class EffectCommands(metaclass=UnoConstMeta, type_name="com.sun.star.presentation.EffectCommands", name_space="com.sun.star.presentation"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.presentation.EffectCommands``"""
        pass

    class EffectCommandsEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.presentation.EffectCommands", name_space="com.sun.star.presentation"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.presentation.EffectCommands`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.presentation import EffectCommands as EffectCommands
    else:
        # keep document generators happy
        from ...lo.presentation.effect_commands import EffectCommands as EffectCommands

    class EffectCommandsEnum(IntEnum):
        """
        Enum of Const Class EffectCommands

        """
        CUSTOM = EffectCommands.CUSTOM
        """
        the command is user defined
        """
        VERB = EffectCommands.VERB
        """
        the command is an OLE verb.
        
        Required parameters are \"Verb\" of type long that specifies the verb to execute.
        """
        PLAY = EffectCommands.PLAY
        """
        the command starts playing on a media object.
        
        Optional parameters are \"MediaTime\" of type double that specifies the start time in milliseconds. If not given, play continues at last position known.
        """
        TOGGLEPAUSE = EffectCommands.TOGGLEPAUSE
        """
        the command toggles the pause status on a media object.
        """
        STOP = EffectCommands.STOP
        """
        the command stops the animation on a media object
        """
        STOPAUDIO = EffectCommands.STOPAUDIO
        """
        the command stops all currently running sound effects.
        """

__all__ = ['EffectCommands', 'EffectCommandsEnum']

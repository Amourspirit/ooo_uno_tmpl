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
# Libre Office Version: 7.3
# Namespace: com.sun.star.i18n
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.i18n import CharacterIteratorMode as CharacterIteratorMode
    if hasattr(CharacterIteratorMode, '_constants') and isinstance(CharacterIteratorMode._constants, dict):
        CharacterIteratorMode._constants['__ooo_ns__'] = 'com.sun.star.i18n'
        CharacterIteratorMode._constants['__ooo_full_ns__'] = 'com.sun.star.i18n.CharacterIteratorMode'
        CharacterIteratorMode._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global CharacterIteratorModeEnum
        ls = [f for f in dir(CharacterIteratorMode) if not callable(getattr(CharacterIteratorMode, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(CharacterIteratorMode, name)
        CharacterIteratorModeEnum = IntEnum('CharacterIteratorModeEnum', _dict)
    build_enum()
else:
    from ...lo.i18n.character_iterator_mode import CharacterIteratorMode as CharacterIteratorMode

    class CharacterIteratorModeEnum(IntEnum):
        """
        Enum of Const Class CharacterIteratorMode

        Constants to specify the type of character iteration.
        
        Used with XBreakIterator.nextCharacters() and XBreakIterator.previousCharacters()
        """
        SKIPCHARACTER = CharacterIteratorMode.SKIPCHARACTER
        """
        skip characters
        """
        SKIPCELL = CharacterIteratorMode.SKIPCELL
        """
        skip cells
        """
        SKIPCONTROLCHARACTER = CharacterIteratorMode.SKIPCONTROLCHARACTER
        """
        skip control characters
        """

__all__ = ['CharacterIteratorMode', 'CharacterIteratorModeEnum']
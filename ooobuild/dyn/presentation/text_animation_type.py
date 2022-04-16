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
# Namespace: com.sun.star.presentation
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.presentation import TextAnimationType as TextAnimationType
    if hasattr(TextAnimationType, '_constants') and isinstance(TextAnimationType._constants, dict):
        TextAnimationType._constants['__ooo_ns__'] = 'com.sun.star.presentation'
        TextAnimationType._constants['__ooo_full_ns__'] = 'com.sun.star.presentation.TextAnimationType'
        TextAnimationType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global TextAnimationTypeEnum
        ls = [f for f in dir(TextAnimationType) if not callable(getattr(TextAnimationType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(TextAnimationType, name)
        TextAnimationTypeEnum = IntEnum('TextAnimationTypeEnum', _dict)
    build_enum()
else:
    from ...lo.presentation.text_animation_type import TextAnimationType as TextAnimationType

    class TextAnimationTypeEnum(IntEnum):
        """
        Enum of Const Class TextAnimationType

        Defines how a target com.sun.star.text.XTextRange is animated inside an com.sun.star.animations.XIterateContainer.
        
        This is stored inside the attribute com.sun.star.animations.XIterateContainer.IterateType.
        """
        BY_PARAGRAPH = TextAnimationType.BY_PARAGRAPH
        """
        the text is animated paragraph by paragraph
        """
        BY_WORD = TextAnimationType.BY_WORD
        """
        the text is animated word by word
        """
        BY_LETTER = TextAnimationType.BY_LETTER
        """
        the text is animated letter by letter.
        """

__all__ = ['TextAnimationType', 'TextAnimationTypeEnum']

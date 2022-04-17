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
# Namespace: com.sun.star.text
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.text import TextMarkupType as TextMarkupType
    if hasattr(TextMarkupType, '_constants') and isinstance(TextMarkupType._constants, dict):
        TextMarkupType._constants['__ooo_ns__'] = 'com.sun.star.text'
        TextMarkupType._constants['__ooo_full_ns__'] = 'com.sun.star.text.TextMarkupType'
        TextMarkupType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global TextMarkupTypeEnum
        ls = [f for f in dir(TextMarkupType) if not callable(getattr(TextMarkupType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(TextMarkupType, name)
        TextMarkupTypeEnum = IntEnum('TextMarkupTypeEnum', _dict)
    build_enum()
else:
    from ...lo.text.text_markup_type import TextMarkupType as TextMarkupType

    class TextMarkupTypeEnum(IntEnum):
        """
        Enum of Const Class TextMarkupType

        Constants to specify the type of text markup.
        
        These constants are used with XTextMarkup.commitTextMarkup()
        
        **since**
        
            OOo 2.3
        """
        SPELLCHECK = TextMarkupType.SPELLCHECK
        """
        Markup originates from spell checking.
        """
        PROOFREADING = TextMarkupType.PROOFREADING
        """
        Markup originates from proofreading.
        
        **since**
        
            OOo 3.0.1
        """
        SMARTTAG = TextMarkupType.SMARTTAG
        """
        Markup originates from smart tag checking.
        """
        SENTENCE = TextMarkupType.SENTENCE
        """
        Markup originates from proofreading An invisible markup type used in proofreading API calls.
        
        **since**
        
            OOo 3.0.1
        """
        TRACK_CHANGE_INSERTION = TextMarkupType.TRACK_CHANGE_INSERTION
        """
        Markups originates from change tracking.
        
        **since**
        
            OOo 3.3
        """
        TRACK_CHANGE_DELETION = TextMarkupType.TRACK_CHANGE_DELETION
        TRACK_CHANGE_FORMATCHANGE = TextMarkupType.TRACK_CHANGE_FORMATCHANGE

__all__ = ['TextMarkupType', 'TextMarkupTypeEnum']
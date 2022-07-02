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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.text
from ..style.numbering_rule import NumberingRule as NumberingRule_cb530c78

class ChapterNumberingRule(NumberingRule_cb530c78):
    """
    Service Class

    describes the rules for chapter numbering in a text document.
    
    Some of the properties that are available in the interface are ignored here.
    
    The type of numbering can only be: NUM_CHARS_UPPER_LETTER, NUM_CHARS_LOWER_LETTER, NUM_ROMAN_UPPER, NUM_ROMAN_LOWER, NUM_ARABIC, or NUM_NUMBER_NONE
    
    In the com.sun.star.style.NumberingAlignment only the field com.sun.star.style.NumberingAlignment.Alignment is applied.
    
    Depending on the numbering types, the parameters for bullets or bit maps may be ignored. The character style name for the numbering symbol is also ignored.

    See Also:
        `API ChapterNumberingRule <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1ChapterNumberingRule.html>`_
    """
    @property
    def HeadingStyleName(self) -> str:
        """
        contains the name of the paragraph style that marks this heading level.
        
        It is necessary that each style name appears only once in the sequence of numbering rules.
        """
        ...



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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.i18n
from typing_extensions import Literal


class TransliterationType(object):
    """
    Const

    Bitmask transliteration types used with XTransliteration.getType() and XTransliteration.getAvailableModules() methods.
    
    Non-IGNORE type modules provide XTransliteration.transliterate().
    IGNORE type modules provide XTransliteration.equals() and XTransliteration.transliterateRange().

    See Also:
        `API TransliterationType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1TransliterationType.html>`_
    """
    NONE: Literal[0]
    ONE_TO_ONE: Literal[1]
    """
    A transliteration module is ONE_TO_ONE if and only if it's mapping between characters is one to one like a-z to A-Z.
    
    Transliteration modules of this type can be used as choice in regular expressions based search/replace.
    """
    NUMERIC: Literal[2]
    """
    A transliteration module can have attribute NUMERIC if it transliterates numbers in different languages like Chinese numbers to Arabic numbers and vice versa.
    
    This mapping need not be one to one, it should be primarily used by number formatting and parsing methods.
    """
    ONE_TO_ONE_NUMERIC: Literal[3]
    """
    A transliteration module is ONE_TO_ONE_NUMERIC if it offers both one to one mapping and handles number also.
    """
    IGNORE: Literal[4]
    """
    With a transliteration IGNORE case, the regular expression A-Z can be transformed to a-z, for example.
    """
    CASCADE: Literal[8]
    """
    If the transliteration is cascaded (uses more than one algorithm).
    """


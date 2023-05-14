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
# Namespace: com.sun.star.text


class ControlCharacter(object):
    """
    Const Class

    These constants are the codes for inserting control characters using XSimpleText.insertControlCharacter() interface.

    See Also:
        `API ControlCharacter <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1ControlCharacter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.ControlCharacter'
    __ooo_type_name__: str = 'const'

    PARAGRAPH_BREAK = 0
    """
    This control character starts a new paragraph.
    """
    LINE_BREAK = 1
    """
    This control character starts a new line in a paragraph.
    """
    HARD_HYPHEN = 2
    """
    This control character equals a dash but prevents this position from being hyphenated.
    """
    SOFT_HYPHEN = 3
    """
    This control character defines a special position as a hyphenation point.
    
    If a word containing a soft hyphen must be split at the end of a line, then this position is preferred.
    """
    HARD_SPACE = 4
    """
    This control character is used to link two words and prevents this concatenation from being hyphenated.
    
    It is printed as a space.
    """
    APPEND_PARAGRAPH = 5
    """
    This control character appends a new paragraph.
    """

__all__ = ['ControlCharacter']

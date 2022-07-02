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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.smarttags
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API SmartTagRecognizerMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1smarttags.html#a2eab74f21d11f78b5aa7826b0c60604f>`_
"""
typeName: str = 'com.sun.star.smarttags.SmartTagRecognizerMode'

CELL: 'uno.Enum'
"""
Text passed to the recognizer is a cell.
"""
CHAR: 'uno.Enum'
"""
Text passed to the recognizer is a single character.
"""
PARAGRAPH: 'uno.Enum'
"""
Text passed to the recognizer is a paragraph.
"""
SINGLE_WORD: 'uno.Enum'
"""
Text passed to the recognizer is a single word.
"""


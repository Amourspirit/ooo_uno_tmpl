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
# Namespace: com.sun.star.rendering
from typing_extensions import Literal


class EmphasisMark:
    """
    Const Class

    These constants control the automatic rendering of emphasis marks.
    
    These constants control the automatic rendering of emphasis marks for a given font.
    
    **since**
    
        OOo 2.0

    See Also:
        `API EmphasisMark <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1EmphasisMark.html>`_
    """
    NONE: Literal[0]
    """
    No automatic emphasis marks.
    """
    DOT_ABOVE: Literal[1]
    """
    Automatic emphasis marks as dots above the glyphs.
    """
    DOT_BELOW: Literal[2]
    """
    Automatic emphasis marks as dots below the glyphs.
    """
    CIRCLE_ABOVE: Literal[3]
    """
    Automatic emphasis marks as circles (unfilled outlines) above the glyphs.
    """
    CIRCLE_BELOW: Literal[4]
    """
    Automatic emphasis marks as circles (unfilled outlines) below the glyphs.
    """
    DISC_ABOVE: Literal[5]
    """
    Automatic emphasis marks as discs (filled circles) above the glyphs.
    """
    DISC_BELOW: Literal[6]
    """
    Automatic emphasis marks as discs (filled circles) below the glyphs.
    """
    ACCENT_ABOVE: Literal[7]
    """
    Automatic emphasis marks as accent marks above the glyphs.
    """
    ACCENT_BELOW: Literal[8]
    """
    Automatic emphasis marks as accent marks below the glyphs.
    """


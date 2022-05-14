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
# Libre Office Version: 7.3
# Namespace: com.sun.star.text
from typing_extensions import Literal


class FontEmphasis(object):
    """
    Const

    Determines the type and position of an emphasis mark in Asian texts.

    See Also:
        `API FontEmphasis <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1FontEmphasis.html>`_
    """
    NONE: Literal[0]
    """
    no emphasis mark is used.
    """
    DOT_ABOVE: Literal[1]
    """
    a dot is set above (or right from vertical text) the text.
    """
    CIRCLE_ABOVE: Literal[2]
    """
    a circle is set above (or right from vertical text) the text.
    """
    DISK_ABOVE: Literal[3]
    """
    a disc is set above (or right from vertical text) the text.
    """
    ACCENT_ABOVE: Literal[4]
    """
    an accent is set above (or right from vertical text) the text.
    """
    DOT_BELOW: Literal[11]
    """
    a dot is set below (or left from vertical text) the text.
    """
    CIRCLE_BELOW: Literal[12]
    """
    a circle is set below (or left from vertical text) the text.
    """
    DISK_BELOW: Literal[13]
    """
    a disk is set below (or left from vertical text) the text.
    """
    ACCENT_BELOW: Literal[14]
    """
    an accent is set below (or left from vertical text) the text.
    """


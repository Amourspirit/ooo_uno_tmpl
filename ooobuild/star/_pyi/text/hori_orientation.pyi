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
# Namespace: com.sun.star.text
from typing_extensions import Literal


class HoriOrientation(object):
    """
    Const

    These enumeration values specify the horizontal orientation.

    See Also:
        `API HoriOrientation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1HoriOrientation.html>`_
    """
    NONE: Literal[0]
    """
    no hard alignment is applied.
    """
    RIGHT: Literal[1]
    """
    The object is aligned at the right side.
    """
    CENTER: Literal[2]
    """
    The object is aligned at the middle.
    """
    LEFT: Literal[3]
    """
    The object is aligned at the left side.
    """
    INSIDE: Literal[4]
    """
    TODO.
    """
    OUTSIDE: Literal[5]
    """
    TODO.
    """
    FULL: Literal[6]
    """
    The object uses the full space (for text tables only).
    """
    LEFT_AND_WIDTH: Literal[7]
    """
    The left offset and the width of the object are defined.
    
    For text tables this means that the tables position is defined by the left margin and the width.
    """


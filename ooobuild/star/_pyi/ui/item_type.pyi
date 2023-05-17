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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class ItemType(object):
    """
    Const

    Determines the type of an item.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ItemType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui_1_1ItemType.html>`_
    """
    DEFAULT: Literal[0]
    """
    a normal item
    """
    SEPARATOR_LINE: Literal[1]
    """
    a separator is inserted as a line.
    """
    SEPARATOR_SPACE: Literal[2]
    """
    a separator is inserted as a space.
    """
    SEPARATOR_LINEBREAK: Literal[3]
    """
    a line break is inserted.
    """


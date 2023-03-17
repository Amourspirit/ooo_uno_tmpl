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
# Libre Office Version: 7.4
# Namespace: com.sun.star.style
from typing_extensions import Literal


class LineSpacingMode(object):
    """
    Const

    These constants specify the interpretation of LineHeight.

    See Also:
        `API LineSpacingMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style_1_1LineSpacingMode.html>`_
    """
    PROP: Literal[0]
    """
    This constant specifies the height value as a proportional value.
    """
    MINIMUM: Literal[1]
    """
    This constant specifies the height as the minimum line height.
    """
    LEADING: Literal[2]
    """
    This constant specifies the height value as the distance to the previous line.
    """
    FIX: Literal[3]
    """
    This constant specifies the height value as a fixed line height.
    """


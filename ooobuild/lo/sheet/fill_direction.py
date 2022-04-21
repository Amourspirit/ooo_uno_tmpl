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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from enum import Enum


class FillDirection(Enum):
    """
    Enum Class

    

    See Also:
        `API FillDirection <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#aa8eeb1312106b2d89cd26342fa09aac9>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.FillDirection'
    __ooo_type_name__: str = 'enum'

    TO_BOTTOM = 'TO_BOTTOM'
    """
    specifies that rows are filled from top to bottom.
    """
    TO_LEFT = 'TO_LEFT'
    """
    specifies that columns are filled from right to left.
    """
    TO_RIGHT = 'TO_RIGHT'
    """
    specifies that columns are filled from left to right.
    """
    TO_TOP = 'TO_TOP'
    """
    specifies that rows are filled from bottom to top.
    """

__all__ = ['FillDirection']


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
# Namespace: com.sun.star.style
# Libre Office Version: 7.3
from enum import Enum


class VerticalAlignment(Enum):
    """
    Enum Class

    

    See Also:
        `API VerticalAlignment <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#a9c2ed22cfbd21f13df24ea193b310aee>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.VerticalAlignment'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.style.VerticalAlignment'

    BOTTOM = 'BOTTOM'
    """
    set the vertical alignment to the bottom margin from the container object.
    """
    MIDDLE = 'MIDDLE'
    """
    set the vertical alignment to the top margin from the container object.
    """
    TOP = 'TOP'
    """
    set the vertical alignment to the center between the top and bottom margins from the container object.
    """

__all__ = ['VerticalAlignment']


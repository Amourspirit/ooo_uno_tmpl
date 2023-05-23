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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from typing import cast
from enum import Enum
from com.sun.star.drawing.DrawViewMode import DrawViewModeProto

class DrawViewMode(Enum):
    """
    Enum Class


    See Also:
        `API DrawViewMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a15072729125e991609f3df469a03f611>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.DrawViewMode'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.drawing.DrawViewMode'

    DRAW = cast(DrawViewModeProto, 'DRAW')
    """
    The view shows the drawing pages.
    """
    HANDOUT = cast(DrawViewModeProto, 'HANDOUT')
    """
    The view shows the handout pages,.
    """
    NOTES = cast(DrawViewModeProto, 'NOTES')
    """
    The view shows the notes pages.
    """

__all__ = ['DrawViewMode']


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
# Namespace: com.sun.star.graphic
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.graphic import GraphicType as GraphicType
    if hasattr(GraphicType, '_constants') and isinstance(GraphicType._constants, dict):
        GraphicType._constants['__ooo_ns__'] = 'com.sun.star.graphic'
        GraphicType._constants['__ooo_full_ns__'] = 'com.sun.star.graphic.GraphicType'
        GraphicType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global GraphicTypeEnum
        ls = [f for f in dir(GraphicType) if not callable(getattr(GraphicType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(GraphicType, name)
        GraphicTypeEnum = IntEnum('GraphicTypeEnum', _dict)
    build_enum()
else:
    from ...lo.graphic.graphic_type import GraphicType as GraphicType

    class GraphicTypeEnum(IntEnum):
        """
        Enum of Const Class GraphicType

        Constants that describe the type of graphic.
        """
        EMPTY = GraphicType.EMPTY
        """
        Graphic is empty.
        """
        PIXEL = GraphicType.PIXEL
        """
        Graphic is represented through single pixels.
        """
        VECTOR = GraphicType.VECTOR
        """
        Graphic is represented through vectors.
        """

__all__ = ['GraphicType', 'GraphicTypeEnum']

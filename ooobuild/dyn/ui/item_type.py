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
# Libre Office Version: 7.2
# Namespace: com.sun.star.ui
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.ui import ItemType as ItemType
    if hasattr(ItemType, '_constants') and isinstance(ItemType._constants, dict):
        ItemType._constants['__ooo_ns__'] = 'com.sun.star.ui'
        ItemType._constants['__ooo_full_ns__'] = 'com.sun.star.ui.ItemType'
        ItemType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global ItemTypeEnum
        ls = [f for f in dir(ItemType) if not callable(getattr(ItemType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(ItemType, name)
        ItemTypeEnum = IntEnum('ItemTypeEnum', _dict)
    build_enum()
else:
    from ...lo.ui.item_type import ItemType as ItemType

    class ItemTypeEnum(IntEnum):
        """
        Enum of Const Class ItemType

        Determines the type of an item.
        
        **since**
        
            OOo 2.0
        """
        DEFAULT = ItemType.DEFAULT
        """
        a normal item
        """
        SEPARATOR_LINE = ItemType.SEPARATOR_LINE
        """
        a separator is inserted as a line.
        """
        SEPARATOR_SPACE = ItemType.SEPARATOR_SPACE
        """
        a separator is inserted as a space.
        """
        SEPARATOR_LINEBREAK = ItemType.SEPARATOR_LINEBREAK
        """
        a line break is inserted.
        """

__all__ = ['ItemType', 'ItemTypeEnum']

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
# Namespace: com.sun.star.datatransfer.dnd
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.datatransfer.dnd import DNDConstants as DNDConstants
    if hasattr(DNDConstants, '_constants') and isinstance(DNDConstants._constants, dict):
        DNDConstants._constants['__ooo_ns__'] = 'com.sun.star.datatransfer.dnd'
        DNDConstants._constants['__ooo_full_ns__'] = 'com.sun.star.datatransfer.dnd.DNDConstants'
        DNDConstants._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global DNDConstantsEnum
        ls = [f for f in dir(DNDConstants) if not callable(getattr(DNDConstants, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(DNDConstants, name)
        DNDConstantsEnum = IntEnum('DNDConstantsEnum', _dict)
    build_enum()
else:
    from ....lo.datatransfer.dnd.dnd_constants import DNDConstants as DNDConstants

    class DNDConstantsEnum(IntEnum):
        """
        Enum of Const Class DNDConstants

        These values represent the type of action or actions to be performed by a Drag and Drop operation.
        """
        ACTION_NONE = DNDConstants.ACTION_NONE
        """
        No action.
        """
        ACTION_COPY = DNDConstants.ACTION_COPY
        """
        Action copy.
        """
        ACTION_MOVE = DNDConstants.ACTION_MOVE
        """
        Action move.
        """
        ACTION_COPY_OR_MOVE = DNDConstants.ACTION_COPY_OR_MOVE
        """
        Action copy or move.
        """
        ACTION_LINK = DNDConstants.ACTION_LINK
        """
        Action link.
        """
        ACTION_REFERENCE = DNDConstants.ACTION_REFERENCE
        """
        Action reference.
        """
        ACTION_DEFAULT = DNDConstants.ACTION_DEFAULT
        """
        Action default.
        """

__all__ = ['DNDConstants', 'DNDConstantsEnum']

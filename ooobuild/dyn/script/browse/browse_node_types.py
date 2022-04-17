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
# Namespace: com.sun.star.script.browse
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.script.browse import BrowseNodeTypes as BrowseNodeTypes
    if hasattr(BrowseNodeTypes, '_constants') and isinstance(BrowseNodeTypes._constants, dict):
        BrowseNodeTypes._constants['__ooo_ns__'] = 'com.sun.star.script.browse'
        BrowseNodeTypes._constants['__ooo_full_ns__'] = 'com.sun.star.script.browse.BrowseNodeTypes'
        BrowseNodeTypes._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global BrowseNodeTypesEnum
        ls = [f for f in dir(BrowseNodeTypes) if not callable(getattr(BrowseNodeTypes, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(BrowseNodeTypes, name)
        BrowseNodeTypesEnum = IntEnum('BrowseNodeTypesEnum', _dict)
    build_enum()
else:
    from ....lo.script.browse.browse_node_types import BrowseNodeTypes as BrowseNodeTypes

    class BrowseNodeTypesEnum(IntEnum):
        """
        Enum of Const Class BrowseNodeTypes

        These constants define the three different types of nodes in the BrowseNode hierarchy.
        """
        SCRIPT = BrowseNodeTypes.SCRIPT
        """
        Indicates node is a script.
        """
        CONTAINER = BrowseNodeTypes.CONTAINER
        """
        Indicates node is a container.
        """
        ROOT = BrowseNodeTypes.ROOT
        """
        Indicates node is root of the tree.
        """

__all__ = ['BrowseNodeTypes', 'BrowseNodeTypesEnum']

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
# Namespace: com.sun.star.sdb.tools
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sdb.tools import CompositionType as CompositionType
    if hasattr(CompositionType, '_constants') and isinstance(CompositionType._constants, dict):
        CompositionType._constants['__ooo_ns__'] = 'com.sun.star.sdb.tools'
        CompositionType._constants['__ooo_full_ns__'] = 'com.sun.star.sdb.tools.CompositionType'
        CompositionType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global CompositionTypeEnum
        ls = [f for f in dir(CompositionType) if not callable(getattr(CompositionType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(CompositionType, name)
        CompositionTypeEnum = IntEnum('CompositionTypeEnum', _dict)
    build_enum()
else:
    from ....lo.sdb.tools.composition_type import CompositionType as CompositionType

    class CompositionTypeEnum(IntEnum):
        """
        Enum of Const Class CompositionType

        specifies which composition should be used when composing a table name.
        
        **since**
        
            OOo 2.0.4
        """
        ForTableDefinitions = CompositionType.ForTableDefinitions
        """
        specifies composition of a name to be used in table definitions
        """
        ForIndexDefinitions = CompositionType.ForIndexDefinitions
        """
        specifies composition of a name to be used in index definitions
        """
        ForDataManipulation = CompositionType.ForDataManipulation
        """
        specifies composition of a name to be used in data manipulation
        """
        ForProcedureCalls = CompositionType.ForProcedureCalls
        """
        specifies composition of a name to be used in procedure calls
        """
        ForPrivilegeDefinitions = CompositionType.ForPrivilegeDefinitions
        """
        specifies composition of a name to be used in privilege definitions
        """
        Complete = CompositionType.Complete
        """
        specifies complete composition of a table name, including catalog and schema (if present), disregarding any database support for catalog and schema in any particular statements
        """

__all__ = ['CompositionType', 'CompositionTypeEnum']

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
# Namespace: com.sun.star.sdbc
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sdbc import BestRowScope as BestRowScope
    if hasattr(BestRowScope, '_constants') and isinstance(BestRowScope._constants, dict):
        BestRowScope._constants['__ooo_ns__'] = 'com.sun.star.sdbc'
        BestRowScope._constants['__ooo_full_ns__'] = 'com.sun.star.sdbc.BestRowScope'
        BestRowScope._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global BestRowScopeEnum
        ls = [f for f in dir(BestRowScope) if not callable(getattr(BestRowScope, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(BestRowScope, name)
        BestRowScopeEnum = IntEnum('BestRowScopeEnum', _dict)
    build_enum()
else:
    from ...lo.sdbc.best_row_scope import BestRowScope as BestRowScope

    class BestRowScopeEnum(IntEnum):
        """
        Enum of Const Class BestRowScope

        determines how long a row identifier is valid.
        """
        TEMPORARY = BestRowScope.TEMPORARY
        """
        indicates that the scope of the best row identifier is very temporary, lasting only while the row is being used.
        
        A possible value for the column SCOPE in the com.sun.star.sdbc.XResultSet object returned by the method XDatabaseMetaData.getBestRowIdentifier().
        """
        TRANSACTION = BestRowScope.TRANSACTION
        """
        indicates that the scope of the best row identifier is the remainder of the current transaction.
        
        A possible value for the column SCOPE in the com.sun.star.sdbc.XResultSet object returned by the method XDatabaseMetaData.getBestRowIdentifier().
        """
        SESSION = BestRowScope.SESSION
        """
        indicates that the scope of the best row identifier is the remainder of the current session.
        
        A possible value for the column SCOPE in the com.sun.star.sdbc.XResultSet object returned by the method XDatabaseMetaData.getBestRowIdentifier().
        """

__all__ = ['BestRowScope', 'BestRowScopeEnum']

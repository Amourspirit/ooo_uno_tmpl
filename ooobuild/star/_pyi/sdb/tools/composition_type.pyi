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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb.tools
from typing_extensions import Literal


class CompositionType(object):
    """
    Const

    specifies which composition should be used when composing a table name.
    
    **since**
    
        OOo 2.0.4

    See Also:
        `API CompositionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdb_1_1tools_1_1CompositionType.html>`_
    """
    ForTableDefinitions: Literal[0]
    """
    specifies composition of a name to be used in table definitions
    """
    ForIndexDefinitions: Literal[1]
    """
    specifies composition of a name to be used in index definitions
    """
    ForDataManipulation: Literal[2]
    """
    specifies composition of a name to be used in data manipulation
    """
    ForProcedureCalls: Literal[3]
    """
    specifies composition of a name to be used in procedure calls
    """
    ForPrivilegeDefinitions: Literal[4]
    """
    specifies composition of a name to be used in privilege definitions
    """
    Complete: Literal[5]
    """
    specifies complete composition of a table name, including catalog and schema (if present), disregarding any database support for catalog and schema in any particular statements
    """


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
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal
"""
Const

determines whether a procedure returns a result or not.

See Also:
    `API ProcedureResult <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1ProcedureResult.html>`_
"""
UNKNOWN: Literal[0]
"""
A possible value for column PROCEDURE_TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedures().

Indicates that it is not known whether the procedure returns a result.
"""
NONE: Literal[1]
"""
A possible value for column PROCEDURE_TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedures().

Indicates that the procedure does not return a result.
"""
RETURN: Literal[2]
"""
A possible value for column PROCEDURE_TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedures().

Indicates that the procedure returns a result.
"""


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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal


class ProcedureColumn(object):
    """
    Const

    indicates the type of a procedure column.

    See Also:
        `API ProcedureColumn <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1ProcedureColumn.html>`_
    """
    UNKNOWN: Literal[0]
    """
    indicates that the type of the column is unknown.
    
    A possible value for the column COLUMN_TYPE in the com.sun.star.sdbc.XResultSet returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedureColumns().
    """
    IN: Literal[1]
    """
    indicates that the column stores IN parameters.
    
    A possible value for the column COLUMN_TYPE in the com.sun.star.sdbc.XResultSet returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedureColumns().
    """
    INOUT: Literal[2]
    """
    indicates that the column stores INOUT parameters.
    
    A possible value for the column COLUMN_TYPE in the com.sun.star.sdbc.XResultSet returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedureColumns().
    """
    RESULT: Literal[3]
    """
    indicates that the column stores results.
    
    A possible value for the column COLUMN_TYPE in the com.sun.star.sdbc.XResultSet returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedureColumns().
    """
    OUT: Literal[4]
    """
    indicates that the column stores OUT parameters.
    
    A possible value for the column COLUMN_TYPE in the com.sun.star.sdbc.XResultSet returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedureColumns().
    """
    RETURN: Literal[5]
    """
    Indicates that the column stores return values.
    
    A possible value for the column COLUMN_TYPE in the com.sun.star.sdbc.XResultSet returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedureColumns().
    """


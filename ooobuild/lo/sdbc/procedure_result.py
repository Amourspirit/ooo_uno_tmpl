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


class ProcedureResult(object):
    """
    Const Class

    determines whether a procedure returns a result or not.

    See Also:
        `API ProcedureResult <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1ProcedureResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.ProcedureResult'
    __ooo_type_name__: str = 'const'

    UNKNOWN = 0
    """
    A possible value for column PROCEDURE_TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedures().
    
    Indicates that it is not known whether the procedure returns a result.
    """
    NONE = 1
    """
    A possible value for column PROCEDURE_TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedures().
    
    Indicates that the procedure does not return a result.
    """
    RETURN = 2
    """
    A possible value for column PROCEDURE_TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getProcedures().
    
    Indicates that the procedure returns a result.
    """

__all__ = ['ProcedureResult']

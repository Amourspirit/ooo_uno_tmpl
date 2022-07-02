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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdbc
from .prepared_statement import PreparedStatement as PreparedStatement_eef40d8c
from .x_out_parameters import XOutParameters as XOutParameters_c6db0c48
from .x_row import XRow as XRow_5f360834

class CallableStatement(PreparedStatement_eef40d8c, XOutParameters_c6db0c48, XRow_5f360834):
    """
    Service Class

    is used to execute SQL stored procedures.
    
    SDBC provides a stored procedure SQL escape that allows stored procedures to be called in a standard way for all RDBMSs. This escape syntax has one form that includes a result parameter and one that does not. If used, the result parameter must be registered as an OUT parameter. The other parameters can be used for input, output, or both. Parameters are referred to sequentially, by number. The first parameter is 1.
    
    {?=call&lt;procedure-name&gt;[&lt;arg1&gt;,&lt;arg2&gt;,...]}{call&lt;procedure-name&gt;[&lt;arg1&gt;,&lt;arg2&gt;,...]}
    
    IN parameter values are set using the set methods inherited from com.sun.star.sdbc.PreparedStatement . The type of all OUT parameters must be registered prior to executing the stored procedure; their values are retrieved after execution via the get methods provided by the com.sun.star.sdbc.XRow.
    
    A CallableStatement can return one com.sun.star.sdbc.XResultSet or multiple com.sun.star.sdbc.ResultSet objects. Multiple ResultSet objects are handled using operations inherited from com.sun.star.sdbc.XPreparedStatement.
    
    For maximum portability, a call's com.sun.star.sdbc.ResultSet objects and update counts should be processed prior to getting the values of output parameters.

    See Also:
        `API CallableStatement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbc_1_1CallableStatement.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.CallableStatement'
    __ooo_type_name__: str = 'service'



__all__ = ['CallableStatement']


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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from __future__ import annotations
from .prepared_statement import PreparedStatement as PreparedStatement_e1880d29
from ..sdbc.callable_statement import CallableStatement as CallableStatement_eccf0d69

class CallableStatement(PreparedStatement_e1880d29, CallableStatement_eccf0d69):
    """
    Service Class

    represents a procedure call.
    
    The service differs only in the access of the columns and parameters to the service com.sun.star.sdbc.CallableStatement.

    See Also:
        `API CallableStatement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1CallableStatement.html>`_
    """
    ...


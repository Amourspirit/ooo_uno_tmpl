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
from .data_settings import DataSettings as DataSettings_a3000b0c
from .x_query_definition import XQueryDefinition as XQueryDefinition_d3bf0cb8
from ..sdbcx.x_columns_supplier import XColumnsSupplier as XColumnsSupplier_f0600da9
from ..sdbcx.x_data_descriptor_factory import XDataDescriptorFactory as XDataDescriptorFactory_46170fe5
from ..sdbcx.x_rename import XRename as XRename_848c09cc

class Query(DataSettings_a3000b0c, XQueryDefinition_d3bf0cb8, XColumnsSupplier_f0600da9, XDataDescriptorFactory_46170fe5, XRename_848c09cc):
    """
    Service Class

    is a stored definition of a SQL query.
    
    It can be used if there is a need to execute SQL statements more than once, or if you want to format the query result fields differently from the underlying table definitions.

    See Also:
        `API Query <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1Query.html>`_
    """
    ...

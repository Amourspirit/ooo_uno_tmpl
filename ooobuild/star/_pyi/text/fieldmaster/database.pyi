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
# Libre Office Version: 7.3
# Namespace: com.sun.star.text.fieldmaster
from ..text_field_master import TextFieldMaster as TextFieldMaster_d6410cc2

class Database(TextFieldMaster_d6410cc2):
    """
    Service Class

    specifies service of a Database field master.
    
    Only one of the properties DataBaseName, DataBaseURL and DataBaseResource should be set. If more than one are set the last one will be used.
    
    **since**
    
        OOo 2.0

    See Also:
        `API Database <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1fieldmaster_1_1Database.html>`_
    """
    @property
    def CommandType(self) -> int:
        """
        contains the CommandType this can be the name of a data base table, a data query or a statement.
        
        (0 = table, 1 = query, 2 = statement)
        """
        ...
    @property
    def DataBaseName(self) -> str:
        """
        specifies the database name.
        """
        ...
    @property
    def DataBaseResource(self) -> str:
        """
        indicates a connection URL, which locates a database driver.
        
        **since**
        
            OOo 2.0
        """
        ...
    @property
    def DataBaseURL(self) -> str:
        """
        indicates the URL of a database file.
        
        **since**
        
            OOo 2.0
        """
        ...
    @property
    def DataColumnName(self) -> str:
        """
        contains the name of the data base table.
        """
        ...
    @property
    def DataTableName(self) -> str:
        """
        contains the command string.
        
        Depending on the CommandType property this can be the name of a data base table, a data query or a statement.
        """
        ...
    @property
    def Name(self) -> str:
        """
        contains the DataColumnName but it enables the fieldmaster and its depending fields to work without setting DataSourceName, DataTableName and CommandType
        
        **since**
        
            OOo 2.3
        """
        ...



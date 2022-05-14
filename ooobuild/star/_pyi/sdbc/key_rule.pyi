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
# Libre Office Version: 7.3
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal


class KeyRule(object):
    """
    Const

    determines the rules for foreign key constraints.

    See Also:
        `API KeyRule <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1KeyRule.html>`_
    """
    CASCADE: Literal[0]
    """
    a possible value for the column's UPDATE_RULE and DELETE_RULE in the com.sun.star.sdbc.XResultSet objects returned by the methods com.sun.star.sdbc.XDatabaseMetaData.getImportedKeys(), com.sun.star.sdbc.XDatabaseMetaData.getExportedKeys(), and com.sun.star.sdbc.XDatabaseMetaData.getCrossReference().
    
    For the column UPDATE_RULE , it indicates that when the primary key is updated, the foreign key (imported key) is changed to agree with it.
    
    For the column DELETE_RULE , it indicates that when the primary key is deleted, rows that imported that key are deleted.
    """
    RESTRICT: Literal[1]
    """
    a possible value for the column's UPDATE_RULE and DELETE_RULE in the com.sun.star.sdbc.XResultSet objects returned by the methods com.sun.star.sdbc.XDatabaseMetaData.getImportedKeys(), com.sun.star.sdbc.XDatabaseMetaData.getExportedKeys(), and com.sun.star.sdbc.XDatabaseMetaData.getCrossReference().
    
    For the column UPDATE_RULE , it indicates that a primary key may not be updated if it has been imported by another table as a foreign key.
    
    For the column DELETE_RULE , it indicates that a primary key may not be deleted if it has been imported by another table as a foreign key.
    """
    SET_NULL: Literal[2]
    """
    a possible value for the column's UPDATE_RULE and DELETE_RULE in the com.sun.star.sdbc.XResultSet objects returned by the methods com.sun.star.sdbc.XDatabaseMetaData.getImportedKeys(), com.sun.star.sdbc.XDatabaseMetaData.getExportedKeys(), and com.sun.star.sdbc.XDatabaseMetaData.getCrossReference().
    
    For the columns UPDATE_RULE and DELETE_RULE , it indicates that when the primary key is updated or deleted, the foreign key (imported key) is changed to NULL.
    """
    NO_ACTION: Literal[3]
    """
    a possible value for the column's UPDATE_RULE and DELETE_RULE in the com.sun.star.sdbc.XResultSet objects returned by the methods com.sun.star.sdbc.XDatabaseMetaData.getImportedKeys(), com.sun.star.sdbc.XDatabaseMetaData.getExportedKeys(), and com.sun.star.sdbc.XDatabaseMetaData.getCrossReference().
    
    For the columns UPDATE_RULE and DELETE_RULE , it indicates that if the primary key has been imported, it cannot be updated or deleted.
    """
    SET_DEFAULT: Literal[4]
    """
    a possible value for the column's UPDATE_RULE and DELETE_RULE in the com.sun.star.sdbc.XResultSet objects returned by the methods com.sun.star.sdbc.XDatabaseMetaData.getImportedKeys(), com.sun.star.sdbc.XDatabaseMetaData.getExportedKeys(), and com.sun.star.sdbc.XDatabaseMetaData.getCrossReference().
    
    For the columns UPDATE_RULE and DELETE_RULE , it indicates that if the primary key is updated or deleted, the foreign key (imported key) is set to the default value.
    """


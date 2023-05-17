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
# Namespace: com.sun.star.sdb.application
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class DatabaseObjectContainer(object):
    """
    Const

    denotes different types of (maybe virtual) containers of database objects
    
    In the database application of OpenOffice.org, database objects (such as tables, queries, forms, reports) can be organized in folders. This hierarchy can be imposed externally, or internally.
    
    For example, when you connect to a database which supports catalogs and/or schemas, then those impose a natural order on the tables, in that a catalog or a schema is a folder of tables.
    
    On the other hand, for forms and reports, OpenOffice.org Base itself allows the user to create folders to organize the documents - in this case, the hierarchy is defined in the database document itself.
    
    **since**
    
        OOo 3.0

    See Also:
        `API DatabaseObjectContainer <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdb_1_1application_1_1DatabaseObjectContainer.html>`_
    """
    TABLES: Literal[1000]
    """
    denotes the virtual folder containing all tables of a database, in a context where such a folder is displayed to the user.
    """
    QUERIES: Literal[1001]
    """
    denotes the virtual folder containing all queries of a database, in a context where such a folder is displayed to the user.
    """
    FORMS: Literal[1002]
    """
    denotes the virtual folder containing all forms of a database document, in a context where such a folder is displayed to the user.
    """
    REPORTS: Literal[1003]
    """
    denotes the virtual folder containing all reports of a database, in a context where such a folder is displayed to the user.
    """
    DATA_SOURCE: Literal[1004]
    """
    denotes the data source itself, which effectively is the root container for all other kind of database objects, including other container types.
    """
    CATALOG: Literal[1005]
    """
    denotes a catalog in a database which supports catalogs
    """
    SCHEMA: Literal[1006]
    """
    denotes a schema in a database which supports schemas
    """
    FORMS_FOLDER: Literal[1007]
    """
    denotes a folder which is used to organize forms in a database document
    """
    REPORTS_FOLDER: Literal[1008]
    """
    denotes a folder which is used to organize reports in a database document
    """


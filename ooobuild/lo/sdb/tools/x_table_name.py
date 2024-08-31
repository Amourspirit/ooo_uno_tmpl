# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdb.tools
from __future__ import annotations
import typing
from abc import abstractmethod, abstractproperty, ABC
if typing.TYPE_CHECKING:
    from ...beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XTableName(ABC):
    """
    allows to manipulate table names.
    
    When, in a database application, dealing with table names, there's many degrees of freedom to deal with. For instance, suppose you want to have the full name of a table object, as it should be used in a SELECT statement's FROM part. This requires you to evaluate whether or not the table has a catalog and/or schema name, to combine the catalog, the schema, and the basic table name into one name, respecting the database's quoting character, and the order in which all those parts should be combined. Additionally, you have to respect the client-side settings which tell OpenOffice.org to use or not use catalogs and schemas in SELECT at all.
    
    The XTableName interface eases this and other, similar tasks around table names.
    
    The component itself does not have life-time control mechanisms, i.e. you cannot explicitly dispose it (com.sun.star.lang.XComponent.dispose()), and you cannot be notified when it dies.However, if your try to access any of its methods or attributes, after the connection which was used to create it was closed, a com.sun.star.lang.DisposedException will be thrown.
    
    **since**
    
        OOo 2.0.4

    See Also:
        `API XTableName <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1tools_1_1XTableName.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb.tools'
    __ooo_full_ns__: str = 'com.sun.star.sdb.tools.XTableName'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.tools.XTableName'

    @abstractmethod
    def getComposedName(self, Type: int, Quote: bool) -> str:
        """
        returns the composed table name, including the catalog and schema name, respecting the database's quoting requirements, plus

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def setComposedName(self, ComposedName: str, Type: int) -> None:
        """
        sets a new composed table name
        """
        ...
    @abstractproperty
    def CatalogName(self) -> str:
        """
        denotes the name of the catalog which the table is a part of
        """
        ...

    @abstractproperty
    def NameForSelect(self) -> str:
        """
        represents the table name in a form to be used in a SELECT statement.
        
        On a per-data-source basis, OpenOffice.org allows to override database meta data information in that you can specify to not use catalog and or schema names in SELECT statements. Using this attribute, you can generate a table name which respects those settings.
        """
        ...

    @abstractproperty
    def SchemaName(self) -> str:
        """
        denotes the name of the schema which the table is a part of
        """
        ...

    @abstractproperty
    def Table(self) -> XPropertySet_bc180bfa:
        """
        is the com.sun.star.sdb.Table object specified by the current name.
        
        Retrieving this attribute is equivalent to obtaining the tables container from the connection (via com.sun.star.sdbcx.XTablesSupplier), and calling its com.sun.star.container.XNameAccess.getByName() method with the ComposedName.
        """
        ...

    @abstractproperty
    def TableName(self) -> str:
        """
        denotes the mere, unqualified table name, excluding any catalog and schema.
        """
        ...


__all__ = ['XTableName']


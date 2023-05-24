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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from __future__ import annotations
import typing
from abc import abstractmethod, abstractproperty
from .x_single_select_query_analyzer import XSingleSelectQueryAnalyzer as XSingleSelectQueryAnalyzer_66ad10b7
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class XSingleSelectQueryComposer(XSingleSelectQueryAnalyzer_66ad10b7):
    """
    simplifies the composing of single select statements.
    
    The interface can be used for composing single SELECT statements without knowing the structure of the used query.

    See Also:
        `API XSingleSelectQueryComposer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XSingleSelectQueryComposer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.XSingleSelectQueryComposer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdb.XSingleSelectQueryComposer'

    @abstractmethod
    def appendFilterByColumn(self, column: XPropertySet_bc180bfa, andCriteria: bool, filterOperator: int) -> None:
        """
        appends a new filter condition by a com.sun.star.sdb.DataColumn providing the name and the value for the filter.
        
        The value property must be supported by the com.sun.star.sdb.DataColumn.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def appendGroupByColumn(self, column: XPropertySet_bc180bfa) -> None:
        """
        appends an additional part to the group criteria of the select statement.
        
        The column must be a com.sun.star.sdbcx.Column.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def appendHavingClauseByColumn(self, column: XPropertySet_bc180bfa, andCriteria: bool, filterOperator: int) -> None:
        """
        appends a new HAVING filter condition by a com.sun.star.sdb.DataColumn providing the name and the value for the filter.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    @abstractmethod
    def appendOrderByColumn(self, column: XPropertySet_bc180bfa, ascending: bool) -> None:
        """
        appends an additional part to the sort order criteria of the select statement.
        
        The column must be a com.sun.star.sdbcx.Column.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def setFilter(self, filter: str) -> None:
        """
        makes it possible to set a filter condition for the query.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def setGroup(self, group: str) -> None:
        """
        makes it possible to set a group for the query.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def setHavingClause(self, filter: str) -> None:
        """
        makes it possible to set a HAVING filter condition for the query.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def setOrder(self, order: str) -> None:
        """
        makes it possible to set a sort condition for the query.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def setStructuredFilter(self, filter: typing.Tuple[typing.Tuple[PropertyValue_c9610c73, ...], ...]) -> None:
        """
        appends a new set of filter criteria which is split into levels.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def setStructuredHavingClause(self, filter: typing.Tuple[typing.Tuple[PropertyValue_c9610c73, ...], ...]) -> None:
        """
        appends a new set of HAVING filter criteria which is split into levels.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    @abstractproperty
    def ElementaryQuery(self) -> str:
        """
        sets a new elementary query for the composer
        
        An elementary query or statement is a (single select) statement whose parts are not covered by the various set and get methods of the composer. That is, if the elementary statement contains a filter clause, a call to XSingleSelectQueryAnalyzer.getFilter() will not return you this filter. Instead, only filters which have been set using for instance setFilter() are covered by the get methods.
        
        The only methods which take all parts of the elementary statement into account are XSingleSelectQueryAnalyzer.getQuery() and XSingleSelectQueryAnalyzer.getQueryWithSubstitution(), which always returns the complete composed query.
        
        As a result, you can use the composer to build cumulative filter expressions. That is, you can set ElementaryQuery to a statement already containing filters, and then use setFilter() to append additional filters.
        
        The very same holds for sort orders, HAVING and GROUP BY clauses.
        
        There are various use cases for this. For instance, you might want to use the statement represented by a QueryDefinition, and extend it with additional filters or sort orders, while not touching the respective parts already present in QueryDefinition.Command. This can be achieved by setting the QueryDefinition.Command as ElementaryQuery of a SingleSelectQueryComposer.
        
        If, in such a scenario, you would be interested in the filter part of the QueryDefinition.Command, you would set it via XSingleSelectQueryAnalyzer.setQuery(), and retrieve the filter part via XSingleSelectQueryAnalyzer.getFilter().
        
        If you'd be interested in the composed filter, you would set the QueryDefinition.Command as ElementaryQuery, add your filter, and propagate the resulting query (XSingleSelectQueryAnalyzer.getQuery()) to an SingleSelectQueryAnalyzer instance via XSingleSelectQueryAnalyzer.setQuery().
        """
        ...


__all__ = ['XSingleSelectQueryComposer']


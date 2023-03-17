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
# Libre Office Version: 7.4
# Namespace: com.sun.star.form.component
import typing
from abc import abstractproperty
from ..data_aware_control_model import DataAwareControlModel as DataAwareControlModel_27110ef8
from .list_box import ListBox as ListBox_f1530d82
if typing.TYPE_CHECKING:
    from ..list_source_type import ListSourceType as ListSourceType_c9850c6b

class DatabaseListBox(DataAwareControlModel_27110ef8, ListBox_f1530d82):
    """
    Service Class

    This service specifies a data-aware list box control model.
    
    The base service for list boxes (ListBox) offers only one possibility to specify the list entries: The display strings in the com.sun.star.awt.UnoControlListBoxModel.StringItemList property and the corresponding values in the ListBox.ListSource property.
    
    This service here extends this mimic. It allows to fill the list from a data source. This means that a second result set is opened, which works on the same connection as the form which the list box belongs to, but can be based on an arbitrary table or SQL statement.
    
    For instance, you may have a form which is bound to a table invoice, and you use it to enter invoices for your customers. Probably, you will have a second table (say customer), which (among other data) contains a unique key for identifying customers. In your invoice table, you will have a foreign key referring to these customers.Now, besides the result set the form is based on (all your invoices), the list box can be instructed to open a second result set, this time for the customer table, and fill its list with entries from this result set.Additionally, it allows to model the relation between the two tables: When the user selects a customer from the list, this customer has the unique id we just talked about (which is not necessarily visible to the user in any way). The list box then automatically transfers this id into the foreign key column of invoice, thus allowing the user to transparently work with human-readable strings instead of pure numbers.Let's call this result set the list is filled from the list result set here ...
    
    The display strings are always taken from the first column of that result set, and the corresponding value as per the BoundColumn property.

    See Also:
        `API DatabaseListBox <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1DatabaseListBox.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.DatabaseListBox'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def SelectedValues(self) -> 'typing.Tuple[object, ...]':
        """
        The selected values.
        """
        ...

    @abstractproperty
    def BoundColumn(self) -> int:
        """
        specifies which column of the list result set should be used for data exchange.
        
        When you make a selection from a list box, the \"BoundColumn\" property reflects which column value of a result set should be used as the value of the component. If the control is bound to a database field, the column value is stored in the database field identified by the property com.sun.star.form.DataAwareControlModel.DataField.
        
        The bound column property is only used if a list source is defined and the list source matches with the types com.sun.star.form.ListSourceType.TABLE, com.sun.star.form.ListSourceType.QUERY, com.sun.star.form.ListSourceType.SQL or com.sun.star.form.ListSourceType.SQLPASSTHROUGH. Otherwise the property is ignored, as there is no result set from which to get the column values.
        """
        ...

    @abstractproperty
    def ListSourceType(self) -> 'ListSourceType_c9850c6b':
        """
        describes the kind of list source used.
        
        Depending on the value of this property, the way the value of ListBox.ListSource is evaluated varies.
        """
        ...

    @abstractproperty
    def SelectedValue(self) -> object:
        """
        The selected value, if there is at most one.
        """
        ...



__all__ = ['DatabaseListBox']


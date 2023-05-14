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
# Namespace: com.sun.star.awt.grid
import typing
from .x_sortable_mutable_grid_data_model import XSortableMutableGridDataModel as XSortableMutableGridDataModel_f6af1377
if typing.TYPE_CHECKING:
    from .x_mutable_grid_data_model import XMutableGridDataModel as XMutableGridDataModel_6387103b
    from ...i18n.x_collator import XCollator as XCollator_892a09e0

class SortableGridDataModel(XSortableMutableGridDataModel_f6af1377):
    """
    Service Class

    provides a default implementation of a XSortableGridData.
    
    This service must be created with a secondary grid data model, which all actual data requests are delegated to. But before providing this data to the service's own clients, it is sorted, according to the sort order defined via the XSortableGridData interface.
    
    The service implementation is able to compare the default scalar types, plus strings.
    
    For determining the data type of a column which the data should be sorted by, the first non-VOID data encountered in this column is taken into account. Further read requests to this column will assume that all non-VOID data is of the same type.
    
    Consequently, you cannot use this service with data sets containing heterogeneous data in a given column.
    
    All requests made via the XMutableGridDataModel are delegated to the XMutableGridDataModel instance passed in the service constructor.
    
    Note that changing the data might result in the sort order being destroyed. If you want to ensure that the data represented by the model is still sorted after your modifications, you should call XSortableGridData.sortByColumn(), again.

    See Also:
        `API SortableGridDataModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1grid_1_1SortableGridDataModel.html>`_
    """
    def create(self, DelegatorModel: 'XMutableGridDataModel_6387103b') -> None:
        """
        creates a new instance of the SortableGridDataModel
        
        For string comparison, a default com.sun.star.i18n.Collator, based on the system's locale, will be used.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def createWithCollator(self, DelegatorModel: 'XMutableGridDataModel_6387103b', Collator: 'XCollator_892a09e0') -> None:
        """
        creates a new instance of the ScortableDefaultGridDataModel, passing a collator to be used for string comparison.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


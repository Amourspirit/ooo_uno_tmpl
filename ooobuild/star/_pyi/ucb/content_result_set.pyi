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
# Namespace: com.sun.star.ucb
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..sdbc.result_set import ResultSet as ResultSet_8ecf0a4f
from ..sdbc.x_closeable import XCloseable as XCloseable_98290a86
from ..sdbc.x_result_set import XResultSet as XResultSet_98e30aa7
from ..sdbc.x_result_set_meta_data_supplier import XResultSetMetaDataSupplier as XResultSetMetaDataSupplier_777010fc
from ..sdbc.x_row import XRow as XRow_5f360834
from .x_content_access import XContentAccess as XContentAccess_ba220bc7

class ContentResultSet(ResultSet_8ecf0a4f, XPropertySet_bc180bfa, XComponent_98dc0ab5, XCloseable_98290a86, XResultSet_98e30aa7, XResultSetMetaDataSupplier_777010fc, XRow_5f360834, XContentAccess_ba220bc7):
    """
    Service Class

    provides access to the children of a folder content.
    
    It can be understand as a table containing a row for each child. The table columns may contain values of properties of the children.

    See Also:
        `API ContentResultSet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ucb_1_1ContentResultSet.html>`_
    """
    @property
    def CursorTravelMode(self) -> int:
        """
        controls the travel mode of the result set cursor.
        
        There are two possible travel modes:
        
        The following pseudo-code illustrates the usage of a non-blocking cursor:
        
        If this property is not supported, the implementation needs to provide a blocking cursor.
        
        The implementation initially needs to set the value of this property to CursorTravelMode.BLOCKING.
        """
        ...
    @property
    def IsRowCountFinal(self) -> bool:
        """
        indicates that all rows of the result set have been obtained.
        """
        ...
    @property
    def RowCount(self) -> int:
        """
        contains the number of rows obtained (so far) from the data source.
        """
        ...



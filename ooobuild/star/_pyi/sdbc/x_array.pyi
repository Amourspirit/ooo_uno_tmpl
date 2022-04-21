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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
    from .x_result_set import XResultSet as XResultSet_98e30aa7

class XArray(XInterface_8f010a43):
    """
    is used for mapping the SQL type com.sun.star.sdbc.DataType.ARRAY.
    
    By default, an Array is a transaction duration reference to an SQL array. By default, an Array is implemented using a SQL LOCATOR(array) internally.

    See Also:
        `API XArray <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XArray.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdbc.XArray']

    def getArray(self, typeMap: 'XNameAccess_e2ab0cf6') -> 'typing.Tuple[object, ...]':
        """
        retrieves the contents of the SQL array designated by this Array object, using the specified typeMap for type map customizations.
        
        If the base type of the array does not match a user-defined type in typeMap , the standard mapping is used instead.

        Raises:
            SQLException: ``SQLException``
        """
    def getArrayAtIndex(self, index: int, count: int, typeMap: 'XNameAccess_e2ab0cf6') -> 'typing.Tuple[object, ...]':
        """
        returns an array containing a slice of the SQL array, beginning with the specified index and containing up to count successive elements of the SQL array.

        Raises:
            SQLException: ``SQLException``
        """
    def getBaseType(self) -> int:
        """
        returns the SDBC type of the elements in the array designated by this Array object.

        Raises:
            SQLException: ``SQLException``
        """
    def getBaseTypeName(self) -> str:
        """
        returns the SQL type name of the elements in the array designated by this Array object.
        
        If the elements are a built-in type, it returns the database-specific type name of the elements. If the elements are a user-defined type (UDT), this method returns the fully-qualified SQL type name.

        Raises:
            SQLException: ``SQLException``
        """
    def getResultSet(self, typeMap: 'XNameAccess_e2ab0cf6') -> 'XResultSet_98e30aa7':
        """
        returns a result set that contains the elements of the array designated by this Array object and uses the given typeMap to map the array elements.
        
        If the base type of the array does not match a user-defined type in typeMap or the typeMap is NULL , the connection type mapping is used instead.
        
        The result set contains one row for each array element, with two columns in each row. The second column stores the element value; the first column stores the index into the array for that element (with the first array element being at index 1). The rows are in ascending order corresponding to the order of the indices.

        Raises:
            SQLException: ``SQLException``
        """
    def getResultSetAtIndex(self, index: int, count: int, typeMap: 'XNameAccess_e2ab0cf6') -> 'XResultSet_98e30aa7':
        """
        returns a result set holding the elements of the subarray that starts at index index and contains up to count successive elements.
        
        This method uses the given typeMap to map the array elements. If the base type of the array does not match a user-defined type in typeMap or the typeMap is NULL , the connection type mapping is used instead.
        
        The result set contains one row for each array element, with two columns in each row. The second column stores the element value; the first column stores the index into the array for that element (with the first array element being at index 1). The rows are in ascending order corresponding to the order of the indices.

        Raises:
            SQLException: ``SQLException``
        """


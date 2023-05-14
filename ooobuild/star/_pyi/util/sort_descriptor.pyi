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
# Namespace: com.sun.star.util
import typing
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class SortDescriptor(XPropertySet_bc180bfa):
    """
    Service Class

    specifies the properties which can be used to describe a sort order applied to an XSortable.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API SortDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1util_1_1SortDescriptor.html>`_
    """
    @property
    def CollatorAlgorithm(self) -> str:
        """
        specifies the algorithm for the compare operator (collator).
        
        The collator algorithm may be defined for separate keys in specific implementations. For those this property may not need to be set.
        """
        ...

    @CollatorAlgorithm.setter
    def CollatorAlgorithm(self, value: str) -> None:
        ...
    @property
    def CollatorLocale(self) -> 'Locale_70d308fa':
        """
        specifies the locale for the compare operator (collator).
        """
        ...

    @CollatorLocale.setter
    def CollatorLocale(self, value: 'Locale_70d308fa') -> None:
        ...
    @property
    def IsCaseSensitive(self) -> bool:
        """
        specifies if the case of letters is important when comparing entries.
        """
        ...

    @IsCaseSensitive.setter
    def IsCaseSensitive(self, value: bool) -> None:
        ...
    @property
    def SortAscending(self) -> bool:
        """
        specifies the sorting order.
        
        The sorting order may be defined for separate keys in specific implementations. For those this property may not need to be set.
        """
        ...

    @SortAscending.setter
    def SortAscending(self, value: bool) -> None:
        ...
    @property
    def SortColumns(self) -> bool:
        """
        specifies if the columns are sorted.
        """
        ...

    @SortColumns.setter
    def SortColumns(self, value: bool) -> None:
        ...


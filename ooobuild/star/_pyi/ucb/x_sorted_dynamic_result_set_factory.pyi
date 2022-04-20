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
# Namespace: com.sun.star.ucb
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .numbered_sorting_info import NumberedSortingInfo as NumberedSortingInfo_fd0e0de6
    from .x_any_compare_factory import XAnyCompareFactory as XAnyCompareFactory_ec090d61
    from .x_dynamic_result_set import XDynamicResultSet as XDynamicResultSet_e0360d0a

class XSortedDynamicResultSetFactory(XInterface_8f010a43):
    """
    Provides a method to create an XDynamicResultSet which will be sorted according to the given sorting options.

    See Also:
        `API XSortedDynamicResultSetFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XSortedDynamicResultSetFactory.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ucb.XSortedDynamicResultSetFactory']

    def createSortedDynamicResultSet(self, Source: 'XDynamicResultSet_e0360d0a', Info: 'typing.Tuple[NumberedSortingInfo_fd0e0de6, ...]', CompareFactory: 'XAnyCompareFactory_ec090d61') -> 'XDynamicResultSet_e0360d0a':
        """
        creates a sorted XDynamicResultSet depending on internal data, an (unsorted) XDynamicResultSet and the sorting info.
        """


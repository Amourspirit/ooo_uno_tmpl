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
# Namespace: com.sun.star.sdb
import typing
from abc import abstractmethod
from ..ui.dialogs.x_executable_dialog import XExecutableDialog as XExecutableDialog_450f0fa1
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924
    from .x_single_select_query_composer import XSingleSelectQueryComposer as XSingleSelectQueryComposer_66e310b9
    from ..sdbc.x_row_set import XRowSet as XRowSet_7a090960

class FilterDialog(XExecutableDialog_450f0fa1):
    """
    Service Class

    This interface could be incomplete since I derived it from its places of use.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API FilterDialog <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1FilterDialog.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.FilterDialog'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createDefault(self) -> None:
        """
        """
        ...
    @abstractmethod
    def createWithQuery(self, QueryComposer: 'XSingleSelectQueryComposer_66e310b9', RowSet: 'XRowSet_7a090960', ParentWindow: 'XWindow_713b0924') -> None:
        """
        """
        ...


__all__ = ['FilterDialog']


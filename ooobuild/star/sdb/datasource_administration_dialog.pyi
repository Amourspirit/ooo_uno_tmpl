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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from __future__ import annotations
import typing
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
from ..ui.dialogs.x_executable_dialog import XExecutableDialog as XExecutableDialog_450f0fa1
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924

class DatasourceAdministrationDialog(XPropertySet_bc180bfa, XInitialization_d46c0cca, XExecutableDialog_450f0fa1):
    """
    Service Class

    provides a user interface for administrating the system wide registered data sources.
    
    Here, system wide registered means registered on the (one and only) instance of the com.sun.star.sdb.DatabaseContext service.

    See Also:
        `API DatasourceAdministrationDialog <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1DatasourceAdministrationDialog.html>`_
    """
    @property
    def ParentWindow(self) -> XWindow_713b0924:
        """
        parent window to use for the administration dialog
        
        This property can't be set while the dialog is being displayed.
        """
        ...
    @ParentWindow.setter
    def ParentWindow(self, value: XWindow_713b0924) -> None:
        ...
    @property
    def Title(self) -> str:
        """
        the title of the (dialog) window
        """
        ...
    @Title.setter
    def Title(self, value: str) -> None:
        ...


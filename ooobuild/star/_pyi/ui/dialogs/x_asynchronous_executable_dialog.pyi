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
# Namespace: com.sun.star.ui.dialogs
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_dialog_closed_listener import XDialogClosedListener as XDialogClosedListener_85ff113f

class XAsynchronousExecutableDialog(XInterface_8f010a43):
    """
    Specifies an interface for an executable dialog in asynchronous mode.

    See Also:
        `API XAsynchronousExecutableDialog <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XAsynchronousExecutableDialog.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.dialogs.XAsynchronousExecutableDialog']

    def setDialogTitle(self, aTitle: str) -> None:
        """
        Sets the title of the dialog.
        """
        ...
    def startExecuteModal(self, xListener: 'XDialogClosedListener_85ff113f') -> None:
        """
        Executes (shows) the dialog and returns immediately.
        """
        ...



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
# Namespace: com.sun.star.awt
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XDialog(XInterface_8f010a43):
    """
    makes it possible to show and hide a dialog and gives access to the title of the dialog.

    See Also:
        `API XDialog <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XDialog.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XDialog']

    def endExecute(self) -> None:
        """
        hides the dialog and then causes XDialog.execute() to return.
        """
        ...
    def execute(self) -> int:
        """
        shows the dialog.
        """
        ...
    def getTitle(self) -> str:
        """
        gets the title of the dialog.
        """
        ...
    def setTitle(self, Title: str) -> None:
        """
        sets the title of the dialog.
        """
        ...



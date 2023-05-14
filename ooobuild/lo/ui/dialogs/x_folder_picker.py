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
from abc import abstractmethod
from .x_executable_dialog import XExecutableDialog as XExecutableDialog_450f0fa1

class XFolderPicker(XExecutableDialog_450f0fa1):
    """
    Specifies a FolderPicker interface.

    See Also:
        `API XFolderPicker <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XFolderPicker.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.XFolderPicker'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XFolderPicker'

    @abstractmethod
    def getDirectory(self) -> str:
        """
        Returns the selected directory as url conforming to Rfc1738.
        """
        ...
    @abstractmethod
    def getDisplayDirectory(self) -> str:
        """
        Returns the root directory that the FolderPicker is showing.
        
        The return value is undefined if the client did not choose a root directory or the previously specified root directory doesn't exist.
        """
        ...
    @abstractmethod
    def setDescription(self, aDescription: str) -> None:
        """
        The implementation may optionally show the given text as a description for the user within the dialog, e.g.
        
        \"Please select a directory\". If the client doesn't set a description the dialog may show a default description.
        """
        ...
    @abstractmethod
    def setDisplayDirectory(self, aDirectory: str) -> None:
        """
        Sets the root directory that the FolderPicker should display.
        
        It is not specified which root directory the FolderPicker chooses if the specified root directory doesn't exist.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XFolderPicker']


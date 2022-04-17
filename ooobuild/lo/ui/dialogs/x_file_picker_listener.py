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
# Libre Office Version: 7.3
# Namespace: com.sun.star.ui.dialogs
import typing
from abc import abstractmethod
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .file_picker_event import FilePickerEvent as FilePickerEvent_25670ed7

class XFilePickerListener(XEventListener_c7230c4a):
    """
    Interface to be implemented by a FilePicker listener.
    
    The XFilePickerListener interface must be implemented by the clients of the FilePicker service which need to be informed about events while the FilePicker service is displayed.

    See Also:
        `API XFilePickerListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XFilePickerListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.XFilePickerListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XFilePickerListener'

    @abstractmethod
    def controlStateChanged(self, aEvent: 'FilePickerEvent_25670ed7') -> None:
        """
        A client receives this event if the state of a control within the FilePicker service dialog changes.
        """
    @abstractmethod
    def dialogSizeChanged(self) -> None:
        """
        A client receives this event if the size of the FilePicker dialog has changed.
        
        If the FilePicker dialog contains a preview the client may ask for the new dimension of the preview area.
        """
    @abstractmethod
    def directoryChanged(self, aEvent: 'FilePickerEvent_25670ed7') -> None:
        """
        A client receives this event if the directory selection within the FilePicker dialog changes.
        """
    @abstractmethod
    def fileSelectionChanged(self, aEvent: 'FilePickerEvent_25670ed7') -> None:
        """
        A client receives this event if the file selection within the FilePicker service dialog changes.
        """
    @abstractmethod
    def helpRequested(self, aEvent: 'FilePickerEvent_25670ed7') -> str:
        """
        A client receives this event if the F1 key or the help button was pressed.
        """

__all__ = ['XFilePickerListener']

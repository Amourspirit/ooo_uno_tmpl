# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.ui.dialogs


class CommonFilePickerElementIds(object):
    """
    Const Class

    These constants are used to specify common controls of a FilePicker dialog.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API CommonFilePickerElementIds <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1CommonFilePickerElementIds.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.CommonFilePickerElementIds'
    __ooo_type_name__: str = 'const'

    PUSHBUTTON_OK = 1
    """
    The control id of the OK button.
    """
    PUSHBUTTON_CANCEL = 2
    """
    The control id of the Cancel button.
    """
    LISTBOX_FILTER = 3
    """
    The filter listbox of a FilePicker dialog.
    """
    CONTROL_FILEVIEW = 4
    """
    Is used to refer to the file view of the file picker.
    
    This view shows the list of all files/folders in the currently selected folder.
    """
    EDIT_FILEURL = 5
    """
    Is used to refer to the edit line where a file or path can be entered by the user.
    """
    LISTBOX_FILTER_LABEL = 6
    """
    The label of the filter listbox of a FilePicker dialog.
    
    **since**
    
        OOo 1.1.2
    """
    EDIT_FILEURL_LABEL = 7
    """
    The label of the file name listbox of a FilePicker dialog.
    
    **since**
    
        OOo 1.1.2
    """

__all__ = ['CommonFilePickerElementIds']

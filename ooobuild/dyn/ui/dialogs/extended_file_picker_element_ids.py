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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.ui.dialogs
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.ui.dialogs import ExtendedFilePickerElementIds as ExtendedFilePickerElementIds
    if hasattr(ExtendedFilePickerElementIds, '_constants') and isinstance(ExtendedFilePickerElementIds._constants, dict):
        ExtendedFilePickerElementIds._constants['__ooo_ns__'] = 'com.sun.star.ui.dialogs'
        ExtendedFilePickerElementIds._constants['__ooo_full_ns__'] = 'com.sun.star.ui.dialogs.ExtendedFilePickerElementIds'
        ExtendedFilePickerElementIds._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global ExtendedFilePickerElementIdsEnum
        ls = [f for f in dir(ExtendedFilePickerElementIds) if not callable(getattr(ExtendedFilePickerElementIds, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(ExtendedFilePickerElementIds, name)
        ExtendedFilePickerElementIdsEnum = IntEnum('ExtendedFilePickerElementIdsEnum', _dict)
    build_enum()
else:
    from ....lo.ui.dialogs.extended_file_picker_element_ids import ExtendedFilePickerElementIds as ExtendedFilePickerElementIds

    class ExtendedFilePickerElementIdsEnum(IntEnum):
        """
        Enum of Const Class ExtendedFilePickerElementIds

        These constants are used to specify extended controls of a FilePicker dialog. A FilePicker service may be initialized so that it has additional controls extending the set of common controls a FilePicker usually supports.
        
        **since**
        
            LibreOffice 6.0
        """
        CHECKBOX_AUTOEXTENSION = ExtendedFilePickerElementIds.CHECKBOX_AUTOEXTENSION
        CHECKBOX_PASSWORD = ExtendedFilePickerElementIds.CHECKBOX_PASSWORD
        CHECKBOX_FILTEROPTIONS = ExtendedFilePickerElementIds.CHECKBOX_FILTEROPTIONS
        CHECKBOX_READONLY = ExtendedFilePickerElementIds.CHECKBOX_READONLY
        CHECKBOX_LINK = ExtendedFilePickerElementIds.CHECKBOX_LINK
        CHECKBOX_PREVIEW = ExtendedFilePickerElementIds.CHECKBOX_PREVIEW
        PUSHBUTTON_PLAY = ExtendedFilePickerElementIds.PUSHBUTTON_PLAY
        LISTBOX_VERSION = ExtendedFilePickerElementIds.LISTBOX_VERSION
        LISTBOX_TEMPLATE = ExtendedFilePickerElementIds.LISTBOX_TEMPLATE
        LISTBOX_IMAGE_TEMPLATE = ExtendedFilePickerElementIds.LISTBOX_IMAGE_TEMPLATE
        CHECKBOX_SELECTION = ExtendedFilePickerElementIds.CHECKBOX_SELECTION
        LISTBOX_VERSION_LABEL = ExtendedFilePickerElementIds.LISTBOX_VERSION_LABEL
        LISTBOX_TEMPLATE_LABEL = ExtendedFilePickerElementIds.LISTBOX_TEMPLATE_LABEL
        LISTBOX_IMAGE_TEMPLATE_LABEL = ExtendedFilePickerElementIds.LISTBOX_IMAGE_TEMPLATE_LABEL
        LISTBOX_FILTER_SELECTOR = ExtendedFilePickerElementIds.LISTBOX_FILTER_SELECTOR
        CHECKBOX_GPGENCRYPTION = ExtendedFilePickerElementIds.CHECKBOX_GPGENCRYPTION
        LISTBOX_IMAGE_ANCHOR = ExtendedFilePickerElementIds.LISTBOX_IMAGE_ANCHOR
        LISTBOX_IMAGE_ANCHOR_LABEL = ExtendedFilePickerElementIds.LISTBOX_IMAGE_ANCHOR_LABEL

__all__ = ['ExtendedFilePickerElementIds', 'ExtendedFilePickerElementIdsEnum']
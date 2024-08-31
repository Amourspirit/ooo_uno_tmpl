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


class ListboxControlActions(object):
    """
    Const Class

    These constants are deprecated and should not be used anymore.
    
    They're superseded by ControlActions.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API ListboxControlActions <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1ListboxControlActions.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.ListboxControlActions'
    __ooo_type_name__: str = 'const'

    ADD_ITEM = 1
    """
    Adds an item to the content of the listbox.
    
    The given item has to be a string.
    """
    ADD_ITEMS = 2
    """
    Adds a sequence of strings to the content of the listbox.
    """
    DELETE_ITEM = 3
    """
    Removes an item from a listbox.
    
    The given value has to be a position. If the position is invalid an exception will be thrown. The index of the first position is 0. The value should be a sal_Int32.
    """
    DELETE_ITEMS = 4
    """
    Removes all items from the listbox.
    """
    SET_SELECT_ITEM = 5
    """
    Selects an item in a listbox.
    
    The given value has to be a position. The index of the first position is 0. A value of -1 removes the selection. If the given position is invalid an exception will be thrown. The value should be a sal_Int32.
    """
    GET_ITEMS = 6
    """
    Returns all items of the listbox as a sequence of strings.
    """
    GET_SELECTED_ITEM = 7
    """
    Returns the currently selected item.
    
    The returned item is an empty string if the listbox is empty or no item is selected.
    """

__all__ = ['ListboxControlActions']

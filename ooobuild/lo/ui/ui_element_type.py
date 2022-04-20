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
# Libre Office Version: 7.2
# Namespace: com.sun.star.ui


class UIElementType(object):
    """
    Const Class

    determine the type of a user interface element which is controlled by a layout manager.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UIElementType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui_1_1UIElementType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.UIElementType'
    __ooo_type_name__: str = 'const'

    UNKNOWN = 0
    """
    unknown user interface element type, which can be used as a wildcard to specify all types.
    """
    MENUBAR = 1
    """
    specifies a menu bar.
    """
    POPUPMENU = 2
    """
    specifies a pop-up menu.
    """
    TOOLBAR = 3
    """
    specifies a toolbar.
    """
    STATUSBAR = 4
    """
    specifies a statusbar.
    """
    FLOATINGWINDOW = 5
    """
    specifies a floating window, which can also be docked.
    """
    PROGRESSBAR = 6
    """
    specifies a floating window, which can also be docked.
    """
    TOOLPANEL = 7
    """
    specifies a tool panel
    """
    DOCKINGWINDOW = 7
    """
    specifies a window that can be docked.
    """
    COUNT = 8
    """
    specifies the number of constants.
    """

__all__ = ['UIElementType']

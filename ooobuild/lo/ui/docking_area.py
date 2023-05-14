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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ui
# Libre Office Version: 7.4
from enum import Enum


class DockingArea(Enum):
    """
    Enum Class

    

    See Also:
        `API DockingArea <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui.html#abab7084b80a737f798ccebf692878cc1>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.DockingArea'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.ui.DockingArea'

    DOCKINGAREA_BOTTOM = 'DOCKINGAREA_BOTTOM'
    """
    the bottom docking area above the status bar.
    """
    DOCKINGAREA_DEFAULT = 'DOCKINGAREA_DEFAULT'
    """
    a default docking area.
    
    It depends on the implementation how to treat this value.
    """
    DOCKINGAREA_LEFT = 'DOCKINGAREA_LEFT'
    """
    the left side docking area.
    """
    DOCKINGAREA_RIGHT = 'DOCKINGAREA_RIGHT'
    """
    the right side docking area.
    """
    DOCKINGAREA_TOP = 'DOCKINGAREA_TOP'
    """
    the top docking area below the menu bar.
    """

__all__ = ['DockingArea']


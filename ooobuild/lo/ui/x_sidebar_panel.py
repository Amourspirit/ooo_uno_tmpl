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
# Namespace: com.sun.star.ui
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .layout_size import LayoutSize as LayoutSize_84cd09ff

class XSidebarPanel(ABC):
    """
    Optional interface of sidebar panels.

    See Also:
        `API XSidebarPanel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XSidebarPanel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui'
    __ooo_full_ns__: str = 'com.sun.star.ui.XSidebarPanel'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.XSidebarPanel'

    @abstractmethod
    def getHeightForWidth(self, nWidth: int) -> LayoutSize_84cd09ff:
        """
        For a given width of the container the layouter asks every ui element for its optimal height.
        
        The height to which a ui element is set may differ from the returned value.
        
        The height is set via the XWindow interface.
        """
        ...
    @abstractmethod
    def getMinimalWidth(self) -> int:
        """
        Minimal possible width of this panel in pixels.
        
        If this value is smaller than the maximum allowed size of the Sidebar (see config option 'org.openoffice.Office.UI.Sidebar.General.MaximumWidth'), the config option will be ignored and the new maximum Sidebar width will be getMinimalWidth() + 100px.
        """
        ...

__all__ = ['XSidebarPanel']



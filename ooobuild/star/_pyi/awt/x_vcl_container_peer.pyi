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
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_window import XWindow as XWindow_713b0924

class XVclContainerPeer(XInterface_8f010a43):
    """
    gives access to the VCL container window implementation.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XVclContainerPeer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XVclContainerPeer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XVclContainerPeer']

    def enableDialogControl(self, bEnable: bool) -> None:
        """
        enable as dialog control.
        """
    def setGroup(self, Windows: 'typing.Tuple[XWindow_713b0924, ...]') -> None:
        """
        sets a group.
        """
    def setTabOrder(self, WindowOrder: 'typing.Tuple[XWindow_713b0924, ...]', Tabs: 'typing.Tuple[object, ...]', GroupControl: bool) -> None:
        """
        sets the tab order.
        """


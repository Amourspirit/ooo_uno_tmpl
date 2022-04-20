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
# Namespace: com.sun.star.ui
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .context_menu_execute_event import ContextMenuExecuteEvent as ContextMenuExecuteEvent_2a210f35
    from .context_menu_interceptor_action import ContextMenuInterceptorAction as ContextMenuInterceptorAction_7cf4114d

class XContextMenuInterceptor(XInterface_8f010a43):
    """
    This interface enables the object to be registered as interceptor to change context menus or prevent them from being executed.

    See Also:
        `API XContextMenuInterceptor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XContextMenuInterceptor.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.XContextMenuInterceptor']

    def notifyContextMenuExecute(self, aEvent: 'ContextMenuExecuteEvent_2a210f35') -> 'ContextMenuInterceptorAction_7cf4114d':
        """
        notifies the interceptor about the request to execute a ContextMenu.
        
        The interceptor has to decide whether the menu should be executed with or without being modified or may ignore the call.
        """


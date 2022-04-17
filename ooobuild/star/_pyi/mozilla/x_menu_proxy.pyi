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
# Namespace: com.sun.star.mozilla
from typing_extensions import Literal
import typing
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .x_menu_proxy_listener import XMenuProxyListener as XMenuProxyListener_2ccf0f55

class XMenuProxy(XComponent_98dc0ab5):
    """
    Allows to execute dispatch for a menu item and handles listeners for changes in menu items.

    See Also:
        `API XMenuProxy <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1mozilla_1_1XMenuProxy.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.mozilla.XMenuProxy']

    def addMenuProxyListener(self, xListener: 'XMenuProxyListener_2ccf0f55') -> None:
        """
        Registers an event listener, which will be called when the menu changes.
        """
    def executeMenuItem(self, ID: int) -> None:
        """
        Executes dispatch for the given menu id.
        """
    def removeMenuProxyListener(self, xListener: 'XMenuProxyListener_2ccf0f55') -> None:
        """
        Unregisters an event listener which was registered with XMenuProxy.addMenuProxyListener().
        """


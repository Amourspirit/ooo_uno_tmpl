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
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..beans.named_value import NamedValue as NamedValue_a37a0af3

class XTabListener(XEventListener_c7230c4a):
    """
    such listener will be informed if tab's was inserted/removed from an XSimpleTabController instance or if the properties of a tab was changed.

    See Also:
        `API XTabListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XTabListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XTabListener']

    def activated(self, ID: int) -> None:
        """
        a tab was activated (e.g.
        
        by using mouse/keyboard or method XSimpleTabController.activateTab()
        """
        ...
    def changed(self, ID: int, Properties: 'typing.Tuple[NamedValue_a37a0af3, ...]') -> None:
        """
        a tab was changed within its properties.
        """
        ...
    def deactivated(self, ID: int) -> None:
        """
        a tab was deactivated, because another tab became the new active state.
        """
        ...
    def inserted(self, ID: int) -> None:
        """
        a new tab was inserted.
        """
        ...
    def removed(self, ID: int) -> None:
        """
        a tab was removed.
        """
        ...



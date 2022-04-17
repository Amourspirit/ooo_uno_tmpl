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
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .item_event import ItemEvent as ItemEvent_845d09e5

class XItemListener(XEventListener_c7230c4a):
    """
    makes it possible to receive events from a component when the state of an item changes.

    See Also:
        `API XItemListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XItemListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XItemListener']

    def itemStateChanged(self, rEvent: 'ItemEvent_845d09e5') -> None:
        """
        is invoked when an item changes its state.
        """


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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .adjustment_event import AdjustmentEvent as AdjustmentEvent_c9280c75


class XAdjustmentListener(XEventListener_c7230c4a):
    """
    makes it possible to receive adjustment events.

    See Also:
        `API XAdjustmentListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XAdjustmentListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XAdjustmentListener'

    def adjustmentValueChanged(self, rEvent: AdjustmentEvent_c9280c75) -> None:
        """
        is invoked when the adjustment has changed.
        """
        ...



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
# Namespace: com.sun.star.beans
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .property_change_event import PropertyChangeEvent as PropertyChangeEvent_1b180ebe


class XVetoableChangeListener(XEventListener_c7230c4a):
    """
    is used to receive PropertyChangeEvents whenever a \"constrained\" property is changed.
    
    You can register an XVetoableChangeListener with a source object so as to be notified of any constrained property updates.

    See Also:
        `API XVetoableChangeListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XVetoableChangeListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.beans.XVetoableChangeListener'

    def vetoableChange(self, aEvent: PropertyChangeEvent_1b180ebe) -> None:
        """
        gets called when a constrained property is changed.

        Raises:
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
        """
        ...



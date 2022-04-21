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
# Namespace: com.sun.star.awt.grid
from typing_extensions import Literal
import typing
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .grid_column_event import GridColumnEvent as GridColumnEvent_8920e1e

class XGridColumnListener(XEventListener_c7230c4a):
    """
    An instance of this interface is used by the XGridColumnModel to get notifications about column model changes.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XGridColumnListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XGridColumnListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.grid.XGridColumnListener']

    def columnChanged(self, event: 'GridColumnEvent_8920e1e') -> None:
        """
        Invoked after a column was modified.
        """


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
# Namespace: com.sun.star.form
from typing_extensions import Literal
import typing
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XUpdateListener(XEventListener_c7230c4a):
    """
    used to listen on objects which allow updating their data.
    
    In addition to just get notified when a data update happened, the listener has a chance to veto updates before they happen.

    See Also:
        `API XUpdateListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XUpdateListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.XUpdateListener']

    def approveUpdate(self, aEvent: 'EventObject_a3d70b03') -> bool:
        """
        is invoked to check the current data.
        
        For a given update process, if one of the XUpdateListeners vetoes the change, the update is canceled, and no further notification happens.
        """
    def updated(self, aEvent: 'EventObject_a3d70b03') -> None:
        """
        is invoked when an object has finished processing the updates and the data has been successfully written.
        """


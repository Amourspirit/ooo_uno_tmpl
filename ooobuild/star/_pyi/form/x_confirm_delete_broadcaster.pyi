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
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_confirm_delete_listener import XConfirmDeleteListener as XConfirmDeleteListener_37920f7b

class XConfirmDeleteBroadcaster(XInterface_8f010a43):
    """
    provides the possibility of receiving an event for confirming deletions of rows in a com.sun.star.form.component.DataForm.

    See Also:
        `API XConfirmDeleteBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XConfirmDeleteBroadcaster.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.XConfirmDeleteBroadcaster']

    def addConfirmDeleteListener(self, aListener: 'XConfirmDeleteListener_37920f7b') -> None:
        """
        remembers the specified listener to receive an event for confirming deletions
        
        XConfirmDeleteListener.confirmDelete() is called before a deletion is performed. You may use the event to write your own confirmation messages.
        """
        ...
    def removeConfirmDeleteListener(self, aListener: 'XConfirmDeleteListener_37920f7b') -> None:
        """
        removes the specified listener.
        """
        ...



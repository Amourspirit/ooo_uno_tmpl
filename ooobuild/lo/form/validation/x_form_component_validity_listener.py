# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.form.validation
from __future__ import annotations
import typing
from abc import abstractmethod
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ...lang.event_object import EventObject as EventObject_a3d70b03

class XFormComponentValidityListener(XEventListener_c7230c4a):
    """
    is the listener interface to be notified of changes of a XValidatableFormComponent

    See Also:
        `API XFormComponentValidityListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1validation_1_1XFormComponentValidityListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.validation'
    __ooo_full_ns__: str = 'com.sun.star.form.validation.XFormComponentValidityListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.validation.XFormComponentValidityListener'

    @abstractmethod
    def componentValidityChanged(self, Source: EventObject_a3d70b03) -> None:
        """
        called when the validity and/or the value of the form component at which the listener is registered changed.
        """
        ...

__all__ = ['XFormComponentValidityListener']


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
# Namespace: com.sun.star.form.validation
import typing
from abc import abstractmethod
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ...lang.event_object import EventObject as EventObject_a3d70b03

class XValidityConstraintListener(XEventListener_c7230c4a):
    """
    specifies an interface for listening for changes in the validity constraints represented by an XValidator.

    See Also:
        `API XValidityConstraintListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1validation_1_1XValidityConstraintListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.validation'
    __ooo_full_ns__: str = 'com.sun.star.form.validation.XValidityConstraintListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.validation.XValidityConstraintListener'

    @abstractmethod
    def validityConstraintChanged(self, Source: 'EventObject_a3d70b03') -> None:
        """
        called when the validity constraint represented by an XValidator, at which the listener is registered, changed.
        """

__all__ = ['XValidityConstraintListener']


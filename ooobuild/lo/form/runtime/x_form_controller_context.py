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
# Namespace: com.sun.star.form.runtime
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ...awt.x_control import XControl as XControl_7a9c098d

class XFormControllerContext(ABC):
    """
    provides a context for a FormController
    
    A FormController knows about the controls it is responsible for, and about the control container which those controls live in. However, it doesn't know about a possible larger context, like a scrollable view which the controls are embedded into. To compensate this, it can be provided a XFormControllerContext.

    See Also:
        `API XFormControllerContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1runtime_1_1XFormControllerContext.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.runtime'
    __ooo_full_ns__: str = 'com.sun.star.form.runtime.XFormControllerContext'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.runtime.XFormControllerContext'

    @abstractmethod
    def makeVisible(self, Control: XControl_7a9c098d) -> None:
        """
        ensures the given control is visible, by scrolling the view if necessary.
        """
        ...

__all__ = ['XFormControllerContext']



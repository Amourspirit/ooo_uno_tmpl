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
# Libre Office Version: 7.4
# Namespace: com.sun.star.form
from typing_extensions import Literal
import typing
from ..awt.x_tab_controller import XTabController as XTabController_bacd0be7
if typing.TYPE_CHECKING:
    from ..awt.x_control import XControl as XControl_7a9c098d
    from .x_form_controller_listener import XFormControllerListener as XFormControllerListener_49ba1012

class XFormController(XTabController_bacd0be7):
    """
    is superseded by com.sun.star.form.runtime.XFormController.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XFormController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XFormController.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.XFormController']

    def addActivateListener(self, l: 'XFormControllerListener_49ba1012') -> None:
        """
        """
        ...
    def getCurrentControl(self) -> 'XControl_7a9c098d':
        """
        """
        ...
    def removeActivateListener(self, l: 'XFormControllerListener_49ba1012') -> None:
        """
        """
        ...



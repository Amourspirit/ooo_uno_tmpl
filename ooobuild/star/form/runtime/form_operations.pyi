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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.form.runtime
from __future__ import annotations
import typing
from .x_form_operations import XFormOperations as XFormOperations_4a450ffe
if typing.TYPE_CHECKING:
    from ..x_form import XForm as XForm_684408a8
    from .x_form_controller import XFormController as XFormController_4a570ffe

class FormOperations(XFormOperations_4a450ffe):
    """
    Service Class

    encapsulates operations on a database form which has a UI representation, and is interacting with the user.
    
    **since**
    
        OOo 2.2

    See Also:
        `API FormOperations <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1runtime_1_1FormOperations.html>`_
    """
    def createWithForm(self, Form: XForm_684408a8) -> None:
        """
        creates a FormOperations instance which works on a com.sun.star.form.component.DataForm instance.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def createWithFormController(self, Controller: XFormController_4a570ffe) -> None:
        """
        creates a FormOperations instance which works on a com.sun.star.form.FormController instance.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


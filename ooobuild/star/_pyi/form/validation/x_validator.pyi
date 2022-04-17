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
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_validity_constraint_listener import XValidityConstraintListener as XValidityConstraintListener_69a2161e

class XValidator(XInterface_8f010a43):
    """
    specifies a component able to validate (the content of) other components
    
    Validators support simple validity checks and retrieving justifications for invalidity.
    
    Validators may additionally support dynamic validity constraints. In such a case, the validity of a given value may change, without the value changing itself.
    To be notified about this, interested components should register as XValidityConstraintListener.

    See Also:
        `API XValidator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1validation_1_1XValidator.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.validation.XValidator']

    def addValidityConstraintListener(self, Listener: 'XValidityConstraintListener_69a2161e') -> None:
        """
        registers the given validity listener.
        
        Usually, an XValidatable instance will also add itself as validity listener, as soon as the validator is introduced to it.
        
        Implementations which do not support dynamic validity constraints should simply ignore this call.

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
    def explainInvalid(self, Value: object) -> str:
        """
        retrieves a justification for the invalidity of the given value
        """
    def isValid(self, Value: object) -> bool:
        """
        determines whether the given value is valid
        """
    def removeValidityConstraintListener(self, Listener: 'XValidityConstraintListener_69a2161e') -> None:
        """
        revokes the given validity listener

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """


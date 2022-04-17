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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.form.validation
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
from .x_validatable_form_component import XValidatableFormComponent as XValidatableFormComponent_3a2e150d
from .x_validity_constraint_listener import XValidityConstraintListener as XValidityConstraintListener_69a2161e

class ValidatableControlModel(FormControlModel_e2990d22, XValidatableFormComponent_3a2e150d, XValidityConstraintListener_69a2161e):
    """
    Service Class

    specifies the model of a form control which supports live validation of its input.
    
    Validatable control models support setting a validator with dynamic validity constraints, and broadcasting changes in their value as well as the validity of their value.

    See Also:
        `API ValidatableControlModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1validation_1_1ValidatableControlModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.validation'
    __ooo_full_ns__: str = 'com.sun.star.form.validation.ValidatableControlModel'
    __ooo_type_name__: str = 'service'



__all__ = ['ValidatableControlModel']


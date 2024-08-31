# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.form.component
from __future__ import annotations
from abc import abstractproperty
from ...awt.uno_control_currency_field_model import UnoControlCurrencyFieldModel as UnoControlCurrencyFieldModel_8e351187
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
from ..x_reset import XReset as XReset_71670917

class CurrencyField(UnoControlCurrencyFieldModel_8e351187, FormControlModel_e2990d22, XReset_71670917):
    """
    Service Class

    This service specifies the ControlModel for an edit field which contains a currency value.

    See Also:
        `API CurrencyField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1CurrencyField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.CurrencyField'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DefaultValue(self) -> float:
        """
        contains a default value for the control.
        """
        ...


__all__ = ['CurrencyField']


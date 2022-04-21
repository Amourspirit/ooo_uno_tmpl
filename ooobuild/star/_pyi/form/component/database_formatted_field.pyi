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
# Libre Office Version: 7.2
# Namespace: com.sun.star.form.component
from ..data_aware_control_model import DataAwareControlModel as DataAwareControlModel_27110ef8
from .formatted_field import FormattedField as FormattedField_5b5c1047

class DatabaseFormattedField(DataAwareControlModel_27110ef8, FormattedField_5b5c1047):
    """
    Service Class

    This service specifies a formatted field model which is data-aware, and can be bound to a database field.

    See Also:
        `API DatabaseFormattedField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1DatabaseFormattedField.html>`_
    """
    @property
    def ConvertEmptyToNull(self) -> bool:
        """
        determines if an empty text should be treated as a NULL value.
        
        When the user enters text into a formatted field control, and after this, the control content is to be committed into the database field the control is bound to, a decision must be made how to deal with empty strings.
        This is controlled by ConvertEmptyToNull.
        
        If the property is set to TRUE, and an empty text is to be committed, this is converted into NULL, else it is written as empty string.
        """



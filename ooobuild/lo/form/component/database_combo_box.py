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
import typing
from abc import abstractmethod
from ..data_aware_control_model import DataAwareControlModel as DataAwareControlModel_27110ef8
from .combo_box import ComboBox as ComboBox_fecc0dd6
if typing.TYPE_CHECKING:
    from com.sun.star.form.ListSourceType import ListSourceTypeProto  # type: ignore

class DatabaseComboBox(DataAwareControlModel_27110ef8, ComboBox_fecc0dd6):
    """
    Service Class

    This service specifies a combo box which is data-aware, and can be bound to a database field.
    
    Like most other data aware controls, such a combo box will display the actual content of the field it is bound to. In addition, as a combo box contains a list where the user can choose items to fill into the control, this list can be filled with different data from a database, too.

    See Also:
        `API DatabaseComboBox <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1DatabaseComboBox.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.DatabaseComboBox'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def ConvertEmptyToNull(self) -> bool:
        """
        determines if an empty text should be treated as a NULL value.
        
        When the user enters text into a combo box, and after this, the control content is to be committed into the database field the control is bound to, a decision must be made how to deal with empty strings.This is controlled by ConvertEmptyToNull.
        
        If the property is set to TRUE, and an empty text is to be committed, this is converted into NULL, else it is written as empty string.
        """
        ...

    @property
    @abstractmethod
    def ListSource(self) -> str:
        """
        describes the source of items in the combo box's list.
        
        The concrete meaning of this property depends on the value of ListSourceType
        """
        ...

    @property
    @abstractmethod
    def ListSourceType(self) -> ListSourceTypeProto:
        """
        specifies the kind of list source.
        
        Note: A value of com.sun.star.form.ListSourceType.VALUELIST is not valid for a combo box. It won't be rejected when setting it, but controls will usually ignore it and leave the list empty.
        """
        ...


__all__ = ['DatabaseComboBox']
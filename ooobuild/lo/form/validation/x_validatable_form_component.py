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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.form.validation
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_validatable import XValidatable as XValidatable_49570fc6
if typing.TYPE_CHECKING:
    from .x_form_component_validity_listener import XFormComponentValidityListener as XFormComponentValidityListener_ac141740

class XValidatableFormComponent(XValidatable_49570fc6):
    """
    is a convenience interface for accessing several aspects of a form component which supports validation.
    
    A validatable form component has two aspects which other parties might be interested in:
    
    An XValidatableFormComponent allows to easily access both of these aspects.
    
    Note that all of the information provided at this interface can also obtained by other means, but much more inconveniently.

    See Also:
        `API XValidatableFormComponent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1validation_1_1XValidatableFormComponent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.validation'
    __ooo_full_ns__: str = 'com.sun.star.form.validation.XValidatableFormComponent'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.validation.XValidatableFormComponent'

    @abstractmethod
    def addFormComponentValidityListener(self, Listener: XFormComponentValidityListener_ac141740) -> None:
        """
        registers the given listener.
        
        XFormComponentValidityListeners are called whenever any of the aspects of the validatable form component (the validity flag, or the value) changed.

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
        ...
    @abstractmethod
    def getCurrentValue(self) -> object:
        """
        retrieves the current value of the component.
        
        The type of the current value, as well as it's semantics, depend on the service implementing this interface.
        
        Again, this is a convenience method. For example, for a com.sun.star.form.component.FormattedField, calling this method is equivalent to retrieving the com.sun.star.awt.UnoControlFormattedFieldModel.EffectiveValue.
        
        If no validator has been set (XValidatable.setValidator()), the value returned here is defined by the service implementing this interface.
        """
        ...
    @abstractmethod
    def isValid(self) -> bool:
        """
        determines whether the current value of the component passed the validity test at the validator.
        
        Calling this is equal to calling XValidator.isValid() with the current value (see getCurrentValue()) of the component, where the validator is obtained via XValidatable.getValidator().
        
        If no validator has been set (XValidatable.setValidator()), this method returns true.
        """
        ...
    @abstractmethod
    def removeFormComponentValidityListener(self, Listener: XFormComponentValidityListener_ac141740) -> None:
        """
        registers the given listener.

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
        ...

__all__ = ['XValidatableFormComponent']


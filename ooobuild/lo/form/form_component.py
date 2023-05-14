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
# Namespace: com.sun.star.form
from abc import abstractproperty
from ..beans.x_property_bag import XPropertyBag as XPropertyBag_bbd00bd8
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_form_component import XFormComponent as XFormComponent_c7fc0c5b
from ..io.x_persist_object import XPersistObject as XPersistObject_af2f0b79
from ..lang.x_component import XComponent as XComponent_98dc0ab5

class FormComponent(XPropertyBag_bbd00bd8, XPropertySet_bc180bfa, XNamed_a6520b08, XFormComponent_c7fc0c5b, XPersistObject_af2f0b79, XComponent_98dc0ab5):
    """
    Service Class

    specifies a component which can be part of a form.
    
    **since**
    
        OOo 2.3

    See Also:
        `API FormComponent <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1FormComponent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.FormComponent'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Name(self) -> str:
        """
        the name of the component.
        
        Note that the name accessed here is the same as when using the com.sun.star.container.XNamed interface.
        """
        ...


__all__ = ['FormComponent']


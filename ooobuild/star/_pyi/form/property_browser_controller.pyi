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
# Namespace: com.sun.star.form
from ..beans.x_fast_property_set import XFastPropertySet as XFastPropertySet_ee6b0d88
from ..beans.x_multi_property_set import XMultiPropertySet as XMultiPropertySet_fd880e05
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..frame.x_controller import XController as XController_b00e0b8f

class PropertyBrowserController(XFastPropertySet_ee6b0d88, XMultiPropertySet_fd880e05, XPropertySet_bc180bfa, XController_b00e0b8f):
    """
    Service Class

    describes a controller which can be used to browse and modify properties of form controls.
    
    The controller can be plugged into a com.sun.star.frame.XFrame, and will provide a visual component for inspecting control properties. This means it allows to interactively control several aspects of a FormControlModel or DataAwareControlModel, such as it's data binding, it's layout, and it's event binding
    
    For using a PropertyBrowserController, you need to
    
    Note that nowadays, this service is only a legacy wrapper using the com.sun.star.inspection.ObjectInspector and the com.sun.star.form.inspection.DefaultFormComponentInspectorModel services, and knitting them together.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API PropertyBrowserController <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1PropertyBrowserController.html>`_
    """
    @property
    def CurrentPage(self) -> str:
        """
        controls the actually visible page.
        
        The aspects of a DataAwareControlModel which can be browsed and modified using this controller can be separated into 3 groups: common aspects, data-awareness related aspects, and bound events.
        The appearance of the visual component created by the controller is that 3 tab pages, one for each group, are displayed (of course if the control does not support any aspects of a given group, the group is omitted).
        With this property, it can be controller which page is currently active.
        
        Valid values are (this list may be extended in the future):
        """
    @property
    def IntrospectedObject(self) -> 'XPropertySet_bc180bfa':
        """
        contains the object to inspect.
        
        Changing this property from outside causes the controller to update its view with the data of the new object
        """



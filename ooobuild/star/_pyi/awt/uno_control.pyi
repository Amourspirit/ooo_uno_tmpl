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
# Namespace: com.sun.star.awt
from ..accessibility.x_accessible import XAccessible as XAccessible_1cbc0eb6
from .x_control import XControl as XControl_7a9c098d
from .x_view import XView as XView_5f670847
from .x_window import XWindow as XWindow_713b0924

class UnoControl(XAccessible_1cbc0eb6, XControl_7a9c098d, XView_5f670847, XWindow_713b0924):
    """
    Service Class

    specifies an abstract control.
    
    All components which implement this service can be integrated in a windowing environment. This service describes the controller of the Smalltalk model view controller design.
    
    You must set a model and a stub to the UnoControl before using other methods. The implementation only allows the change of the graphics (XView) if the window is not visible. The change of the graphics in visible state should redirect the output to these graphics, but this behavior is implementation-specific.
    
    The change of data directly at the control may not affect the model data. To ensure this behavior, modify the data of the model.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API UnoControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControl.html>`_
    """



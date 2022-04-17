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
# Namespace: com.sun.star.ui
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
from ..lang.x_single_component_factory import XSingleComponentFactory as XSingleComponentFactory_46cc0fef

class UIElementSettings(XIndexAccess_f0910d6d, XSingleComponentFactory_46cc0fef):
    """
    Service Class

    describes the internal structure of a configurable user interface element.
    
    No assumption is made about any graphical representation: You could have a menu or a toolbar working with the same UIElementSettings although limitations based on the real user interface element may be visible.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UIElementSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ui_1_1UIElementSettings.html>`_
    """
    @property
    def UIName(self) -> str:
        """
        determine an optional user interface name of the user interface element.
        
        A toolbar can show its user interface name on the window title, when it is in floating mode.
        """



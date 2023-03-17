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
# Libre Office Version: 7.4
# Namespace: com.sun.star.frame
from ..awt.x_user_input_interception import XUserInputInterception as XUserInputInterception_2a7e0f4f
from ..datatransfer.x_transferable_supplier import XTransferableSupplier as XTransferableSupplier_b602128c
from .x_controller import XController as XController_b00e0b8f
from .x_dispatch_provider import XDispatchProvider as XDispatchProvider_fc690de6
from ..ui.x_context_menu_interception import XContextMenuInterception as XContextMenuInterception_38f90fac
from ..view.x_selection_supplier import XSelectionSupplier as XSelectionSupplier_fed20e15

class Controller(XUserInputInterception_2a7e0f4f, XTransferableSupplier_b602128c, XController_b00e0b8f, XDispatchProvider_fc690de6, XContextMenuInterception_38f90fac, XSelectionSupplier_fed20e15):
    """
    Service Class

    is an abstract service for a component which offers a deeper integration of desktop components than a com.sun.star.awt.XWindow can offer
    
    Such components can be loaded into a Frame inside a Desktop environment. A controller is a richer component then a pure window, but full featured components need a XModel interface too. (see service com.sun.star.document.OfficeDocument for further information)

    See Also:
        `API Controller <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1Controller.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.Controller'
    __ooo_type_name__: str = 'service'



__all__ = ['Controller']


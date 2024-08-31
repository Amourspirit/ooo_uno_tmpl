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
# Libre Office Version: 7.4
# Namespace: com.sun.star.form.control
from __future__ import annotations
from ...awt.uno_control import UnoControl as UnoControl_8f2c0a67
from ...container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
from ...container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
from ..x_bound_component import XBoundComponent as XBoundComponent_d4830cbf
from ..x_grid import XGrid as XGrid_6836089a
from ..x_grid_control import XGridControl as XGridControl_af710b7b
from ..x_grid_field_data_supplier import XGridFieldDataSupplier as XGridFieldDataSupplier_34aa0f4c
from ...frame.x_dispatch_provider_interception import XDispatchProviderInterception as XDispatchProviderInterception_c2a512da
from ...util.x_mode_selector import XModeSelector as XModeSelector_bbdc0be4
from ...util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0
from ...view.x_selection_supplier import XSelectionSupplier as XSelectionSupplier_fed20e15

class GridControl(UnoControl_8f2c0a67, XBoundComponent_d4830cbf, XGridControl_af710b7b, XGrid_6836089a, XGridFieldDataSupplier_34aa0f4c, XEnumerationAccess_4bac0ffc, XDispatchProviderInterception_c2a512da, XIndexAccess_f0910d6d, XSelectionSupplier_fed20e15, XModeSelector_bbdc0be4, XModifyBroadcaster_fd990df0):
    """
    Service Class

    describes a table-like control for displaying data.
    
    The model of the control has to support the com.sun.star.form.component.GridControl service.

    See Also:
        `API GridControl <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1control_1_1GridControl.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.control'
    __ooo_full_ns__: str = 'com.sun.star.form.control.GridControl'
    __ooo_type_name__: str = 'service'


__all__ = ['GridControl']


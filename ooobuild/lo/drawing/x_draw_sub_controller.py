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
# Namespace: com.sun.star.drawing
from __future__ import annotations
from ..beans.x_fast_property_set import XFastPropertySet as XFastPropertySet_ee6b0d88
from .x_draw_view import XDrawView as XDrawView_b0b80b75
from ..view.x_selection_supplier import XSelectionSupplier as XSelectionSupplier_fed20e15

class XDrawSubController(XFastPropertySet_ee6b0d88, XDrawView_b0b80b75, XSelectionSupplier_fed20e15):
    """
    View dependent part of the Draw and Impress controller.
    
    During the lifetime of an Impress application the com.sun.star.drawing.DrawingDocumentDrawView changes its sub controllers whenever the view in the center pane is replaced by another one. The sub controller handles the things that are not common to all views, i.e. properties, the current page/slide, and the selection.

    See Also:
        `API XDrawSubController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XDrawSubController.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.XDrawSubController'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.XDrawSubController'


__all__ = ['XDrawSubController']


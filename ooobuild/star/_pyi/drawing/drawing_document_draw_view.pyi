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
# Namespace: com.sun.star.drawing
import typing
from ..awt.x_window import XWindow as XWindow_713b0924
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_draw_view import XDrawView as XDrawView_b0b80b75
from ..frame.controller import Controller as Controller_a5330b37
from ..view.x_form_layer_access import XFormLayerAccess as XFormLayerAccess_e12f0cfe
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from .x_draw_page import XDrawPage as XDrawPage_b07a0b57

class DrawingDocumentDrawView(Controller_a5330b37, XWindow_713b0924, XPropertySet_bc180bfa, XDrawView_b0b80b75, XFormLayerAccess_e12f0cfe):
    """
    Service Class

    This component integrates a view to a DrawPages or MasterPage from a DrawingDocument.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API DrawingDocumentDrawView <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1DrawingDocumentDrawView.html>`_
    """
    @property
    def CurrentPage(self) -> 'XDrawPage_b07a0b57':
        """
        This is the drawing page that is currently visible.
        """
    @property
    def IsLayerMode(self) -> bool:
        """
        If the view is in layer mode, the user can modify the layer of the model of this view in the user interface.
        """
    @property
    def IsMasterPageMode(self) -> bool:
        """
        If the view is in master page mode, the view shows the master pages of this model.
        """
    @property
    def ViewOffset(self) -> 'Point_5fb2085e':
        """
        defines the offset from the top left position of the displayed page to the top left position of the view area in 100th/mm.
        
        **since**
        
            OOo 1.1.2
        """
    @property
    def VisibleArea(self) -> 'Rectangle_84b109e9':
        """
        This is the area that is currently visible.
        """
    @property
    def ZoomType(self) -> int:
        """
        This property defines the zoom type for the document.
        
        Note: After setting other types then com.sun.star.view.DocumentZoomType.BY_VALUE, implementations may calculate the required zoom value and set the type to com.sun.star.view.DocumentZoomType.BY_VALUE afterwards.
        
        **since**
        
            OOo 1.1.2
        """
    @property
    def ZoomValue(self) -> int:
        """
        Defines the zoom value to use.
        
        Valid only if the ZoomType is set to com.sun.star.view.DocumentZoomType.BY_VALUE.
        
        **since**
        
            OOo 1.1.2
        """



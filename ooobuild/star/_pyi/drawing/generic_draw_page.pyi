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
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_shape_binder import XShapeBinder as XShapeBinder_d4f70c91
from .x_shape_combiner import XShapeCombiner as XShapeCombiner_ef7b0d6c
from .x_shape_grouper import XShapeGrouper as XShapeGrouper_e2a30d21
from .x_shapes import XShapes as XShapes_9a800ab0
if typing.TYPE_CHECKING:
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
    from ..view.paper_orientation import PaperOrientation as PaperOrientation_e36f0d47

class GenericDrawPage(XPropertySet_bc180bfa, XNamed_a6520b08, XShapeBinder_d4f70c91, XShapeCombiner_ef7b0d6c, XShapeGrouper_e2a30d21, XShapes_9a800ab0):
    """
    Service Class

    This abstract service is implemented by every page of a DrawingDocument.
    
    Example to create and insert a couple of LineShapes:
    
    **since**
    
        LibreOffice 7.2

    See Also:
        `API GenericDrawPage <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1GenericDrawPage.html>`_
    """
    @property
    def BackgroundFullSize(self) -> bool:
        """
        does the background cover the full page or only inside the margins?
        
        **since**
        
            LibreOffice 7.2
        """
    @property
    def BorderBottom(self) -> int:
        """
        This is the border at the bottom.
        """
    @property
    def BorderLeft(self) -> int:
        """
        This is the border at the left.
        """
    @property
    def BorderRight(self) -> int:
        """
        This is the border at the right.
        """
    @property
    def BorderTop(self) -> int:
        """
        This is the border at the top.
        """
    @property
    def Height(self) -> int:
        """
        This is the height.
        """
    @property
    def IsBackgroundDark(self) -> bool:
        """
        this property is true if the averaged background filling colors luminance is below an application specified threshold value.
        
        This can be used to determine the actual value of an auto color.
        """
    @property
    def NavigationOrder(self) -> 'XIndexAccess_f0910d6d':
        """
        this index access defines a navigation order for the top level shapes inside this page.
        
        By default this is equal to the index access of the slide itself, making the z-order the default navigation order for top level shapes.
        """
    @property
    def Number(self) -> int:
        """
        This is the number of this page, starting with 1.
        """
    @property
    def Orientation(self) -> 'PaperOrientation_e36f0d47':
        """
        This is the orientation of this page.
        """
    @property
    def UserDefinedAttributes(self) -> 'XNameContainer_cb90e47':
        """
        this property stores xml attributes.
        
        They will be saved to and restored from automatic styles inside xml files.
        """
    @property
    def Width(self) -> int:
        """
        This is the width.
        """



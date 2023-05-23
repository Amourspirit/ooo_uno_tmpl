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
# Namespace: com.sun.star.text
import typing
from ..drawing.shape import Shape as Shape_85cc09e5
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from ..drawing.homogen_matrix3 import HomogenMatrix3 as HomogenMatrix3_f0fb0d69
    from .text_content_anchor_type import TextContentAnchorType as TextContentAnchorType_2cbe0f4a
    from .wrap_text_mode import WrapTextMode as WrapTextMode_b1dd0b91
    from .x_text_frame import XTextFrame as XTextFrame_9a7e0ab5
    from .x_text_range import XTextRange as XTextRange_9a910ab7

class Shape(Shape_85cc09e5):
    """
    Service Class

    specifies the service of shapes in a text document
    
    **since**
    
        LibreOffice 6.4

    See Also:
        `API Shape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1Shape.html>`_
    """
    @property
    def AllowOverlap(self) -> bool:
        """
        This defines if the shape is allowed to overlap with other anchored objects.
        
        **since**
        
            LibreOffice 6.4
        """
        ...
    @AllowOverlap.setter
    def AllowOverlap(self, value: bool) -> None:
        ...
    @property
    def AnchorFrame(self) -> 'XTextFrame_9a7e0ab5':
        """
        contains the text frame the current frame is anchored to.
        
        The value is valid only if the AnchorType is TextContentAnchorType.AT_FRAME.
        """
        ...
    @AnchorFrame.setter
    def AnchorFrame(self, value: 'XTextFrame_9a7e0ab5') -> None:
        ...
    @property
    def AnchorPageNo(self) -> int:
        """
        contains the number of the page where the objects are anchored.
        
        The value is valid only if the AnchorType is TextContentAnchorType.AT_PAGE.
        """
        ...
    @AnchorPageNo.setter
    def AnchorPageNo(self, value: int) -> None:
        ...
    @property
    def AnchorType(self) -> 'TextContentAnchorType_2cbe0f4a':
        """
        specifies how the text content is attached to its surrounding Text.
        """
        ...
    @AnchorType.setter
    def AnchorType(self, value: 'TextContentAnchorType_2cbe0f4a') -> None:
        ...
    @property
    def BottomMargin(self) -> int:
        """
        contains the bottom margin of the object.
        """
        ...
    @BottomMargin.setter
    def BottomMargin(self, value: int) -> None:
        ...
    @property
    def ContourOutside(self) -> bool:
        """
        the text flows only around the contour of the object.
        """
        ...
    @ContourOutside.setter
    def ContourOutside(self, value: bool) -> None:
        ...
    @property
    def EndPositionInHoriL2R(self) -> 'Point_5fb2085e':
        """
        determines the end position of the shape in horizontal left-to-right layout
        
        This property is needed for the export of the OASIS Open Office file format to the OpenOffice.org file format. It provides the end position property of the included service com.sun.star.drawing.Shape converted to the horizontal left-to-right layout.
        
        **since**
        
            OOo 2.0
        """
        ...
    @EndPositionInHoriL2R.setter
    def EndPositionInHoriL2R(self, value: 'Point_5fb2085e') -> None:
        ...
    @property
    def HoriOrient(self) -> int:
        """
        determines the horizontal orientation of the object.
        """
        ...
    @HoriOrient.setter
    def HoriOrient(self, value: int) -> None:
        ...
    @property
    def HoriOrientPosition(self) -> int:
        """
        contains the horizontal position of the object (1/100 mm).
        
        It is only valid if \"HoriOrient\" is HoriOrientation_NONE.
        """
        ...
    @HoriOrientPosition.setter
    def HoriOrientPosition(self, value: int) -> None:
        ...
    @property
    def HoriOrientRelation(self) -> int:
        """
        determines the environment of the object to which the orientation is related.
        """
        ...
    @HoriOrientRelation.setter
    def HoriOrientRelation(self, value: int) -> None:
        ...
    @property
    def LeftMargin(self) -> int:
        """
        contains the left margin of the object.
        """
        ...
    @LeftMargin.setter
    def LeftMargin(self, value: int) -> None:
        ...
    @property
    def Opaque(self) -> bool:
        """
        determines if the object is opaque or transparent for text.
        """
        ...
    @Opaque.setter
    def Opaque(self, value: bool) -> None:
        ...
    @property
    def PositionLayoutDir(self) -> int:
        """
        determines layout direction the position attributes of the shape is given
        
        Valid values are given by PositionLayoutDir
        
        **since**
        
            OOo 2.0
        """
        ...
    @PositionLayoutDir.setter
    def PositionLayoutDir(self, value: int) -> None:
        ...
    @property
    def RightMargin(self) -> int:
        """
        contains the right margin of the object.
        """
        ...
    @RightMargin.setter
    def RightMargin(self, value: int) -> None:
        ...
    @property
    def StartPositionInHoriL2R(self) -> 'Point_5fb2085e':
        """
        determines the start position of the shape in horizontal left-to-right layout
        
        This property is needed for the export of the OASIS Open Office file format to the OpenOffice.org file format. It provides the start position property of the included service com.sun.star.drawing.Shape converted to the horizontal left-to-right layout.
        
        **since**
        
            OOo 2.0
        """
        ...
    @StartPositionInHoriL2R.setter
    def StartPositionInHoriL2R(self, value: 'Point_5fb2085e') -> None:
        ...
    @property
    def Surround(self) -> 'WrapTextMode_b1dd0b91':
        """
        determines the type of the surrounding text.
        """
        ...
    @Surround.setter
    def Surround(self, value: 'WrapTextMode_b1dd0b91') -> None:
        ...
    @property
    def SurroundAnchorOnly(self) -> bool:
        """
        determines if the text of the paragraph in which the object is anchored, wraps around the object.
        """
        ...
    @SurroundAnchorOnly.setter
    def SurroundAnchorOnly(self, value: bool) -> None:
        ...
    @property
    def SurroundContour(self) -> bool:
        """
        determines if the text wraps around the contour of the object.
        """
        ...
    @SurroundContour.setter
    def SurroundContour(self, value: bool) -> None:
        ...
    @property
    def TextRange(self) -> 'XTextRange_9a910ab7':
        """
        contains a text range where the shape should be anchored to.
        
        There are two different ways to get newly created shapes into the text document. One of them is to use the insertTextContent() method of the com.sun.star.text.XSimpleText. The other is to call the add() method of the com.sun.star.drawing.XShapes interface. To be able to determine an anchor position for shape that are anchored at a certain text position the property TextRange is used.
        
        This property is used when the shape gets inserted/added and becomes invalid after that.
        """
        ...
    @TextRange.setter
    def TextRange(self, value: 'XTextRange_9a910ab7') -> None:
        ...
    @property
    def TopMargin(self) -> int:
        """
        contains the top margin of the object.
        """
        ...
    @TopMargin.setter
    def TopMargin(self, value: int) -> None:
        ...
    @property
    def TransformationInHoriL2R(self) -> 'HomogenMatrix3_f0fb0d69':
        """
        determines the transformation of the shape in horizontal left-to-right layout
        
        This property is needed for the export of the OASIS Open Office file format to the OpenOffice.org file format. It provides the transformation property of the included service com.sun.star.drawing.Shape converted to the horizontal left-to-right layout.
        
        **since**
        
            OOo 2.0
        """
        ...
    @TransformationInHoriL2R.setter
    def TransformationInHoriL2R(self, value: 'HomogenMatrix3_f0fb0d69') -> None:
        ...
    @property
    def VertOrient(self) -> int:
        """
        determines the vertical orientation of the object.
        """
        ...
    @VertOrient.setter
    def VertOrient(self, value: int) -> None:
        ...
    @property
    def VertOrientPosition(self) -> int:
        """
        contains the vertical position of the object (1/100 mm).
        
        It is only valid if TextEmbeddedObject.VertOrient is VertOrientation.NONE.
        """
        ...
    @VertOrientPosition.setter
    def VertOrientPosition(self, value: int) -> None:
        ...
    @property
    def VertOrientRelation(self) -> int:
        """
        determines the environment of the object to which the orientation is related.
        """
        ...
    @VertOrientRelation.setter
    def VertOrientRelation(self, value: int) -> None:
        ...
    @property
    def WrapInfluenceOnPosition(self) -> int:
        """
        determines the influence of the text wrap on the positioning of the shape
        
        The value of this property is only evaluated for the positioning of the shape, if the text document setting ConsiderTextWrapOnObjPos is TRUE. Valid values are given by WrapInfluenceOnPosition
        
        **since**
        
            OOo 2.0
        """
        ...
    @WrapInfluenceOnPosition.setter
    def WrapInfluenceOnPosition(self, value: int) -> None:
        ...

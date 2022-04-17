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
# Namespace: com.sun.star.text
import typing
from .base_frame import BaseFrame as BaseFrame_8f020a33
from .x_text_frame import XTextFrame as XTextFrame_9a7e0ab5
if typing.TYPE_CHECKING:
    from ..drawing.text_vertical_adjust import TextVerticalAdjust as TextVerticalAdjust_2c160f3e
    from .x_text import XText as XText_690408ca

class TextFrame(BaseFrame_8f020a33, XTextFrame_9a7e0ab5):
    """
    Service Class

    specifies a rectangular shape which contains a Text object and is attached to a piece of surrounding Text.
    
    This example shows how to create a TextFrame and insert it at the very beginning of Text component. The macro is ready to run, if it is a script within a text document.
    
    **since**
    
        LibreOffice 6.3

    See Also:
        `API TextFrame <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextFrame.html>`_
    """
    @property
    def EditInReadonly(self) -> bool:
        """
        determines if the text frame should be editable in a read-only document.
        
        (This is usually used in forms.)
        """
    @property
    def FrameHeightAbsolute(self) -> int:
        """
        contains the metric height value of the frame.
        """
    @property
    def FrameHeightPercent(self) -> int:
        """
        specifies a width relative to the width of the surrounding text.
        
        If the value for \"HeightPercent\" is 0, the absolute value from is used.
        """
    @property
    def FrameIsAutomaticHeight(self) -> bool:
        """
        If \"AutomaticHeight\" is set, then the object grows if it is required by the frame content.
        """
    @property
    def FrameWidthAbsolute(self) -> int:
        """
        contains the metric width value of the frame.
        """
    @property
    def FrameWidthPercent(self) -> int:
        """
        specifies a width relative to the width of the surrounding text.
        
        If the value for \"WidthPercent\" is 0, the absolute value from is used.
        """
    @property
    def IsFollowingTextFlow(self) -> bool:
        """
        controls, if the frame follows the text flow or can leave its layout environment
        
        If set, the frame follows the text flow and doesn't leaves the layout environment, which is given by its anchor, above and below. E.g.: Anchor resides in the document body then the frame doesn't leave the document body above and below and follows the text flow through the document bodies of the different pages.
        
        If not set, the frame doesn't follow the text flow and stays on the page, on which its anchor is found, but it may leave the layout environment, which is given by its anchor. E.g.: Anchor resides in the document body then the frame stays on page, where this document body is, but it could leave the document body above and below, e.g. overlapping with the page header.
        
        Note: The areas for the vertical orientation relation at page areas are interpreted in dependence to this property (
        """
    @property
    def ParentText(self) -> 'XText_690408ca':
        """
        Parent text of this text frame.
        
        This might be a header text, body text, etc.
        
        **since**
        
            LibreOffice 6.3
        """
    @property
    def SizeType(self) -> int:
        """
        determines the interpretation of the height and relative height properties.
        """
    @property
    def TextVerticalAdjust(self) -> 'TextVerticalAdjust_2c160f3e':
        """
        adjusts the vertical position of the text inside of the frame.
        
        **since**
        
            LibreOffice 4.3
        """
    @property
    def WidthType(self) -> int:
        """
        determines the interpretation of the width and relative width properties.
        
        **since**
        
            OOo 2.4
        """
    @property
    def WritingMode(self) -> int:
        """
        contains the writing direction, as represented by the com.sun.star.text.WritingMode2 constants
        """



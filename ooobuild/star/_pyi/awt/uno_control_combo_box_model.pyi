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
import typing
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
from .x_item_list import XItemList as XItemList_83fb09d7
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..util.color import Color as Color_68e908c5

class UnoControlComboBoxModel(UnoControlModel_c8ce0c58, XItemList_83fb09d7):
    """
    Service Class

    specifies the standard model of a UnoControlComboBox.
    
    **since**
    
        LibreOffice 5.4

    See Also:
        `API UnoControlComboBoxModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlComboBoxModel.html>`_
    """
    @property
    def StringItemList(self) -> 'typing.Tuple[str, ...]':
        """
        specifies the list of items.
        """
        ...
    @property
    def TypedItemList(self) -> 'typing.Tuple[object, ...]':
        """
        specifies the list of raw typed (not stringized) items.
        
        This list corresponds with the StringItemList and if given has to be of the same length, the elements' positions matching those of their string representation in StringItemList.
        
        If a new value is entered via the ComboBox edit then this list will be invalidated.
        
        **since**
        
            LibreOffice 5.4
        """
        ...
    @property
    def Align(self) -> int:
        """
        specifies the horizontal alignment of the text in the control.
        """
        ...
    @property
    def Autocomplete(self) -> bool:
        """
        specifies whether automatic completion of text is enabled.
        """
        ...
    @property
    def BackgroundColor(self) -> 'Color_68e908c5':
        """
        specifies the background color (RGB) of the control.
        """
        ...
    @property
    def Border(self) -> int:
        """
        specifies the border style of the control.
        """
        ...
    @property
    def BorderColor(self) -> int:
        """
        specifies the color of the border, if present
        
        Not every border style (see Border) may support coloring. For instance, usually a border with 3D effect will ignore the BorderColor setting.
        
        **since**
        
            OOo 2.0
        """
        ...
    @property
    def Dropdown(self) -> bool:
        """
        specifies if the control has a drop down button.
        """
        ...
    @property
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...
    @property
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """
        ...
    @property
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
        ...
    @property
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
        ...
    @property
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """
        ...
    @property
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """
        ...
    @property
    def HideInactiveSelection(self) -> bool:
        """
        specifies whether the selection in the control should be hidden when the control is not active (focused).
        
        **since**
        
            OOo 2.0
        """
        ...
    @property
    def LineCount(self) -> int:
        """
        specifies the maximum line count displayed in the drop down box.
        """
        ...
    @property
    def MaxTextLen(self) -> int:
        """
        specifies the maximum character count.
        
        There's no limitation, if set to 0.
        """
        ...
    @property
    def MouseWheelBehavior(self) -> int:
        """
        defines how the mouse wheel can be used to scroll through the control's content.
        
        Usually, the mouse wheel scroll through the control's entry list. Using this property, and one of the MouseWheelBehavior constants, you can control under which circumstances this is possible.
        """
        ...
    @property
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """
        ...
    @property
    def ReadOnly(self) -> bool:
        """
        specifies that the content of the control cannot be modified by the user.
        """
        ...
    @property
    def Tabstop(self) -> bool:
        """
        specifies that the control can be reached with the TAB key.
        """
        ...
    @property
    def Text(self) -> str:
        """
        specifies the text displayed in the control.
        """
        ...
    @property
    def TextColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the control.
        """
        ...
    @property
    def TextLineColor(self) -> 'Color_68e908c5':
        """
        specifies the text line color (RGB) of the control.
        """
        ...
    @property
    def WritingMode(self) -> int:
        """
        denotes the writing mode used in the control, as specified in the com.sun.star.text.WritingMode2 constants group.
        
        Only com.sun.star.text.WritingMode2.LR_TB and com.sun.star.text.WritingMode2.RL_TB are supported at the moment.
        
        **since**
        
            OOo 3.1
        """
        ...



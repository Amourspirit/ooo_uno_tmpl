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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.awt.tab
from __future__ import annotations
from .x_tab_page_model import XTabPageModel as XTabPageModel_dcde0c96

class UnoControlTabPageModel(XTabPageModel_dcde0c96):
    """
    Service Class

    specifies the standard model of a XTabPageModel.
    
    **since**
    
        OOo 3.4

    See Also:
        `API UnoControlTabPageModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1tab_1_1UnoControlTabPageModel.html>`_
    """
    @property
    def HScroll(self) -> bool:
        """
        specifies that a horizontal scrollbar should be added to the dialog
        
        **since**
        
            LibreOffice 7.1
        """
        ...
    @HScroll.setter
    def HScroll(self, value: bool) -> None:
        ...
    @property
    def HelpText(self) -> str:
        """
        specifies the help text of the dialog.
        """
        ...
    @HelpText.setter
    def HelpText(self, value: str) -> None:
        ...
    @property
    def HelpURL(self) -> str:
        """
        specifies the help URL of the dialog.
        """
        ...
    @HelpURL.setter
    def HelpURL(self, value: str) -> None:
        ...
    @property
    def ScrollHeight(self) -> int:
        """
        specifies the total height of the scrollable dialog content
        
        **since**
        
            LibreOffice 7.1
        """
        ...
    @ScrollHeight.setter
    def ScrollHeight(self, value: int) -> None:
        ...
    @property
    def ScrollLeft(self) -> int:
        """
        specifies the horizontal position of the scrolled dialog content
        
        **since**
        
            LibreOffice 7.1
        """
        ...
    @ScrollLeft.setter
    def ScrollLeft(self, value: int) -> None:
        ...
    @property
    def ScrollTop(self) -> int:
        """
        specifies the vertical position of the scrolled dialog content
        
        **since**
        
            LibreOffice 7.1
        """
        ...
    @ScrollTop.setter
    def ScrollTop(self, value: int) -> None:
        ...
    @property
    def ScrollWidth(self) -> int:
        """
        specifies the total width of the scrollable dialog content
        
        **since**
        
            LibreOffice 7.1
        """
        ...
    @ScrollWidth.setter
    def ScrollWidth(self, value: int) -> None:
        ...
    @property
    def Title(self) -> str:
        """
        specifies the text that is displayed in the caption bar of the dialog.
        """
        ...
    @Title.setter
    def Title(self, value: str) -> None:
        ...
    @property
    def VScroll(self) -> bool:
        """
        specifies that a vertical scrollbar should be added to the dialog
        
        **since**
        
            LibreOffice 7.1
        """
        ...
    @VScroll.setter
    def VScroll(self, value: bool) -> None:
        ...


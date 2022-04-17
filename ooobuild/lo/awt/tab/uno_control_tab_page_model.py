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
# Namespace: com.sun.star.awt.tab
from abc import abstractproperty
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
    __ooo_ns__: str = 'com.sun.star.awt.tab'
    __ooo_full_ns__: str = 'com.sun.star.awt.tab.UnoControlTabPageModel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def HScroll(self) -> bool:
        """
        specifies that a horizontal scrollbar should be added to the dialog
        
        **since**
        
            LibreOffice 7.1
        """

    @abstractproperty
    def HelpText(self) -> str:
        """
        specifies the help text of the dialog.
        """

    @abstractproperty
    def HelpURL(self) -> str:
        """
        specifies the help URL of the dialog.
        """

    @abstractproperty
    def ScrollHeight(self) -> int:
        """
        specifies the total height of the scrollable dialog content
        
        **since**
        
            LibreOffice 7.1
        """

    @abstractproperty
    def ScrollLeft(self) -> int:
        """
        specifies the horizontal position of the scrolled dialog content
        
        **since**
        
            LibreOffice 7.1
        """

    @abstractproperty
    def ScrollTop(self) -> int:
        """
        specifies the vertical position of the scrolled dialog content
        
        **since**
        
            LibreOffice 7.1
        """

    @abstractproperty
    def ScrollWidth(self) -> int:
        """
        specifies the total width of the scrollable dialog content
        
        **since**
        
            LibreOffice 7.1
        """

    @abstractproperty
    def Title(self) -> str:
        """
        specifies the text that is displayed in the caption bar of the dialog.
        """

    @abstractproperty
    def VScroll(self) -> bool:
        """
        specifies that a vertical scrollbar should be added to the dialog
        
        **since**
        
            LibreOffice 7.1
        """



__all__ = ['UnoControlTabPageModel']

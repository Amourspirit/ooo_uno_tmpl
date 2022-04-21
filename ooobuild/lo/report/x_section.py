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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.report
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_child import XChild as XChild_a6390b07
from ..container.x_container import XContainer as XContainer_d6fb0cc6
from ..container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
from ..drawing.x_shapes import XShapes as XShapes_9a800ab0
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .x_group import XGroup as XGroup_86540a09
    from .x_report_definition import XReportDefinition as XReportDefinition_ec30e81
    from ..util.color import Color as Color_68e908c5

class XSection(XPropertySet_bc180bfa, XChild_a6390b07, XContainer_d6fb0cc6, XEnumerationAccess_4bac0ffc, XShapes_9a800ab0, XComponent_98dc0ab5):
    """
    identifies a XSection inside a report.
    
    A section acts like a container of report components. This generic construction allows the definition of hierarchies of reports and their dependent subreports.

    See Also:
        `API XSection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XSection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report'
    __ooo_full_ns__: str = 'com.sun.star.report.XSection'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.XSection'

    @abstractproperty
    def BackColor(self) -> 'Color_68e908c5':
        """
        Defines the background color of the section.
        """

    @abstractproperty
    def BackTransparent(self) -> bool:
        """
        determines if the background color is set to transparent.
        """

    @abstractproperty
    def CanGrow(self) -> bool:
        """
        Specifies that elements with dynamic state will be expanded vertically when then content of the element is larger than it's container.
        
        If this property is disabled the content will be truncated when its size is larger than the container.
        """

    @abstractproperty
    def CanShrink(self) -> bool:
        """
        Represents ...
        """

    @abstractproperty
    def ConditionalPrintExpression(self) -> str:
        """
        Defines the expression which is executed before printing the section.
        
        If the return value of the expression is TRUE then the section will be printed.
        """

    @abstractproperty
    def ForceNewPage(self) -> int:
        """
        Specifies whether the section is printed on a separate page.
        
        Not valid for page header or page footer.
        """

    @abstractproperty
    def Group(self) -> 'XGroup_86540a09':
        """
        Specifies the parent of the section if it is a group header or group footer.
        """

    @abstractproperty
    def Height(self) -> int:
        """
        Defines the height of the section.
        """

    @abstractproperty
    def KeepTogether(self) -> bool:
        """
        Specifies that the section is printed on one page.
        
        Not valid for page header or page footer.
        """

    @abstractproperty
    def Name(self) -> str:
        """
        Defines the name of the section.
        """

    @abstractproperty
    def NewRowOrCol(self) -> int:
        """
        Specifies whether the section is printed in a new row or column within a multi column report.
        
        Not valid for page header or page footer.
        """

    @abstractproperty
    def RepeatSection(self) -> bool:
        """
        Defines that the group header should be repeated on the next page when a group spans more than one page.
        
        It only applies to group headers.
        """

    @abstractproperty
    def ReportDefinition(self) -> 'XReportDefinition_ec30e81':
        """
        Specifies the parent of the section if it is a page header or page footer.
        """

    @abstractproperty
    def Visible(self) -> bool:
        """
        Defines if the section should be visible in report.
        """


__all__ = ['XSection']


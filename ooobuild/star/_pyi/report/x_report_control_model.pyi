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
from typing_extensions import Literal
import typing
from ..container.x_container import XContainer as XContainer_d6fb0cc6
from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe
from .x_report_component import XReportComponent as XReportComponent_df0e2b
from .x_report_control_format import XReportControlFormat as XReportControlFormat_3d4e0fc2
if typing.TYPE_CHECKING:
    from .x_format_condition import XFormatCondition as XFormatCondition_ffb00e0c

class XReportControlModel(XContainer_d6fb0cc6, XIndexContainer_1c040ebe, XReportComponent_df0e2b, XReportControlFormat_3d4e0fc2):
    """

    See Also:
        `API XReportControlModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XReportControlModel.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.report.XReportControlModel']

    def createFormatCondition(self) -> 'XFormatCondition_ffb00e0c':
        """
        Creates a format condition.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
    @property
    def ConditionalPrintExpression(self) -> str:
        """
        Describes the print expression of the report control model.
        
        If the expression evaluates to true than the report control model will be printed otherwise not.
        """

    @property
    def DataField(self) -> str:
        """
        Specifies which content should be shown.
        
        The value can be
        """

    @property
    def PrintWhenGroupChange(self) -> bool:
        """
        Specifies that the element gets printed when the group changes.
        
        The default value is TRUE.
        """



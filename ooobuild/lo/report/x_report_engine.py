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
# Libre Office Version: 7.3
# Namespace: com.sun.star.report
import typing
from abc import abstractmethod, abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ..frame.x_frame import XFrame as XFrame_7a570956
    from ..frame.x_model import XModel as XModel_7a6e095c
    from .x_report_definition import XReportDefinition as XReportDefinition_ec30e81
    from ..sdbc.x_connection import XConnection as XConnection_a36a0b0c
    from ..task.x_status_indicator import XStatusIndicator as XStatusIndicator_e2d00d34
    from ..util.url import URL as URL_57ad07b9

class XReportEngine(XPropertySet_bc180bfa, XComponent_98dc0ab5):
    """
    identifies a XReportEngine which allows the creation of OpenDocument files.
    
    The following events are supported by the report engine. OnPageStarted Is fired when a new page started. OnReportStarted Is fired when a new report started. OnGroupStarted Is fired when a new group started. OnGroupEnded Is fired when the group ended. OnReportEnded Is fired when the report ended. OnPageEnded Is fired when the page ended.

    See Also:
        `API XReportEngine <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XReportEngine.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.report'
    __ooo_full_ns__: str = 'com.sun.star.report.XReportEngine'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.report.XReportEngine'

    @abstractmethod
    def createDocument(self) -> 'URL_57ad07b9':
        """
        creates a report document.

        Raises:
            com.sun.star.lang.DisposedException: ``DisposedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.uno.Exception: ``Exception``
        """
    @abstractmethod
    def createDocumentAlive(self, frame: 'XFrame_7a570956') -> 'XModel_7a6e095c':
        """
        creates a report document.
        
        OJ: Has to be discussed if this method is useful.

        Raises:
            com.sun.star.lang.DisposedException: ``DisposedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.uno.Exception: ``Exception``
        """
    @abstractmethod
    def createDocumentModel(self) -> 'XModel_7a6e095c':
        """
        creates a report document.

        Raises:
            com.sun.star.lang.DisposedException: ``DisposedException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.uno.Exception: ``Exception``
        """
    @abstractmethod
    def interrupt(self) -> None:
        """
        allows to interrupt the creation process of the report document.

        Raises:
            com.sun.star.lang.DisposedException: ``DisposedException``
            com.sun.star.uno.Exception: ``Exception``
        """
    @abstractproperty
    def ActiveConnection(self) -> 'XConnection_a36a0b0c':
        """
        specifies the active connection which is used to create the resulting report.
        """

    @abstractproperty
    def MaxRows(self) -> int:
        """
        defines the maximum number of rows which should be fetched for the report.
        
        If the limit is exceeded, the excess rows are silently dropped.
        There is no limitation, if set to zero.
        """

    @abstractproperty
    def ReportDefinition(self) -> 'XReportDefinition_ec30e81':
        """
        specifies the report definition object which is used to create the resulting report.
        """

    @abstractproperty
    def StatusIndicator(self) -> 'XStatusIndicator_e2d00d34':
        """
        specifies the status indicator which shows the progress of the report generation process.
        """


__all__ = ['XReportEngine']

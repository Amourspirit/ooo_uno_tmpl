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
from typing_extensions import Literal
import typing
from ..document.x_document_sub_storage_supplier import XDocumentSubStorageSupplier as XDocumentSubStorageSupplier_da021351
from ..document.x_storage_based_document import XStorageBasedDocument as XStorageBasedDocument_6b1310b2
from ..document.x_view_data_supplier import XViewDataSupplier as XViewDataSupplier_2ae20f28
from ..embed.x_visual_object import XVisualObject as XVisualObject_c6c80c28
from ..frame.x_loadable import XLoadable as XLoadable_989a0a7f
from ..frame.x_model import XModel as XModel_7a6e095c
from .x_functions_supplier import XFunctionsSupplier as XFunctionsSupplier_1ee10f09
from .x_report_component import XReportComponent as XReportComponent_df0e2b
from ..style.x_style_families_supplier import XStyleFamiliesSupplier as XStyleFamiliesSupplier_4c5a1020
from ..ui.xui_configuration_manager_supplier import XUIConfigurationManagerSupplier as XUIConfigurationManagerSupplier_ab1c1243
from ..util.x_closeable import XCloseable as XCloseable_99ee0aa8
from ..util.x_modifiable2 import XModifiable2 as XModifiable2_b0320b3c
if typing.TYPE_CHECKING:
    from ..document.x_event_broadcaster import XEventBroadcaster as XEventBroadcaster_2b120f2b
    from .x_groups import XGroups as XGroups_90d00a7c
    from .x_section import XSection as XSection_9b630ad1
    from ..sdbc.x_connection import XConnection as XConnection_a36a0b0c

class XReportDefinition(XDocumentSubStorageSupplier_da021351, XStorageBasedDocument_6b1310b2, XViewDataSupplier_2ae20f28, XVisualObject_c6c80c28, XLoadable_989a0a7f, XModel_7a6e095c, XFunctionsSupplier_1ee10f09, XReportComponent_df0e2b, XStyleFamiliesSupplier_4c5a1020, XUIConfigurationManagerSupplier_ab1c1243, XCloseable_99ee0aa8, XModifiable2_b0320b3c):
    """
    identifies a XReportComponent as being a (sub-) report.
    
    This interface does not really provide an own functionality, it is only for easier runtime identification of report components.
    
    A report fulfills several tasks, like storing the structure of its report components and it provides the event environment for its contained elements.

    See Also:
        `API XReportDefinition <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1XReportDefinition.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.report.XReportDefinition']

    def getAvailableMimeTypes(self) -> 'typing.Tuple[str, ...]':
        """
        returns a sequence of the currently supported output formats.

        Raises:
            com.sun.star.lang.DisposedException: ``DisposedException``
            com.sun.star.uno.Exception: ``Exception``
        """
    def getEventBroadcaster(self) -> 'XEventBroadcaster_2b120f2b':
        """
        makes it possible to register listeners which are called whenever a document event occurs.
        
        This is a workaround due to the fact that this interface can not be directly inherited from com.sun.star.document.XEventBroadcaster because the methods addEventListener and removeEventListener are already defined in com.sun.star.lang.XComponent. A queryInterface call is still supported to the com.sun.star.document.XEventBroadcaster interface.

        Raises:
            com.sun.star.lang.DisposedException: ``DisposedException``
            com.sun.star.uno.Exception: ``Exception``
        """
    @property
    def ActiveConnection(self) -> 'XConnection_a36a0b0c':
        """
        specifies the active connection which is used to create the resulting report.
        """

    @property
    def Caption(self) -> str:
        """
        Represents the title of the report in print preview.
        """

    @property
    def Command(self) -> str:
        """
        is the command which should be executed, the type of command depends on the CommandType.
        
        In case of a CommandType of CommandType.COMMAND, means in case the Command specifies an SQL statement, the inherited com.sun.star.sdbc.RowSet.EscapeProcessing becomes relevant:
        It then can be to used to specify whether the SQL statement should be analyzed on the client side before sending it to the database server.
        The default value for com.sun.star.sdbc.RowSet.EscapeProcessing is TRUE. By switching it to FALSE, you can pass backend-specific SQL statements, which are not standard SQL, to your database.
        """

    @property
    def CommandType(self) -> int:
        """
        specifies the type of the command to be executed to retrieve a result set.
        
        Command needs to be interpreted depending on the value of this property.
        
        This property is only meaningful together with the Command property, thus either both or none of them are present.
        """

    @property
    def DataSourceName(self) -> str:
        """
        is the name of the datasource to use, this could be a named datasource or the URL of a data access component.
        """

    @property
    def Detail(self) -> 'XSection_9b630ad1':
        """
        returns the detail section.
        """

    @property
    def EscapeProcessing(self) -> bool:
        """
        specifies if the Command should be analyzed on the client side before sending it to the database server.
        
        The default value of this property is TRUE. By switching it to FALSE, you can pass backend-specific SQL statements, which are not standard SQL, to your database.
        
        This property is usually present together with the Command and CommandType properties, and is evaluated if and only if CommandType equals CommandType.COMMAND.
        """

    @property
    def Filter(self) -> str:
        """
        specifies an additional filter to optionally use.
        
        The Filter string has to form a SQL WHERE-clause, without the WHERE-string itself.
        
        If a DataSourceName, Command and CommandType are specified, a RowSet can be created with this information. If the results provided by the row set are to be additionally filtered, the Filter property can be used.
        
        Note that the Filter property does not make sense if a ResultSet has been specified in the DataAccessDescriptor.
        """

    @property
    def GroupKeepTogether(self) -> int:
        """
        Specifies whether groups in a multi column report are kept together.
        """

    @property
    def Groups(self) -> 'XGroups_90d00a7c':
        """
        Represents the groups of the report.
        """

    @property
    def MimeType(self) -> str:
        """
        Represents the output format (media (mime) type) of the resulting document when executing this report.
        """

    @property
    def PageFooter(self) -> 'XSection_9b630ad1':
        """
        returns the page footer if the PageFooterOn is TRUE.
        """

    @property
    def PageFooterOn(self) -> bool:
        """
        Defines that the page footer is on.
        
        Default is TRUE.
        """

    @property
    def PageFooterOption(self) -> int:
        """
        Represents the location of the page footer.
        """

    @property
    def PageHeader(self) -> 'XSection_9b630ad1':
        """
        returns the page header if the PageHeaderOn is TRUE.
        """

    @property
    def PageHeaderOn(self) -> bool:
        """
        Defines that the page header is on.
        
        Default is TRUE.
        """

    @property
    def PageHeaderOption(self) -> int:
        """
        Represents the location of the page header.
        """

    @property
    def ReportFooter(self) -> 'XSection_9b630ad1':
        """
        returns the report footer if the ReportFooterOn is TRUE.
        """

    @property
    def ReportFooterOn(self) -> bool:
        """
        Defines that the report footer is on.
        
        Default is FALSE.
        """

    @property
    def ReportHeader(self) -> 'XSection_9b630ad1':
        """
        returns the report header if the ReportHeaderOn is TRUE.
        """

    @property
    def ReportHeaderOn(self) -> bool:
        """
        Defines that the report header is on.
        
        Default is FALSE.
        """


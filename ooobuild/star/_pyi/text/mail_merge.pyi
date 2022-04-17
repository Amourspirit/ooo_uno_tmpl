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
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..sdb.data_access_descriptor import DataAccessDescriptor as DataAccessDescriptor_6c50e2c
from ..task.x_job import XJob as XJob_5fa1082e
from .x_mail_merge_broadcaster import XMailMergeBroadcaster as XMailMergeBroadcaster_27c30f02
from ..util.x_cancellable import XCancellable as XCancellable_afc30b64
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..frame.x_model import XModel as XModel_7a6e095c
    from ..sdbc.x_connection import XConnection as XConnection_a36a0b0c
    from ..sdbc.x_result_set import XResultSet as XResultSet_98e30aa7

class MailMerge(DataAccessDescriptor_6c50e2c, XPropertySet_bc180bfa, XJob_5fa1082e, XMailMergeBroadcaster_27c30f02, XCancellable_afc30b64):
    """
    Service Class

    Gives access to mail merge functionality.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API MailMerge <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1MailMerge.html>`_
    """
    @property
    def BlindCopiesTo(self) -> 'typing.Tuple[str, ...]':
        """
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def CopiesTo(self) -> 'typing.Tuple[str, ...]':
        """
        contains a list of e-Mail addresses to
        
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def PrintOptions(self) -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        contains the properties that are defined in <com.sun.star.view.PrintOptions>.
        
        This property is only evaluated for printer output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def Selection(self) -> 'typing.Tuple[object, ...]':
        """
        contains a selection that refers to bookmarks of the ResultSet.
        
        This property is relevant in conjunction with the ResultSet only. A single element of this array describes a bookmark relative to the result set.
        Note that this implies that the ResultSet needs to support the com.sun.star.sdbcx.XRowLocate interface.
        
        If this array is empty, the whole result set, as described by ResultSet respectively the triple (DataSourceName, CommandType, Command).
        
        For the interaction of this property with other data access relevant properties, see the com.sun.star.sdb.DataAccessDescriptor service.
        """
    @property
    def ActiveConnection(self) -> 'XConnection_a36a0b0c':
        """
        contains the connection to the database.
        
        For the interaction of this property with other data access relevant properties, see the com.sun.star.sdb.DataAccessDescriptor service.
        """
    @property
    def AddressFromColumn(self) -> str:
        """
        contains the name of the data base column that contains the e-Mail address to the e-Mail to.
        
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def AttachmentFilter(self) -> str:
        """
        contains the name of the document filter to save the attached mail merge document.
        
        This property is only valid if \"SendAsAttachment\" is set to TRUE.
        
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def AttachmentName(self) -> str:
        """
        contains the name of the attachment.
        
        This property is only valid if \"SendAsAttachment\" is set to TRUE.
        
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def Command(self) -> str:
        """
        contains the database command.
        
        For the interaction of this property with other data access relevant properties, see the com.sun.star.sdb.DataAccessDescriptor service.
        """
    @property
    def CommandType(self) -> int:
        """
        determines the type of the database command as described in com.sun.star.sdb.CommandType
        
        For the interaction of this property with other data access relevant properties, see the com.sun.star.sdb.DataAccessDescriptor service.
        """
    @property
    def DataSourceName(self) -> str:
        """
        contains the name of the data source that is to be used for merging.
        
        For the interaction of this property with other data access relevant properties, see the com.sun.star.sdb.DataAccessDescriptor service.
        """
    @property
    def DocumentURL(self) -> str:
        """
        contains the URL of a text document that is to be processed.
        
        If this property is not set an empty document is created.
        """
    @property
    def EscapeProcessing(self) -> bool:
        """
        returns if escape processing is on or off.
        
        For the interaction of this property with other data access relevant properties, see the com.sun.star.sdb.DataAccessDescriptor service.
        """
    @property
    def FileNameFromColumn(self) -> bool:
        """
        determines whether file names of created files are generated using the content of a database column.
        
        This property is only evaluated for file output.
        """
    @property
    def FileNamePrefix(self) -> str:
        """
        contains the name of the column to generate the output file names.
        
        If FileNameFromColumn is true the content of the related column is added to the OutputURL.
        
        If \"OutputURL\" or \"FileNamePrefix\" are empty the missing value is generated from the location or title of the source documents.
        
        This property is only evaluated for file output.
        """
    @property
    def Filter(self) -> str:
        """
        contains a filter expression for an SQL statement.
        
        For the interaction of this property with other data access relevant properties, see the com.sun.star.sdb.DataAccessDescriptor service.
        """
    @property
    def InServerPassword(self) -> str:
        """
        Contains the password of the incoming mail server.
        
        It is necessary to set this if the mail server configuration is set to \"SMTP after POP\" authentication and the password is not already stored in the configuration for security reasons.
        
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def MailBody(self) -> str:
        """
        contains the text of the mail body.
        
        This property is only valid if the property \"SendAsAttachment\" is set to TRUE
        
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def Model(self) -> 'XModel_7a6e095c':
        """
        provides access to the model of the document to be processed.
        
        This property will automatically be set to the documents model if a document URL was set.
        """
    @property
    def OutServerPassword(self) -> str:
        """
        Contains the password of the outgoing mail server.
        
        It is necessary to set this if the password is not already stored in the configuration for security reasons.
        
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def OutputType(self) -> int:
        """
        determines the destination of the mail merge action.
        """
    @property
    def OutputURL(self) -> str:
        """
        contains the path where generated files are created.
        
        If \"OutputURL\" or \"FileNamePrefix\" are empty the missing value is generated from the location or title of the source documents.
        
        This property is only evaluated for file output.
        """
    @property
    def ResultSet(self) -> 'XResultSet_98e30aa7':
        """
        provides access to a com.sun.star.sdbc.XResultSet of a com.sun.star.sdbc.ResultSet service.
        
        Note that any superservices of com.sun.star.sdbc.ResultSet are also allowed. Especially, this member can denote an instance of the com.sun.star.sdb.RowSet, or an instance obtained by calling com.sun.star.sdb.XResultSetAccess.createResultSet() on such a com.sun.star.sdb.RowSet. This becomes important in conjunction with the Selection property.
        
        For the interaction of this property with other data access relevant properties, see the com.sun.star.sdb.DataAccessDescriptor service.
        """
    @property
    def SaveAsSingleFile(self) -> bool:
        """
        determines that the output of the mail merge is saved in one single file.
        
        This property is only evaluated for file output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def SaveFilter(self) -> str:
        """
        contains the name of the document filter to save the output file(s).
        
        This property is only evaluated for file output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def SendAsAttachment(self) -> bool:
        """
        determines that the created mail merge document is sent as attachment.
        
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def SendAsHTML(self) -> bool:
        """
        determines that the created mail merge document is sent as body in HTML format.
        
        This property is only valid if the property \"SendAsAttachment\" is set to FALSE.
        
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """
    @property
    def SinglePrintJobs(self) -> bool:
        """
        determines whether single print jobs will be generated per output document.
        
        This property is only evaluated for printer output.
        """
    @property
    def Subject(self) -> str:
        """
        contains the subject of the e-Mail message.
        
        This property is only evaluated for e-Mail output.
        
        **since**
        
            OOo 2.0
        """


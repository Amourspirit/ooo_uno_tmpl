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
# Namespace: com.sun.star.mail
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..datatransfer.x_transferable import XTransferable as XTransferable_2d800f38
    from .mail_attachment import MailAttachment as MailAttachment_c6770c37

class XMailMessage(XInterface_8f010a43):
    """
    Represents a mail message.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XMailMessage <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1mail_1_1XMailMessage.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.mail.XMailMessage']

    def addAttachment(self, aMailAttachment: 'MailAttachment_c6770c37') -> None:
        """
        Add a file attachment to a mail message.
        
        param aMailAttachment [in] specifies a file which should be attached to this mail message.
        """
        ...
    def addBccRecipient(self, sRecipientAddress: str) -> None:
        """
        Add a BCC recipients e-mail address to the list of recipients of this mail message.
        
        If the e-mail address doesn't conform to RFC 822 sending the mail message will fail.
        """
        ...
    def addCcRecipient(self, sRecipientAddress: str) -> None:
        """
        Add a Cc recipients e-mail address to the list of recipients of this mail message.
        
        If the e-mail address doesn't conform to RFC 822 sending the mail message will fail.
        """
        ...
    def addRecipient(self, sRecipientAddress: str) -> None:
        """
        Add a recipients e-mail address to the list of recipients of this mail message.
        
        If the e-mail address doesn't conform to RFC 822 sending the mail message will fail.
        """
        ...
    def getAttachments(self) -> 'typing.Tuple[MailAttachment_c6770c37, ...]':
        """
        Return a sequence of MailAttachment's that will be attached to this mail message.
        """
        ...
    def getBccRecipients(self) -> 'typing.Tuple[str, ...]':
        """
        Return a sequence of the e-mail addresses of all the BCC recipients of this mail message.
        """
        ...
    def getCcRecipients(self) -> 'typing.Tuple[str, ...]':
        """
        Return a sequence of the e-mail addresses of all the Cc recipients of this mail message.
        """
        ...
    def getRecipients(self) -> 'typing.Tuple[str, ...]':
        """
        Return a sequence of the e-mail addresses of all recipients of this mail message.
        """
        ...

    @property
    def Body(self) -> 'XTransferable_2d800f38':
        """
        The body of the mail message.
        
        It is expected that the transferable delivers the data as a string. Although a transferable may support multiple data flavors only the first data flavor supplied will be used to retrieve the data and it is expected that the data will be provided as a string.
        """
        ...

    @Body.setter
    def Body(self, value: 'XTransferable_2d800f38') -> None:
        ...
    @property
    def ReplyToAddress(self) -> str:
        """
        The e-mail address where replies on this mail message should be sent to.
        
        If the e-mail address doesn't conform to RFC 822 sending the mail message later will fail. If no ReplyToAddress is set replies go to the SenderAddress.
        """
        ...

    @ReplyToAddress.setter
    def ReplyToAddress(self, value: str) -> None:
        ...
    @property
    def SenderAddress(self) -> str:
        """
        The e-mail address of the sender of this mail message.
        
        The e-mail address has to conform to RFC 822.
        """
        ...

    @SenderAddress.setter
    def SenderAddress(self, value: str) -> None:
        ...
    @property
    def SenderName(self) -> str:
        """
        The display name of the sender of this mail message.
        """
        ...

    @SenderName.setter
    def SenderName(self, value: str) -> None:
        ...
    @property
    def Subject(self) -> str:
        """
        The subject of a mail message.
        """
        ...

    @Subject.setter
    def Subject(self, value: str) -> None:
        ...


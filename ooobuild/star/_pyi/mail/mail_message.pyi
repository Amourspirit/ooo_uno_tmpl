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
# Namespace: com.sun.star.mail
import typing
from .x_mail_message import XMailMessage as XMailMessage_ae200b4b
if typing.TYPE_CHECKING:
    from ..datatransfer.x_transferable import XTransferable as XTransferable_2d800f38
    from .mail_attachment import MailAttachment as MailAttachment_c6770c37

class MailMessage(XMailMessage_ae200b4b):
    """
    Service Class

    
    **since**
    
        OOo 2.0

    See Also:
        `API MailMessage <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1mail_1_1MailMessage.html>`_
    """
    def create(self, sTo: str, sFrom: str, sSubject: str, xBody: 'XTransferable_2d800f38') -> None:
        """
        Constructs an instance of a mail message.
        """
    def createWithAttachment(self, sTo: str, sFrom: str, sSubject: str, xBody: 'XTransferable_2d800f38', aMailAttachment: 'MailAttachment_c6770c37') -> None:
        """
        Constructs an instance of a mail message.
        """



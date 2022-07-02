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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.mail
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from ..datatransfer.x_transferable import XTransferable as XTransferable_2d800f38


class MailAttachment(object):
    """
    Struct Class

    A MailAttachment specifies a mail message attachment.
    
    **since**
    
        OOo 2.0

    See Also:
        `API MailAttachment <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1mail_1_1MailAttachment.html>`_
    """
    typeName: Literal['com.sun.star.mail.MailAttachment']

    def __init__(self, Data: typing.Optional[XTransferable_2d800f38] = ..., ReadableName: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Data (XTransferable, optional): Data value.
            ReadableName (str, optional): ReadableName value.
        """
        ...


    @property
    def Data(self) -> XTransferable_2d800f38:
        """
        The actual data which should be attached to a mail message.
        
        It is expected that the transferable delivers the data as sequence of bytes. Although a transferable may support multiple data flavors only the first data flavor supplied will be used to retrieve the data and it is expected that the type of the data is a sequence of bytes.
        """
        ...


    @property
    def ReadableName(self) -> str:
        """
        The name of the attachment as seen by the recipient of the mail message.
        
        ReadableName must not be empty.
        """
        ...



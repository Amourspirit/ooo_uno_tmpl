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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .outgoing_message_state import OutgoingMessageState as OutgoingMessageState_c200e54


class RecipientInfo(object):
    """
    Struct Class

    contains all information needed to send a message using one send protocol.
    
    To send one message via two different protocols, two RecipientInfos are needed - to send one message to different users with one protocol, one RecipientInfo can be used.

    See Also:
        `API RecipientInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1RecipientInfo.html>`_
    """
    typeName: Literal['com.sun.star.ucb.RecipientInfo']

    def __init__(self, ProtocolType: typing.Optional[str] = ..., State: typing.Optional[OutgoingMessageState_c200e54] = ..., To: typing.Optional[str] = ..., CC: typing.Optional[str] = ..., BCC: typing.Optional[str] = ..., Newsgroups: typing.Optional[str] = ..., Server: typing.Optional[str] = ..., Username: typing.Optional[str] = ..., Password: typing.Optional[str] = ..., VIMPostOfficePath: typing.Optional[str] = ..., ProtocolErrorString: typing.Optional[str] = ..., ProtocolErrorNumber: typing.Optional[int] = ..., SendTries: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            ProtocolType (str, optional): ProtocolType value.
            State (OutgoingMessageState, optional): State value.
            To (str, optional): To value.
            CC (str, optional): CC value.
            BCC (str, optional): BCC value.
            Newsgroups (str, optional): Newsgroups value.
            Server (str, optional): Server value.
            Username (str, optional): Username value.
            Password (str, optional): Password value.
            VIMPostOfficePath (str, optional): VIMPostOfficePath value.
            ProtocolErrorString (str, optional): ProtocolErrorString value.
            ProtocolErrorNumber (int, optional): ProtocolErrorNumber value.
            SendTries (int, optional): SendTries value.
        """


    @property
    def ProtocolType(self) -> str:
        """
        the protocol to use for sending (i.e.
        
        \"NNTP\", \"SMTP\", \"VIM\").
        """


    @property
    def State(self) -> OutgoingMessageState_c200e54:
        """
        the current state of the message.
        """


    @property
    def To(self) -> str:
        """
        the recipient(s) (e.g.
        
        e-mail address/es).
        
        Multiple addresses are separated by commas.
        """


    @property
    def CC(self) -> str:
        """
        the recipient(s) of a \"carbon copy\" (e.g.
        
        e-mail address/es).
        
        Multiple addresses are separated by commas.
        """


    @property
    def BCC(self) -> str:
        """
        the recipient(s) of \"blind carbon copy\" (e.g.
        
        e-mail address/es).
        
        Multiple addresses are separated by commas.
        """


    @property
    def Newsgroups(self) -> str:
        """
        the newsgroup(s) to which an article is be posted.
        
        Multiple addresses are separated by commas.
        """


    @property
    def Server(self) -> str:
        """
        the name of the server to be used for sending the message.
        """


    @property
    def Username(self) -> str:
        """
        the user name to be used for authorizing on the send server.
        """


    @property
    def Password(self) -> str:
        """
        the password to be used for authorizing on the send server.
        """


    @property
    def VIMPostOfficePath(self) -> str:
        """
        the Post Office Path (VIM only).
        """


    @property
    def ProtocolErrorString(self) -> str:
        """
        string representing the last error (generated by send server).
        """


    @property
    def ProtocolErrorNumber(self) -> int:
        """
        the number representing the last error (generated by send server).
        """


    @property
    def SendTries(self) -> int:
        """
        the count of tries to send a message.
        
        This count is 1 if the message was sent with the first try and increases with every unsuccessful retry.
        """



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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from .authentication_request import AuthenticationRequest as AuthenticationRequest_1b520eeb
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..task.interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7

class URLAuthenticationRequest(AuthenticationRequest_1b520eeb):
    """
    Exception Class

    An error specifying lack of correct authentication data (e.g., to log into an account).
    
    **since**
    
        OOo 3.2

    See Also:
        `API URLAuthenticationRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1URLAuthenticationRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.URLAuthenticationRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.ucb.URLAuthenticationRequest'
    __pyunostruct__: str = 'com.sun.star.ucb.URLAuthenticationRequest'

    typeName: str = 'com.sun.star.ucb.URLAuthenticationRequest'
    """Literal Constant ``com.sun.star.ucb.URLAuthenticationRequest``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Classification: typing.Optional[InteractionClassification_6c4d10e7] = InteractionClassification_6c4d10e7.ERROR, ServerName: typing.Optional[str] = '', Diagnostic: typing.Optional[str] = '', HasRealm: typing.Optional[bool] = False, Realm: typing.Optional[str] = '', HasUserName: typing.Optional[bool] = False, UserName: typing.Optional[str] = '', HasPassword: typing.Optional[bool] = False, Password: typing.Optional[str] = '', HasAccount: typing.Optional[bool] = False, Account: typing.Optional[str] = '', URL: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            ServerName (str, optional): ServerName value.
            Diagnostic (str, optional): Diagnostic value.
            HasRealm (bool, optional): HasRealm value.
            Realm (str, optional): Realm value.
            HasUserName (bool, optional): HasUserName value.
            UserName (str, optional): UserName value.
            HasPassword (bool, optional): HasPassword value.
            Password (str, optional): Password value.
            HasAccount (bool, optional): HasAccount value.
            Account (str, optional): Account value.
            URL (str, optional): URL value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Classification": Classification,
            "ServerName": ServerName,
            "Diagnostic": Diagnostic,
            "HasRealm": HasRealm,
            "Realm": Realm,
            "HasUserName": HasUserName,
            "UserName": UserName,
            "HasPassword": HasPassword,
            "Password": Password,
            "HasAccount": HasAccount,
            "Account": Account,
            "URL": URL,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._url = kwargs["URL"]
        inst_keys = ('URL',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def URL(self) -> str:
        """
        The URL for which authentication is requested.
        """
        return self._url
    
    @URL.setter
    def URL(self, value: str) -> None:
        self._url = value


__all__ = ['URLAuthenticationRequest']

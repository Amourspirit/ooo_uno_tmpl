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
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class SendMediaTypes(object):
    """
    Struct Class

    contains a list of Internet media types (like \"text/plain\" and \"text/html\"), that are related to a send protocol.

    See Also:
        `API SendMediaTypes <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1SendMediaTypes.html>`_
    """
    typeName: Literal['com.sun.star.ucb.SendMediaTypes']

    def __init__(self, Value: typing.Optional[typing.Tuple[str, ...]] = ..., ProtocolType: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Value (typing.Tuple[str, ...], optional): Value value.
            ProtocolType (str, optional): ProtocolType value.
        """


    @property
    def Value(self) -> typing.Tuple[str, ...]:
        """
        a list of Internet media types
        """


    @property
    def ProtocolType(self) -> str:
        """
        the protocol to which the information is related (i.e.
        
        \"NNTP\", \"SMTP\", \"VIM\").
        """



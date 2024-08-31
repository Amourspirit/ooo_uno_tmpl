# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class SendMediaTypes(object):
    """
    Struct Class

    contains a list of Internet media types (like \"text/plain\" and \"text/html\"), that are related to a send protocol.

    See Also:
        `API SendMediaTypes <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1SendMediaTypes.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.SendMediaTypes'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.SendMediaTypes'
    """Literal Constant ``com.sun.star.ucb.SendMediaTypes``"""

    def __init__(self, ProtocolType: typing.Optional[str] = '', Value: typing.Optional[typing.Tuple[str, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            ProtocolType (str, optional): ProtocolType value.
            Value (typing.Tuple[str, ...], optional): Value value.
        """
        super().__init__()

        if isinstance(ProtocolType, SendMediaTypes):
            oth: SendMediaTypes = ProtocolType
            self.ProtocolType = oth.ProtocolType
            self.Value = oth.Value
            return

        kargs = {
            "ProtocolType": ProtocolType,
            "Value": Value,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._protocol_type = kwargs["ProtocolType"]
        self._value = kwargs["Value"]


    @property
    def ProtocolType(self) -> str:
        """
        the protocol to which the information is related (i.e.
        
        \"NNTP\", \"SMTP\", \"VIM\").
        """
        return self._protocol_type

    @ProtocolType.setter
    def ProtocolType(self, value: str) -> None:
        self._protocol_type = value

    @property
    def Value(self) -> typing.Tuple[str, ...]:
        """
        a list of Internet media types
        """
        return self._value

    @Value.setter
    def Value(self, value: typing.Tuple[str, ...]) -> None:
        self._value = value


__all__ = ['SendMediaTypes']

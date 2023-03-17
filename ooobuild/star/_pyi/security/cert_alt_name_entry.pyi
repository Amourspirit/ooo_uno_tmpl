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
# Namespace: com.sun.star.security
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from .ext_alt_name_type import ExtAltNameType as ExtAltNameType_8c0df5


class CertAltNameEntry(object):
    """
    Struct Class

    struct contains a single entry within a Subject Alternative Name Extension of a X509 certificate.

    See Also:
        `API CertAltNameEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1security_1_1CertAltNameEntry.html>`_
    """
    typeName: Literal['com.sun.star.security.CertAltNameEntry']

    def __init__(self, Type: typing.Optional[ExtAltNameType_8c0df5] = ..., Value: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Type (ExtAltNameType, optional): Type value.
            Value (object, optional): Value value.
        """
        ...


    @property
    def Type(self) -> ExtAltNameType_8c0df5:
        """
        defines the type of the value.
        
        With this information you can determine how to interpret the Any value.
        """
        ...


    @property
    def Value(self) -> object:
        """
        stores the value of entry.
        """
        ...



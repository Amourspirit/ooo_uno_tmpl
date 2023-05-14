# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.configuration.backend
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class PropertyInfo(object):
    """
    Struct Class

    This structure contains all the information related to a property.

    See Also:
        `API PropertyInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1configuration_1_1backend_1_1PropertyInfo.html>`_
    """
    typeName: Literal['com.sun.star.configuration.backend.PropertyInfo']

    def __init__(self, Name: typing.Optional[str] = ..., Type: typing.Optional[str] = ..., Value: typing.Optional[object] = ..., Protected: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Type (str, optional): Type value.
            Value (object, optional): Value value.
            Protected (bool, optional): Protected value.
        """
        ...


    @property
    def Name(self) -> str:
        """
        The full name of the Property for eg.
        
        org.openoffice.Inet/Settings/ooInetHTTPProxyName
        """
        ...


    @property
    def Type(self) -> str:
        """
        The type of the Property.
        """
        ...


    @property
    def Value(self) -> object:
        """
        The value of the property.
        """
        ...


    @property
    def Protected(self) -> bool:
        """
        Is the property protected, if true the property can not be over written in later layer.
        """
        ...



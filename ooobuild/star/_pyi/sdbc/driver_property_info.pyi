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
# Namespace: com.sun.star.sdbc
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class DriverPropertyInfo(object):
    """
    Struct Class

    describes the driver properties for making a connection.
    
    The DriverPropertyInfo is of interest only to advanced programmers who need to interact with a driver to discover and supply properties for connections.

    See Also:
        `API DriverPropertyInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdbc_1_1DriverPropertyInfo.html>`_
    """
    typeName: Literal['com.sun.star.sdbc.DriverPropertyInfo']

    def __init__(self, Choices: typing.Optional[typing.Tuple[str, ...]] = ..., Name: typing.Optional[str] = ..., Description: typing.Optional[str] = ..., IsRequired: typing.Optional[bool] = ..., Value: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Choices (typing.Tuple[str, ...], optional): Choices value.
            Name (str, optional): Name value.
            Description (str, optional): Description value.
            IsRequired (bool, optional): IsRequired value.
            Value (str, optional): Value value.
        """


    @property
    def Choices(self) -> typing.Tuple[str, ...]:
        """
        contains a sequence of possible values if the value for the field DriverPropertyInfo.value may be selected from a particular set of values; otherwise empty.
        """


    @property
    def Name(self) -> str:
        """
        is the name of the property.
        """


    @property
    def Description(self) -> str:
        """
        is a brief description of the property, which may be null.
        """


    @property
    def IsRequired(self) -> bool:
        """
        is TRUE if a value must be supplied for this property during Driver.connect and FALSE otherwise.
        """


    @property
    def Value(self) -> str:
        """
        specifies the current value of the property, based on the driver-supplied default values.
        
        This field may be empty if no value is known.
        """



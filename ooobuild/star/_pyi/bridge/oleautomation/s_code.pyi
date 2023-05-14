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
# Namespace: com.sun.star.bridge.oleautomation
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class SCode(object):
    """
    Struct Class

    is the UNO representation of the Automation type SCODE.
    
    A SCODE is used to express errors in Automation. In UNO it could be represented by a long and therefore a typedef from long to a particular error type would do. But a typedef cannot be expressed in all language bindings. In the case where no typedefs are supported the actual type is used. That is, a typedef'd error type would be represented as int in Java. The information that the int is an error type is lost.
    
    When calling Automation objects from UNO the distinction between error type and long is important. Therefore the Scode is declared as struct.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API SCode <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1bridge_1_1oleautomation_1_1SCode.html>`_
    """
    typeName: Literal['com.sun.star.bridge.oleautomation.SCode']

    def __init__(self, Value: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Value (int, optional): Value value.
        """
        ...


    @property
    def Value(self) -> int:
        ...

    @Value.setter
    def Value(self, value: int) -> None:
        ...


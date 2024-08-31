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
# Namespace: com.sun.star.bridge.oleautomation
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class Currency(object):
    """
    Struct Class

    is the UNO representation of the Automation type CY, also know as CURRENCY.
    
    A CY could actually be represented as hyper in UNO and therefore a typedef from hyper to a currency type would do. But a typedef cannot be expressed in all language bindings. In the case where no typedefs are supported the actual type is used. That is, a typedef'd currency type would be represented as long in Java. The information that the long is a currency type is lost.
    
    When calling Automation objects from UNO the distinction between hyper and a currency type is important. Therefore Currency is declared as struct.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API Currency <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1bridge_1_1oleautomation_1_1Currency.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.bridge.oleautomation'
    __ooo_full_ns__: str = 'com.sun.star.bridge.oleautomation.Currency'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.bridge.oleautomation.Currency'
    """Literal Constant ``com.sun.star.bridge.oleautomation.Currency``"""

    def __init__(self, Value: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Value (int, optional): Value value.
        """
        super().__init__()

        if isinstance(Value, Currency):
            oth: Currency = Value
            self.Value = oth.Value
            return

        kargs = {
            "Value": Value,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._value = kwargs["Value"]


    @property
    def Value(self) -> int:
        """
        corresponds to the Automation type CY.
        """
        return self._value

    @Value.setter
    def Value(self, value: int) -> None:
        self._value = value


__all__ = ['Currency']

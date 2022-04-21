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
# Namespace: com.sun.star.beans
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .property_state import PropertyState as PropertyState_c97b0c77


class PropertyValue(object):
    """
    Struct Class

    specifies a property value.

    See Also:
        `API PropertyValue <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1PropertyValue.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.PropertyValue'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.beans.PropertyValue'
    """Literal Constant ``com.sun.star.beans.PropertyValue``"""

    def __init__(self, Name: typing.Optional[str] = '', Handle: typing.Optional[int] = 0, Value: typing.Optional[object] = None, State: typing.Optional[PropertyState_c97b0c77] = PropertyState_c97b0c77.DIRECT_VALUE) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Handle (int, optional): Handle value.
            Value (object, optional): Value value.
            State (PropertyState, optional): State value.
        """
        super().__init__()

        if isinstance(Name, PropertyValue):
            oth: PropertyValue = Name
            self.Name = oth.Name
            self.Handle = oth.Handle
            self.Value = oth.Value
            self.State = oth.State
            return

        kargs = {
            "Name": Name,
            "Handle": Handle,
            "Value": Value,
            "State": State,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._handle = kwargs["Handle"]
        self._value = kwargs["Value"]
        self._state = kwargs["State"]


    @property
    def Name(self) -> str:
        """
        specifies the name of the property.
        
        The name is unique within a sequence of PropertyValues. Upper and lower case are distinguished.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Handle(self) -> int:
        """
        contains an implementation-specific handle for the property.
        
        It may be -1 if the implementation has no handle. If available it can be used for fast lookups.
        """
        return self._handle
    
    @Handle.setter
    def Handle(self, value: int) -> None:
        self._handle = value

    @property
    def Value(self) -> object:
        """
        contains the value of the property or VOID, if no value is available.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: object) -> None:
        self._value = value

    @property
    def State(self) -> PropertyState_c97b0c77:
        """
        determines if the value comes from the object itself or from a default and if the value cannot be determined exactly.
        """
        return self._state
    
    @State.setter
    def State(self, value: PropertyState_c97b0c77) -> None:
        self._state = value


__all__ = ['PropertyValue']

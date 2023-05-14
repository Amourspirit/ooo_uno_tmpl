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
# Namespace: com.sun.star.beans
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class Ambiguous(object):
    """
    Struct Class

    A value of a given type that can be ambiguous.
    
    This structure is used as the type of interface attributes corresponding to instances of com.sun.star.beans.Property that have the com.sun.star.beans.PropertyAttribute.MAYBEAMBIGUOUS.

    See Also:
        `API Ambiguous <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Ambiguous_3_01T_01_4.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.Ambiguous'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.beans.Ambiguous'
    """Literal Constant ``com.sun.star.beans.Ambiguous``"""

    def __init__(self, Value: typing.Optional[object] = None, IsAmbiguous: typing.Optional[bool] = None) -> None:
        """
        Constructor

        Arguments:
            Value (object, optional): Value value.
            IsAmbiguous (bool, optional): IsAmbiguous value.
        """
        super().__init__()

        if isinstance(Value, Ambiguous):
            oth: Ambiguous = Value
            self.Value = oth.Value
            self.IsAmbiguous = oth.IsAmbiguous
            return

        kargs = {
            "Value": Value,
            "IsAmbiguous": IsAmbiguous,
        }
        if kargs["Value"] is UNO_NONE:
            kargs["Value"] = None
        if kargs["IsAmbiguous"] is UNO_NONE:
            kargs["IsAmbiguous"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._value = kwargs["Value"]
        self._is_ambiguous = kwargs["IsAmbiguous"]


    @property
    def Value(self) -> object:
        """
        The underlying value of this structure instance.
        
        Even if this structure instance is ambiguous, this member should contain a useful value. If there is no useful value for an ambiguous structure instance, com.sun.star.beans.Optional can be used as the type of this member.
        """
        return self._value

    @Value.setter
    def Value(self, value: object) -> None:
        self._value = value

    @property
    def IsAmbiguous(self) -> bool:
        """
        Marks this structure instance as ambiguous.
        """
        return self._is_ambiguous

    @IsAmbiguous.setter
    def IsAmbiguous(self, value: bool) -> None:
        self._is_ambiguous = value


__all__ = ['Ambiguous']

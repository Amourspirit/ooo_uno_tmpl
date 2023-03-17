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
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from .get_property_tolerant_result import GetPropertyTolerantResult as GetPropertyTolerantResult_7c4e115e
from .property_state import PropertyState as PropertyState_c97b0c77
import typing


class GetDirectPropertyTolerantResult(GetPropertyTolerantResult_7c4e115e):
    """
    Struct Class

    specifies information being retrieved about a single property.
    
    This type is used for the elements in the sequence returned by com.sun.star.beans.XTolerantMultiPropertySet.GetDirectPropertyTolerantResult.

    See Also:
        `API GetDirectPropertyTolerantResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1GetDirectPropertyTolerantResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.GetDirectPropertyTolerantResult'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.beans.GetDirectPropertyTolerantResult'
    """Literal Constant ``com.sun.star.beans.GetDirectPropertyTolerantResult``"""

    def __init__(self, Result: typing.Optional[int] = 0, State: typing.Optional[PropertyState_c97b0c77] = PropertyState_c97b0c77.DIRECT_VALUE, Value: typing.Optional[object] = None, Name: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Result (int, optional): Result value.
            State (PropertyState, optional): State value.
            Value (object, optional): Value value.
            Name (str, optional): Name value.
        """

        if isinstance(Result, GetDirectPropertyTolerantResult):
            oth: GetDirectPropertyTolerantResult = Result
            self.Result = oth.Result
            self.State = oth.State
            self.Value = oth.Value
            self.Name = oth.Name
            return

        kargs = {
            "Result": Result,
            "State": State,
            "Value": Value,
            "Name": Name,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        inst_keys = ('Name',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Name(self) -> str:
        """
        specifies the name of the property.
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value


__all__ = ['GetDirectPropertyTolerantResult']

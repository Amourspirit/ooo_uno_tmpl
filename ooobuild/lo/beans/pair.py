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


class Pair(object):
    """
    Struct Class

    A tuple, or pair.
    
    This structure allows for conveniently packing together two values of any type, and could be useful as the result type of methods.
    
    **since**
    
        OOo 3.0

    See Also:
        `API Pair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Pair_3_01T_00_01U_01_4.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.beans'
    __ooo_full_ns__: str = 'com.sun.star.beans.Pair'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.beans.Pair'
    """Literal Constant ``com.sun.star.beans.Pair``"""

    def __init__(self, First: typing.Optional[object] = None, Second: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            First (object, optional): First value.
            Second (object, optional): Second value.
        """
        super().__init__()

        if isinstance(First, Pair):
            oth: Pair = First
            self.First = oth.First
            self.Second = oth.Second
            return

        kargs = {
            "First": First,
            "Second": Second,
        }
        if kargs["First"] is UNO_NONE:
            kargs["First"] = None
        if kargs["Second"] is UNO_NONE:
            kargs["Second"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._first = kwargs["First"]
        self._second = kwargs["Second"]


    @property
    def First(self) -> object:
        """
        first object.
        """
        return self._first
    
    @First.setter
    def First(self, value: object) -> None:
        self._first = value

    @property
    def Second(self) -> object:
        """
        second object.
        """
        return self._second
    
    @Second.setter
    def Second(self, value: object) -> None:
        self._second = value


__all__ = ['Pair']

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
# Namespace: com.sun.star.chart
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing


class ChartDataValue(object):
    """
    Struct Class

    describes a single data value, including the error
    
    This struct is currently used nowhere.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API ChartDataValue <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1ChartDataValue.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartDataValue'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.chart.ChartDataValue'
    """Literal Constant ``com.sun.star.chart.ChartDataValue``"""

    def __init__(self, Value: typing.Optional[float] = 0.0, HighError: typing.Optional[float] = 0.0, LowError: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            Value (float, optional): Value value.
            HighError (float, optional): HighError value.
            LowError (float, optional): LowError value.
        """
        super().__init__()

        if isinstance(Value, ChartDataValue):
            oth: ChartDataValue = Value
            self.Value = oth.Value
            self.HighError = oth.HighError
            self.LowError = oth.LowError
            return

        kargs = {
            "Value": Value,
            "HighError": HighError,
            "LowError": LowError,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._value = kwargs["Value"]
        self._high_error = kwargs["HighError"]
        self._low_error = kwargs["LowError"]


    @property
    def Value(self) -> float:
        """
        value by itself.
        """
        return self._value
    
    @Value.setter
    def Value(self, value: float) -> None:
        self._value = value

    @property
    def HighError(self) -> float:
        """
        highest possible error value.
        """
        return self._high_error
    
    @HighError.setter
    def HighError(self, value: float) -> None:
        self._high_error = value

    @property
    def LowError(self) -> float:
        """
        lowest possible error value.
        """
        return self._low_error
    
    @LowError.setter
    def LowError(self, value: float) -> None:
        self._low_error = value


__all__ = ['ChartDataValue']

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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing


class UpperLowerMarginScale(object):
    """
    Struct Class

    specifies an upper and lower margin.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UpperLowerMarginScale <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1UpperLowerMarginScale.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame.status'
    __ooo_full_ns__: str = 'com.sun.star.frame.status.UpperLowerMarginScale'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.frame.status.UpperLowerMarginScale'
    """Literal Constant ``com.sun.star.frame.status.UpperLowerMarginScale``"""

    def __init__(self, Upper: typing.Optional[int] = 0, Lower: typing.Optional[int] = 0, ScaleUpper: typing.Optional[int] = 0, ScaleLower: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Upper (int, optional): Upper value.
            Lower (int, optional): Lower value.
            ScaleUpper (int, optional): ScaleUpper value.
            ScaleLower (int, optional): ScaleLower value.
        """
        super().__init__()

        if isinstance(Upper, UpperLowerMarginScale):
            oth: UpperLowerMarginScale = Upper
            self.Upper = oth.Upper
            self.Lower = oth.Lower
            self.ScaleUpper = oth.ScaleUpper
            self.ScaleLower = oth.ScaleLower
            return

        kargs = {
            "Upper": Upper,
            "Lower": Lower,
            "ScaleUpper": ScaleUpper,
            "ScaleLower": ScaleLower,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._upper = kwargs["Upper"]
        self._lower = kwargs["Lower"]
        self._scale_upper = kwargs["ScaleUpper"]
        self._scale_lower = kwargs["ScaleLower"]


    @property
    def Upper(self) -> int:
        """
        specifies a upper margin in 1/100th mm.
        """
        return self._upper
    
    @Upper.setter
    def Upper(self, value: int) -> None:
        self._upper = value

    @property
    def Lower(self) -> int:
        """
        specifies a lower margin in 1/100th mm.
        """
        return self._lower
    
    @Lower.setter
    def Lower(self, value: int) -> None:
        self._lower = value

    @property
    def ScaleUpper(self) -> int:
        """
        specifies a scale value for the upper margin.
        """
        return self._scale_upper
    
    @ScaleUpper.setter
    def ScaleUpper(self, value: int) -> None:
        self._scale_upper = value

    @property
    def ScaleLower(self) -> int:
        """
        specifies a scale value for the lower margin.
        """
        return self._scale_lower
    
    @ScaleLower.setter
    def ScaleLower(self, value: int) -> None:
        self._scale_lower = value


__all__ = ['UpperLowerMarginScale']

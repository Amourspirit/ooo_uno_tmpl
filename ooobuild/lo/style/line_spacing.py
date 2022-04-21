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
# Namespace: com.sun.star.style
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing


class LineSpacing(object):
    """
    Struct Class

    This structure is used to specify the height of a text line.

    See Also:
        `API LineSpacing <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1style_1_1LineSpacing.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.style'
    __ooo_full_ns__: str = 'com.sun.star.style.LineSpacing'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.style.LineSpacing'
    """Literal Constant ``com.sun.star.style.LineSpacing``"""

    def __init__(self, Mode: typing.Optional[int] = 0, Height: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Mode (int, optional): Mode value.
            Height (int, optional): Height value.
        """
        super().__init__()

        if isinstance(Mode, LineSpacing):
            oth: LineSpacing = Mode
            self.Mode = oth.Mode
            self.Height = oth.Height
            return

        kargs = {
            "Mode": Mode,
            "Height": Height,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._mode = kwargs["Mode"]
        self._height = kwargs["Height"]


    @property
    def Mode(self) -> int:
        """
        This value specifies the way the height is specified.
        """
        return self._mode
    
    @Mode.setter
    def Mode(self, value: int) -> None:
        self._mode = value

    @property
    def Height(self) -> int:
        """
        This value specifies the height in regard to Mode.
        """
        return self._height
    
    @Height.setter
    def Height(self, value: int) -> None:
        self._height = value


__all__ = ['LineSpacing']

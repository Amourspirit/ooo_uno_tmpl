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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class Selection(object):
    """
    Struct Class

    specifies a numerical range.

    See Also:
        `API Selection <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Selection.html>`_
    """
    typeName: Literal['com.sun.star.awt.Selection']

    def __init__(self, Min: typing.Optional[int] = ..., Max: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Min (int, optional): Min value.
            Max (int, optional): Max value.
        """


    @property
    def Min(self) -> int:
        """
        specifies the lower limit of the range.
        """


    @property
    def Max(self) -> int:
        """
        specifies the upper limit of the range.
        """



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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..util.time import Time as Time_604e0855


class XTimeField(XInterface_8f010a43):
    """
    gives access to the value and settings of a time field.

    See Also:
        `API XTimeField <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XTimeField.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XTimeField'

    def getFirst(self) -> Time_604e0855:
        """
        returns the currently set first value which is set on POS1 key.
        """
        ...
    def getLast(self) -> Time_604e0855:
        """
        returns the currently set last value which is set on END key.
        """
        ...
    def getMax(self) -> Time_604e0855:
        """
        returns the currently set maximum time value that can be entered by the user.
        """
        ...
    def getMin(self) -> Time_604e0855:
        """
        returns the currently set minimum time value that can be entered by the user.
        """
        ...
    def getTime(self) -> Time_604e0855:
        """
        returns the time value which is currently displayed in the time field.
        """
        ...
    def isEmpty(self) -> bool:
        """
        returns whether currently an empty value is set for the time.
        """
        ...
    def isStrictFormat(self) -> bool:
        """
        returns whether the format is currently checked during user input.
        """
        ...
    def setEmpty(self) -> None:
        """
        sets an empty value for the time.
        """
        ...
    def setFirst(self, Time: Time_604e0855) -> None:
        """
        sets the first value to be set on POS1 key.
        """
        ...
    def setLast(self, Time: Time_604e0855) -> None:
        """
        sets the last value to be set on END key.
        """
        ...
    def setMax(self, Time: Time_604e0855) -> None:
        """
        sets the maximum time value that can be entered by the user.
        """
        ...
    def setMin(self, Time: Time_604e0855) -> None:
        """
        sets the minimum time value that can be entered by the user.
        """
        ...
    def setStrictFormat(self, bStrict: bool) -> None:
        """
        determines if the format is checked during user input.
        """
        ...
    def setTime(self, Time: Time_604e0855) -> None:
        """
        sets the time value which is displayed in the time field.
        """
        ...



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
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class DeviceInfo(object):
    """
    Struct Class

    contains information about a device.

    See Also:
        `API DeviceInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1DeviceInfo.html>`_
    """
    typeName: Literal['com.sun.star.awt.DeviceInfo']

    def __init__(self, Width: typing.Optional[int] = ..., Height: typing.Optional[int] = ..., LeftInset: typing.Optional[int] = ..., TopInset: typing.Optional[int] = ..., RightInset: typing.Optional[int] = ..., BottomInset: typing.Optional[int] = ..., PixelPerMeterX: typing.Optional[float] = ..., PixelPerMeterY: typing.Optional[float] = ..., BitsPerPixel: typing.Optional[int] = ..., Capabilities: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Width (int, optional): Width value.
            Height (int, optional): Height value.
            LeftInset (int, optional): LeftInset value.
            TopInset (int, optional): TopInset value.
            RightInset (int, optional): RightInset value.
            BottomInset (int, optional): BottomInset value.
            PixelPerMeterX (float, optional): PixelPerMeterX value.
            PixelPerMeterY (float, optional): PixelPerMeterY value.
            BitsPerPixel (int, optional): BitsPerPixel value.
            Capabilities (int, optional): Capabilities value.
        """
        ...


    @property
    def Width(self) -> int:
        """
        contains the width of the device in pixels.
        """
        ...


    @property
    def Height(self) -> int:
        """
        contains the height of the device in pixels.
        """
        ...


    @property
    def LeftInset(self) -> int:
        """
        contains the inset from the left.
        """
        ...


    @property
    def TopInset(self) -> int:
        """
        contains the inset from the top.
        """
        ...


    @property
    def RightInset(self) -> int:
        """
        contains the inset from the right.
        """
        ...


    @property
    def BottomInset(self) -> int:
        """
        contains the inset from the bottom.
        """
        ...


    @property
    def PixelPerMeterX(self) -> float:
        """
        contains the X-axis resolution of the device in pixel/meter.
        """
        ...


    @property
    def PixelPerMeterY(self) -> float:
        """
        contains the Y-axis resolution of the device in pixel/meter.
        """
        ...


    @property
    def BitsPerPixel(self) -> int:
        """
        contains the color-depth of the device.
        """
        ...


    @property
    def Capabilities(self) -> int:
        """
        specifies special operations which are possible on the device.
        """
        ...



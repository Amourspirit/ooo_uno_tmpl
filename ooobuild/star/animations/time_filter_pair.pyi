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
# Namespace: com.sun.star.animations
# Libre Office Version: 7.4
import typing


class TimeFilterPair(object):
    """
    Struct Class


    See Also:
        `API TimeFilterPair <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1animations_1_1TimeFilterPair.html>`_
    """
    typeName: str = 'com.sun.star.animations.TimeFilterPair'

    def __init__(self, Time: typing.Optional[float] = ..., Progress: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            Time (float, optional): Time value.
            Progress (float, optional): Progress value.
        """
        ...

    @property
    def Time(self) -> float:
        ...
    @Time.setter
    def Time(self, value: float) -> None:
        ...
    @property
    def Progress(self) -> float:
        ...
    @Progress.setter
    def Progress(self, value: float) -> None:
        ...

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
# Namespace: com.sun.star.sheet.opencl
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .open_cl_device import OpenCLDevice as OpenCLDevice_180d0e41


class OpenCLPlatform(object):
    """
    Struct Class


    See Also:
        `API OpenCLPlatform <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1opencl_1_1OpenCLPlatform.html>`_
    """
    typeName: Literal['com.sun.star.sheet.opencl.OpenCLPlatform']

    def __init__(self, Devices: typing.Optional[typing.Tuple[OpenCLDevice_180d0e41, ...]] = ..., Name: typing.Optional[str] = ..., Vendor: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Devices (typing.Tuple[OpenCLDevice, ...], optional): Devices value.
            Name (str, optional): Name value.
            Vendor (str, optional): Vendor value.
        """
        ...


    @property
    def Devices(self) -> typing.Tuple[OpenCLDevice_180d0e41, ...]:
        ...


    @property
    def Name(self) -> str:
        """
        The name of the platform as returned by OpenCL.
        """
        ...


    @property
    def Vendor(self) -> str:
        ...



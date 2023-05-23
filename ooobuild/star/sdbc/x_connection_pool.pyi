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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdbc
import typing

from .x_driver_access import XDriverAccess as XDriverAccess_b9ec0bba
from .x_driver_manager import XDriverManager as XDriverManager_c6470c23


class XConnectionPool(XDriverAccess_b9ec0bba, XDriverManager_c6470c23):
    """

    See Also:
        `API XConnectionPool <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XConnectionPool.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdbc.XConnectionPool'


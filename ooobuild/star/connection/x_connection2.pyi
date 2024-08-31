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
# Namespace: com.sun.star.connection
from __future__ import annotations
import typing

import uno
from .x_connection import XConnection as XConnection_f2320da0


class XConnection2(XConnection_f2320da0):
    """
    XConnection2 extends the XConnection interface with available and readSomeBytes

    See Also:
        `API XConnection2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1connection_1_1XConnection2.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.connection.XConnection2'

    def available(self) -> int:
        """
        Gives the number of bytes available via read without blocking.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def readSomeBytes(self, aData: uno.ByteSequence, nMaxBytesToRead: int) -> int:
        """
        Blocks if no data is available otherwise reads at max nMaxBytesToRead but at least 1 byte.

        * ``aData`` is an out direction argument.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...



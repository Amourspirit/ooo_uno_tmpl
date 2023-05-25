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
# Namespace: com.sun.star.io
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_input_stream import XInputStream as XInputStream_98d40ab4

class XInputStreamProvider(XInterface_8f010a43):
    """
    Interface for providing an input stream.
    
    Every time createInputStream() is called a new input stream is returned, always pointing to the begin of the same data. All input streams returned by createInputStream() are completely independent from each other.

    See Also:
        `API XInputStreamProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XInputStreamProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.XInputStreamProvider'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.io.XInputStreamProvider'

    @abstractmethod
    def createInputStream(self) -> XInputStream_98d40ab4:
        """
        Creates a new input stream, every time providing the same data.
        """
        ...

__all__ = ['XInputStreamProvider']



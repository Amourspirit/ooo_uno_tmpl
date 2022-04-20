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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.io
import typing
from abc import abstractmethod
from .x_output_stream import XOutputStream as XOutputStream_a4e00b35

class XSequenceOutputStream(XOutputStream_a4e00b35):
    """
    This interface offers access to the written bytes.

    See Also:
        `API XSequenceOutputStream <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XSequenceOutputStream.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.XSequenceOutputStream'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.io.XSequenceOutputStream'

    @abstractmethod
    def getWrittenBytes(self) -> 'typing.Tuple[int, ...]':
        """
        allows to get access to the written data

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
            com.sun.star.io.IOException: ``IOException``
        """

__all__ = ['XSequenceOutputStream']


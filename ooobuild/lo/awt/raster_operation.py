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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from typing import cast
from enum import Enum
from com.sun.star.awt.RasterOperation import RasterOperationProto

class RasterOperation(Enum):
    """
    Enum Class


    See Also:
        `API RasterOperation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#a54da390665a5b42acc81143cd24926fd>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.RasterOperation'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.awt.RasterOperation'

    ALLBITS = cast(RasterOperationProto, 'ALLBITS')
    """
    All bits which are affected by this operation are set to 1.
    """
    INVERT = cast(RasterOperationProto, 'INVERT')
    """
    All bits which are affected by this operation are inverted.
    """
    OVERPAINT = cast(RasterOperationProto, 'OVERPAINT')
    """
    sets all pixel as written in the output operation.
    """
    XOR = cast(RasterOperationProto, 'XOR')
    """
    uses the pixel written as one and the current pixel as the other operator of an exclusive or-operation.
    """
    ZEROBITS = cast(RasterOperationProto, 'ZEROBITS')
    """
    All bits which are affected by this operation are set to 0.
    """

__all__ = ['RasterOperation']


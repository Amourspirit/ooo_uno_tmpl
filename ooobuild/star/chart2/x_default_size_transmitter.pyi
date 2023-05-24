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
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef


class XDefaultSizeTransmitter(XInterface_8f010a43):
    """
    Allows to set a default size.
    
    This size will be used in case no further information si available.

    See Also:
        `API XDefaultSizeTransmitter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XDefaultSizeTransmitter.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.chart2.XDefaultSizeTransmitter'

    def setDefaultSize(self, aSize100ThMm: Size_576707ef) -> None:
        """
        set a default size
        """
        ...



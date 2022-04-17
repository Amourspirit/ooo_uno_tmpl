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
# Libre Office Version: 7.3
# Namespace: com.sun.star.chart2
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..util.color import Color as Color_68e908c5

class XColorScheme(XInterface_8f010a43):
    """

    See Also:
        `API XColorScheme <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XColorScheme.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.XColorScheme'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.XColorScheme'

    @abstractmethod
    def getColorByIndex(self, nIndex: int) -> 'Color_68e908c5':
        """
        returns the default color for the nth data series.
        
        This may be a system wide color or a color coming from a color scheme.
        
        Usually there exist a fixed number of default colors. This method should always return a valid Color. If the index (i) is higher than the number of default colors (n), the method should return the modulus (i mod n), i.e., the colors should repeat in a cyclic way.
        """

__all__ = ['XColorScheme']

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
    from .x_diagram import XDiagram as XDiagram_96fe0a59

class XDiagramProvider(XInterface_8f010a43):
    """
    Gives access to a single diagram.
    
    This interface is needed by the wrapper for the old API (namespace com.sun.star.chart).

    See Also:
        `API XDiagramProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XDiagramProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.XDiagramProvider'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.XDiagramProvider'

    @abstractmethod
    def getDiagram(self) -> 'XDiagram_96fe0a59':
        """
        """
    @abstractmethod
    def setDiagram(self, xDiagram: 'XDiagram_96fe0a59') -> None:
        """
        """

__all__ = ['XDiagramProvider']


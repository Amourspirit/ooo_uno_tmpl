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
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from .x_color_scheme import XColorScheme as XColorScheme_c4be0bf8
    from .x_legend import XLegend as XLegend_8cce09f3
    from .data.x_data_source import XDataSource as XDataSource_f6340d57

class XDiagram(XInterface_8f010a43):
    """

    See Also:
        `API XDiagram <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XDiagram.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.chart2.XDiagram']

    def getDefaultColorScheme(self) -> 'XColorScheme_c4be0bf8':
        """
        returns an XColorScheme that defines the default colors for data series (or data points) in the diagram.
        """
        ...
    def getFloor(self) -> 'XPropertySet_bc180bfa':
        """
        returns the property set that determines the visual appearance of the floor if any.
        
        The floor is the bottom of a 3D diagram. For a 2D diagram NULL is returned.
        """
        ...
    def getLegend(self) -> 'XLegend_8cce09f3':
        """
        returns the legend, which may represent data series and other information about a diagram in a separate box.
        """
        ...
    def getWall(self) -> 'XPropertySet_bc180bfa':
        """
        returns the property set that determines the visual appearance of the wall.
        
        The wall is the area behind the union of all coordinate systems used in a diagram.
        """
        ...
    def setDefaultColorScheme(self, xColorScheme: 'XColorScheme_c4be0bf8') -> None:
        """
        sets an XColorScheme that defines the default colors for data series (or data points) in the diagram.
        """
        ...
    def setDiagramData(self, xDataSource: 'XDataSource_f6340d57', aArguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        sets new data to the diagram.
        
        For standard parameters that may be used, see the service StandardDiagramCreationParameters.
        """
        ...
    def setLegend(self, xLegend: 'XLegend_8cce09f3') -> None:
        """
        sets a new legend.
        """
        ...



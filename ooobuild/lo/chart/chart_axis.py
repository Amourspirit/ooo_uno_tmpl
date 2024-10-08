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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.chart
from __future__ import annotations
import typing
from abc import abstractmethod
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_axis import XAxis as XAxis_71210907
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..xml.user_defined_attributes_supplier import UserDefinedAttributesSupplier as UserDefinedAttributesSupplier_9fbe1222
if typing.TYPE_CHECKING:
    from .time_increment import TimeIncrement as TimeIncrement_c7e70c4e
    from com.sun.star.chart.ChartAxisArrangeOrderType import ChartAxisArrangeOrderTypeProto  # type: ignore
    from com.sun.star.chart.ChartAxisPosition import ChartAxisPositionProto  # type: ignore
    from com.sun.star.chart.ChartAxisLabelPosition import ChartAxisLabelPositionProto  # type: ignore
    from com.sun.star.chart.ChartAxisMarkPosition import ChartAxisMarkPositionProto  # type: ignore

class ChartAxis(LineProperties_f13f0da9, CharacterProperties_1d4f0ef3, UserDefinedAttributesSupplier_9fbe1222, XPropertySet_bc180bfa, XAxis_71210907):
    """
    Service Class

    Specifies the axes in a diagram.
    
    Note: The text properties correlate to all axis description elements, not to just a single text element.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ChartAxis <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartAxis.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart'
    __ooo_full_ns__: str = 'com.sun.star.chart.ChartAxis'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def ArrangeOrder(self) -> ChartAxisArrangeOrderTypeProto:
        """
        The axis description may be arranged in a special order for a better placement.
        """
        ...

    @property
    @abstractmethod
    def AutoMax(self) -> bool:
        """
        The maximum value of the axis scale is calculated by the chart if this property is TRUE.
        """
        ...

    @property
    @abstractmethod
    def AutoMin(self) -> bool:
        """
        The minimum value of the axis scale is calculated by the chart if this property is TRUE.
        """
        ...

    @property
    @abstractmethod
    def AutoOrigin(self) -> bool:
        """
        The origin is calculated by the chart if this property is TRUE.
        """
        ...

    @property
    @abstractmethod
    def AutoStepHelp(self) -> bool:
        """
        The number of help intervals within a main interval is calculated by the chart if this property is TRUE.
        """
        ...

    @property
    @abstractmethod
    def AutoStepMain(self) -> bool:
        """
        The distance between the main tick marks is calculated by the chart if this property is TRUE.
        """
        ...

    @property
    @abstractmethod
    def AxisType(self) -> int:
        """
        determines which type of axis this is, e.g.
        
        a date-axis or a category-axis
        
        **since**
        
            OOo 3.4
        """
        ...

    @property
    @abstractmethod
    def CrossoverPosition(self) -> ChartAxisPositionProto:
        """
        Determines where the axis crosses the other axis.
        """
        ...

    @property
    @abstractmethod
    def CrossoverValue(self) -> float:
        """
        Determines the scale value on the other axis when CrossoverPosition is set to VALUE.
        """
        ...

    @property
    @abstractmethod
    def DisplayLabels(self) -> bool:
        """
        Properties for axes labels:
        
        Determines whether to display text at the axis or not.
        """
        ...

    @property
    @abstractmethod
    def GapWidth(self) -> int:
        """
        Specifies the width of the gaps between each set of data points in a bar chart.
        
        The value is given in percent of the width of a bar; the valid range is 0 to 600%.
        """
        ...

    @property
    @abstractmethod
    def HelpMarks(self) -> int:
        """
        Determines the type of the help marks.
        """
        ...

    @property
    @abstractmethod
    def LabelPosition(self) -> ChartAxisLabelPositionProto:
        """
        Determines where the axis labels are placed.
        """
        ...

    @property
    @abstractmethod
    def LinkNumberFormatToSource(self) -> bool:
        """
        determines whether to use the number format given by the container application, e.g.
        
        a spreadsheet document, or from the own property NumberFormat.
        """
        ...

    @property
    @abstractmethod
    def Logarithmic(self) -> bool:
        """
        Determines if the axis is scaled logarithmically or not (linear).
        """
        ...

    @property
    @abstractmethod
    def MarkPosition(self) -> ChartAxisMarkPositionProto:
        """
        Determines where the interval marks are placed.
        """
        ...

    @property
    @abstractmethod
    def Marks(self) -> int:
        """
        Properties for interval marks:
        
        Determines the type of the marks.
        """
        ...

    @property
    @abstractmethod
    def Max(self) -> float:
        """
        Properties for scaling:
        
        Contains the maximum value for the axis scale.
        """
        ...

    @property
    @abstractmethod
    def Min(self) -> float:
        """
        Contains the minimum value for the axis scale.
        """
        ...

    @property
    @abstractmethod
    def NumberFormat(self) -> int:
        """
        Contains the type id for the number formatter of the axis.
        """
        ...

    @property
    @abstractmethod
    def Origin(self) -> float:
        """
        Indicates the reference value where bars or areas have their grounding.
        
        This property has only an effect when the used ODF file format does not allow for further axis positioning or the axis is a secondary y-axis.
        """
        ...

    @property
    @abstractmethod
    def Overlap(self) -> int:
        """
        Properties related to bar charts:
        
        Determines the overlap of the bars in a bar-type chart.
        
        The value is given in percent of the width of the bars. The valid range is -100% to +100%. +100% means full overlap, -100% indicates a distance of one bar between 2 neighboring bars.
        """
        ...

    @property
    @abstractmethod
    def ReverseDirection(self) -> bool:
        """
        Determines if the axis orientation is mathematical or reversed.
        """
        ...

    @property
    @abstractmethod
    def StepHelp(self) -> float:
        """
        """
        ...

    @property
    @abstractmethod
    def StepHelpCount(self) -> int:
        """
        Contains the number of help intervals within a main interval.
        
        E.g. a StepHelpCount of 5 divides the main interval into 5 pieces and thus produces 4 help tick marks.
        """
        ...

    @property
    @abstractmethod
    def StepMain(self) -> float:
        """
        Contains the distance between the main tick marks.
        """
        ...

    @property
    @abstractmethod
    def TextBreak(self) -> bool:
        """
        Determines if long text is broken into multiple lines.
        """
        ...

    @property
    @abstractmethod
    def TextCanOverlap(self) -> bool:
        """
        Determines if certain labels are hidden, if they would otherwise overlap.
        
        In this case, the value of this property must be set to FALSE.
        """
        ...

    @property
    @abstractmethod
    def TextRotation(self) -> int:
        """
        Determines the rotation of the text elements (axis description) in 100th degrees.
        """
        ...

    @property
    @abstractmethod
    def TimeIncrement(self) -> TimeIncrement_c7e70c4e:
        """
        if the current axis is a date-axis the intervals are chosen as given with TimeIncrement
        
        **since**
        
            OOo 3.4
        """
        ...


__all__ = ['ChartAxis']
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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.4
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class ChartAxisMarkPositionProto(Protocol):
    """Protocol for ChartAxisMarkPosition"""

    @property
    def typeName(self) -> Literal["com.sun.star.chart.ChartAxisMarkPosition"]:
        ...
    value: Any
    AT_AXIS: ChartAxisMarkPositionProto
    AT_LABELS: ChartAxisMarkPositionProto
    AT_LABELS_AND_AXIS: ChartAxisMarkPositionProto

AT_AXIS: ChartAxisMarkPositionProto
"""
The interval marks are drawn at the axis line.

This makes a difference to \"AT_LABELS\" only when the labels are not placed near the axis (
"""
AT_LABELS: ChartAxisMarkPositionProto
"""
The interval marks are drawn besides the axis labels.
"""
AT_LABELS_AND_AXIS: ChartAxisMarkPositionProto
"""
Interval marks are drawn at the axis line and also besides the axis labels.

This makes a difference to \"AT_LABELS\" only when the labels are not placed near the axis (
"""


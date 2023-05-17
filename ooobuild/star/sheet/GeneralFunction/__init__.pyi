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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from com.sun.star._pyi.sheet.general_function import GeneralFunction as PyiGeneralFunction
"""
Enum


See Also:
    `API GeneralFunction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#ad184d5bd9055f3b4fd57ce72c781758d>`_
"""
typeName: str = 'com.sun.star.sheet.GeneralFunction'

AUTO: PyiGeneralFunction = ...
"""
specifies the use of a user-defined list.

function is determined automatically.
"""
AVERAGE: PyiGeneralFunction = ...
"""
average of all numerical values is calculated.
"""
COUNT: PyiGeneralFunction = ...
"""
all values, including non-numerical values, are counted.
"""
COUNTNUMS: PyiGeneralFunction = ...
"""
numerical values are counted.
"""
MAX: PyiGeneralFunction = ...
"""
maximum value of all numerical values is calculated.
"""
MIN: PyiGeneralFunction = ...
"""
minimum value of all numerical values is calculated.
"""
NONE: PyiGeneralFunction = ...
"""
no cells are moved.

sheet is not linked.

new values are used without changes.

nothing is calculated.

nothing is imported.

no condition is specified.
"""
PRODUCT: PyiGeneralFunction = ...
"""
product of all numerical values is calculated.
"""
STDEV: PyiGeneralFunction = ...
"""
standard deviation is calculated based on a sample.
"""
STDEVP: PyiGeneralFunction = ...
"""
standard deviation is calculated based on the entire population.
"""
SUM: PyiGeneralFunction = ...
"""
sum of all numerical values is calculated.
"""
VAR: PyiGeneralFunction = ...
"""
variance is calculated based on a sample.
"""
VARP: PyiGeneralFunction = ...
"""
variance is calculated based on the entire population.
"""


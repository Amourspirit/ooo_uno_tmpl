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
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.chart2.AxisOrientation import MATHEMATICAL as AXIS_ORIENTATION_MATHEMATICAL
    from com.sun.star.chart2.AxisOrientation import REVERSE as AXIS_ORIENTATION_REVERSE

    class AxisOrientation(uno.Enum):
        """
        Enum Class

        ENUM AxisOrientation

        See Also:
            `API AxisOrientation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html#aceb583a87538899d77ffbe62d2176a43>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.chart2.AxisOrientation', value)

        __ooo_ns__: str = 'com.sun.star.chart2'
        __ooo_full_ns__: str = 'com.sun.star.chart2.AxisOrientation'
        __ooo_type_name__: str = 'enum'

        MATHEMATICAL = cast("AxisOrientation", AXIS_ORIENTATION_MATHEMATICAL)
        """
        means equal to the primary writing direction
        """
        REVERSE = cast("AxisOrientation", AXIS_ORIENTATION_REVERSE)
        """
        means the opposite of the primary writing direction
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class AxisOrientation(metaclass=UnoEnumMeta, type_name="com.sun.star.chart2.AxisOrientation", name_space="com.sun.star.chart2"):
        """Dynamically created class that represents ``com.sun.star.chart2.AxisOrientation`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['AxisOrientation']

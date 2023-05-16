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
import uno
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoEnumMeta
    class LegendPosition(metaclass=UnoEnumMeta, type_name="com.sun.star.chart2.LegendPosition", name_space="com.sun.star.chart2"):
        """Dynamically created class that represents ``com.sun.star.chart2.LegendPosition`` Enum. Class loosly mimics Enum"""
        pass
else:
    from com.sun.star.chart2.LegendPosition import CUSTOM as LEGEND_POSITION_CUSTOM
    from com.sun.star.chart2.LegendPosition import LINE_END as LEGEND_POSITION_LINE_END
    from com.sun.star.chart2.LegendPosition import LINE_START as LEGEND_POSITION_LINE_START
    from com.sun.star.chart2.LegendPosition import PAGE_END as LEGEND_POSITION_PAGE_END
    from com.sun.star.chart2.LegendPosition import PAGE_START as LEGEND_POSITION_PAGE_START


    class LegendPosition(uno.Enum):
        """
        Enum Class

        ENUM LegendPosition

        See Also:
            `API LegendPosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html#a85df18f245c9e4d24e32ebb9ee879042>`_
        """
        __ooo_ns__: str = 'com.sun.star.chart2'
        __ooo_full_ns__: str = 'com.sun.star.chart2.LegendPosition'
        __ooo_type_name__: str = 'enum'

        @property
        def typeName(self) -> str:
            return 'com.sun.star.chart2.LegendPosition'

        CUSTOM = LEGEND_POSITION_CUSTOM
        """
        The position of the legend is given by an offset value.
        """
        LINE_END = LEGEND_POSITION_LINE_END
        """
        In LTR mode this is the right-hand side.
        """
        LINE_START = LEGEND_POSITION_LINE_START
        """
        In LTR mode this is the left-hand side.
        """
        PAGE_END = LEGEND_POSITION_PAGE_END
        """
        In LTR mode this is the bottom side.
        """
        PAGE_START = LEGEND_POSITION_PAGE_START
        """
        In LTR mode this is the top side.
        """

__all__ = ['LegendPosition']


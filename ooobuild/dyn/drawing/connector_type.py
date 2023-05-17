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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.drawing.ConnectorType import CURVE as CONNECTOR_TYPE_CURVE
    from com.sun.star.drawing.ConnectorType import LINE as CONNECTOR_TYPE_LINE
    from com.sun.star.drawing.ConnectorType import LINES as CONNECTOR_TYPE_LINES
    from com.sun.star.drawing.ConnectorType import STANDARD as CONNECTOR_TYPE_STANDARD

    class ConnectorType(uno.Enum):
        """
        Enum Class


        See Also:
            `API ConnectorType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a086c6f6507c67c8809b218d90998c5d6>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.drawing.ConnectorType', value)

        __ooo_ns__: str = 'com.sun.star.drawing'
        __ooo_full_ns__: str = 'com.sun.star.drawing.ConnectorType'
        __ooo_type_name__: str = 'enum'

        CURVE: ConnectorType = CONNECTOR_TYPE_CURVE
        """
        the ConnectorShape is drawn as a curve
        """
        LINE: ConnectorType = CONNECTOR_TYPE_LINE
        """
        the ConnectorShape is drawn as a straight line
        
        This is the PolygonKind for a LineShape.
        """
        LINES: ConnectorType = CONNECTOR_TYPE_LINES
        """
        the connector is drawn with three lines
        """
        STANDARD: ConnectorType = CONNECTOR_TYPE_STANDARD
        """
        the graphic is rendered in the default color style of the output device,
        
        use the length measurement.
        
        the connector is drawn with three lines, with the middle line perpendicular to the other two
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class ConnectorType(metaclass=UnoEnumMeta, type_name="com.sun.star.drawing.ConnectorType", name_space="com.sun.star.drawing"):
        """Dynamically created class that represents ``com.sun.star.drawing.ConnectorType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['ConnectorType']

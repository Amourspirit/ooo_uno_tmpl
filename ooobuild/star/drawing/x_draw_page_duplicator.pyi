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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_draw_page import XDrawPage as XDrawPage_b07a0b57


class XDrawPageDuplicator(XInterface_8f010a43):
    """
    makes it possible to duplicate pages within the same document.

    See Also:
        `API XDrawPageDuplicator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XDrawPageDuplicator.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.drawing.XDrawPageDuplicator'

    def duplicate(self, xPage: XDrawPage_b07a0b57) -> XDrawPage_b07a0b57:
        """
        creates a duplicate of a DrawPage or MasterPage, including the Shapes on that page and inserts it into the same model.
        """
        ...



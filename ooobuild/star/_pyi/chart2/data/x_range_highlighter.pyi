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
# Namespace: com.sun.star.chart2.data
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .highlighted_range import HighlightedRange as HighlightedRange_403d0f62
    from ...view.x_selection_change_listener import XSelectionChangeListener as XSelectionChangeListener_58bf104d

class XRangeHighlighter(XInterface_8f010a43):
    """

    See Also:
        `API XRangeHighlighter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1data_1_1XRangeHighlighter.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.chart2.data.XRangeHighlighter']

    def addSelectionChangeListener(self, xListener: 'XSelectionChangeListener_58bf104d') -> None:
        """
        registers an event listener, which is called when the selection is changed and affects different source ranges
        """
    def getSelectedRanges(self) -> 'typing.Tuple[HighlightedRange_403d0f62, ...]':
        """
        Returns a list of ranges that are used by objects that are currently selected.
        """
    def removeSelectionChangeListener(self, xListener: 'XSelectionChangeListener_58bf104d') -> None:
        """
        unregisters an event listener which was registered with XRangeHighlighter.addSelectionChangeListener() before.
        """


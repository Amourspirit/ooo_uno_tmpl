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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_sheet_filter_descriptor import XSheetFilterDescriptor as XSheetFilterDescriptor_47cc0ff7

class XSheetFilterable(XInterface_8f010a43):
    """
    represents something that can be filtered using an XSheetFilterDescriptor.

    See Also:
        `API XSheetFilterable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetFilterable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSheetFilterable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetFilterable'

    @abstractmethod
    def createFilterDescriptor(self, bEmpty: bool) -> XSheetFilterDescriptor_47cc0ff7:
        """
        creates a filter descriptor.
        """
        ...
    @abstractmethod
    def filter(self, xDescriptor: XSheetFilterDescriptor_47cc0ff7) -> None:
        """
        performs a filter operation, using the settings of the passed filter descriptor.
        """
        ...

__all__ = ['XSheetFilterable']


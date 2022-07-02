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
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_consolidation_descriptor import XConsolidationDescriptor as XConsolidationDescriptor_6b7610ee

class XConsolidatable(XInterface_8f010a43):
    """
    provides methods to consolidate ranges in a spreadsheet document.
    
    Consolidation combines the cells of multiple cell ranges, using a specific function.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XConsolidatable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XConsolidatable.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XConsolidatable']

    def consolidate(self, xDescriptor: 'XConsolidationDescriptor_6b7610ee') -> None:
        """
        consolidates data from several cell ranges, using the settings in the passed descriptor.
        """
        ...
    def createConsolidationDescriptor(self, bEmpty: bool) -> 'XConsolidationDescriptor_6b7610ee':
        """
        creates a consolidation descriptor.
        """
        ...



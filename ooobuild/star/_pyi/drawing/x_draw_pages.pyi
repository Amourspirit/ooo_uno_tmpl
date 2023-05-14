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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.drawing
from typing_extensions import Literal
import typing
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from .x_draw_page import XDrawPage as XDrawPage_b07a0b57

class XDrawPages(XIndexAccess_f0910d6d):
    """
    gives access to a container of DrawPages or MasterPages.
    
    The pages are stored in an index container. The order is determined by the index.
    
    You usually get this interface if you use the XDrawPagesSupplier or the XMasterPagesSupplier at a model that contains DrawPages or MasterPages

    See Also:
        `API XDrawPages <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XDrawPages.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.XDrawPages']

    def insertNewByIndex(self, nIndex: int) -> 'XDrawPage_b07a0b57':
        """
        creates and inserts a new DrawPage or MasterPage into this container
        """
        ...
    def remove(self, xPage: 'XDrawPage_b07a0b57') -> None:
        """
        removes a DrawPage or MasterPage from this container.
        """
        ...



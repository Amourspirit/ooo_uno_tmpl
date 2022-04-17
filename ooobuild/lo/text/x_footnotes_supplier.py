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
# Namespace: com.sun.star.text
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d

class XFootnotesSupplier(XInterface_8f010a43):
    """
    makes it possible to access the footnotes within the context (e.g.
    
    document).

    See Also:
        `API XFootnotesSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XFootnotesSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XFootnotesSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XFootnotesSupplier'

    @abstractmethod
    def getFootnoteSettings(self) -> 'XPropertySet_bc180bfa':
        """
        """
    @abstractmethod
    def getFootnotes(self) -> 'XIndexAccess_f0910d6d':
        """
        returns a collection of footnotes.
        """

__all__ = ['XFootnotesSupplier']

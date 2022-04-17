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
# Namespace: com.sun.star.presentation
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47

class XCustomPresentationSupplier(XInterface_8f010a43):
    """
    must be supported to provide access to customized presentations of a presentation document.

    See Also:
        `API XCustomPresentationSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1presentation_1_1XCustomPresentationSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.XCustomPresentationSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.presentation.XCustomPresentationSupplier'

    @abstractmethod
    def getCustomPresentations(self) -> 'XNameContainer_cb90e47':
        """
        """

__all__ = ['XCustomPresentationSupplier']


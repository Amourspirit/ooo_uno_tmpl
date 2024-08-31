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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.xforms
from __future__ import annotations
import typing
from abc import abstractproperty
from ..form.binding.list_entry_source import ListEntrySource as ListEntrySource_48260fe4
from ..form.binding.value_binding import ValueBinding as ValueBinding_18de0e7d
from ..form.validation.x_validator import XValidator as XValidator_2a5c0f13
if typing.TYPE_CHECKING:
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47

class Binding(ListEntrySource_48260fe4, ValueBinding_18de0e7d, XValidator_2a5c0f13):
    """
    Service Class

    represent a binding to one or more nodes in the DOM tree of an XModel.

    See Also:
        `API Binding <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xforms_1_1Binding.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xforms'
    __ooo_full_ns__: str = 'com.sun.star.xforms.Binding'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def BindingNamespaces(self) -> XNameContainer_cb90e47:
        """
        among other properties, there is this one
        
        It is unclear to me whether this is an implementation detail or a supported interface.
        
        The value supports the service com.sun.star.xml.NamespaceContainer
        """
        ...


__all__ = ['Binding']


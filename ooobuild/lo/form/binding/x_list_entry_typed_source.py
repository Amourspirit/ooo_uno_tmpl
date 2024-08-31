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
# Namespace: com.sun.star.form.binding
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_list_entry_source import XListEntrySource as XListEntrySource_576b103c

class XListEntryTypedSource(XListEntrySource_576b103c):
    """
    specifies a source of string list entries with corresponding underlying data values
    
    **since**
    
        LibreOffice 5.4

    See Also:
        `API XListEntryTypedSource <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1binding_1_1XListEntryTypedSource.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.binding'
    __ooo_full_ns__: str = 'com.sun.star.form.binding.XListEntryTypedSource'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.binding.XListEntryTypedSource'

    @abstractmethod
    def getAllListEntriesTyped(self, DataValues: typing.Tuple[object, ...]) -> typing.Tuple[str, ...]:
        """
        provides access to the entirety of all list entries, along with the corresponding underlying data values.

        * ``DataValues`` is an out direction argument.
        """
        ...

__all__ = ['XListEntryTypedSource']


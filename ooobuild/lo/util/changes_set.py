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
# TypeDef
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.util
import typing
from .element_change import ElementChange

ChangesSet = typing.NewType('ChangesSet', typing.Tuple[ElementChange, ...])
"""
TypeDef type alias

describes a set of changes occurring as a batch transaction.

See Also:
    `API ChangesSet <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1util.html#af3741b059f727ead3518cbb4b259038e>`_
"""


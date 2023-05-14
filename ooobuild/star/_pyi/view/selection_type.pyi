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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.view
# Libre Office Version: 7.4
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class SelectionType(Enum):
    """
    Enum

    

    See Also:
        `API SelectionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1view.html#acffca3b33fddce63d3220bc7487e879d>`_
    """
    typeName: str = 'com.sun.star.view.SelectionType'

    MULTI: 'uno.Enum'
    """
    The selection can contain zero or more objects.
    """
    NONE: 'uno.Enum'
    """
    No selection is possible.
    
    The selection is always empty.
    """
    RANGE: 'uno.Enum'
    """
    The selection can contain zero or more objects.
    
    all selected objects must be part of a continues range
    """
    SINGLE: 'uno.Enum'
    """
    The selection can only contain one or zero objects.
    """


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
# Namespace: com.sun.star.util
from typing_extensions import Literal
import typing
from .x_searchable import XSearchable as XSearchable_a4e80b08
if typing.TYPE_CHECKING:
    from .x_replace_descriptor import XReplaceDescriptor as XReplaceDescriptor_fd510df9
    from .x_search_descriptor import XSearchDescriptor as XSearchDescriptor_ef600d93

class XReplaceable(XSearchable_a4e80b08):
    """
    makes it possible to replace strings in a text described by a SearchDescriptor.
    
    Example: replace all bold words \"search for\" by \"look for\"

    See Also:
        `API XReplaceable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XReplaceable.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.util.XReplaceable']

    def createReplaceDescriptor(self) -> 'XReplaceDescriptor_fd510df9':
        """
        creates a descriptor which contains properties that specify a search in this container.
        """
    def replaceAll(self, xDesc: 'XSearchDescriptor_ef600d93') -> int:
        """
        searches for all occurrences of whatever is specified.
        """


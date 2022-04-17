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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.style
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .horizontal_alignment import HorizontalAlignment as HorizontalAlignment_1f800f02

class NumberingAlignment(ABC):
    """
    Service Class

    specify the alignment of a numbering level.

    See Also:
        `API NumberingAlignment <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1NumberingAlignment.html>`_
    """
    @property
    def Alignment(self) -> 'HorizontalAlignment_1f800f02':
        """
        set the alignment from the numbering.
        
        Use the com.sun.star.style.HorizontalAlignment enum to change the alignment.
        """
    @property
    def Insertion(self) -> int:
        """
        the distance between the numbering symbol and text.
        """
    @property
    def TextMarginDistance(self) -> int:
        """
        the minimum distance between the numbering symbol and the following text.
        """
    @property
    def TextNumberingDistance(self) -> int:
        """
        the distance between left margin and the numbering symbol.
        """



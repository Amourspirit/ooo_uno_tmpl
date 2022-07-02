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
# Namespace: com.sun.star.text
import typing
from abc import abstractproperty
from .text_portion import TextPortion as TextPortion_a6f80b5d
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from .x_text import XText as XText_690408ca
    from ..util.date_time import DateTime as DateTime_84de09d3

class RedlinePortion(TextPortion_a6f80b5d):
    """
    Service Class

    A RedlinePortion is a TextPortion that marks a change that has been recorded by the change tracking.

    See Also:
        `API RedlinePortion <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1RedlinePortion.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.RedlinePortion'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def IsInHeaderFooter(self) -> bool:
        """
        determines whether the portion is member of a header or footer text.
        """
        ...

    @abstractproperty
    def MergeLastPara(self) -> bool:
        """
        determines whether the last paragraph of a redline text has to be merged with a possible following text content (i.e.
        
        a text table)
        """
        ...

    @abstractproperty
    def RedlineAuthor(self) -> str:
        """
        contains the name of the author of the change.
        """
        ...

    @abstractproperty
    def RedlineComment(self) -> str:
        """
        contains a comment for the change.
        """
        ...

    @abstractproperty
    def RedlineDateTime(self) -> 'DateTime_84de09d3':
        """
        contains the date and time of the change.
        """
        ...

    @abstractproperty
    def RedlineIdentifier(self) -> str:
        """
        contains a unique identifier for the redline.
        
        This is necessary for file export filters to able to recognize redline portions that point to the same redline.
        """
        ...

    @abstractproperty
    def RedlineSuccessorData(self) -> 'PropertyValues_d6470ce6':
        """
        contains the data of a second level redline data
        
        The elements of the sequence are:
        """
        ...

    @abstractproperty
    def RedlineText(self) -> 'XText_690408ca':
        """
        provides access to the text of the redline.
        
        This interface is only provided if the change is not visible. The visibility depends on the redline display options that are set at the documents property set (RedlineDisplayType).
        """
        ...

    @abstractproperty
    def RedlineType(self) -> str:
        """
        contains the type of the change
        
        Valid type names are:
        """
        ...



__all__ = ['RedlinePortion']


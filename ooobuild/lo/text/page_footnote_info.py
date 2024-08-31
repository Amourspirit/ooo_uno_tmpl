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
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from com.sun.star.text.HorizontalAdjust import HorizontalAdjustProto  # type: ignore

class PageFootnoteInfo(ABC):
    """
    Service Class

    specifies the properties of the footnote area of a page or a page style.

    See Also:
        `API PageFootnoteInfo <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1PageFootnoteInfo.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.PageFootnoteInfo'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def FootnoteBottomDistance(self) -> int:
        """
        contains the distance between the separator line and the footnote section.
        """
        ...

    @property
    @abstractmethod
    def FootnoteHeight(self) -> int:
        """
        contains the maximum height of the footnote section.
        
        If 0, the maximum is the height of the page.
        """
        ...

    @property
    @abstractmethod
    def FootnoteSeparatorLineAdjust(self) -> HorizontalAdjustProto:
        """
        contains the adjustment of the footnote separator line.
        """
        ...

    @property
    @abstractmethod
    def FootnoteSeparatorLinePenWidth(self) -> int:
        """
        contains the width of the pen for the footnote separator line.
        """
        ...

    @property
    @abstractmethod
    def FootnoteSeparatorLineWidth(self) -> int:
        """
        contains the relative width of the footnote separator line.
        """
        ...

    @property
    @abstractmethod
    def FootnoteSeparatorLineWidthPercent(self) -> int:
        """
        contains the relative width of the footnote separator line.
        """
        ...

    @property
    @abstractmethod
    def FootnoteTopDistance(self) -> int:
        """
        contains the distance between the text and footnote section.
        """
        ...


__all__ = ['PageFootnoteInfo']
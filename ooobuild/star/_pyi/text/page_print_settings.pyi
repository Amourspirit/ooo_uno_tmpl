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
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from abc import ABC

class PagePrintSettings(ABC):
    """
    Service Class

    These properties describe the way the XPagePrintable interface prints the page on one printer page.

    See Also:
        `API PagePrintSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1PagePrintSettings.html>`_
    """
    @property
    def BottomMargin(self) -> int:
        """
        contains the right margin of the printer page.
        """
    @property
    def HoriMargin(self) -> int:
        """
        contains the margin between the rows of printed pages.
        """
    @property
    def IsLandscape(self) -> bool:
        """
        defines if the printer page is used in landscape format.
        """
    @property
    def LeftMargin(self) -> int:
        """
        contains the left margin of the printer page.
        """
    @property
    def PageColumns(self) -> int:
        """
        contains the number of pages per printed row of pages.
        """
    @property
    def PageRows(self) -> int:
        """
        contains the number of pages per printed column of pages.
        """
    @property
    def RightMargin(self) -> int:
        """
        contains the right margin of the printer page.
        """
    @property
    def TopMargin(self) -> int:
        """
        contains the top margin of the printer page.
        """
    @property
    def VertMargin(self) -> int:
        """
        contains the margin between the columns of printed pages.
        """



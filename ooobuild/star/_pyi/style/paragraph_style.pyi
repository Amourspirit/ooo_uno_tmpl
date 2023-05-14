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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.style
from .paragraph_properties import ParagraphProperties as ParagraphProperties_1e240efc
from .style import Style as Style_7336094a
from ..xml.para_user_defined_attributes_supplier import ParaUserDefinedAttributesSupplier as ParaUserDefinedAttributesSupplier_e8be13a6

class ParagraphStyle(ParagraphProperties_1e240efc, Style_7336094a, ParaUserDefinedAttributesSupplier_e8be13a6):
    """
    Service Class

    specifies a style sheet for paragraphs within a com.sun.star.text.Text.

    See Also:
        `API ParagraphStyle <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1style_1_1ParagraphStyle.html>`_
    """
    @property
    def Category(self) -> int:
        """
        determines the category of a paragraph style.
        """
        ...
    @Category.setter
    def Category(self, value: int) -> None:
        ...
    @property
    def CharDiffHeight(self) -> float:
        """
        """
        ...
    @CharDiffHeight.setter
    def CharDiffHeight(self, value: float) -> None:
        ...
    @property
    def CharDiffHeightAsian(self) -> float:
        """
        This value contains the character height as difference in point to the height of the character in the parent style in Asian text.
        """
        ...
    @CharDiffHeightAsian.setter
    def CharDiffHeightAsian(self, value: float) -> None:
        ...
    @property
    def CharDiffHeightComplex(self) -> float:
        """
        This value contains the character height as difference in point to the height of the character in the parent style in complex text.
        """
        ...
    @CharDiffHeightComplex.setter
    def CharDiffHeightComplex(self, value: float) -> None:
        ...
    @property
    def CharPropHeight(self) -> int:
        """
        This value contains the character height as percentage value relative to the height of the character in the parent style.
        """
        ...
    @CharPropHeight.setter
    def CharPropHeight(self, value: int) -> None:
        ...
    @property
    def CharPropHeightAsian(self) -> int:
        """
        This value contains the character height as percentage value relative to the height of the character in the parent style in Asian text.
        """
        ...
    @CharPropHeightAsian.setter
    def CharPropHeightAsian(self, value: int) -> None:
        ...
    @property
    def CharPropHeightComplex(self) -> int:
        """
        This value contains the character height as percentage value relative to the height of the character in the parent style in complex text.
        """
        ...
    @CharPropHeightComplex.setter
    def CharPropHeightComplex(self, value: int) -> None:
        ...
    @property
    def PageStyleName(self) -> str:
        """
        returns the name of the page style in use
        
        For setting the page style you have to use the com.sun.star.text.PageDescName properties.
        """
        ...
    @PageStyleName.setter
    def PageStyleName(self, value: str) -> None:
        ...
    @property
    def ParaBottomMarginRelative(self) -> int:
        """
        determines the Bottom margin of the paragraph relative to the ParaBottomMargin of the parent style.
        
        If the value of ParaBottomMarginRelative is 100 the current ParaBottomMargin value is used.
        """
        ...
    @ParaBottomMarginRelative.setter
    def ParaBottomMarginRelative(self, value: int) -> None:
        ...
    @property
    def ParaLeftMarginRelative(self) -> int:
        """
        determines the left margin of the paragraph relative to the ParaLeftMargin of the parent style.
        
        If the value of ParaLeftMarginRelative is 100 the current ParaLeftMargin value is used.
        """
        ...
    @ParaLeftMarginRelative.setter
    def ParaLeftMarginRelative(self, value: int) -> None:
        ...
    @property
    def ParaRightMarginRelative(self) -> int:
        """
        determines the right margin of the paragraph relative to the ParaRightMargin of the parent style.
        
        If the value of ParaRightMarginRelative is 100 the current ParaRightMargin value is used.
        """
        ...
    @ParaRightMarginRelative.setter
    def ParaRightMarginRelative(self, value: int) -> None:
        ...
    @property
    def ParaTopMarginRelative(self) -> int:
        """
        determines the top margin of the paragraph relative to the ParaTopMargin of the parent style.
        
        If the value of ParaTopMarginRelative is 100 the current ParaTopMargin value is used.
        """
        ...
    @ParaTopMarginRelative.setter
    def ParaTopMarginRelative(self, value: int) -> None:
        ...


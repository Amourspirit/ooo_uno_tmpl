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
# Namespace: com.sun.star.text
from __future__ import annotations
import typing
from .x_text_content import XTextContent as XTextContent_b16e0ba5
if typing.TYPE_CHECKING:
    from com.sun.star.text.TextContentAnchorType import TextContentAnchorTypeProto  # type: ignore
    from com.sun.star.text.WrapTextMode import WrapTextModeProto  # type: ignore

class TextContent(XTextContent_b16e0ba5):
    """
    Service Class

    is an object which can be anchored in a text, like instances of TextFrame or TextField.
    
    If the concrete TextContent has a textual representation which fades into the surrounding text, then XTextField is used.
    
    If the concrete TextContent has a \"floating\" object, like a graphic, com.sun.star.drawing.XShape is used.

    See Also:
        `API TextContent <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextContent.html>`_
    """
    @property
    def AnchorTypes(self) -> typing.Tuple[TextContentAnchorTypeProto, ...]:
        """
        contains the anchor type of the text content.
        """
        ...
    @AnchorTypes.setter
    def AnchorTypes(self, value: typing.Tuple[TextContentAnchorTypeProto, ...]) -> None:
        ...
    @property
    def AnchorType(self) -> TextContentAnchorTypeProto:
        """
        specifies how the text content is attached to its surrounding Text.
        """
        ...
    @AnchorType.setter
    def AnchorType(self, value: TextContentAnchorTypeProto) -> None:
        ...
    @property
    def TextWrap(self) -> WrapTextModeProto:
        """
        specifies if the text content is a shape and how the text is wrapped around the shape.
        """
        ...
    @TextWrap.setter
    def TextWrap(self, value: WrapTextModeProto) -> None:
        ...
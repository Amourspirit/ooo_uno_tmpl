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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class LineBreakUserOptions(object):
    """
    Struct Class

    Line break options passed in calls to XBreakIterator.getLineBreak().

    See Also:
        `API LineBreakUserOptions <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1LineBreakUserOptions.html>`_
    """
    typeName: Literal['com.sun.star.i18n.LineBreakUserOptions']

    def __init__(self, forbiddenBeginCharacters: typing.Optional[str] = ..., forbiddenEndCharacters: typing.Optional[str] = ..., applyForbiddenRules: typing.Optional[bool] = ..., allowPunctuationOutsideMargin: typing.Optional[bool] = ..., allowHyphenateEnglish: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            forbiddenBeginCharacters (str, optional): forbiddenBeginCharacters value.
            forbiddenEndCharacters (str, optional): forbiddenEndCharacters value.
            applyForbiddenRules (bool, optional): applyForbiddenRules value.
            allowPunctuationOutsideMargin (bool, optional): allowPunctuationOutsideMargin value.
            allowHyphenateEnglish (bool, optional): allowHyphenateEnglish value.
        """
        ...


    @property
    def forbiddenBeginCharacters(self) -> str:
        """
        Characters not allowed at the beginning of a line.
        """
        ...


    @property
    def forbiddenEndCharacters(self) -> str:
        """
        Characters not allowed at the end of a line.
        """
        ...


    @property
    def applyForbiddenRules(self) -> bool:
        """
        If the forbidden characters rules are to be applied or not.
        """
        ...


    @property
    def allowPunctuationOutsideMargin(self) -> bool:
        """
        If punctuation characters are allowed at the end of the line if outside of the margins, resulting in a line not being wrapped if only the punctuation would wrap.
        """
        ...


    @property
    def allowHyphenateEnglish(self) -> bool:
        """
        Allow English hyphenation.
        """
        ...



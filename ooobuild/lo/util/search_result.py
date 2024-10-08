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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.util
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
import typing


class SearchResult(object):
    """
    Struct Class


    See Also:
        `API SearchResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1SearchResult.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.SearchResult'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.util.SearchResult'
    """Literal Constant ``com.sun.star.util.SearchResult``"""

    def __init__(self, subRegExpressions: typing.Optional[int] = 0, startOffset: typing.Optional[typing.Tuple[int, ...]] = (), endOffset: typing.Optional[typing.Tuple[int, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            subRegExpressions (int, optional): subRegExpressions value.
            startOffset (typing.Tuple[int, ...], optional): startOffset value.
            endOffset (typing.Tuple[int, ...], optional): endOffset value.
        """
        super().__init__()

        if isinstance(subRegExpressions, SearchResult):
            oth: SearchResult = subRegExpressions
            self.subRegExpressions = oth.subRegExpressions
            self.startOffset = oth.startOffset
            self.endOffset = oth.endOffset
            return

        kargs = {
            "subRegExpressions": subRegExpressions,
            "startOffset": startOffset,
            "endOffset": endOffset,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._sub_reg_expressions = kwargs["subRegExpressions"]
        self._start_offset = kwargs["startOffset"]
        self._end_offset = kwargs["endOffset"]


    @property
    def subRegExpressions(self) -> int:
        """
        Number of subexpressions.
        
        If it is 0, then no match found; this value is 1 for ABSOLUTE and APPROXIMATE match. The start and endOffset are always dependent on the search direction.
        
        For example, if you search \"X\" in the text \"-X-\" the offsets are:
        
        Forward, the startOffset is inclusive, the endOffset exclusive. Backward, the startOffset is exclusive, the endOffset inclusive.
        
        For regular expressions it can be greater than 1. If the value is 1, startoffset[0] and endoffset[0] points to the matching sub string if value is > 1, still startoffset[0] and endoffset[0] points to the matching substring for whole regular expression startoffset[i] and endoffset[i] points to the matching substring of i th matching substring.
        """
        return self._sub_reg_expressions

    @subRegExpressions.setter
    def subRegExpressions(self, value: int) -> None:
        self._sub_reg_expressions = value

    @property
    def startOffset(self) -> typing.Tuple[int, ...]:
        return self._start_offset

    @startOffset.setter
    def startOffset(self, value: typing.Tuple[int, ...]) -> None:
        self._start_offset = value

    @property
    def endOffset(self) -> typing.Tuple[int, ...]:
        return self._end_offset

    @endOffset.setter
    def endOffset(self, value: typing.Tuple[int, ...]) -> None:
        self._end_offset = value


__all__ = ['SearchResult']

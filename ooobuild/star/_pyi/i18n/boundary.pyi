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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class Boundary(object):
    """
    Struct Class

    contains start and end position of a word.
    
    It is used in word break iterator and text conversion.

    See Also:
        `API Boundary <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1Boundary.html>`_
    """
    typeName: Literal['com.sun.star.i18n.Boundary']

    def __init__(self, startPos: typing.Optional[int] = ..., endPos: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            startPos (int, optional): startPos value.
            endPos (int, optional): endPos value.
        """


    @property
    def startPos(self) -> int:
        """
        Start position of a word, inclusive
        """


    @property
    def endPos(self) -> int:
        """
        End position of a word, exclusive
        """



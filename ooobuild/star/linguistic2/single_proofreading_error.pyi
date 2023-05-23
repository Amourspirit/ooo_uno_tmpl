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
# Namespace: com.sun.star.linguistic2
# Libre Office Version: 7.4
import typing
from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class SingleProofreadingError(object):
    """
    Struct Class

    holds a single error found by the proofreader.
    
    **since**
    
        OOo 3.0.1

    See Also:
        `API SingleProofreadingError <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1linguistic2_1_1SingleProofreadingError.html>`_
    """
    typeName: str = 'com.sun.star.linguistic2.SingleProofreadingError'

    def __init__(self, aSuggestions: typing.Optional[typing.Tuple[str, ...]] = ..., aProperties: typing.Optional[typing.Tuple[PropertyValue_c9610c73, ...]] = ..., nErrorStart: typing.Optional[int] = ..., nErrorLength: typing.Optional[int] = ..., nErrorType: typing.Optional[int] = ..., aRuleIdentifier: typing.Optional[str] = ..., aShortComment: typing.Optional[str] = ..., aFullComment: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            aSuggestions (typing.Tuple[str, ...], optional): aSuggestions value.
            aProperties (typing.Tuple[PropertyValue, ...], optional): aProperties value.
            nErrorStart (int, optional): nErrorStart value.
            nErrorLength (int, optional): nErrorLength value.
            nErrorType (int, optional): nErrorType value.
            aRuleIdentifier (str, optional): aRuleIdentifier value.
            aShortComment (str, optional): aShortComment value.
            aFullComment (str, optional): aFullComment value.
        """
        ...

    @property
    def aSuggestions(self) -> typing.Tuple[str, ...]:
        ...
    @aSuggestions.setter
    def aSuggestions(self, value: typing.Tuple[str, ...]) -> None:
        ...
    @property
    def aProperties(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        ...
    @aProperties.setter
    def aProperties(self, value: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        ...
    @property
    def nErrorStart(self) -> int:
        ...
    @nErrorStart.setter
    def nErrorStart(self, value: int) -> None:
        ...
    @property
    def nErrorLength(self) -> int:
        ...
    @nErrorLength.setter
    def nErrorLength(self, value: int) -> None:
        ...
    @property
    def nErrorType(self) -> int:
        ...
    @nErrorType.setter
    def nErrorType(self, value: int) -> None:
        ...
    @property
    def aRuleIdentifier(self) -> str:
        ...
    @aRuleIdentifier.setter
    def aRuleIdentifier(self, value: str) -> None:
        ...
    @property
    def aShortComment(self) -> str:
        ...
    @aShortComment.setter
    def aShortComment(self, value: str) -> None:
        ...
    @property
    def aFullComment(self) -> str:
        ...
    @aFullComment.setter
    def aFullComment(self, value: str) -> None:
        ...

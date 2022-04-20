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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class RuleTerm(object):
    """
    Struct Class

    describes a term.
    
    A term is used to select objects to which a rule should apply.

    See Also:
        `API RuleTerm <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1RuleTerm.html>`_
    """
    typeName: Literal['com.sun.star.ucb.RuleTerm']

    def __init__(self, Property: typing.Optional[str] = ..., Operand: typing.Optional[object] = ..., Operator: typing.Optional[int] = ..., CaseSensitive: typing.Optional[bool] = ..., RegularExpression: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Property (str, optional): Property value.
            Operand (object, optional): Operand value.
            Operator (int, optional): Operator value.
            CaseSensitive (bool, optional): CaseSensitive value.
            RegularExpression (bool, optional): RegularExpression value.
        """


    @property
    def Property(self) -> str:
        """
        the name of the property used to match the term.
        """


    @property
    def Operand(self) -> object:
        """
        the value of the property used to compare with the document property.
        """


    @property
    def Operator(self) -> int:
        """
        the operator used to compare the property of the document with the given value (e.g.
        
        \"contains\" or \"greater equal\").
        
        The value can be one of the RuleOperator constants.
        """


    @property
    def CaseSensitive(self) -> bool:
        """
        this flag indicates whether a string \"operand\" shall be compared case sensitive.
        """


    @property
    def RegularExpression(self) -> bool:
        """
        this flag indicates whether a string \"operand\" shall be treated as a regular expression.
        """



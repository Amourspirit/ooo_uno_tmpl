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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.3
from typing_extensions import Literal
from enum import Enum


class ConditionOperator(Enum):
    """
    Enum Class

    

    See Also:
        `API ConditionOperator <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#adab1b2b49825a75bed998dd77963eff9>`_
    """
    BETWEEN: Literal['BETWEEN']
    """
    the value has to be between the two specified values.
    """
    EQUAL: Literal['EQUAL']
    """
    value has to be equal to the specified value.
    
    The cell value is equal to the specified value.
    """
    FORMULA: Literal['FORMULA']
    """
    the specified formula has to give a non-zero result.
    """
    GREATER: Literal['GREATER']
    """
    the value has to be greater than the specified value.
    
    value has to be greater than the specified value.
    """
    GREATER_EQUAL: Literal['GREATER_EQUAL']
    """
    the value has to be greater than or equal to the specified value.
    
    The cell value is greater or equal to the specified value.
    
    value has to be greater than or equal to the specified value.
    """
    LESS: Literal['LESS']
    """
    the value has to be less than the specified value.
    
    value has to be less than the specified value.
    """
    LESS_EQUAL: Literal['LESS_EQUAL']
    """
    the value has to be less than or equal to the specified value.
    
    The cell value is less or equal to the specified value.
    
    value has to be less than or equal to the specified value.
    """
    NONE: Literal['NONE']
    """
    no cells are moved.
    
    sheet is not linked.
    
    new values are used without changes.
    
    nothing is calculated.
    
    nothing is imported.
    
    no condition is specified.
    """
    NOT_BETWEEN: Literal['NOT_BETWEEN']
    """
    the value has to be outside of the two specified values.
    """
    NOT_EQUAL: Literal['NOT_EQUAL']
    """
    the value must not be equal to the specified value.
    
    value must not be equal to the specified value.
    """


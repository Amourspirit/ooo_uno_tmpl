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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sdb
from typing_extensions import Literal
"""
Const

specifies different mode how boolean comparison predicates are to be generated by a SingleSelectQueryComposer.

See Also:
    `API BooleanComparisonMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdb_1_1BooleanComparisonMode.html>`_
"""
EQUAL_INTEGER: Literal[0]
"""
denotes the default comparison

Most databases support comparing boolean expressions or column values directly with integer values: column = 0 respectively column = 1.
"""
IS_LITERAL: Literal[1]
"""
requires to use IS boolean_literal for boolean comparison.

That is, the generated comparison predicates will be column IS TRUE resp. column IS FALSE.
"""
EQUAL_LITERAL: Literal[2]
"""
requires to use = boolean_literal for boolean comparison.

That is, the generated comparison predicates will be column = TRUE resp. column = FALSE.
"""
ACCESS_COMPAT: Literal[3]
"""
requires to use an Microsoft Access compatible syntax for boolean comparison.
"""


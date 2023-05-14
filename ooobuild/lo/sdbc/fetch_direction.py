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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdbc


class FetchDirection(object):
    """
    Const Class

    indicates in which direction a result set should fetch next, just for optimization.

    See Also:
        `API FetchDirection <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1FetchDirection.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.FetchDirection'
    __ooo_type_name__: str = 'const'

    FORWARD = 1000
    """
    The rows in a result set will be processed in a forward direction; first-to-last.
    """
    REVERSE = 1001
    """
    The rows in a result set will be processed in a reverse direction; last-to-first.
    """
    UNKNOWN = 1002
    """
    The order in which rows in a result set will be processed is unknown:
    """

__all__ = ['FetchDirection']

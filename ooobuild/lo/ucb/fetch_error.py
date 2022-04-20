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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.ucb


class FetchError(object):
    """
    Const Class

    These values are used to specify whether and which error has occurred while fetching data of some ContentResultSet rows.

    See Also:
        `API FetchError <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb_1_1FetchError.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.FetchError'
    __ooo_type_name__: str = 'const'

    SUCCESS = 0
    """
    indicates that fetching of data was successful.
    """
    ENDOFDATA = 1
    """
    indicates that during fetching we went beyond the last or first row.
    
    Therefore the FetchResult does not contain the full count of demanded rows, but the maximum possible count must be contained.
    """
    EXCEPTION = 2
    """
    indicates that during fetching we got an exception.
    
    The row, that causes the exception, and all following ( \"following\" in read order! ) rows are not contained in the FetchResult. Therefore the FetchResult does not contain the full count of demanded rows. But all properly read rows so far must be contained.
    """

__all__ = ['FetchError']

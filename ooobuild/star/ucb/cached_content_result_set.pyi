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
# Namespace: com.sun.star.ucb
from __future__ import annotations
from .content_result_set import ContentResultSet as ContentResultSet_d4ee0cc8

class CachedContentResultSet(ContentResultSet_d4ee0cc8):
    """
    Service Class

    is used on client side to access a ContentResultSet remote optimized.
    
    The CachedContentResultSet will not load every single property or even row just in that moment you ask for it, but load the data for some rows beforehand.
    
    Every time when a new package of data is loaded, the so far loaded data will be released, so the cash will not grow and grow and grow.

    See Also:
        `API CachedContentResultSet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ucb_1_1CachedContentResultSet.html>`_
    """
    @property
    def FetchDirection(self) -> int:
        """
        contains the direction for fetching rows from an underlying database.
        
        The value can be one of the com.sun.star.sdbc.FetchDirection constants group.
        
        The default value is implementation specific.
        
        If you set the value to com.sun.star.sdbc.FetchDirection.UNKNOWN an implementation specific direction will be used.
        """
        ...
    @FetchDirection.setter
    def FetchDirection(self, value: int) -> None:
        ...
    @property
    def FetchSize(self) -> int:
        """
        contains the number of result set rows that should be fetched from an underlying database.
        
        The default fetch size is implementation specific.
        
        Every negative value for parameter FetchSize will force an implementation specific value to be set.
        """
        ...
    @FetchSize.setter
    def FetchSize(self, value: int) -> None:
        ...


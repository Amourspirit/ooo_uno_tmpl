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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.3
from enum import Enum


class LineCap(Enum):
    """
    Enum Class

    

    See Also:
        `API LineCap <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a6d67f779dcbc9e19f8bc6cdfbb6c23f8>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.LineCap'
    __ooo_type_name__: str = 'enum'

    BUTT = 'BUTT'
    """
    the line will end without any additional shape
    """
    ROUND = 'ROUND'
    """
    the dash is a point
    
    the lines join with an arc
    
    the line will get a half circle as additional cap
    """
    SQUARE = 'SQUARE'
    """
    the line will get a half square as additional cap
    
    the line uses a square for the line end.
    """

__all__ = ['LineCap']

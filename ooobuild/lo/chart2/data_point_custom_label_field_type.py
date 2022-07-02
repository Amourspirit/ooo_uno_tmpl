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
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.2
from enum import Enum


class DataPointCustomLabelFieldType(Enum):
    """
    Enum Class

    

    See Also:
        `API DataPointCustomLabelFieldType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html#a364615e20b0759c6c5100f6a47add923>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.DataPointCustomLabelFieldType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.chart2.DataPointCustomLabelFieldType'

    CATEGORYNAME = 'CATEGORYNAME'
    """
    """
    CELLRANGE = 'CELLRANGE'
    """
    """
    CELLREF = 'CELLREF'
    """
    """
    NEWLINE = 'NEWLINE'
    """
    """
    PERCENTAGE = 'PERCENTAGE'
    """
    """
    SERIESNAME = 'SERIESNAME'
    """
    """
    TEXT = 'TEXT'
    """
    """
    VALUE = 'VALUE'
    """
    """

__all__ = ['DataPointCustomLabelFieldType']


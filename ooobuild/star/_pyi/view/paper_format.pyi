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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.view
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class PaperFormat(Enum):
    """
    Enum

    

    See Also:
        `API PaperFormat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1view.html#a12ab04987d08416f8347a9790c7abf3e>`_
    """
    typeName: str = 'com.sun.star.view.PaperFormat'

    A3: 'uno.Enum'
    """
    specifies the paper format as A3.
    """
    A4: 'uno.Enum'
    """
    specifies the paper format as A4.
    """
    A5: 'uno.Enum'
    """
    specifies the paper format as A5.
    """
    B4: 'uno.Enum'
    """
    specifies the paper format as B4.
    """
    B5: 'uno.Enum'
    """
    specifies the paper format as B5.
    """
    LEGAL: 'uno.Enum'
    """
    specifies the paper format as Legal.
    """
    LETTER: 'uno.Enum'
    """
    specifies the paper format as Letter.
    """
    TABLOID: 'uno.Enum'
    """
    specifies the paper format as Tabloid.
    """
    USER: 'uno.Enum'
    """
    The real paper size is user defined in 100th mm.
    """


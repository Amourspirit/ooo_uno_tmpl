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
# Namespace: com.sun.star.mozilla
# Libre Office Version: 7.2
from enum import Enum


class MozillaProductType(Enum):
    """
    Enum Class

    

    See Also:
        `API MozillaProductType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1mozilla.html#a2bcdf854763e98ee224085041ac2ffa5>`_
    """
    __ooo_ns__: str = 'com.sun.star.mozilla'
    __ooo_full_ns__: str = 'com.sun.star.mozilla.MozillaProductType'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.mozilla.MozillaProductType'

    Default = 'Default'
    """
    Any product.
    """
    Firefox = 'Firefox'
    """
    Mozilla's next generation web browser.
    """
    Mozilla = 'Mozilla'
    """
    Mozilla browse and mail suite.
    """
    Thunderbird = 'Thunderbird'
    """
    Mozilla's next generation e-mail client.
    """

__all__ = ['MozillaProductType']


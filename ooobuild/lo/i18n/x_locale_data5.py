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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.i18n
import typing
from abc import abstractmethod
from .x_locale_data4 import XLocaleData4 as XLocaleData4_a7ae0a9e
if typing.TYPE_CHECKING:
    from .locale_data_item2 import LocaleDataItem2 as LocaleDataItem2_cad20bd3
    from ..lang.locale import Locale as Locale_70d308fa

class XLocaleData5(XLocaleData4_a7ae0a9e):
    """
    Access locale specific data.
    
    Derived from com.sun.star.i18n.XLocaleData4 this provides an additional method to return an instance of com.sun.star.i18n.LocaleDataItem2
    
    **since**
    
        LibreOffice 6.0

    See Also:
        `API XLocaleData5 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XLocaleData5.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XLocaleData5'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XLocaleData5'

    @abstractmethod
    def getLocaleItem2(self, Locale: 'Locale_70d308fa') -> 'LocaleDataItem2_cad20bd3':
        """
        returns an instance of com.sun.star.i18n.LocaleDataItem2 for a Locale.
        """

__all__ = ['XLocaleData5']


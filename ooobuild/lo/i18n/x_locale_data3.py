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
from .x_locale_data2 import XLocaleData2 as XLocaleData2_a7ac0a9c
if typing.TYPE_CHECKING:
    from .calendar2 import Calendar2 as Calendar2_88c10994
    from ..lang.locale import Locale as Locale_70d308fa

class XLocaleData3(XLocaleData2_a7ac0a9c):
    """
    Access locale specific data.
    
    Derived from com.sun.star.i18n.XLocaleData2 this provides an additional method to return a sequence of all com.sun.star.i18n.Calendar2 elements available for that locale.
    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API XLocaleData3 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XLocaleData3.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.XLocaleData3'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.i18n.XLocaleData3'

    @abstractmethod
    def getAllCalendars2(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[Calendar2_88c10994, ...]':
        """
        returns all LC_CALENDAR calendars for a locale.
        """

__all__ = ['XLocaleData3']


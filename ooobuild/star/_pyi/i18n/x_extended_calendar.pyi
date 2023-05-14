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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.i18n
from typing_extensions import Literal
from .x_calendar import XCalendar as XCalendar_888d09ba

class XExtendedCalendar(XCalendar_888d09ba):
    """
    This interface provides access to locale specific calendar systems.
    
    It is derived from com.sun.star.i18n.XCalendar and provides additional functionality to display parts of the date currently set at the calendar.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XExtendedCalendar <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XExtendedCalendar.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.i18n.XExtendedCalendar']

    def getDisplayString(self, nCalendarDisplayCode: int, nNativeNumberMode: int) -> str:
        """
        Returns a string (number or name to display) matching the given code constant.
        
        Note that the string returned depends completely on the locale's calendar. It is not predictable if the string will be numeric or a name, or if in case it returns a numeric string how many digits that will have. For example, a short year display string will normally be two digits with a Gregorian calendar, but with a Jewish calendar it will have three digits.
        """
        ...



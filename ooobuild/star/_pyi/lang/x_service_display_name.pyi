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
# Namespace: com.sun.star.lang
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .locale import Locale as Locale_70d308fa

class XServiceDisplayName(XInterface_8f010a43):
    """
    provides a name for the service to be used in displays.
    
    This name can be used in displays (dialogs, menus, etc.) to provide a more memorable / meaningful name than the service name or its implementation name. It should not be used to identify / select a specific service / implementation.

    See Also:
        `API XServiceDisplayName <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XServiceDisplayName.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.lang.XServiceDisplayName']

    def getServiceDisplayName(self, aLocale: 'Locale_70d308fa') -> str:
        """
        returns the display name of the service for a given language.
        
        The caller may specify a com.sun.star.lang.Locale for the preferred language of the resulting string. However, if that locale is not supported the resulting string may be given in a different language. Usually this should be English.
        """
        ...



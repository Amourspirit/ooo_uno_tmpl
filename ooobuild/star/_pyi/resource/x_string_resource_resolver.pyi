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
# Namespace: com.sun.star.resource
from typing_extensions import Literal
import typing
from ..util.x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XStringResourceResolver(XModifyBroadcaster_fd990df0):
    """
    Interface to access strings in a resource.
    
    The interface is derived from com.sun.star.util.XModifyBroadcaster
    
    All registered com.sun.star.util.XModifyListener interfaces will be notified if either the current locale changes or if a string is added, changed or removed. This usually will only happen if the implementing object also supports the interface com.sun.star.resource.XStringResourceManager and is used in the design mode of a Dialog or String table editor. But also changing the locale at runtime can be supported in this way.

    See Also:
        `API XStringResourceResolver <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1resource_1_1XStringResourceResolver.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.resource.XStringResourceResolver']

    def getCurrentLocale(self) -> 'Locale_70d308fa':
        """
        Returns the current locale specified in the accessed resource.
        
        If no locale is available, the returned Locale structure only contains empty strings.
        """
    def getDefaultLocale(self) -> 'Locale_70d308fa':
        """
        Returns the default locale of the accessed resource.
        
        In many cases this will be the locale of the Office initially used to create the resource.
        """
    def getLocales(self) -> 'typing.Tuple[Locale_70d308fa, ...]':
        """
        Returns a sequence of all supported locales.
        """
    def getResourceIDs(self) -> 'typing.Tuple[str, ...]':
        """
        Returns a sequence of all valid Resource IDs for the current locale.
        """
    def getResourceIDsForLocale(self, locale: 'Locale_70d308fa') -> 'typing.Tuple[str, ...]':
        """
        Returns a sequence of all valid Resource IDs for a specific locale.
        
        It's not recommended to use this method to get the best performance as the implementation may be optimized for the use of the current locale.
        """
    def hasEntryForId(self, ResourceID: str) -> bool:
        """
        Checks if the resource contains an entry for the given ResourceID and current locale.
        """
    def hasEntryForIdAndLocale(self, ResourceID: str, locale: 'Locale_70d308fa') -> bool:
        """
        Checks if the resource contains an entry for the given ResourceID and locale.
        
        It's not recommended to use this method to get the best performance as the implementation may be optimized for the use of the current locale.
        """
    def resolveString(self, ResourceID: str) -> str:
        """
        Resolves the passed ResourceID for the current locale.
        
        This locale is set during initialization of the object implementing this interface or - in case that also the interface com.sun.star.resource.XStringResourceManager is supported - by using the XStringResourceManager.setLocale method.

        Raises:
            com.sun.star.resource.MissingResourceException: ``MissingResourceException``
        """
    def resolveStringForLocale(self, ResourceID: str, locale: 'Locale_70d308fa') -> str:
        """
        Resolves the passed ResourceID for a specific locale.
        
        It's not recommended to use this method to get the best performance as the implementation may be optimized for the use of the current locale.

        Raises:
            com.sun.star.resource.MissingResourceException: ``MissingResourceException``
        """


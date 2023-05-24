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
# Namespace: com.sun.star.gallery
from __future__ import annotations
import typing
from abc import abstractmethod
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
if typing.TYPE_CHECKING:
    from .x_gallery_theme import XGalleryTheme as XGalleryTheme_e28e0d13

class XGalleryThemeProvider(XNameAccess_e2ab0cf6):
    """
    provides access to the Gallery themes.
    
    It also allows inserting and removing of Gallery themes by name.
    
    This interface extends the interface com.sun.star.container.XNameAccess which provides access to existing Gallery themes collection.

    See Also:
        `API XGalleryThemeProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1gallery_1_1XGalleryThemeProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.gallery'
    __ooo_full_ns__: str = 'com.sun.star.gallery.XGalleryThemeProvider'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.gallery.XGalleryThemeProvider'

    @abstractmethod
    def insertNewByName(self, ThemeName: str) -> XGalleryTheme_e28e0d13:
        """
        creates a new Gallery theme and adds it to the collection.

        Raises:
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...
    @abstractmethod
    def removeByName(self, ThemeName: str) -> None:
        """
        deletes a Gallery theme from the collection.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...

__all__ = ['XGalleryThemeProvider']


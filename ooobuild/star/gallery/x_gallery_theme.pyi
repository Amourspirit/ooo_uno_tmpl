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

from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..lang.x_component import XComponent as XComponent_98dc0ab5


class XGalleryTheme(XIndexAccess_f0910d6d):
    """
    provides access to the items of a Gallery themes.
    
    It also allows inserting and removing of single items.
    
    This interface extends the interface com.sun.star.container.XIndexAccess which provides access to existing Gallery items collection.

    See Also:
        `API XGalleryTheme <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1gallery_1_1XGalleryTheme.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.gallery.XGalleryTheme'

    def getName(self) -> str:
        """
        retrieves the name of the Gallery theme
        """
        ...
    def insertDrawingByIndex(self, Drawing: XComponent_98dc0ab5, Index: int) -> int:
        """
        inserts an item

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def insertGraphicByIndex(self, Graphic: XGraphic_a4da0afc, Index: int) -> int:
        """
        inserts an item

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def insertURLByIndex(self, URL: str, Index: int) -> int:
        """
        inserts an item

        Raises:
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def removeByIndex(self, Index: int) -> None:
        """
        deletes an item from the collection

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def update(self) -> None:
        """
        updates the theme
        
        This method iterates over each item of the Gallery theme and updates it accordingly. Main purpose is to automatically regenerate the thumbnails and to remove invalid items, that is items who have got a URL that has become invalid. This method also optimizes underlying data structures.
        """
        ...



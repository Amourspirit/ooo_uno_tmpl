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
# Namespace: com.sun.star.text
import typing
from abc import abstractmethod
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
if typing.TYPE_CHECKING:
    from .x_auto_text_group import XAutoTextGroup as XAutoTextGroup_c9770c70

class XAutoTextContainer(XNameAccess_e2ab0cf6):
    """
    handles blocks of AutoTextEntry.

    See Also:
        `API XAutoTextContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XAutoTextContainer.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XAutoTextContainer'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XAutoTextContainer'

    @abstractmethod
    def insertNewByName(self, aGroupName: str) -> 'XAutoTextGroup_c9770c70':
        """
        creates a new AutoText group.
        
        The name must follow the pattern groupname*pathid, where:
        
        If only groupname is specified, the path defaults to 0, the Office Basis layer.
        Note that in some systems the user may lack of write access to the Office Basis directory.
        
        Example:

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
    @abstractmethod
    def removeByName(self, aGroupName: str) -> None:
        """
        deletes the specified AutoText group.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """

__all__ = ['XAutoTextContainer']

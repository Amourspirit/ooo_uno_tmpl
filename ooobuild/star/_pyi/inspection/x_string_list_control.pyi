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
# Libre Office Version: 7.2
# Namespace: com.sun.star.inspection
from typing_extensions import Literal
import typing
from .x_property_control import XPropertyControl as XPropertyControl_3f260fe2

class XStringListControl(XPropertyControl_3f260fe2):
    """
    defines the interface for an XPropertyControl which, additionally to the basic behavior, supports a list of strings interpreted as possible property values.
    
    A control which would canonically implement this interface is a list box control: The string list defined by XStringListControl would in the control be represented as drop-down list containing all the strings.
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API XStringListControl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XStringListControl.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.inspection.XStringListControl']

    def appendListEntry(self, NewEntry: str) -> None:
        """
        appends a new entry to the end of the list
        """
    def clearList(self) -> None:
        """
        clears the whole list
        """
    def getListEntries(self) -> 'typing.Tuple[str, ...]':
        """
        gets all list entries
        """
    def prependListEntry(self, NewEntry: str) -> None:
        """
        prepends a new entry to the beginning of the list
        """


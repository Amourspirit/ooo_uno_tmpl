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
# Namespace: com.sun.star.ucb
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_content import XContent as XContent_79db0975
    from .x_content_identifier import XContentIdentifier as XContentIdentifier_edc90d78

class XContentAccess(XInterface_8f010a43):
    """
    specifies methods for obtaining information on a content in different levels.
    
    For example, if there is a cursor which points to XContents, this interface could be used to give the user access to the content under the cursor. If the client only needs the identifier string of the content, there is no need to first create the content object, then to obtain the string from it and after that to release the content.

    See Also:
        `API XContentAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XContentAccess.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ucb.XContentAccess']

    def queryContent(self) -> 'XContent_79db0975':
        """
        returns the content ( \"most expensive method\" ).
        """
        ...
    def queryContentIdentifier(self) -> 'XContentIdentifier_edc90d78':
        """
        returns the identifier object of the content.
        """
        ...
    def queryContentIdentifierString(self) -> str:
        """
        returns the identifier string of the content ( \"cheap method\" ).
        
        Note that this string can be used later to recreate the content.
        """
        ...



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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .x_content import XContent as XContent_79db0975
from .x_content_identifier import XContentIdentifier as XContentIdentifier_edc90d78


class ContentEvent(EventObject_a3d70b03):
    """
    Struct Class

    A structure for content events.

    See Also:
        `API ContentEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1ContentEvent.html>`_
    """
    typeName: Literal['com.sun.star.ucb.ContentEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Action: typing.Optional[int] = ..., Content: typing.Optional[XContent_79db0975] = ..., Id: typing.Optional[XContentIdentifier_edc90d78] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Action (int, optional): Action value.
            Content (XContent, optional): Content value.
            Id (XContentIdentifier, optional): Id value.
        """
        ...


    @property
    def Action(self) -> int:
        """
        The action.
        
        The value can be one of the ContentAction constants.
        """
        ...


    @property
    def Content(self) -> XContent_79db0975:
        """
        The content to that the action is related (e.g., the content that was just physically destroyed, the content that was just inserted into a folder content).
        
        This member must be filled as follows:
        """
        ...


    @property
    def Id(self) -> XContentIdentifier_edc90d78:
        """
        A content identifier, which must be filled according to the action notified (e.g., the id of the folder content into which another content was inserted).
        
        This member must be filled as follows:
        """
        ...



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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class ItemStatus(object):
    """
    Struct Class

    describes a state of a property.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ItemStatus <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1ItemStatus.html>`_
    """
    typeName: Literal['com.sun.star.frame.status.ItemStatus']

    def __init__(self, State: typing.Optional[int] = ..., aStateData: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            State (int, optional): State value.
            aStateData (object, optional): aStateData value.
        """


    @property
    def State(self) -> int:
        """
        numerical value which describes the current state of an item.
        """


    @property
    def aStateData(self) -> object:
        """
        optional data which can be used by an implementation to send additional information.
        
        The content is dependent on the specific implementation.
        """


